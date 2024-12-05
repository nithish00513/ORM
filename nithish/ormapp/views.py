from django.urls import path
from . import views
urlpatterns = [
    path('loans/', views.loan_list, name='loan_list'),
]
