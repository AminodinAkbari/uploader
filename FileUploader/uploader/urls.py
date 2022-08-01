from django.urls import path
from uploader import APIs

urlpatterns = [
    path('GET', APIs.FileUplodaerAPI.as_view() , name = 'get_method'),
    path('DELETE/<int:pk>', APIs.FileDeleteAPI.as_view() , name='deleting'),
    path('POST', APIs.NewFileAPI.as_view() , name='posting'),
]