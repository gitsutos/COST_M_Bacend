from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import redirect, HttpResponse
from rest_framework.decorators import api_view

from .serializers import CostsSerializer
from .models import Costs


# Create your views here.
class LatestCosts(APIView):
    def get(self, request, format=None):
        costs = Costs.objects.all()
        serializer = CostsSerializer(costs, many=True)
        return Response(serializer.data)


@api_view(["POST"])
def add_costs(request):
    serializer = CostsSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return HttpResponse("Succesfull")
    else:
        print(serializer.errors)
        return HttpResponse(f"Succ{serializer.errors}esfull")

@api_view(["DELETE"])
def delete_costs(request, pk):
    serializer = CostsSerializer(id=pk)
    serializer.save()