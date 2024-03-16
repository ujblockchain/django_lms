from django.contrib import admin

from .models import Student, Mentor, BankDetails, Course

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'email', 'is_registered')
    search_fields = ('first_name', 'last_name', 'age')
    list_filter = ('is_registered', 'age')

admin.site.register(Student, StudentAdmin)
admin.site.register(Mentor)
admin.site.register(BankDetails)
admin.site.register(Course)
