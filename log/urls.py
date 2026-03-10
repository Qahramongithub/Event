from django.urls import path
from log.views import LogEventView

urlpatterns = [
    path('log', LogEventView.as_view()),
]
