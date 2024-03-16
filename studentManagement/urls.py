from django.urls import path, include


from . import views

app_name = 'studentManagementSystem'

urlpatterns = [
    path("", views.index, name='index'), 
    path("<int:student_id>", views.student_detail, name='student_detail') ,
    path("accounts/", include("django.contrib.auth.urls")),
    path("signup/", views.authView, name="signup")
]
