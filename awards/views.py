from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import  ProfileUpdateForm, ProjectForm
from .models import Profile, Project
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer, ProjectSerializer
from rest_framework import status
# from .permissions import IsAdminOrReadOnly

# Create your views here.

def index(request):
    context = {
        'projects': Project.objects.all(),
        
    }
    
    return render(request, 'index.html', context)

@login_required(login_url='/accounts/login/')
def my_profile(request):
    projects = Project.objects.all()
    user= request.user
    return render(request, 'myprofile.html', locals())

@login_required(login_url='/accounts/login/')
def user_profile(request, user_id):
    user_new=get_object_or_404(User, pk=user_id)
    projects = Project.get_profile_projects(user_id)
    if request.user == user_new:
        return redirect('myaccount')
    return render(request, 'profile.html', locals())
        
   
    
@login_required(login_url='/accounts/login/')
def update_profile(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if  p_form.is_valid():
           
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('myaccount')

    else:
       
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        
        'p_form': p_form
    }

    return render(request, 'update_profile.html', context)
@login_required(login_url='/accounts/login/')  
def upload_project(request):
    user = request.user
    print(user)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit = False)
            project.user = user
            project.save()
            print(project.user)
            return redirect('welcome')
    else:
        form = ProjectForm()
    return render(request, "upload_project.html", {"form":form})
class ProfileList(APIView):
    # permission_classes = (IsAdminOrReadOnly,)
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)

class ProjectList(APIView):
    # permission_classes = (IsAdminOrReadOnly,)
    def get(self, request, format=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)

def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_project(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})