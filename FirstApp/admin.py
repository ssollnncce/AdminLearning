from django.contrib import admin
from .models import teacher, faculty, course

admin.site.register(faculty)

# Register your models here.

#admin.site.register(teacher)
# Define the admin class
class teacherAdmin(admin.ModelAdmin) :
    list_display = ('first_name', 'last_name', 'date_of_birth')
# Register the admin class with the associated model
admin.site.register(teacher, teacherAdmin)

#admin.site.register(course)
# Define the admin class
class courseAdmin(admin.ModelAdmin) :
    list_display = ('title', 'teacher', 'display_faculty')
# Register the admin class with the associated model
admin.site.register(course, courseAdmin)
