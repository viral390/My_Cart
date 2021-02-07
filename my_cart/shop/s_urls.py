from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="shophome"),
    path('about/', views.about, name="about as"),
    path('contact/', views.contact, name="contact us"),
    path('search/', views.search, name="search"),
    path('product/<int:myid>', views.productviews, name="product views"),
    path('checkout/', views.checkout, name="check out"),
    path('tracker/', views.tracker, name="tracking status")
]