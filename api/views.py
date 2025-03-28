from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer

@api_view(['GET'])
def get_items(request):
    itens = Item.objects.all()
    serializer = ItemSerializer(itens, many=True)
    return Response(serializer.data)
