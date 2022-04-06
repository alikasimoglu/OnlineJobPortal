from django.urls import path, include
from profiles.views import ProfilesView, SignUpView, JobSeekerSignUpView, RecruiterSignUpView
from django.contrib.auth import views as auth_views


app_name = 'profiles'
urlpatterns = [
    path('', ProfilesView.as_view(), name='profiles'),
    path('', include('django.contrib.auth.urls')),
    path('kayit/', SignUpView.as_view(), name='signup'),
    path('kayit/is-arayan/', JobSeekerSignUpView.as_view(), name='jobseeker_signup'),
    path('kayit/ik-uzmani/', RecruiterSignUpView.as_view(), name='recruiter_signup'),
    path('giris-yap/', auth_views.LoginView.as_view(template_name='profiles/login.html'), name='login'),
    path('cikis-yap/', auth_views.LogoutView.as_view(), name='logout'),
]
