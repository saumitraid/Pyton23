from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from . models import Student
# Create your views here.

def home(request):
    return render(request, 'myapp/home.html')

def about(reqest):
    allStd=Student.objects.all()
    return render(reqest, 'myapp/about.html', {'allStd':allStd})
    # return HttpResponse('<h1>About Page</h1>')

# def contact(request):
#     if request.GET:
#         name=request.GET.get('name')
#         email_id=request.GET.get('email_id')
#         # return HttpResponse('<h1>Your name is  {} and email is {}</h1>'.format(name, email_id))
#         context={'name':name, 'email_id':email_id}
#         return render(request, 'myapp/contact.html', context)
#     else:
#         return render(request, 'myapp/contact.html')

def contact(request):
    if request.POST:
        std=Student()
        std.name=request.POST.get('name')
        std.email_id=request.POST.get('email_id')
        std.city=request.POST.get('city')
        try:
            std.save()
            messages.success(request, 'Student data save successfully')
        except Exception as e:
            messages.error(request, 'Student data not save successfully')
        return render(request, 'myapp/contact.html')
    else:
        return render(request, 'myapp/contact.html')

def deleteData(request, id):
    try:
        Student.objects.filter(id=id).delete()
        messages.success(request, 'Student data delete successfully')
    except Exception as e:
        messages.error(request, 'Student data not delete successfully')
    return redirect('/about')