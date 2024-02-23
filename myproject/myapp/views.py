from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'myapp/home.html')

def about(reqest):
    return render(reqest, 'myapp/about.html')
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
        name=request.POST.get('name')
        email_id=request.POST.get('email_id')
        # return HttpResponse('<h1>Your name is  {} and email is {}</h1>'.format(name, email_id))
        context={'name':name, 'email_id':email_id}
        return render(request, 'myapp/contact.html', context)
    else:
        return render(request, 'myapp/contact.html')
