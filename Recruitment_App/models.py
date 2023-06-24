from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
# Create your models here.


JOB_TYPE = (
    ('Part Time', 'Part Time'),
    ('Full Time', 'Full Time'),
    ('Freelance', 'Freelancer'),
)

# CATEGORY = (
#     ('Web Design', 'Web Design'),
#     ('Graphic Design', 'Graphic Design'),
#     ('Web Developing', 'Web Developing'),
#     ('Software Engineering', 'Software Engineering'),
#     ('HR', 'HR'),
#     ('Marketing', 'Marketing'),
# )

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Any', 'Any'),
)

# SKILLS=(
#     ('Python', 'Python'),
#     ('Django', 'Django'),
#     ('HTML', 'HTML'),
#     ('CSS', 'CSS'),
#     ('JavaScript', 'JavaScript'),
#     ('React', 'React'),
#     ('Node.js', 'Node.js'),
#     ('SQL', 'SQL'),
#     ('NoSQL', 'NoSQL'),
#     ('C', 'C'),
#     ('C++', 'C++'),
#     ('C#', 'C#'),
#     ('Java', 'Java'),
#     ('PHP', 'PHP'),
# )


class minimum_experience(models.Model):
    minimum = models.IntegerField()
    
    def __str__(self):
        return self.minimum

class maximum_experience(models.Model):
    maximum = models.IntegerField()
    
    def __str__(self):
        return self.maximum

class Skills(models.Model):
    skill = models.CharField(max_length=50)

    def __str__(self):
        return self.skill

class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category

class Education(models.Model):
    education = models.CharField(max_length=50)
    
    def __str__(self):
        return self.education

class JobListing(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             null=True, editable=False, blank=True)
    title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=200)
    employment_status = models.CharField(choices=JOB_TYPE, max_length=10)
    vacancy = models.IntegerField(null=True)
    gender = models.CharField(choices=GENDER, max_length=30, null=True)
    category = models.ForeignKey(Category,related_name='Category', on_delete=models.CASCADE,null=True)
    description = models.TextField()
    education = models.ForeignKey(Education,  on_delete=models.CASCADE,null=True)
    responsibilities = models.TextField()
    minimum_exp = models.ForeignKey(minimum_experience, on_delete=models.CASCADE,null=True,max_length=20)
    maximum_exp = models.ForeignKey(maximum_experience, on_delete=models.CASCADE,null=True,max_length=20)
    job_location = models.CharField(max_length=120)
    Salary = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(blank=True, upload_to='media', null=True)
    application_deadline = models.DateTimeField()
    published_on = models.DateTimeField(default=timezone.now)
    skill = models.ForeignKey(Skills,related_name='Skills', on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("jobs:job-single", args=[self.id])


class ApplyJob(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile_no = models.BigIntegerField(null=True)
    file = models.FileField(upload_to='media',blank=True,null=True)
    coverletter = models.CharField(max_length=200, null=True)
    joblisting = models.ForeignKey(JobListing,null=True, on_delete=models.CASCADE)
    status = models.CharField(null=True,max_length=10,default=0)
    
    def __str__(self):
        return self.name