from django.urls import path
from . import views


urlpatterns = [
    path('show/', views.ShowRollView.as_view()),
    path('call/', views.CallTheRollView.as_view()),
    path('complete/', views.CompleteView.as_view()),
]
