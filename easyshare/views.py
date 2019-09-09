from django.shortcuts import render, get_object_or_404
from . models import Posts
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



def index(request):
    if not request.user.is_authenticated():
        return render(request, 'users/login.html')
    else:
     context = {
        'items': Posts.objects.all()
        }
    return render(request, 'easyshare/index.html', context)


class postListview(ListView, LoginRequiredMixin):
        model = Posts
        template_name = 'easyshare/index.html'
        context_object_name = 'items'
        ordering = ['-date_posted']
        paginate_by = 4


class UserpostListview(ListView):
    model = Posts
    template_name = 'easyshare/user_post.html'
    context_object_name = 'items'
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Posts.objects.filter(author=user).order_by('-date_posted')



class postDetailview(DetailView):
    model = Posts


class postCreateview(LoginRequiredMixin, CreateView):
    model = Posts
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class postUpdateview(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Posts
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        items = self.get_object()
        if self.request.user == items.author:
            return True
        return False


class postDeleteview(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Posts
    success_url = '/'

    def test_func(self):
        items = self.get_object()
        if self.request.user == items.author:
            return True
        return False


def about(request):
    return render(request, 'easyshare/about.html', {'tit': 'about'})


