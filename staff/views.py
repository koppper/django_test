from rest_framework import viewsets, status, permissions, filters, generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import Staff
from .serializers import StaffSerializer


class FilterStaff(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Staff.objects.order_by('salary')
    filter_backends = [filters.SearchFilter]
    search_fields = ['FIO', 'position', 'salary', 'parent__id']
    serializer_class = StaffSerializer


class StaffViewSet(viewsets.ViewSet):
    serializer_class = StaffSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def list(self, request):
        queryset = Staff.objects.order_by('id')
        serializer = StaffSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = Staff.objects.all()
        staff = get_object_or_404(queryset, pk=pk)
        serializer = StaffSerializer(staff)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = StaffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def update(self, request, pk=None, *args, **kwargs):
        queryset = Staff.objects.all()
        if not pk:
            return Response({'Error': 'Update not allowed'})
        try:
            instance = get_object_or_404(queryset, pk=pk)
        except Staff.DoesNotExist:
             return Response({'Error': 'Object does not exists'}, status=404)

        serializer = StaffSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    def destroy(self, request, pk=None, *args, **kwargs):
        staff = Staff.objects.get(pk=pk)
        if not staff:
             return Response({'Error': 'Object does not exists'}, status=404)
        staff.delete()
        return Response({"Delete": 'Object deleted'}, status=status.HTTP_204_NO_CONTENT)