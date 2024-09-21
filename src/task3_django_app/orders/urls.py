from django.urls import path
from . import views

urlpatterns = [
    path('top-customers/', views.top_customers_view, name='top_customers'),
]