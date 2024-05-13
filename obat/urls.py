from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('category/', views.Category_list),
    path('category/<int:pk>/', views.Category_detail),
    path('book/', views.Book_list),
    path('book/<int:pk>/', views.Book_detail),
    path('sale/', views.Sale_list),
    path('sale/<int:pk>/', views.Sale_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)