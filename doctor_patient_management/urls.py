from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from users import views  # Import the home view from the users app

urlpatterns = [
    path('admin/', admin.site.urls),         # Admin site URLs
    path('users/', include('users.urls')),  # Include the users app URLs for signup, login, etc.
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

