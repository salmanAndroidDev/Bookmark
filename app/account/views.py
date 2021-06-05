from django.http import HttpResponse

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from account.forms import LoginForm, UserEditForm, ProfileEditForm
from django.contrib import messages
from account.forms import UserRegistrationForm

from account.models import Profile


def login_view(request):
    """Login view"""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Success")
                else:
                    return HttpResponse("Not activated")
            else:
                return HttpResponse("Login failed")
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


@login_required
def dashboard(request):
    """Dashboard view"""
    return render(request, 'account/dashboard.html',
                  {'section': 'dashboard'
                   })


def register(request):
    """view for user registration"""
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, 'account/registration_done.html',
                          context={'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html',
                  context={'user_form': user_form})


@login_required
def edit(request):
    """view for editin user"""
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)

        if user_form.is_valid and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully changed')
        else:
            messages.error(request, 'Error uploading your data')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,
                  'account/edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})
