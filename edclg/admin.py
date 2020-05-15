from django.contrib import admin
from .models import Teachers,Courseupdate,pdfstore,comments,userpermission,student_list_byteach,student_attend
 


# Register your models here.

admin.site.register(Teachers)
admin.site.register(Courseupdate)
admin.site.register(pdfstore)
admin.site.register(comments)
admin.site.register(userpermission)
admin.site.register(student_list_byteach)
admin.site.register(student_attend)



