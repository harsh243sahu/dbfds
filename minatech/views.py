from django.shortcuts import render,redirect
from . models import *
from django.contrib.auth.models import User , auth 
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def register(request):
    return render(request,'register.html')
# def contact(request):
#     return render(request,'contact.html')

def contact(request):
    if request.method=="POST":
        print(request)
        name=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        phone=request.POST['phone']
        desc=request.POST['desc']
        print(name,lastname,email)
        obj=Contact(name=name,email=email,phone=phone,desc=desc).save()
        return redirect('/contact')
    else:
        return render(request, "contact.html")

def course(request):
    a=courses.objects.all()
    context={'data':a}
    return render(request,'courses.html',context)
def blog(request):
    b=blogs.objects.all()
    context={'data':b}
    return render(request,'blog.html',context)

def singleBlog(request,id):
    obj = blogs.objects.get(id=id)
    context = {
        'singleBlog': obj
    }
    return render(request,'blog.html',context)

def singleCourse(request,id):
    obj = courses.objects.get(id=id)
    courseContentList  = courseContent.objects.filter(course=obj)
    context={
        'videoContent':courseContentList.first(),
        'Singledata':obj,
        'singleCourseView':True,
        'courseContentList':courseContentList,
        'playerView':True   
    }   
    return render(request,'courses.html',context)


def courseTimeline(request,id):
    obj = courseContent.objects.get(id=id)
    courseContentList = courseContent.objects.filter(course=obj.course)
    context = {
        'videoContent':obj,
        'courseContentList':courseContentList,
        'playerView':True
    }
    return render(request,'courses.html',context)


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.info(request,'login Successfull!!')
            return redirect('/')
        else:
            messages.info(request,'invlaid credentails')
            return redirect('/')


def register(request):
    if request.method == "POST":
        first = request.POST['first_name']
        last = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(first_name=first,last_name=last,username=username,password=password,email=username,is_superuser=False)
        messages.info(request,'registration successful!!')
        auth.login(request,user)
        return redirect('/')

def logout(request):
    auth.logout(request)
    return redirect('/')