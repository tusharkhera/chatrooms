from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from .models import *
from .forms import GroupForm, SignUpForm, MyAuthenticationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm , PasswordResetForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Create your views here.
def index(request, group_name) :
    grp = Group.objects.filter(name=group_name).first()
    chats = []
    if grp :
        chats = Chat.objects.filter(group=grp)
    else:
        grp = Group(name = group_name)
        grp.save()

    return render(request, 'index.html', {'g_name' : group_name, 'chats':chats})

def home(request) :
    if request.method == 'GET' :
        fm = GroupForm()
        return render(request, 'home.html', {'form':fm})
    else:
        return HttpResponseRedirect('/room/' + request.POST.get('group') + '/')
    
class SignUpView(View) :
    def get(self,request):
        if not request.user.is_authenticated :
            fm = SignUpForm()
            return render(request, 'signUp.html', {'form':fm})
        else:
            return HttpResponseRedirect('/')
    def post(self,request):
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account created successfully !!')
            fm.save()    
        return render(request, 'signUp.html', {'form':fm})

def log_in(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = MyAuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully')
                    return HttpResponseRedirect('/')
        else:            
            fm = MyAuthenticationForm()
        return render(request, 'login.html', {'form':fm})
    else:
        return HttpResponseRedirect('/')    

def log_out(request):
    logout(request)
    return HttpResponseRedirect('/login/')