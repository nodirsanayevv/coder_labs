from django.urls import path
from .views import UserList, UserDetail, ContactDetail, ContactList, ServiceList, ServiceDetail, CategoryList, CategoryDetail


urlpatterns = [
    path('api/<int:pk>', CategoryDetail.as_view()),
    path('qat/', CategoryList.as_view()),
    path('user/', UserList.as_view()),
    path('con/', UserDetail.as_view()),
    path('contact/', ContactList.as_view()),
    path('con/<int:pk>', ContactDetail.as_view()),
    path('cat/', ServiceDetail.as_view()),
    path('qot/', ServiceList.as_view())


]