from django.db import models
from django.contrib.auth.models import User





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
    unid = models.ForeignKey(Courseupdate,on_delete=models.CASCADE)
    def __str__(self):
        return self.teacheremail +"     |     " + self.unqid


class comments(models.Model):
    unqid = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=50,blank=True)
    message = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name + "&" + self.email



class userpermission(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    teachercheck = models.BooleanField(default=False)
    teacher_attendenceperm = models.BooleanField(default=False) 
    usern = models.CharField(max_length=100,blank=True)
    def __str__(self):
        return self.user.username



class student_list_byteach(models.Model):
    name = models.CharField(max_length=50,blank=True)
    email = models.EmailField(max_length=254)
    college = models.CharField(max_length=50,blank=True)
    temail = models.EmailField(max_length=254,default='teacher email here')


    def __str__(self):
        return self.name
    




class student_attend(models.Model):
    semail = models.EmailField(max_length=254,blank=True)
    temail = models.EmailField(max_length=254,blank=True)
    date = models.DateField(auto_now_add=True)
    present = models.BooleanField(default=False)
    def __str__(self):
        return self.semail
     