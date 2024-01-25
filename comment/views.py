from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Comment
from .forms import CommentForm

@method_decorator(login_required, name='dispatch')
class CommentCreateView(LoginRequiredMixin,CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment_form.html'
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] =Comment.objects.all()
        context['type'] = 'Review'
        context['button_text'] = 'Review'
        context['icon'] = 'fa-regular fa-comment-dots text-info'
        context['has_account'] = "Return "
        context['redirect'] = "homepage"
        context['user_to_another'] = "home"
        return context
