from .models import UserProfile


def account_type_processor(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = 'not logged in'
    user_account_type = UserProfile.objects.filter(user__username=username)
    print(user_account_type)
    return {'user_type': user_account_type}
