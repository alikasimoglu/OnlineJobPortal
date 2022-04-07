from django.urls import path
from mainsite.views import IndexView, JobSeekerProfilesView, JobsView, JobDetailView, JobUpdateView, JobCreateView, \
    AppliedApplicantsView


app_name = 'mainsite'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('is-arayanlar/', JobSeekerProfilesView.as_view(), name='jobseeker_profiles'),
    path('is-ilanlari/', JobsView.as_view(), name='job_list'),
    path('is-ilanlari/ilan-detayi/<slug:slug>/', JobDetailView.as_view(), name='job_details'),
    path('is-ilanlari/ilan-guncelle/<slug:slug>/', JobUpdateView.as_view(), name='job_update'),
    path('is-ilani-ekle/', JobCreateView.as_view(), name='job_create'),
    path('ilan-basvurulari/', AppliedApplicantsView.as_view(), name='applied_applicants_list'),
]
