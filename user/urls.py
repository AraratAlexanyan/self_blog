from django.urls import path

from user.views import UserCreate, UserLists, UserVerify, UserDetailView

urlpatterns = [
    path('', UserLists.as_view()),
    path('<int:pk>/', UserDetailView.as_view()),
    path('reg/', UserCreate.as_view()),
    path('verify_token/', UserVerify.as_view()),
]