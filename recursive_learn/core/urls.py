from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm, ChangeOldPasswordForm

app_name = 'core'

urlpatterns = [
     path('', views.index, name='index'),
     path('contact/', views.contact, name='contact'),
     path('about/', views.about, name='about'),

     path('signup/', views.signup, name='signup'),
     path('login/', auth_views.LoginView.as_view(authentication_form=LoginForm,
          template_name="user/login.html"), name="login"),
     path('logout/', views.logout_view, name='logout'),
     path('update_mail/', views.update_email, name='update_mail'),
     path('change_email_done/', views.change_email_done, name='change_email_done'),
     path('change_password_done/', views.change_password_done, name='change_password_done'),
     path('details_user/', views.details_user, name='details_user'),
     path('change_password_old/', auth_views.PasswordChangeView.as_view(success_url='/change_password_done/',
          form_class=ChangeOldPasswordForm, template_name='user/password_change.html'), name='password_change'),

     path('restore_password_mail/', views.restore_password_mail, name='restore_password_mail'),
     path('verification_step/', views.verification_step, name='verification_step'),
     path('restore_password/', views.restore_password, name='restore_password'),
     path('error_verification/', views.error_verification, name='error_verification'),
     path('restore_password_done/', views.restore_password_done, name='restore_password_done'),
]
