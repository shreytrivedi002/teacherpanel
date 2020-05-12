from django.contrib import admin
from .models import Teachers,Courseupdate,pdfstore,comments
 


# Register your models here.

admin.site.register(Teachers)
admin.site.register(Courseupdate)
admin.site.register(pdfstore)
admin.site.register(comments)
