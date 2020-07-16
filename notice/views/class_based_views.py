from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, FormView, UpdateView, DetailView, DeleteView

from notice.forms import NoticeForm
from notice.models import Notice


class NoticeListView(ListView):
    model = Notice
    paginate_by = 20
    template_name = 'list.html'


class NoticeCreateView(CreateView, FormView):
    model = Notice
    form_class = NoticeForm
    template_name = 'form.html'

    def get_success_url(self):
        return self.object.get_absolute_url()


class NoticeUpdateView(UpdateView, FormView):
    model = Notice
    form_class = NoticeForm
    template_name = 'form.html'

    def get_success_url(self):
        return self.object.get_absolute_url()


class NoticeDetailView(DetailView):
    model = Notice
    template_name = 'detail.html'


class NoticeDeleteView(DeleteView):
    model = Notice
    template_name = 'delete.html'

    def get_success_url(self):
        return self.object.get_absolute_url()