from .models import Menu, MenuCategory, Booking
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, renderer_classes, throttle_classes
from rest_framework.views import APIView
from .serializers import MenuSerializer, BookingSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from .serializers import CategorySerializer
from django.shortcuts import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from .permissions import IsStaffOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import permission_classes
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from .throttles import TenCallsPerMinute
from django.contrib.auth.models import User, Group

class MenuAPIViewGeneric(generics.ListCreateAPIView):
     permission_classes = [IsStaffOrReadOnly]
     queryset = Menu.objects.all()
     serializer_class = MenuSerializer  #display and store records
     ordering_fields = ['price', 'name']#menu-generic?ordering=name
     filterset_fields = ['price']


class SingleMenuItemAPIViewGeneric(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
     queryset = Menu.objects.all()
     serializer_class = MenuSerializer  #display and store records

@api_view()
def category_detail(request, pk):
    permission_classes = [IsStaffOrReadOnly]
    category = get_object_or_404(MenuCategory,pk=pk)
    serialized_category = CategorySerializer(category)
    return Response(serialized_category.data) 

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@renderer_classes([TemplateHTMLRenderer])
def book_view(request):
     ordering_fields = ['name', 'date', 'time', 'created_at', 'guests']
     ordering = request.GET.get('ordering')
     # If 'ordering' is present and is one of the allowed fields, order the queryset
     if ordering in ordering_fields:
        bookings = Booking.objects.all().order_by(ordering)
     else:
        bookings = Booking.objects.all()
     serialized_item = BookingSerializer(bookings, many=True)
    #  print("Bookings Queryset:", bookings)
    #  print("Serialized Data:", serialized_item.data)
     return Response({'data':serialized_item.data}, template_name='booking.html')


class MenuAPIView(viewsets.ViewSet):
    permission_classes = [IsStaffOrReadOnly]
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

@api_view()
@permission_classes([IsAuthenticated])
def manager_view(request):
    if request.user.groups.filter(name='Manager').exists():
        return Response({"message":"Only Manager Should See This"})
    else:
        return Response({"message": "You are not authorized"}, 403)
    
@api_view()
@throttle_classes([AnonRateThrottle])
def throttle_check(request):
    return Response({"message":"successful"}) 

# @api_view()
# @throttle_classes([UserRateThrottle])
# def throttle_check_auth(request):
#     return Response({"message":"successful"}) 

@api_view()
@permission_classes([IsAuthenticated])
@throttle_classes([TenCallsPerMinute])
def throttle_check_auth(request):
    return Response({"message":"successful"}) 

@api_view()
@permission_classes([IsAuthenticated])
def secret(request):
    return Response({"message":"successful"})

@api_view(['POST', 'DELETE'])
@permission_classes([IsAdminUser])
def managers(request):
    username = request.data['username']#if username is present add user to group
    if username:
        user = get_object_or_404(User, username=username)
        managers = Group.objects.get(name="Manager")
        if request.method == 'POST':
            managers.user_set.add(user)
        elif request.method == 'DELETE':
            managers.user_set.remove(user)
        return Response({"message": "ok"})
    return Response({"message": "error"}, status.HTTP_400_BAD_REQUEST)