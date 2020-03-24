from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_user, name="login"),
    path("logout", views.logout_user , name = "logout"),
    path("register", views.register_user , name = "register"),
    path("hotel/<int:hotels_id>", views.hotel, name="hotel"),
    path("book", views.book, name="book"),
    path("cart", views.cart, name="cart"),
    path("history", views.history, name="history"),
    path("delete/<int:books_id>", views.delete, name="delete"),
]