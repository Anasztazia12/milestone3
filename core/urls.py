from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('map/', views.map_page, name='map'),
    path('cafes/', views.cafe_list_page, name='cafe_list'),
    path('login/', views.login_page, name='login'),
    path('signup/', views.signup_page, name='signup'),
    path('logout/', views.logout_page, name='logout'),
    path('delete-account/', views.delete_account, name='delete_account'),
    path('add-cafe/', views.add_cafe_page, name='add_cafe'),
    path('my-cafes/', views.my_cafes_page, name='my_cafes'),
    path('cafe/<int:cafe_id>/edit/', views.edit_cafe_page, name='edit_cafe'),
    path('cafe/<int:cafe_id>/delete/', views.delete_cafe_page, name='delete_cafe'),
    path('cafe/<int:cafe_id>/favourite/', views.toggle_favourite, name='toggle_favourite'),
]
