from django.contrib import admin
from myapp.models import student
# Register your models here.
#admin.site.register(student)

class studentAdmin(admin.ModelAdmin):
    list_display=('id','Name','Sex','Birth','Email','Phone','Home_Address')
    list_filter = ('Name','Sex')
    search_fields = ('Name',)
    ordering = ('id',)

admin.site.register(student,studentAdmin)