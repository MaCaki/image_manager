from django.contrib import admin

from .models import GradeType, GradeField, Option

admin.site.register(GradeType)
admin.site.register(GradeField)
admin.site.register(Option)
