from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from .forms import UserPost
from .models import Post
from django.views import View

# Create your views here.

class PostShowView(TemplateView):
    template_name = 'home.html'
    def get_context_data(xelf, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        nc = UserPost()
        user_post = Post.objects.all()
        context = {'user_post': user_post, 'form': nc}
        return context
    
    def post(self, request):
        nc = UserPost(request.POST)
        if nc.is_valid():
            author = nc.cleaned_data['author']
            title = nc.cleaned_data['title']
            content = nc.cleaned_data['content']
            image = nc.cleaned_data['image']
            upload = Post(author=author, title=title, content=content, image=image)
            upload.save()
            return HttpResponseRedirect('home/')

class PostUpdateView(View):
    def get(self, request):
        pi = Post.objects.get(pk=id)
        nc = UserPost(instance=pi)
        return HttpResponseRedirect('/')

    def post(self, request, id):
        pi = Post.objects.get(pk=id)
        nc = UserPost(request.POST, instance=pi)
        if nc.is_valid():
            nc.save()
        return HttpResponseRedirect('home/')
    
class PostDeleteView(RedirectView):
    url = "/"
    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['id']
        Post.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)



