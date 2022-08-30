from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('create/employee/profile/<int:employee_id>/', views.CreateEmployeeProfile.as_view(), name='index'),
    path('create/employee/profile/W4/<int:employee_id>/', views.CreateEmployeeProfileW4.as_view(), name='section_w4'),
    path('update/employee/profile/', views.UpdateEmployeeProfile.as_view(), name='update'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
