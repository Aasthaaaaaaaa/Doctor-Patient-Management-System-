from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    # Directly reference the 'usertype' field if it's a valid field in the model
    list_display = ['username', 'first_name', 'last_name', 'email', 'usertype', 'is_staff', 'is_active']

    # OR create a custom method to display the user type
    def user_type_display(self, obj):
        return obj.get_user_type_display()  # This will return the display name ('Doctor' or 'Patient')
    
    user_type_display.short_description = 'User Type'  # Optional: Set the label for this field in the admin

    # Add this method to list_display if you want to display the user type as a human-readable value
    list_display = ['username', 'first_name', 'last_name', 'email', 'user_type_display', 'is_staff', 'is_active']

# Register the CustomUser model and the CustomUserAdmin class
admin.site.register(CustomUser, CustomUserAdmin)
