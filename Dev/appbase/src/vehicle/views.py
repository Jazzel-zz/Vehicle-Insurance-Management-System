from app.settings import MEDIA_ROOT
from django.shortcuts import render
from django.views.generic import (
    CreateView, ListView, UpdateView, DeleteView, DetailView, TemplateView)
from . mixins import FormUserNeededMixin, UserOwnerMixin
from . forms import VechicleModelForm
from . models import Vehicle
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.forms import modelformset_factory

# Create your views here.


class VehicleCreateView(FormUserNeededMixin, CreateView):
    form_class = VechicleModelForm
    template_name = 'vehicle/vehicle_add.html'


class VehicleDetailView(UserOwnerMixin, DetailView):
    queryset = Vehicle.objects.all()


class VehicleListView(ListView):
    def get_queryset(self, *args, **kwargs):
        queryset = Vehicle.objects.filter(user=self.request.user)
        # print(self.request.GET)
        query = self.request.GET.get("q", None)
        if query is not None:
            queryset = queryset.filter(
                Q(content__icontains=query) | Q(user__username__icontains=query))
        return queryset


class VehicleUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = Vehicle.objects.all()
    form_class = VechicleModelForm
    template_name = 'vehicle/vehicle_edit.html'


class VehicleDeleteView(LoginRequiredMixin, UserOwnerMixin, DeleteView):
    model = Vehicle
    success_url = reverse_lazy("vehicle:list")


class VideoConference(TemplateView):
    template_name = 'vehicle/video-conference.html'
