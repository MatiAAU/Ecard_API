from django.contrib import admin
from django.urls import path
from .views import employee_list, employee_detail, GenericAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/', employee_list),
    path('detail/<int:pk>/', employee_detail),
    path('generic/employee/<int:pk>/', GenericAPIView.as_view()),
]
