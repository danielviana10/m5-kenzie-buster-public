from django.urls import path
from .views import LoginJWTView, UserDetailView, UserView

urlpatterns = [
    path("users/", UserView.as_view()),
    path("users/login/", LoginJWTView.as_view()),
    path("users/<int:user_id>/", UserDetailView.as_view()),
]
