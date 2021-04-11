from django.shortcuts import render, redirect

from .forms import SignUpForm, LoginForm

from django.contrib.auth import login, authenticate, logout


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'ConstructionReporter/index.html', )
    else:
        return redirect('/cr')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'ConstructionReporter/signup.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'ConstructionReporter/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'ConstructionReporter/index.html', )
