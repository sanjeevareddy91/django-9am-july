from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Team_Info
from .forms import Team_InfoModelForm
from django.contrib import messages
# Create your views here.

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

def register_user(request):
    return render(request,'register_user.html')