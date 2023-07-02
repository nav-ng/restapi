from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register("movie", MovieView, basename="movie")
# router.register("book", BookView, basename="book")
router.register("company", CompanyView, basename="company")


urlpatterns = [
    path('first/', TodoView.as_view(), name='first'),
    # path('work1/', StudentView.as_view(), name='work1'),
    path('second/<int:id>', TodoDetailView.as_view(), name='second'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('third/', PersonView.as_view(), name='third'),
    path('fourth/<int:id>', PersonDetailView.as_view(), name='fourth'),
    # path('work2/', EmployeeView.as_view(), name='work2'),
    # path('work3/<int:id>', EmployeeDetailView.as_view(), name='work3'),
    path('userview/', UserView.as_view(), name='userview')
] + router.urls


