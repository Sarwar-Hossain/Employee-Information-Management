from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('home/', views.MyView.as_view(), name='index'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
