
from django.shortcuts import get_object_or_404,render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .models import Order
from rest_framework import status
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated

from .serializers import OrderSerializer
# Create your views here.

# create new order end point
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def new_order(request):
    data =  request.data
    serializer = OrderSerializer(data=data)
    if serializer.is_valid():
    # Check if the title is unique 
        if Order.objects.filter(title=serializer.validated_data['title']).exists():
            return Response({'Err': 'Order with the same title alredy exists .'}, status=status.HTTP_400_BAD_REQUEST)
            
        order = Order.objects.create(
            **data,
            user=request.user
        )
        res = OrderSerializer(order,many=False)
        return Response({'Order':res.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# get all orders
@api_view(['GET'])
def getAll(request):
    if request.method == 'GET':
        orders = Order.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size = 2
        paginated_orders =paginator.paginate_queryset(orders, request)
        serializer = OrderSerializer(paginated_orders, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

# get order by id 
@api_view(['GET'])
def getOrderById(request,pk):
    order = get_object_or_404(Order,id=pk)
    serializer = OrderSerializer(order,many=False)
    return Response({'Order':serializer.data},status=status.HTTP_200_OK)

# Update order 
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_order(request, pk):
    order = get_object_or_404(Order, id=pk)

    # Check if the user has permission to update the order
    if order.user != request.user:
        return Response({'Error': 'Sorry, you cannot update this order.'}, status=status.HTTP_403_FORBIDDEN)

    # Extraction
    new_status = request.data.get('status', order.status)
    new_title = request.data.get('title', order.title)

    if order.status == 'Pending':
        # Users cannot update certain fields in 'Pending' status
        if new_status!='Cancelled' or 'title' in request.data or 'description' in request.data or 'price' in request.data:
            return Response({'error': 'Users cannot update title, description, or price in "Pending" status, you can only cancel the order.'}, status=status.HTTP_400_BAD_REQUEST)
        # Users can cancel the order, moving it to "Cancelled" 
        if new_status == 'Cancelled':
            pass
    elif order.status == 'Processing':
        # Users can update all fields in 'Processing' 
        if new_title != order.title and Order.objects.filter(title=new_title).exists():
            return Response({'error': 'Title must be unique.'}, status=status.HTTP_400_BAD_REQUEST)
        if new_status!='Shipped' and new_status!='Processing':
            return Response({'error': 'Users cannot update status of the order to anything but shipped.'}, status=status.HTTP_400_BAD_REQUEST)

        # Users can mark the order as "Shipped" when ready
        if new_status == 'Shipped' and new_status!='Processing':
            pass
    elif order.status == 'Shipped':
        # Users cannot update certain fields in 'Shipped' status
        if new_status!='Delivered' or 'title' in request.data or 'description' in request.data or 'price' in request.data:
            return Response({'error': 'Users cannot update title, description, or price in "Shipped" status , you can only deliver the order.'}, status=status.HTTP_400_BAD_REQUEST)

        # Users can mark the order as "Delivered" when delivered to the customer
        if new_status == 'Delivered':
            pass
    elif order.status == 'Delivered':
        # Users cannot update certain fields in 'Delivered' status
        if 'title' in request.data or 'description' in request.data or 'price' in request.data:
            return Response({'error': 'Users cannot update title, description, or price in "Delivered" status.'}, status=status.HTTP_400_BAD_REQUEST)
    elif order.status == 'Cancelled':
        # Users cannot update certain fields in 'Cancelled' status
        if 'title' in request.data or 'description' in request.data or 'price' in request.data:
            return Response({'error': 'Users cannot update title, description, or price in "Cancelled" status.'}, status=status.HTTP_400_BAD_REQUEST)
    else:
       return Response({'error': f'Invalid status: {order.status}'}, status=status.HTTP_400_BAD_REQUEST)

    # Update order properties
    order.title = request.data.get('title', order.title)
    order.description = request.data.get('description', order.description)
    order.price = request.data.get('price', order.price)
    order.status = new_status
    order.timestamp = timezone.now()
    order.save()
    order.save()

    serializer = OrderSerializer(order, many=False)
    return Response({'Order Updated': serializer.data})

# Delete order 
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_Order(request,pk):
    order =  get_object_or_404(Order,id=pk)
    if order.user != request.user:
        return Response({'Error':'Sorry you cannot delete'},status=status.HTTP_403_FORBIDDEN) 
    order.delete()
    return Response({'details':'deleted successfully'},status=status.HTTP_200_OK)

# get Order By Title
@api_view(['GET'])
def getOrderByTitle(request):
    title = request.data['title']

    orders = Order.objects.filter(title__iexact=title)
    # since its match exact title we return one
    serializer = OrderSerializer(orders, many=False)
    return Response(serializer.data)

# get Order By Title
@api_view(['GET'])
def getOrderByTitleQuery(request,pk):
    orders = Order.objects.filter(title__icontains=pk)
    # since its list we return Many
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

