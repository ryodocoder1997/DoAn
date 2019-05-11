from django.shortcuts import render
from django.contrib.auth.models import User
from .models import UserInfo, Contacts
from django.apps import apps


def show_user_profile(request, username):
    current_user = ''
    if request.user.is_authenticated:
        current_user = request.user
    user_basic = User.objects.filter(username=username)
    user_info = UserInfo.objects.filter(username__user__username=username)

    user_profile = apps.get_model('accounts', 'UserProfile')
    user_type = user_profile.objects.filter(account_type='T')
    user_exclude = user_type.exclude(user__username=username)

    if len(current_user.username) > 0:
        user_exclude = user_exclude.exclude(user__username=current_user)

    user_suggest_list = []
    user_suggest_info_list = []
    result_suggest_list = []
    for user in user_exclude:
        user_suggest = User.objects.filter(username=user)
        user_suggest_list.append(user_suggest)

        user_suggest_info = UserInfo.objects.filter(username__user__username=user)
        user_suggest_info_list.append(user_suggest_info)

        result_suggest = zip(user_suggest, user_suggest_info)
        result_suggest_list.append(result_suggest)

    user_contact = Contacts.objects.filter(username__user__username=username)
    return render(request, "user-profile.html",
                  {'UserBasics': user_basic, 'UserInfos': user_info, 'Suggest': result_suggest_list, 'Contacts': user_contact})
