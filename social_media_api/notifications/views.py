from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Notification
from .serializers import NotificationSerializer


# Create your views here.

class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user).order_by('-timestamp')

# Utility function to create notification
def create_notification(actor, recipient, verb, target=None):
    if actor != recipient:  # don't notify self-actions
        Notification.objects.create(actor=actor, recipient=recipient, verb=verb, target=target)



