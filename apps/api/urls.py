from django.urls import path

from .views import UserSimpleView

urlpatterns = [
    path('/',UserSimpleView.as_view(), name = 'users'),
]