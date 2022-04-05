from django.urls import path
from .views import *
# from connect_app import views

app_name = "connect_app"

urlpatterns = [
    path('', PostShowView.as_view(), name='post'),
    path('delete/<int:id>/', PostDeleteView.as_view(), name='delete_post'),
    path('<int:id>/', PostUpdateView.as_view(), name='update_post'),
]
