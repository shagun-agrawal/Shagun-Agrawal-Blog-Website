from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .forms import UserForm,Login,DataForm
from .models import User,Data
from django.urls import reverse_lazy
from django.contrib import messages
# Create your views here.
def home(request):
    form=Data.objects.all()
    return render(request, 'home.html',{'form':form})
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def login(request):
    if request.method == 'POST':
        form=Login(request.POST)
        if form.is_valid():
            email=form.cleaned_data.get('email')
            password=form.cleaned_data.get('password') 
            # user = authenticate(username=username , password=password)
            try:
                user=User.objects.get(email=email, password=password)
                      
              
                return render(request,'reffer.html')
            except(User.DoesNotExist):
                messages.warning(request,'! Email or password did not match')
                # return redirect(reverse_lazy('login'))
        else:
            messages.warning(request,'!Enter A Valid Email')
    else:
        form=Login()
    return render(request,'login.html',{'form':form})

def dashboard(request):
    if request.method=='POST':
        form=DataForm(request.POST, request.FILES)
        form.save()
        stud = Data.objects.all()
        return render(request,'showupdate.html',{'stu':stud})
    else:
        form = DataForm()
    return render(request, 'dashboard.html', {'form':form})
def signup(request):
    if request.method == 'POST':
        form=UserForm(request.POST)
       # print(form)
        
        if form.is_valid():
            email=form.cleaned_data.get('email')
            birthdate=form.cleaned_data.get('birthdate')
            try:
                user=User.objects.get(email=email, birthdate=birthdate)
                messages.warning(request,'!This Email Is Already Exixt')
            except(User.DoesNotExist):
                form.save()
                messages.success(request,'Congratulation! Your Account Has Been Created')

    else:
        form=UserForm()
    return render(request,'signup.html',{'form':form})
def showform(request):
    stud = Data.objects.all()
    return render(request,'showupdate.html',{'stu':stud})
def deletefun(request, id):
    dl=Data.objects.get(pk=id)
    dl.delete()
    stud = Data.objects.all()
    return render(request,'showupdate.html',{'stu':stud})
    
def update(request, id):
    task=Data.objects.get(pk=id)
    if request.method == 'POST':
           form=DataForm(request.POST, request.FILES, instance=task)
           image=request.POST.get('photo')
           print(image)
           if form.is_valid():
               form.save()
               stud = Data.objects.all()
               return render(request,'showupdate.html',{'stu':stud})
    else:
           form=DataForm(instance=task)
    context={'form':form}
    return render(request,'update.html',context)
    
