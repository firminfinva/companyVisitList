from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


from django.views import View
from django.shortcuts import redirect
from django.db import transaction
import datetime
from .models import Visitors



class CustomLoginView(LoginView):
    template_name = 'home/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


class RegisterPage(FormView):
    template_name = 'home/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)


class VisitList(LoginRequiredMixin, ListView):
    model = Visitors
    context_object_name = 'tasks'
    template_name = 'home/visit_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_superuser:
            context['tasks'] = context['tasks'].filter(user=self.request.user)
            context['count'] = context['tasks'].filter(checked_in=False).count()

            search_input = self.request.GET.get('search-area') or ''
            if search_input:
                context['tasks'] = context['tasks'].filter(
                    visitor__icontains=search_input)

            context['search_input'] = search_input
        else:

            context['tasks'] = context['tasks'].filter(visitee__icontains=self.request.user)
            context['tasks'] = context['tasks'].filter(checked_in=False)
            context['count'] = context['tasks'].filter(checked_in=False).count()

            search_input = self.request.GET.get('search-area') or ''
            if search_input:
                context['tasks'] = context['tasks'].filter(
                    visitor__icontains=search_input)

            context['search_input'] = search_input

        return context

class VisitDetail(LoginRequiredMixin, DetailView):
    model = Visitors
    context_object_name = 'task'
    template_name = 'home/visit.html'




class CreateVisit(LoginRequiredMixin, CreateView):
    model = Visitors
    fields = ['visitee', 'visitor', 'motif']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateVisit, self).form_valid(form)

class VisitUpdate(LoginRequiredMixin, UpdateView):
    model = Visitors
    fields = ['visitee', 'visitor', 'motif', 'checked_in', 'active']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        if form.instance.checked_in:
           form.instance.leaving_time = datetime.datetime.now()
           form.instance.checked_in = True
           form.instance.active = False
        else:
            form.instance.checked_in = True
            form.instance.active = True
        return super(VisitUpdate, self).form_valid(form)

class DeleteVisit(LoginRequiredMixin, DeleteView):
    model = Visitors
    context_object_name = 'task'
    success_url = reverse_lazy('home')

    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user=owner)