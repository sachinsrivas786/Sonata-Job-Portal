from django.contrib import admin

from Recruitment_App.models import minimum_experience,maximum_experience,JobListing,ApplyJob, Skills,Category

# Register your models here.
admin.site.register(JobListing)
admin.site.register(ApplyJob)
admin.site.register(Skills)
admin.site.register(Category)
admin.site.register(minimum_experience)
admin.site.register(maximum_experience)