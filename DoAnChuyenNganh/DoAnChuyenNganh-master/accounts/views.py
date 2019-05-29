from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import ExtendedUserCreationForm, UserProfileForm
from django.apps import apps
from .models import UserProfile
from django.contrib.auth.models import User


def home(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = 'not logged in'
    user_information = apps.get_model('polls', 'UserInfo')
    user_tutor = UserProfile.objects.filter(account_type='T')
    user_academy = UserProfile.objects.filter(account_type='A')

    userTutor = []
    for tutor in user_tutor:
        tutorName = User.objects.filter(username=tutor)
        tutorInfo = user_information.objects.filter(username__user__username=tutor)
        userTutor.append(tutorInfo)

    userAcademy = []
    for academy in user_academy:
        academyName = User.objects.filter(username=academy)
        academyrInfo = user_information.objects.filter(username__user__username=academy)
        userAcademy.append(academyrInfo)

    context = {'username': username, 'tutor': userTutor, 'academy': userAcademy, 'tutorName': tutorName, 'academyName': academyName}
    return render(request, 'homepage.html', context)


def signup(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('home')
    else:
        form = ExtendedUserCreationForm()
        profile_form = UserProfileForm()

    context = {'form': form, 'profile_form': profile_form}
    return render(request, 'signup.html', context)
