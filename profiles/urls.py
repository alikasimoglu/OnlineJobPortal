from django.urls import path, reverse_lazy
from profiles import views
from profiles.views import SignUpView, JobSeekerSignUpView, RecruiterSignUpView, \
    JobSeekerProfileUpdateView, JobSeekerProfileView, RecruiterProfileView, RecruiterProfileUpdateView
from django.contrib.auth import views as auth_views


app_name = 'profiles'
urlpatterns = [
    # Log-in and Logout
    path('kayit/', SignUpView.as_view(), name='signup'),
    path('kayit/is-arayan/', JobSeekerSignUpView.as_view(), name='jobseeker_signup'),
    path('kayit/ik-uzmani/', RecruiterSignUpView.as_view(), name='recruiter_signup'),
    path('giris-yap/', auth_views.LoginView.as_view(template_name='profiles/login.html'), name='login'),
    path('cikis-yap/', auth_views.LogoutView.as_view(), name='logout'),
    # Mainsite urls
    path('is-arayan/profil/<slug:slug>/', JobSeekerProfileView.as_view(), name='jobseeker_profile'),
    path('is-arayan/guncelle/<slug:slug>/', JobSeekerProfileUpdateView.as_view(), name='jobseeker_profile_update'),
    path('ik-uzmani/profil/<slug:slug>/', RecruiterProfileView.as_view(), name='recruiter_profile'),
    path('ik-uzmani/guncelle/<slug:slug>/', RecruiterProfileUpdateView.as_view(), name='recruiter_profile_update'),
    path("ilana-basvur/<int:job_id>/", views.apply_job_view, name="apply_job"),
]
