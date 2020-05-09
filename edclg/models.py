from django.db import models






class Teachers(models.Model):
    name = models.CharField(max_length=50)
    institution = models.CharField(max_length=150)
    email = models.CharField(max_length=100)
    





class pdfstore(models.Model):
    unqid = models.TextField(max_length=50)
    file = models.FileField(upload_to='media')
    date = models.DateTimeField(auto_now_add=True)






class Courseupdate(models.Model):
    unqid = models.TextField(max_length=50)
    title = models.CharField(max_length=60)
    subject = models.CharField(max_length=50)
    desc = models.CharField( max_length=100)
    name = models.CharField(max_length=50)
    file = models.FileField(upload_to='media')




