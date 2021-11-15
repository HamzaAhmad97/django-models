from django.db import models
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Snack

class SnackListView(ListView):
    model = Snack
    template_name = "snacks/snack_list.html"

class SnackDetail(DetailView):
    model = Snack
    template_name = "snacks/snack_detail.html"