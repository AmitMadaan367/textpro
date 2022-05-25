from django.shortcuts import render

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# from .models import *
from django.contrib.auth.models import User

from ab.forms import *



def index(request):
    return render(request, 'index.html')

data=None
dict_graph=None

@login_required
def userdash(request):
    
    return render(request, 'userdashboard.html',{"work":"True"})



def signup_page(request):
    if request.method=="POST":
        form=signupform(request.POST)
        if form.is_valid():
            name=request.POST["Name"]
            email=request.POST["Email"]
            password=request.POST["Password"]
            Firstname=request.POST["Firstname"]
            lastname=request.POST["lastname"]
            user = User.objects.create_user(username=name,email=email,password=password,first_name=Firstname,last_name=lastname)
            user.save()
            return redirect('/signin/')
    else:
        form = signupform()
        print("notdshksfdhjsdfhsdfahlsafd")
    return render(request,'signup.html',{"form":form})





def login_user(request):
    if request.user.is_authenticated:
        print("Logged in")
        return redirect("/userdash/")
    else:
        print("Not logged in")

    if request.method == 'POST':
        form = loginform(request.POST)
        if form.is_valid():
            username = request.POST.get('Username')
            print(username)
            password = request.POST.get('Password')
            print(password)
            user = authenticate(username=username, password=password)
            if user:
                print("yesssssssssssssssss")
                login(request,user)
                return redirect("/userdash/")

    else:
        form = loginform()
        print("not")
    return render(request, 'signin.html', {"form": form})



@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })

@login_required
def user_logout(request):
    logout(request)
    return redirect('/signin/')



def read(request):
    
    return redirect("/userdash/")





from io import BytesIO
import base64
import matplotlib.pyplot as plt
import numpy as np


def showimage(request):
    global dict_graph
    data5=[]
    for i,key in enumerate(dict_graph):
        if i==0:
            continue
    #     print(dict_graph[key])    
        plt.figure(figsize=(7,7))
        plt.pie(dict_graph[key],labels=[key+'\nhighlighted',key+'\nunhighlighted'],shadow=True,autopct='%1.1f%%');
    #     print(key)
    #     g.show()
        if key == 'total':
            print("yes")
            plt.title('Total HighLighted v/s Total UnHighLighted')
        else:
            print("no")
            plt.title(f'{key.capitalize()} HighLighted v/s {key.capitalize()} UnHighLighted')


        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()

        graphic = base64.b64encode(image_png)
        graphic = graphic.decode('utf-8')
        data5.append(graphic)
    return render(request, 'show.html',{'data5':data5})







