from django.urls import path
from .views import PostListView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('home/', PostListView.as_view(), name='blog-home'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('password-reset/',
        auth_views.PasswordResetView.as_view(template_name='user/password_reset.html'),
        name='password_reset'),
    path('password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'),
        name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'),
        name='password_reset_confirm'),
    path('password-reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'),
        name='password_reset_complete'),
]



