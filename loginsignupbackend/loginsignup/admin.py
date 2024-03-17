from django.contrib import admin
from .models import loginsignup

class loginsignupAdmin(admin.ModelAdmin):
    list_display = ("name", "email","password","dlnum","permitnum")


    #register Model

admin.site.register (loginsignup, loginsignupAdmin)
