from django.shortcuts import get_object_or_404, render
from django.views import generic

from . import models


def shelter_list(request):
    shelters = models.Shelter.objects.all()
    context = {"shelters": shelters}
    return render(request, "shelter_list.html", context)


def shelter_detail(request, pk):
    shelter = get_object_or_404(models.Shelter, pk=pk)
    context = {"shelter": shelter}
    return render(request, "shelter_detail.html", context)


class DogCreateView(generic.CreateView):
    model = models.Dog
    template_name = "dog_form.html"
    fields = ["shelter", "name", "description"]


class DogDetailView(generic.DetailView):
    model = models.Dog
    template_name = "dog_detail.html"
    context_object_name = "dog"
