from django.urls import path, include, re_path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    #path('', views.index, name='index'), # Index URL
    path("logout/", views.logout_request, name="logout"),
    # path('login/', views.new_login, name='login'),
    path('login/', views.new_new_login, name='login'),
    # path('signup/', views.signup, name='signup'),
    path('reset_password', auth_views.PasswordResetView.as_view(template_name="reset_password.html"), name="reset_password"),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name="reset_password_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="reset_password_form.html"), name="password_reset_confirm"),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name="reset_password_complete.html"), name="password_reset_complete"),
]

