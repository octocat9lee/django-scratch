from django.urls import re_path, path
from . import views

# namespace
app_name = "file_upload"

urlpatterns = [
    re_path(r'^upload/', views.model_form_upload, name='model_form_upload'),
    path('', views.file_list, name='file_list'),
]
