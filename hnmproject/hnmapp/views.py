from django.shortcuts import render
from hnmapp.models import UserGroups
from .tasks import fetch_user_groups

def user_groups_view(request):
    fetch_user_groups.delay()
    user_groups = UserGroups.objects.all()
    context = {'user_groups': user_groups}
    return render(request, 'hnmapp/user_groups.html', context)
