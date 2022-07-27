from urllib import response
from django.test import TestCase, RequestFactory, Client

from .models import Developer, Project
from .views import developer, project
# Create your tests here.

class DeveloperTC(TestCase):
    def setUp(self) -> None:
        Developer.objects.create(first_name='Richard', last_name='Evans', language='C++')
    
    def test_objects_create(self):
        dev_0 = Developer.objects.get(first_name='Richard')
        self.assertEqual(dev_0.language, 'C++')
        self.assertEqual(dev_0.last_name, 'Evans')

class ProjectTC(TestCase):
    def setUp(self) -> None:
        dev_0 = Developer.objects.create(first_name='Richard', last_name='Evans', language='C++')
        Project.objects.create(name='Project 1', description='Description', date_start='2019-01-01', date_end='2020-10-10', cost=100, developer=dev_0)
    
    def test_objects_create(self):
        proj_0 = Project.objects.get(name='Project 1')
        self.assertEqual(proj_0.name, 'Project 1')
        self.assertEqual(proj_0.developer.first_name, 'Richard')
        
class RequestTC(TestCase):
    def setUp(self) -> None:
        self.developer = Developer.objects.create(first_name='Richard', last_name='Evans', language='C++')
        self.client = Client()
        self.factory = RequestFactory()
    
    def test_search(self):
        request = self.client.get(f'/en/?from=2020-01-01&to=2021-01-01&currency=VND')
        self.assertEqual(request.status_code, 200)

    def test_developer(self):
        request = self.factory.get(f'/developer/detail/<pk>/')
        response = developer.DeveloperUpdateView.as_view()(request, pk=self.developer.id)
        self.assertEqual(response.status_code, 200)
    
    def test_project(self):
        request = self.factory.post('/project/create/')
        data = {
            'name': 'A', 
            'description': 'B',
            'date_start': '2020-01-01',
            'date_end': '2021-01-01',
            'cost': '10', 
            'developer': self.developer,
        }
        response = project.ProjectCreateView.as_view()(request, **data)
        self.assertEqual(response.status_code, 200)