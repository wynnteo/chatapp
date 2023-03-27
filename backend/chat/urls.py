from django.urls import path
from .views import MessageList

urlpatterns = [
    path('messages/', MessageList.as_view()),
]
