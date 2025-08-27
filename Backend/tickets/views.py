from django.contrib.auth import get_user_model
from rest_framework import generics, filters
from rest_framework import status as http_status
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers


User = get_user_model()


class TicketListView(generics.ListCreateAPIView):

    queryset = models.Ticket.objects.all()
    serializer_class = serializers.TicketSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = [
        "title",
        "description",
        "priority",
        "sector",
        "status",
        "created_by__username",
        "assigned_to__username",
        "updated_by__username",
    ]


class TicketDetailView(generics.RetrieveDestroyAPIView):

    queryset = models.Ticket.objects.all()
    serializer_class = serializers.TicketSerializer


class TicketUpdateView(APIView):

    model_class = models.Ticket

    def patch(self, request, *args, **kwargs):
        data = request.data
        user = self.request.user
        ticket_id = kwargs.get("pk")

        ticket = models.Ticket.objects.get(id=ticket_id)

        status_ticket = data.get("status")

        if status_ticket == "Resolvido":
            user_is_technician = user.groups.filter(name="Tecnico").exists()
            if not user_is_technician:
                return Response(
                    {"detail": "Não autorizado. Apenas técnicos podem resolver chamados."},
                    status=http_status.HTTP_403_FORBIDDEN
                )

        serializer = serializers.TicketSerializer(ticket, data=data, partial=True)
        if serializer.is_valid():
            serializer.save(updated_by=user)
            return Response(serializer.data, status=http_status.HTTP_200_OK)

        return Response(serializer.errors, status=http_status.HTTP_400_BAD_REQUEST)