
from django.shortcuts import render
from django.views import generic
from django.core.auth.mixins import LoginRequiredMixin, PermissionsRequiredMixin
from braces.views import SelectRelatedMixin
from . import models
from . import forms
from django.http import Http404

from django.contrib.auth import get_user_model
User = get_user_model()


# Create your views here.

class PostList(SelectRelatedMixin,generic.ListView):
	model = models.Post
	select_related = ('user','group')
	

class UserPosts(generic.ListView):
	model = models.Post
	template_name="posts/user_post_list.html"

	def get_queryset(self,*args,**kwargs):
		try:
			self.post_user=user.objects.prefetch_related('posts').get(username__iexact=self.kwargs.get('username'))
		except User.DoesNotExists:
			raise Http404
		else:
			return self.post_user.posts.all()

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		context['post_user'] = self.post_user
		return context

class PostDetail(SelectRelatedMixin,generic.DetailView):
	model = models.Post
	select_related = ('user','group')

	def get_queryset(self):
		queryset =  super().get_queryset()




class CreatePost(CreateView):
	model = models.Post


class DeletePost
