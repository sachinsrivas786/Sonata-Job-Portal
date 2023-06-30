from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path('', views.home, name="home"),
    path('Signup',views.Signup,name="Signup"),
    path('SignIn',views.SignIn, name='SignIn'),
    path('Login', views.Login, name="Login"),
    path('Logout',views.Logout,name="Logout"),
    path('about',views.about, name="about"),
    path('post_job/',views.post_job, name="post_job"),
    path('job_detail/<joblisting_id>/',views.job_detail,name="job_detail"),
    path('job_list',views.job_list,name="job_list"),
    path('apply_job/<joblisting_id>/',views.apply_job,name="apply_job"),
    path('appliedJob',views.appliedJob,name="appliedJob"),
    path('applied_user_details',views.applied_user_details,name="applied_user_details"),
    path('profile',views.profile,name="profile"),
    path('profile_update',views.profile_update,name="profile_update"),
    path('search',views.search,name="search"),
    path('edit_profile',views.edit_profile,name="edit_profile"),
    # HR URLs

    path('hr_view_post/',views.hr_view_post, name="hr_view_post"),
    path('update_job/',views.update_job, name="update_job"),
    path('applied_job_view/<joblisting_id>/',views.applied_job_view,name="applied_job_view"),
    
    path('applied_user_full_details/',views.applied_user_full_details,name="applied_user_full_details"),
]