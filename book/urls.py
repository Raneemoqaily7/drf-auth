from django.urls import path
from .views import  BookListView
from rest_framework_simplejwt import views as jwt_views

urlpatterns =[
    path ('book-list', BookListView.as_view() , name ='book_list'),
    path('token' , jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    path('refresh' , jwt_views.TokenRefreshView.as_view() , name ='token_refresh_pair'),

]


    # "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1NDMyNTkxNSwiaWF0IjoxNjU0MjM5NTE1LCJqdGkiOiI3ZDZhZThhN2YxYzY0MjczODczZGYyOTY1N2Y4ZDllNCIsInVzZXJfaWQiOjF9.Pmt3MYHoTOrtpgF_OFZaLqP-7WIXjQ7alwU88m04A0M",
    # "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU0MjM5ODE1LCJpYXQiOjE2NTQyMzk1MTUsImp0aSI6IjA4NzI5MjAwOTBkNjQxMjQ4OTYyOGIwYTExMzllZGU4IiwidXNlcl9pZCI6MX0.D5jFCrDMI9SzHI-Zu14oInRa_iLcckNMq-nRbx0BjhQ"