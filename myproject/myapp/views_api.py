from .models import Menu, MenuCategory, Booking
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.views import APIView
from .serializers import MenuSerializer, BookingSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from .serializers import CategorySerializer
from django.shortcuts import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer

class MenuAPIViewGeneric(generics.ListCreateAPIView):
     queryset = Menu.objects.all()
     serializer_class = MenuSerializer  #display and store records


class SingleMenuItemAPIViewGeneric(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
     queryset = Menu.objects.all()
     serializer_class = MenuSerializer  #display and store records

@api_view()
def category_detail(request, pk):
    category = get_object_or_404(MenuCategory,pk=pk)
    serialized_category = CategorySerializer(category)
    return Response(serialized_category.data) 

@api_view(['GET'])
@renderer_classes([TemplateHTMLRenderer])
def book_view(request):
     bookings = Booking.objects.all()
     serialized_item = BookingSerializer(bookings, many=True)
    #  print("Bookings Queryset:", bookings)
    #  print("Serialized Data:", serialized_item.data)
     return Response({'data':serialized_item.data}, template_name='booking.html')


class MenuAPIView(viewsets.ViewSet):
    def list(self, request):
            # Retrieve all menu items from the database
            menu_items = Menu.objects.select_related('category').all() #using category makes sql queries more efficient
            # Serialize the menu items
            serializer = MenuSerializer(menu_items, many=True)
            # Return the serialized data as JSON response
            return Response(serializer.data, status=status.HTTP_200_OK)
    def create(self, request):
        item = request.data.get('name')
        return Response({"message":"Creating a menu item:" + item}, status.HTTP_201_CREATED)
    def update(self, request, pk=None):
        return Response({"message":"Updating a menu item"}, status.HTTP_200_OK)
    def retrieve(self, request, pk=None):
        return Response({"message":"Displaying a menu item"}, status.HTTP_200_OK)
    def partial_update(self, request, pk=None):
        return Response({"message":"Partially updating a menu item"}, status.HTTP_200_OK)
    def destroy(self, request, pk=None):
        return Response({"message":"Deleting a menu item"}, status.HTTP_200_OK)
