from django.contrib import admin

from .models import Grade, GradeType, GradeField, Option

admin.site.register(GradeType)
admin.site.register(GradeField)
admin.site.register(Option)
admin.site.register(Grade)
