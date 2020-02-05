from django.urls import path
from . import views
from .views import (
    ClientListView,
    ClientUpdateView,
    ClientDetailView,
    ClientDeleteView,
    ClientCreateView,
    CommentCreateView,
    CommentListView,
)


urlpatterns = [
    path('<int:pk>/edit/',
         ClientUpdateView.as_view(), name='client_edit'),
    path('<int:pk>/',
         ClientDetailView.as_view(), name='client_detail'),
    path('<int:pk>/delete/',
         ClientDeleteView.as_view(), name='client_delete'),
    path('new/', ClientCreateView.as_view(), name='client_new'),
    path('', views.ClientListView.as_view(), name='client_list'),
    path('<int:pk>/add/', CommentCreateView.as_view(), name='add_comment'),
    path('<int:pk>/comments', views.CommentListView.as_view(), name='view_comment'),


]
