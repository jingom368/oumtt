from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('reservations/', views.getReservations, name='reservations'),
    path('contacts/', views.getContact, name='contact'),
    # path('reservations/<str:pk>/update/', views.updateNote, name='update-reservation'),
    # path('notes/create/', views.createNote, name='create-note'),
    # path('notes/<str:pk>/delete/', views.deleteNote, name='delete-note'),

    path('reservations/<str:pk>/', views.getReservation, name='reservation'),
    path('images/', views.getImage, name='image'),
]