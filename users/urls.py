from django.urls import path
from . import views  # Import your views file

urlpatterns = [
    path('', views.landing_page, name='landing_page'),  # Landing page (root path)
    path('signup/', views.signup, name='signup'),  # Signup page
    path('login/', views.login_view, name='login'),  # Login page
    path('logout/', views.logout_view, name='logout'),  # Logout page
    path('doctor-dashboard/', views.doctor_dashboard, name='doctor_dashboard'),  # Doctor's dashboard
    path('patient-dashboard/', views.patient_dashboard, name='patient_dashboard'),  # Patient's dashboard
]
