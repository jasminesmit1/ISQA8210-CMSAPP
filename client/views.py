from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from .models import models
from .models import Client, Comment
from django.urls import reverse_lazy


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    login_url = 'login'
    template_name = 'client_list.html'

    def get_context_data(self):
        clients = Client.objects.filter(author=self.request.user)
        return {'clients': clients}


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = 'client_detail.html'
    login_url = 'login'


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    fields = ('name', 'notes', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone', 'acct_number')
    template_name = 'client_edit.html'


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    template_name = 'client_delete.html'
    success_url = reverse_lazy('client_list')


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    template_name = 'client_new.html'
    fields = ('name', 'notes', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone', 'acct_number', )
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'comment.html'
    fields = ['comment']
    login_url = 'login'

    def form_valid(self, form):
        client = Client.objects.get(id=self.kwargs['pk'])
        form.instance.client = client
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentListView(LoginRequiredMixin, ListView):
    model = Comment
    template_name = 'commentlist.html'
    login_url = 'login'

    def get_context_data(self):
        client = Client.objects.get(id=self.kwargs['pk'])
        comments = Comment.objects.filter(client=client)
        print(comments)
        return {'comments': comments, 'client': client}
