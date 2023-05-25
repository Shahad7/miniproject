from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseForbidden,JsonResponse
from django.urls import reverse
from django.contrib.auth import login,logout,authenticate
from .models import Book,myuser,Library,Rent
import json
from django.core.mail import send_mail
from . import cron
# Create your views here.
def index(request):
    if request.method == "GET":      
        return render(request,'hello/index.html')
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        username = str(data['username'])
        password = str(data['password'])
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return JsonResponse({"result":"true","role":user.role})   
        else:
            return JsonResponse({"result":"false"})

def student(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            if request.user.role == 'STUDENT':
                return render(request,'hello/student.html')
            else:
                return HttpResponseForbidden()
        else:
            return HttpResponseForbidden()

    

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('hello:index'))

def librarian(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            if request.user.role == 'LIBRARIAN':
                return render(request,'hello/librarian.html')
            else:
                return HttpResponseForbidden()
        else:
            return HttpResponseForbidden()
        
    if request.method == "POST":
        title = request.POST["title"]
        author = request.POST["author"]
        stock = request.POST["stock"]
        if "image" in request.FILES:
            photo = request.FILES["image"]
        else:
            photo = None
        libid = request.user.libid
        book = Book(title=title,author=author,photo=photo,stock=stock,libid=libid)
        book.save()
        return HttpResponseRedirect(reverse('hello:librarian'))

def delete(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        bid = int(data['bid'])
        book = Book.objects.get(id=bid)
        if book.photo:
            book.photo.delete()
        book.delete()
        return HttpResponseRedirect(reverse('hello:librarian'))

def retrieve(request):
    return JsonResponse(list(Book.objects.all().filter(libid=request.user.libid).values()),safe=False)

def signup(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        name = request.POST["name"]
        email = request.POST["email"]
        role = 'STUDENT' 
        lid = int(request.POST["library"])
        user = myuser.objects.create_user(username=username,password=password,name=name,
        email=email,role=role,libid=lid)
        user.save()
        return HttpResponseRedirect(reverse("hello:index"))
    else:
        return render(request,'hello/signup.html',{
            'library':Library.objects.all()
        })

def libup(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        name = request.POST["name"]
        email = request.POST["email"]
        lname = request.POST["library"]
        role = 'LIBRARIAN'
        lib = Library(name=lname)
        lib.save()
        lid = lib.id
        user = myuser.objects.create_user(username=username,password=password,
        name=name,email=email,role=role,libid=lid)
        user.save()
        return HttpResponseRedirect(reverse("hello:index"))
    else:
        return render(request,'hello/libup.html')

def rent(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        bid = int(data['bid'])
        sid = int(request.user.id)
 #       book = Book.objects.get(pk=bid)
 #       student = myuser.objects.get(pk=sid)
 #       ren = Rent(bid=book,sid=student)
        ren = Rent(bid=bid,sid=sid)
        ren.save()
        book = Book.objects.get(pk=bid)
        book.stock -= 1
        book.save()
    

def mail(request):
    send_mail(
        'mail test',
        'valar morghulis',
        '',
        [''],
        fail_silently = False,
    )

    return HttpResponseRedirect(reverse('hello:login'))

def cron_view(request):
    return render(request,'hello/cron.html',{
        'count':cron.count
    })

def duplicate(request,type,value):

    if type == 'username':
        if myuser.objects.filter(username=value).exists():
            return JsonResponse({"result":"duplicate"})
        else:
            return JsonResponse({"result":"unique"})
    else:
        if Library.objects.filter(name=value).exists():
            return JsonResponse({"result":"duplicate"})
        else:
            return JsonResponse({"result":"unique"})

def updateStock(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        bid = int(data['bid'])
        value = int(data['value'])
        book = Book.objects.get(id=bid)
        book.stock = value
        book.save()
        return HttpResponseRedirect(reverse('hello:librarian'))
    