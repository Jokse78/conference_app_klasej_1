
from django.urls import path
from events.views import (
    EventDetailView,
    RegisterVisitorView,
    UserEventList,
)

urlpatterns = [
    # /events/2/
    path( '<int:pk>/', EventDetailView.as_view(), name = "event-detail" ),
    path( 'register/<int:renginio_id>/', RegisterVisitorView.as_view(), name = "register-visitor" ),
    path('my-events/', UserEventList.as_view(), name = "user-events"),
    ]