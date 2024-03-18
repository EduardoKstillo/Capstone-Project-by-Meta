from django.shortcuts import render
from rest_framework import viewsets, generics, authentication
from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes


def index(request):
    return render(request, 'index.html')

@api_view()
@permission_classes([IsAuthenticated])
@authentication_classes([authentication.TokenAuthentication])
def msg(request):
    return Response({"message": "This view is protected"})


class BookingViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    # authentication_classes = [authentication.TokenAuthentication]


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
