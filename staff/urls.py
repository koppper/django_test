from staff import views
from django.urls import path
from .views import StaffViewSet, FilterStaff


staff_list = StaffViewSet.as_view({'get': 'list', 'post': 'create'})
staff_detail = StaffViewSet.as_view({'put': 'update',
                                                  'delete': 'destroy',
                                                  "get": 'retrieve'})

urlpatterns = [
    path('staff/', staff_list, name="banner_list"),
    path('staff/<int:pk>/', staff_detail, name='banner_detail'),
    path('staff/filter/', FilterStaff.as_view())

]