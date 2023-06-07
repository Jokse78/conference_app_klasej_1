from.views import ConferenceListView, ConferenceDetailView, ConfeneceLikeView
from django.urls import path





urlpatterns = [
    # Visi views kurie yra ne funkcijos, o klases,
    # juos kvieciam su papildoma as_view()
    path("", ConferenceListView.as_view()), # /conferences/
    path( "<int:pk>/", ConferenceDetailView.as_view(), name = "conference-detail" ), # /conferences/1/, /conferences/10/
    path("like/<int:konferencijos_id>/", ConfeneceLikeView.as_view(), name = "conference-like"),
]