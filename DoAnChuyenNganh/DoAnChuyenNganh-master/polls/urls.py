from django.urls import path
from . import views

urlpatterns = [
    path('<username>', views.show_user_profile, name='show_user_profile')
]
