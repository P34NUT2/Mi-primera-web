from django.urls import path
from .views import OfferCreateView, MyOffersView, OffersReceivedView, OfferStatusUpdateView

urlpatterns = [
    path('task/<int:task_id>/offer/', OfferCreateView.as_view(), name='create_offer'),
    path('my-offers/<slug:username>', MyOffersView.as_view(), name='my_offers'),
    path('received/<slug:username>', OffersReceivedView.as_view(), name='offers_received'),
    path('offer/<int:pk>/status/<str:action>/', OfferStatusUpdateView.as_view(), name='offer_status_update'),
]


