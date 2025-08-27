from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from tickets.views import TicketListView, TicketCreateView, TicketUpdateView

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('home/', TicketListView.as_view(), name='home'),
    path('ticket/create/', TicketCreateView.as_view(), name='ticket-create'),
    path('ticket/update/<int:pk>/', TicketUpdateView.as_view(), name='ticket-update'),
]
