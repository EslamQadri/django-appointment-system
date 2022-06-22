from django.contrib import admin
from .models import appointments
# Register your models here.
@admin.register(appointments)
class appointmentsAdmin(admin.ModelAdmin):
      list_display=['user','Reserve','Cancel','approve','make_as_missed','make_as_finished']