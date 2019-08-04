from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(default='default')
    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)


    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()
class Project(models.Model):
    project_name = models.CharField(max_length=100)
    project_caption = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_image = models.ImageField(upload_to = 'project_images/', blank = True)
    project_url=models.URLField(max_length=250, default="Type your project link")

    def save_project(self):
        self.save()
    def delete_project(self):
        self.delete()
    @classmethod
    def get_profile_projects(cls, user):
        projects = Project.objects.filter(user__pk=user)
        return projects

    @classmethod
    def search_project(cls, name):
        project = Project.objects.filter(project_name__icontains = name)
        return project
   
# class Rating(models.Model):
#     RATING_CHOICES = (
#         (1, '1'),
#         (2, '2'),
#         (3, '3'),
#         (4, '4'),
#         (5, '5'),
#         (6, '6'),
#         (7, '7'),
#         (8, '8'),
#         (9, '9'),
#         (10,'10'),
#     )
#     project=models.ForeignKey(Project,on_delete=models.CASCADE)
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     design_rating = models.IntegerField(choices=RATING_CHOICES,null=True)
#     usability_rating=models.IntegerField(choices=RATING_CHOICES,null=True)
#     content_rating=models.IntegerField(choices=RATING_CHOICES,null=True)
    