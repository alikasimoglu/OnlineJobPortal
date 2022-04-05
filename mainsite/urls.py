from django.urls import path

from mainsite.views.index import IndexView

app_name = 'mainsite'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
