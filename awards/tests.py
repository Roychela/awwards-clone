from django.test import TestCase
from .models import Project,Profile
from django.contrib.auth.models import User
# Create your tests here.
class ProjectTestClass(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("newuser", "test")
        self.project_ferrari = Project(project_name='project_ferrari',project_caption='this is a test instance',project_image='test.png',project_url='test.com',user=self.user)
        self.project_ferrari.save_project()
        self.project_gucci = Project(project_name='project_gucci',project_caption='this is a test instance',project_image='test2.png',project_url='test.com',user=self.user)
        self.project_gucci.save_project()

    def test_instance(self):
        self.assertTrue(isinstance(self.project_ferrari,Project))

    def tearDown(self):
        Project.objects.all().delete()
        Profile.objects.all().delete()
        User.objects.all().delete()

        
    def test_save_project(self):
        self.project_ferrari.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects)>0)
# class ProfileTestClass(TestCase):
#     '''
#     test class for Profile model
#     '''
#     def setUp(self):
#         self.user = User.objects.create_user("testuser", "secret")
#         self.profile_test = Profile(image='image.png',user=self.user)
#         self.profile_test.save()
#     def tearDown(self):
#         Profile.objects.all().delete()
#         User.objects.all().delete()


#     def test_instance_true(self):
#         self.profile_test.save()
#         self.assertTrue(isinstance(self.profile_test, Profile))
