from django.shortcuts import get_object_or_404, render

from . import models


def shelter_list(request):
    shelters = models.Shelter.objects.all()
    context = {"shelters": shelters}
    return render(request, "shelter_list.html", context)


def shelter_detail(request, pk):
    shelter = get_object_or_404(models.Shelter, pk=pk)
    context = {"shelter": shelter}
    return render(request, "shelter_detail.html", context)
