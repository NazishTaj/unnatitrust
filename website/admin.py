from django.contrib import admin
from .models import Gallery

admin.site.register(Gallery)
from .models import StudentRegistration

@admin.register(StudentRegistration)
class StudentRegistrationAdmin(admin.ModelAdmin):
    list_display = ("First_Name", "Last_Name", "phone", "course", "created_at")
    search_fields = ("First_Name", "Last_Name", "phone")


admin.site.site_header = "Unnati Trust Admin"
admin.site.site_title = "Unnati Admin Panel"
admin.site.index_title = "Welcome to Unnati Admin Dashboard"
