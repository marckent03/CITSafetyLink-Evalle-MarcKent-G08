from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Dashboard router
    path('dashboard/', views.dashboard_router, name='dashboard_router'),
    path('dashboard/student/', views.student_dashboard, name='student_dashboard'),
    path('dashboard/security/', views.security_dashboard, name='security_dashboard'),
    
    # Profile
    path('profile/', views.profile, name='profile'),
]