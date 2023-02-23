from django.contrib import admin
from django.urls import path
from reja.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginView, name='login'),
    path('logout/',logoutView, name='logout'),
    path('todo/', home, name='todo'),
    path('reja/<int:pk>/', reja_ochir),
    path('register/', RegisterView.as_view(), name='register')

]
