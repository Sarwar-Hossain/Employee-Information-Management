from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.AdminLoginView.as_view(), name='admin_login'),
    path('create/employee/user/', views.CreateEmployeeUser.as_view(), name='create_employee_user'),
    path('delete/employee/user/', views.DeleteUser.as_view(), name='delete_user'),
    path('logout/', views.AdminLogoutView.as_view(), name='admin_logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
