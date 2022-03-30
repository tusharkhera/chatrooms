from dateutil import tz
from django.shortcuts import render, HttpResponseRedirect
from django.views import View
import pytz
from .models import *
from .forms import GroupForm, JoinForm, SignUpForm, MyAuthenticationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm , PasswordResetForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.utils.crypto import get_random_string




# Create your views here.
def index(request, group_id) :
    if request.user.is_authenticated :
        grp = Group.objects.filter(unique_id=group_id).first()
        chats = []
        u_id = group_id
        g_name = Group.objects.get(unique_id=group_id).name
        admin = Group.objects.get(unique_id=group_id).admin
        print(admin)
        if grp :
            chats = Chat.objects.filter(group=grp)
        else:
            pass

        return render(request, 'index.html', {'g_name' : g_name, 'g_id' : u_id, 'chats':chats, 'admin':admin})
    else:
        return HttpResponseRedirect('/login/')



def home(request) :
    return render(request, 'home.html')

def createRoom(request) :
    if request.user.is_authenticated :
        if request.method == 'GET' :
            fm = GroupForm()
            return render(request, 'createRoom.html', {'form':fm})
        else:
            u_id = get_random_string(32)
            grp = Group(name = request.POST.get('group'), unique_id = u_id, admin=request.user)
            grp.save()
            ins = Group.objects.get(unique_id = u_id)
            db = ChatList(chat_user=request.user, grp= ins)
            db.save()
            return HttpResponseRedirect('/room/' + u_id + '/')
    else:
        return HttpResponseRedirect('/login/')


def joinRoom(request) :
    if request.user.is_authenticated :
        if request.method == 'GET' :
            fm = JoinForm()
            return render(request, 'joinRoom.html', {'form':fm})
        else:
            ins = Group.objects.get(unique_id = request.POST.get('room_id'))
            if not ChatList.objects.filter(chat_user=request.user, grp= ins) :
                db = ChatList(chat_user=request.user, grp= ins)
                db.save()
            u_id = request.POST.get('room_id')
            return HttpResponseRedirect('/room/' + u_id + '/')
    else:
        return HttpResponseRedirect('/login/')
    
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

def chats(request) :
    if request.user.is_authenticated :
        chats = ChatList.objects.filter(chat_user=request.user)
        last_msg = []
        last_msg_time = []
        for x in chats :
            temp = Chat.objects.filter(group=x.grp).last()
            last_msg.append(temp.content)
            last_msg_time.append(temp.timestamp.astimezone(pytz.timezone('Asia/Kolkata')).strftime("%H:%M"))
        print(last_msg_time)
        return render(request, 'chatlist.html', {'chats':chats, 'l_msg':last_msg, 'l_m_time':last_msg_time})
    else:
        return HttpResponseRedirect('/login/')

def delete_room(request) :
    print(request.POST.get('grp-id'))
    ins = Group.objects.get(unique_id = request.POST.get('grp-id'))
    ins.delete()
    return HttpResponseRedirect('/')