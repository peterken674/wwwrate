from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm, NewProjectForm, UpdateProfileForm
from django.contrib import messages
from .models import Project, Review

# Create your views here.
def index(request):

    projects = Project.objects.all()
    if request.method == 'POST':
        upload_form = NewProjectForm(request.POST, request.FILES)
        if upload_form.is_valid():
            upload_form.instance.owner = request.user.profile
            upload_form.save()

            return redirect('index')

    else:
        upload_form = NewProjectForm()



    context = {'upload_form': upload_form, 'projects':projects}
    return render(request, 'index.html', context)

def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')

    else:

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Username or password is incorrect.')

    context = {}
    return render(request, 'auth/login.html', context)

def register_user(request):
    if request.user.is_authenticated:
        return redirect('/')

    else:
        form = CreateUserForm()
        title = 'New Account'

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')

    context = {'form': form, 'title': title}
    return render(request, 'auth/register.html', context)

def logout_user(request):
    logout(request)
    return redirect('login')


def profile(request):

    my_projects = Project.objects.all().filter(owner=request.user.profile)

    if request.method == 'POST':
        update_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if update_form.is_valid:
            update_form.save()
    else:
        update_form = UpdateProfileForm()

    context = {'update_form':update_form}
    
    return render(request, 'profile.html', context)

def project(request, project_id):

    project = Project.objects.get(id=project_id)
    reviews = Review.objects.all().filter(project=project)

    context = {'project': project, 'reviews':reviews}

    return render(request, 'project.html', context)
