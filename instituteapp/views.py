from django.shortcuts import render
from .models import Course,FeedbackData,ContactData
from .forms import FeedbackForm
from django.http import HttpResponse

def home(request):
    return render(request,'inhe_home.html')

def contact(request):
    if request.method=='POST':
        data=ContactData(name=request.POST.get('name'),
                    email=request.POST.get('email_id'),
                    mobile=request.POST.get('mobile'),
                    comments=request.POST.get('message'),
                    )
        data.save()
        return render(request,'callyou.html')
    return render(request,'inhe_contact.html')

def services(request):
    data = Course.objects.all()
    return render(request, 'inhe_services.html', {'data': data})


import datetime
date1 = datetime.datetime.now()

def gallery(request):
    return render(request,'inhe_gallery.html')


def feedbacks(request):
    if request.method=="POST":
        fform=FeedbackForm(request.POST)
        if fform.is_valid():
            name1=request.POST.get('Name')
            rating1=request.POST.get('Rating')
            feedback1=request.POST.get('Feedback')

            data =FeedbackData(
                name=name1,
                rating=rating1,
                date=date1,
                feedback=feedback1
            )
            data.save()
            fform=FeedbackForm()
            feedback=FeedbackData.objects.all()
            return render(request,'inhe_feedbacks.html',{'fform':fform ,'Feedbacks':feedback})
        else:
            return  HttpResponse("user missed some values")
    else:
        fform = FeedbackForm()
        feedback = FeedbackData.objects.all()
        print(feedback)
        return render(request, 'inhe_feedbacks.html',{'fform':fform,'Feedbacks':feedback})
