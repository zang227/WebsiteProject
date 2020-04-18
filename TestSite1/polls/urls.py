from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login-home'),
    path('signup/', views.signup, name='signup-page'),
    path('signup2/', views.signup2, name='signup2-page'),
    path('home/',views.home, name='home-page'),
    path('search/', views.search, name='search-page'),
    path('report/', views.report, name='report-page'),
    path('profile/', views.profile, name='profile-page'),
]