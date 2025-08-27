from django.urls import path
from . import views

urlpatterns = [
    path('tickets/', views.TicketListView.as_view(), name='ticket-list'),
    path('tickets/<int:pk>/detail/', views.TicketDetailView.as_view(), name='ticket-detail'),
    path('tickets/<int:pk>/update/', views.TicketUpdateView.as_view(), name='ticket-update'),
]