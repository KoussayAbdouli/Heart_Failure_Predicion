
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_page , name="Home Page"),
    path ('PredictionPage/',views.index , name = "Home"),
    path('result/',views.result , name="result")
]
