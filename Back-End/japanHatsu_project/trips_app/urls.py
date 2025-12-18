from django.urls import path
from .views import TripGeneratorView, ItineraryItemCollectionView, ItineraryItemDetailView

urlpatterns = [
    path("trips/generate/", TripGeneratorView.as_view(), name="trip-generate"),
    path("trips/<int:trip_id>/items/", ItineraryItemCollectionView.as_view(), name="itineraryitem-create"),
    path("trips/<int:trip_id>/items/<int:item_id>/", ItineraryItemDetailView.as_view(), name="itineraryitem-detail"),
]
