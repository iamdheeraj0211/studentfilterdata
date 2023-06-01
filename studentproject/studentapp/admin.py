from django.contrib import admin
from .models import Student, Marks
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    class Meta:
        model = Student
        list_display = "__all__"


admin.site.register(Student, StudentAdmin)


class MarksAdmin(admin.ModelAdmin):
    class Meta:
        model = Marks
        list_display = "__all__"


admin.site.register(Marks, MarksAdmin)
