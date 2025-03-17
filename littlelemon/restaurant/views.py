from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics,viewsets,permissions
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer

# Create your views here.
def sayHello(request):
    return HttpResponse('Hello world')

def index(request):
    return render(request, 'index.html', {})


class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class SingleMenuItemView(generics.RetrieveUpdateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
    fields = '__all__'