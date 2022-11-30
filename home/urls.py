from django.urls import path
from .views import CustomLoginView, RegisterPage, VisitList, CreateVisit, VisitUpdate, DeleteVisit
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('', VisitList.as_view(), name='home'),
    path('create-visit/', CreateVisit.as_view(), name='create-visit'),
    path('visit-update/<int:pk>/', VisitUpdate.as_view(), name='visit-update'),
    path('delete-visit/<int:pk>/', DeleteVisit.as_view(), name='delete-visit'),
]