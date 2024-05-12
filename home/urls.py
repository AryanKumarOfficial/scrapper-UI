from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Home"),
    # path("/blog", views.blog, name="Blog"),
    # path("/create", views.create, name="Create"),
    # path("/profile", views.profile, name="Profile"),
    # path("/password", views.password, name="Password"),
    # path("/login", views.login, name="Login"),
    # path("/logout", views.logout, name="Logout"),
    # path("/delete", views.delete, name="Delete"),
    # path("/register", views.register, name="Register"),
    # path("/reset", views.reset, name="Reset"),
    path("scrap", views.scrap, name="Scrap"),
]