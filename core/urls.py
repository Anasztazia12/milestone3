from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('map/', views.map_page, name='map'),
    path('login/', views.login_page, name='login'),
    path('signup/', views.signup_page, name='signup'),
    path('logout/', views.logout_page, name='logout'),
    path('delete-account/', views.delete_account, name='delete_account'),
    path('add-cafe/', views.add_cafe_page, name='add_cafe'),
]
