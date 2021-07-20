from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('auth/login/', views.login_user, name='login'),
    path('auth/register/', views.register_user, name='register'),
    path('accounts/logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('project/<project_id>', views.project, name='project'),
    path('api/profiles/', views.ProfileList.as_view())
]