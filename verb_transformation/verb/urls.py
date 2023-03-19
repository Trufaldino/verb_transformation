from django.urls import path

from .views import verb_tense_view

urlpatterns = [
    path('', verb_tense_view),
]
