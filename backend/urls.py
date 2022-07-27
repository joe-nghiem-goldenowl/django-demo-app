from django.urls import path
from .views import developer, project

urlpatterns = [
    path('', project.ProjectListView.as_view()),
    path('project/detail/<pk>/', project.ProjectUpdateView.as_view()),
    path('project/delete/<pk>/', project.ProjectDeleteView.as_view()),
    path('project/create/', project.ProjectCreateView.as_view()),
    path('developer/add/', developer.DeveloperCreateView.as_view()),
    path('developer/detail/<pk>/', developer.DeveloperUpdateView.as_view()),
]