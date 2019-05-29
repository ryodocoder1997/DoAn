from django.shortcuts import render
from django.contrib.auth.models import User
from .models import UserInfo, Contacts, Introductions, Video, Schedules, StudyProcess, TypicalStudents, Classes, \
    Teachers
from django.apps import apps


def show_user_profile(request, username):
    current_user = ''
    if request.user.is_authenticated:
        current_user = request.user
    user_basic = User.objects.filter(username=username)
    user_info = UserInfo.objects.filter(username__user__username=username)

    user_profile = apps.get_model('accounts', 'UserProfile')
    user_type_tutor = user_profile.objects.filter(account_type='T')
    user_tutor_exclude = user_type_tutor.exclude(user__username=username)

    user_type_academy = user_profile.objects.filter(account_type='A')
    user_academy_exclude = user_type_academy.exclude(user__username=username)

    if len(current_user.username) > 0:
        user_exclude_for_tutor = user_tutor_exclude.exclude(user__username=current_user)
        user_exclude_for_academy = user_academy_exclude.exclude(user__username=current_user)

        user_suggest_list_tutor = []
        user_suggest_info_list_tutor = []
        result_suggest_list_tutor = []
        for user_tutor in user_exclude_for_tutor:
            user_suggest_tutor = User.objects.filter(username=user_tutor)
            user_suggest_list_tutor.append(user_suggest_tutor)

            user_suggest_info_tutor = UserInfo.objects.filter(username__user__username=user_tutor)
            user_suggest_info_list_tutor.append(user_suggest_info_tutor)

            result_suggest = zip(user_suggest_tutor, user_suggest_info_tutor)
            result_suggest_list_tutor.append(result_suggest)

        user_suggest_list_academy = []
        user_suggest_info_list_academy = []
        result_suggest_list_academy = []

        for user_academy in user_exclude_for_academy:
            user_suggest_academy = User.objects.filter(username=user_academy)
            user_suggest_list_academy.append(user_suggest_academy)

            user_suggest_info_academy = UserInfo.objects.filter(username__user__username=user_academy)
            user_suggest_info_list_academy.append(user_suggest_info_academy)

            result_suggest = zip(user_suggest_academy, user_suggest_info_academy)
            result_suggest_list_academy.append(result_suggest)

    user_contact = Contacts.objects.filter(username__user__username=username)

    user_introduction = Introductions.objects.filter(username__user__username=username)
    user_video_url = Video.objects.filter(username__user__username=username)
    for vid in user_video_url:
        vid.video_url = vid.video_url[32:43]
    user_schedule = Schedules.objects.filter(username__user__username=username)
    user_study_process = StudyProcess.objects.filter(username__user__username=username)
    user_typical = TypicalStudents.objects.filter(username__user__username=username)
    user_classes = Classes.objects.filter(username__user__username=username)
    user_teachers = Teachers.objects.filter(username__user__username=username)

    return render(request, "user-profile.html",
                  {'UserBasics': user_basic, 'UserInfos': user_info, 'TutorSuggest': result_suggest_list_tutor,
                   'AcademySuggest': result_suggest_list_academy, 'Contacts': user_contact,
                   'Introductions': user_introduction, 'Videos': user_video_url,
                   'Schedules': user_schedule, 'StudyProcesses': user_study_process, 'Typicals': user_typical,
                   'Classes': user_classes, 'Teachers': user_teachers})