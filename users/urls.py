from django.urls import path
from . import views  # Import your views file

urlpatterns = [
    path('signup/', views.signup, name='signup'),  # Signup page
    path('login/', views.login_view, name='login'),  # Login page (updated to match the function name)
    path('logout/', views.logout_view, name='logout'),
    path('logout/', views.logout_view, name='logout'),  # Use logout_view instead of user_logout
    path('doctor-dashboard/', views.doctor_dashboard, name='doctor_dashboard'),  # Doctor's dashboard
    path('patient-dashboard/', views.patient_dashboard, name='patient_dashboard'),  # Patient's dashboard
]
