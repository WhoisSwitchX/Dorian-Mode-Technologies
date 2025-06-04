from django.urls import path
from .views import *

urlpatterns = [
    # API endpoints
    path('api/bugs/', BugListCreateView.as_view(), name='bug-list-create'),
    path('api/bugs/<int:pk>/', BugDetailView.as_view(), name='bug-detail-api'),

    # Template-based views
    path('', home, name='home'),
    path('bugs/', bug_list, name='bug-list'),
    path('bugs/new/', bug_create, name='bug-create'),
    path('bugs/<int:pk>/', bug_detail, name='bug-detail'),
    path('bugs/<int:pk>/edit/', bug_edit, name='bug-edit'),
]
