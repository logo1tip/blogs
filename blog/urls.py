from django.urls import path
from .views import *


urlpatterns = [
    path('product/create', ProductCreateView.as_view()),
]