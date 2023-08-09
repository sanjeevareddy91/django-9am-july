from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Team_Info,RegisteredUser
from .forms import Team_InfoModelForm,TeamInfoForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views import View
# Create your views here.

# Function Based Views
def hello_world(request):
    return HttpResponse("Hello World!")

def first(request):
    return render(request,'first.html')

def register(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('psw')
        print(email,password)
    return render(request,'register.html')

def add_team(request):
    if request.method == "POST":
        # 1st way
        team_name = request.POST.get('team_name')
        nick_name = request.POST.get('nick_name')
        captain_name = request.POST.get('captain_name')
        started_year = request.POST.get('started_year')
        team_logo = request.FILES.get('team_logo')
        # print(team_logo,team_name,captain_name)
        # Team_Info.objects.create(team_name=team_name,nick_name=nick_name,captain_name=captain_name,started_year=started_year,team_logo=team_logo)

        # Alternating Way
        data = {keys:request.POST[keys] for keys in request.POST if keys != 'csrfmiddlewaretoken'}
        data['team_logo'] = request.FILES.get('team_logo')
        Team_Info.objects.create(**data)
        messages.success(request,f"{team_name} added to the IPL Teams List")
        return redirect('list_team')
    return render(request,'add_team.html')

def list_team(request):
    all_data = Team_Info.objects.all()
    return render(request,'list_team.html',{'data':all_data})


def update_team(request,id):
    team_data = Team_Info.objects.get(id=id)
    print("data")
    if request.method == "POST":
        # 1st Way
        # team_name = request.POST.get('team_name')
        # nick_name = request.POST.get('nick_name')
        # captain_name = request.POST.get('captain_name')
        # started_year = request.POST.get('started_year')
        # team_logo = request.FILES.get('team_logo')
        # team_data.team_name = team_name
        # team_data.nick_name = nick_name
        # team_data.captain_name = captain_name
        # team_data.started_year = started_year
        # if team_logo:
        #     team_data.team_logo = team_logo
        # team_data.save()

        # Alternate Way
        data = {keys:request.POST[keys] for keys in request.POST if keys != 'csrfmiddlewaretoken'}
        if request.FILES.get('team_logo'):
            data['team_logo'] = request.FILES.get('team_logo')
        Team_Info.objects.filter(id=id).update(**data)
        messages.success(request,"Team Updated")
        return redirect('list_team')
    return render(request,'update_team.html',{'data':team_data})

def delete_team(request,id):
    data = Team_Info.objects.get(id=id)
    print(data)
    data.delete()
    return redirect('list_team')

def team_modelform(request):
    if request.method == "POST":
        form = Team_InfoModelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            return HttpResponse("Data invalid")
        return redirect('list_team')
    else:
        form = Team_InfoModelForm()
    return render(request,'model_form.html',{'form':form})

def team_info_form(request):
    if request.method == "POST":
        form = TeamInfoForm(request.POST,request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            Team_Info.objects.create(**data)
            return HttpResponse("Team Added")
        else:
            return HttpResponse("Form invalid")
    else:
        form = TeamInfoForm()
    return render(request,'normal_form.html',{'form':form})
    
def register_user(request):
    if request.method == "POST":
        data = {keys:request.POST[keys] for keys in request.POST if keys != 'csrfmiddlewaretoken'}
        print(data)
        data['username'] = data['email'].split('@')[0] # sanjeev@gmail.com --> ['sanjeev','gmail.com']
        print(data)
        user_data = User(username=data['username'],email=data['email'])
        user_data.set_password(data['password'])
        user_data.save()
        RegisteredUser.objects.create(mobile=data['mobile'],user=user_data)
        messages.success(request,"User added successfully!")
        return redirect('login_user')
    return render(request,'register_user.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user_data = User.objects.filter(username=username) | User.objects.filter(email=username)
        # import pdb;pdb.set_trace()
        if user_data:
            print(user_data)
            username = user_data[0].username
            # username = user_data.first().username
            user = authenticate(username=username,password=password)
            if user:
                login(request,user)
                messages.success(request,f"{user.username} loggedin successfully")
                return redirect('list_team')
            else:
                messages.error(request,"username and password not matched")
        else:
            messages.error(request,'No account existed with username or email')
        # import pdb;pdb.set_trace()
    return render(request,'login.html')


# Class Based Views:

class HelloView(View):
    def get(self,request):
        return HttpResponse("Hello World!")

# 1st way
# class RegisterView(View):
#     def get(self,request):
#         return render(request,"register.html")

# 2nd Way

from django.views.generic.base import TemplateView

class RegisterView(TemplateView):
    template_name = 'register.html'


# CreateView

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class TeamCreateView(CreateView):
    model  = Team_Info
    fields = "__all__"
    success_url = reverse_lazy('list_team')


# ListView
from django.views.generic.list import ListView

class TeamListView(ListView):
    model  = Team_Info


# DetailView

from django.views.generic.detail import DetailView

class TeamDetailView(DetailView):
    model  = Team_Info


# UpdateView

from django.views.generic.edit import UpdateView

class TeamUpdateView(UpdateView):
    model  = Team_Info
    fields = "__all__"
    success_url = reverse_lazy('list_team')

# DeleteView

from django.views.generic.edit import DeleteView

class TeamDeleteView(DeleteView):
    model  = Team_Info
    fields = "__all__"
    success_url = reverse_lazy('list_team')

# Django Rest Framework


# HTTP Methods:
    # GET
    # POST
    # PUT
    # DELETE


# Function Based APIS
@api_view(['GET','POST'])
def rest_hello(request):
    if request.method == "GET":
        return Response({'message':"Hello World!"})
    else:
        return Response(request.data)

@api_view(['GET','POST'])
def add_team_api(request):
    if request.method == "GET":
        # data = Team_Info.objects.all()
        # import pdb;pdb.set_trace()
        # print(data)
        # team_data = []
        # for ele in data:
        #     dict_data = {}
        #     dict_data['team_name'] = ele.team_name
        #     dict_data['nick_name'] = ele.nick_name
        #     dict_data['captain_name'] = ele.captain_name
        #     dict_data['started_year'] = ele.started_year
        #     team_data.append(dict_data)

        # 2nd way
        data = Team_Info.objects.values()
        return Response({"status":"success","teams":data})
    else:
        data = request.data
        if len(data['team_name'])>30 or len(data['nick_name'])>4:
            return Response({"message":"Data is invalid"})
        
        Team_Info.objects.create(**data)
        return Response({
            'message':"Team Added Successfully",
            "team":data
        })

@api_view(['GET','PUT','DELETE'])
def team_get_update_delete_api(request,id):
    data = Team_Info.objects.filter(id=id)
    if request.method == "GET":
        data = data.values()
        if data:
            return Response({'message':"GET Successful","data":data[0]})
        else:
            return Response({'message':"Team with this ID doesnot exist"})
    elif request.method == "PUT":
        if data:
            data.update(**request.data)
            return Response({
                'message':"Team Updated Successfully",
                "team": request.data
            })
        else:
            return Response({'message':"Team with this ID doesnot exist"})
    elif request.method == "DELETE":
        if data:
            data.delete()
            return Response({
                'message':"Team Deleted Successfully",
            })
        else:
            return Response({'message':"Team with this ID doesnot exist"})