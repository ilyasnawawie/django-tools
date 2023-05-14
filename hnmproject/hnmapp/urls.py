from django.urls import path
from hnmapp.views import user_groups_view

urlpatterns = [
    # other URL patterns
    path('user-groups/', user_groups_view, name='user_groups'),
]
