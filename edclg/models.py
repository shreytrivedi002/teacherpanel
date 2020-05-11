from django.db import models






class Teachers(models.Model):
    name = models.CharField(max_length=50)
    institution = models.CharField(max_length=150)
    email = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Courseupdate(models.Model):
    unqid = models.TextField(max_length=50)
    title = models.CharField(max_length=60)
    subject = models.CharField(max_length=50)
    desc = models.CharField( max_length=100)
    email = models.CharField(max_length=50)
    file = models.FileField(upload_to='media')
    def __str__(self):
        return self.email +"       |       "+ self.unqid


class pdfstore(models.Model):

    teacheremail = models.CharField(max_length=100)
    unqid = models.TextField(max_length=50)
    file = models.FileField(upload_to='media')
    date = models.DateTimeField(auto_now_add=True)
    unid = models.ForeignKey(Courseupdate,on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.teacheremail +"     |     " + self.unqid


