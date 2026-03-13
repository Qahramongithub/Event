from django.urls import path
from log.views import LogEventView, ProgramLogEventView

urlpatterns = [
    path('log/device', DeviceLogEventView.as_view()),
    path('log/program', ProgramLogEventView.as_view()),
]
