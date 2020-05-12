from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from user.forms import UserRegisterForm ,contactform , reqform
from django.views.decorators.csrf import csrf_protect
from django.core.mail import send_mail
from .models import Teachers ,Courseupdate,pdfstore,comments
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login ,logout
from .forms import pdfupform
import random
import string




def createuser(request):
    if request.method == 'POST':
        email = request.POST['email']
        passp = request.POST['pass1']
        passq = request.POST['pass2']

        try:
            user_exists = User.objects.get(username=request.POST['email'])
            context = {
                'ualtaken':"Email You are Trying to Enter is Already Taken !!!"
            }
            return render(request,'clghome.html',context)
        except User.DoesNotExist:
            if passp == passq:
                user = User.objects.create_user(username=email,password=passp)
                user.save()
                return redirect('clghome')
            else:
                context={
                'nomatch':"passowrds do not match!!!"
                }
                return render(request,'clghome.html',context)










def rand():
    letters = string.ascii_letters
    kub = ( ''.join(random.choice(letters) for i in range(45)) )
    return kub




def clghome(request):
    qid = Courseupdate.objects.only('unqid')
    last_ten = pdfstore.objects.order_by('-id')[:10][::-1]#changed from course update to pdfstore
    context ={
        # 'display':Courseupdate.objects.all()
        # 'docdisplay'
        'display' : last_ten
    }
    return render(request,'clghome.html',context)



def profile(request):
    return render(request,'profile.html')









@login_required
def up(request):
    global rock
    rock = rand()
    gshock = rock
    if gshock==rock:
        global mrock
        mrock=rock


    context = {
        'id':rock,
        'data':Teachers.objects.only('name')
    }
    return render(request, 'upload.html', context )


def dashboard(request):
    return render(request, 'dashboard.html')



# def signin(request):
#     return render(request,'signin.html')


def pdf(request):
    if request.method == 'POST':
        unid = request.POST['uid']
        nam = request.POST['titl']
        sub = request.POST['subject']
        # a = request.POST['url']
        uname = request.POST['email']
        disc = request.POST['desc']
        obj = Courseupdate(unqid=unid,title=nam,subject=sub,desc=disc,email=uname)

        if obj :
            obj.save()
            form = pdfupform()
            context ={
                'form':form,
                'id':unid,#changed from mrock to unid
                'name':uname
            }
            return render(request, 'pdf.html',context)
    else:
        form = pdfupform()
        return render(request, 'upload.html', {
            'form': form
        })



def updone(request):
    g = request.POST['uid']
    temail = request.POST['teacheremail']
    geto = Courseupdate.objects.get(unqid=g)
    if request.method == 'POST':
        form = pdfupform(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.unqid = g
            instance.teacheremail = temail
            instance.unid = geto#changes here
            instance.save()
            context={
                'success':"HURRAY!!! You Uploaded a new Material For your Students"
            }
            return render(request,'dashboard.html',context)
    else:
        form = pdfupform()
        return render(request, 'upload.html', {
        'form': form
    })





def signin(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('clghome')
        else:
            context={
            'invalid':"Unable to Log you In!!! Invalid your Credentials..."
        }
        return render(request,'signin.html',context)

    else:
        context={
            # 'invalid':"Unable to Log you In!!! Check your Credentials..."
        }
        return render(request,'signin.html',context)




def signout(request):
    logout(request)
    return redirect('clghome')




def coursesingle(request,unqid,temail):
    comment = comments.objects.filter(unqid=unqid)
    count = comments.objects.filter(unqid=unqid).count()
    material = pdfstore.objects.filter(unqid=unqid)
    teacher = User.objects.filter(username=temail)
    file = pdfstore.objects.filter(teacheremail=temail)
    context = {
        'material': material,
        'teacher': teacher,
        'cmt':comment,
        'cmtcount':count,
        'files':file
    }
    return render(request,'course-single.html',context)






def commentsave(request):
    uid = request.GET['uid']
    name = request.GET['name']
    email = request.GET['email']
    subject = request.GET['subject']
    message = request.GET['message']
    instance = comments(unqid=uid,name=name,email=email,subject=subject,message=message)
    if uid != '' and name != '' and email != '' and message !='':
        instance.save()
        return redirect('clghome')