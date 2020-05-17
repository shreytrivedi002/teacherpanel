from django import template
from edclg.models import student_attend,student_list_byteach
from time import gmtime, strftime
from datetime import date

register = template.Library()

@register.filter
def filterlist(indexable, i):
    return indexable[i]
    
@register.simple_tag
def button_check(teacher_email, student_email):
    # [:1][::-1]
        # show = strftime("%Y-%m-%d", gmtime())

    today = date.today()
    attendence_list = student_attend.objects.filter(semail=student_email,temail=teacher_email).order_by('-id').filter(date__year=today.year,date__month=today.month,date__day=today.day)
    if attendence_list:
        for a in attendence_list:
            if a.date == today:
                val = a.present
                if val:
                    return val
                else:
                    val = 'lol'
                    return val
            
        else:
            val = 'lol'
            if val:
                return val
            else:
                val = 'lol'
                return val
    else:
        val = 'lol'
        return val


@register.simple_tag
def studentdetail(username):
    ins = student_list_byteach.objects.filter(email=username)
    return ins
    