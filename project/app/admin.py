from django.contrib import admin
from .models import StudentModel
from .models import StudentQuery
# Register your models here.
admin.site.register(StudentModel)
admin.site.register(StudentQuery)