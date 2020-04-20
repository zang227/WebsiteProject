from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login-home'),
    path('signup/', views.signup, name='signup-page'),
    path('signup2/', views.signup2, name='signup2-page'),
    path('home/<int:applicant_id>',views.home, name='home-page'),
    path('search/<int:applicant_id>', views.search, name='search-page'),
    path('report/<int:applicant_id>', views.report, name='report-page'),
    path('profile/<int:applicant_id>', views.profile, name='profile-page'),
    path('editProfile/<int:applicant_id>', views.editProfile, name='editProfile-page'),
    path('post/<int:applicant_id>', views.post, name='post-page'),
]