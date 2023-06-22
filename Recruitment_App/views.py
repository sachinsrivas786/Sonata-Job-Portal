from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User 
from django.contrib.auth  import authenticate,  login, logout
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from Recruitment_App.models import minimum_experience,maximum_experience, Education, JobListing,Category, Skills,ApplyJob

from django.core.paginator import Paginator
from django.db.models import Q 


# Create your views here.

def home(request):
    
        education = Education.objects.all()
        joblisting = JobListing.objects.all()
        category = Category.objects.all()
        skill = Skills.objects.all()
        paginator = Paginator(joblisting,6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'index.html',{'joblisting':page_obj,'skill':skill,'category':category,'education':education})

def search(request):
    # minimum = minimum_experience.objects.all()
    # maximum = maximum_experience.objects.all()
    # category = Category.objects.all()

    if request.method == "POST":
        searched = request.POST['searched']
        # employment_status = request.POST['employment_status']
        # minimum = minimum_experience.objects.filter(minimum_exp__contains=searched)
        # maximum = maximum_experience.objects.filter(maximum_exp__contains=searched)
        # category = Category.objects.all()
        joblisting = JobListing.objects.filter(Q(company_name__contains=searched) | Q(employment_status__contains=searched) |  Q(job_location__contains=searched))

        return render(request, 'index.html',{'searched':searched,'joblisting':joblisting})
    else:
        return render(request, 'index.html',{'searched':searched,'joblisting':joblisting})
        
def profile(request):
    return render(request, 'home.html')

def profile_update(request):
    return render(request, 'profile.html' )

def Signup(request):
    return render(request, 'Sign-In.html')

def SignIn(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        
        print(username,email,pass1,pass2)

        # # check for errorneous input
        # if len(username)<10:
        #     messages.error(request, " Your user name must be under 10 characters")
        #     return redirect('/')

        # if not username.isalnum():
        #     messages.error(request, " User name should only contain letters and numbers")
        #     return redirect('/')
        
        if (pass1!= pass2):
            messages.error(request, " Passwords do not match")
            return redirect('Signup')
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()
        messages.success(request, " Account has been successfully created")
        return redirect('Signup')
    else:
        # return HttpResponse("404 - Not found")
        messages.error(request, "failed")
        return redirect('Signup')

def Login(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST.get('username')
        pass1 =request.POST.get('pass1')

        print(username,pass1)
        user=authenticate(request,username = username, password = pass1)
        if user is not None:
            if user.is_active:
                request.session.set_expiry(420)
                login(request, user)
                messages.success(request, "Successfully Logged In")
                return redirect('home')
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect('Signup')

    # return HttpResponse("404- Not found")
    return redirect('home')

def Logout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('/')

# def profile(request):
#     user = User.objects.get(id = request.user.id)
#     return render(request, 'profile.html',{'user':user})

# def profile_update(request):
#     if request.method != "POST":
#         messages.eroor(request,"Invalid Method!")
#         return redirect('profile')
#     else:
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         pass1=request.POST.get('pass1')
#         pass2=request.POST.get('pass2')
        
#         try:
#             user = User.objects.get(id = request.user.id)
#             user.username = username
#             user.email = email
#             if pass1 != None and pass1 != "":
#                 user.set_password(pass1)
#             user.save()
#             messages.success(request, "Profile Updated Successfully")
#             return redirect('profile')
        
#         except:
#             messages.error(request, "Failed to Update Profile")
#             return redirect('profile')



# @login_required

def post_job(request):
    minimum = minimum_experience.objects.all()
    maximum = maximum_experience.objects.all()
    category = Category.objects.all()
    skill = Skills.objects.all()
    education = Education.objects.all() 
    if not request.user.is_authenticated:
        return redirect("/Login")
    if request.method == "POST":
        title = request.POST['title']
        company_name = request.POST['company_name']
        employment_status = request.POST['employment_status']
        vacancy = request.POST['vacancy']
        gender = request.POST['gender']
        category_id = request.POST['category_id']
        published_on = request.POST['published_on']
        application_deadline = request.POST['application_deadline']
        Salary = request.POST['Salary']
        image = request.FILES['image']
        skill_id = request.POST['skill_id']
        minimum_exp = request.POST['minimum_exp']
        maximum_exp = request.POST['maximum_exp']
        job_location = request.POST['job_location']
        description = request.POST['description']
        responsibilities = request.POST['responsibilities']
        education_id = request.POST['education_id']
        user = request.user

        job = JobListing.objects.create(user=user,vacancy=vacancy,responsibilities=responsibilities,gender=gender,company_name=company_name,employment_status=employment_status, title=title,published_on=published_on, application_deadline=application_deadline, Salary=Salary, image=image, job_location=job_location, description=description)
        
        job.category_id = category_id
        job.skill_id = skill_id
        job.education_id = education_id
        job.minimum_exp_id = minimum_exp
        job.maximum_exp_id = maximum_exp
        job.save()
        alert = True
        return render(request, "postjob.html", {'alert':alert,'category':category,'skill':skill,'education':education,'minimum':minimum,'maximum':maximum})
    return render(request, "postjob.html",{'category':category,'skill':skill,'education':education,'minimum':minimum,'maximum':maximum})


def about(request):
    return render(request,'about.html')

def job_detail(request,joblisting_id):
    category = Category.objects.all()
    education = Education.objects.all() 
    skill = Skills.objects.all()
    joblisting = JobListing.objects.filter(id = joblisting_id)
    applyjob = ApplyJob.objects.filter(joblisting_id__in=joblisting)
    return render(request,'job-detail.html',{'joblisting':joblisting,'category':category,'skill':skill,'education':education,'applyjob':applyjob})

def apply_job(request,joblisting_id):
    user = User.objects.get(id = request.user.id)
    joblisting = JobListing.objects.filter(id = joblisting_id)
    applyjob = ApplyJob.objects.filter(joblisting_id=joblisting,user=user)
    
    if not request.user.is_authenticated:
        return redirect("/Login")
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        mobile_no = request.POST['mobile_no']
        coverletter = request.POST['coverletter']
            
        joblisting = JobListing.objects.get(id = joblisting_id)

        ticket = ApplyJob.objects.create(joblisting_id=joblisting.id,user_id=user.id,name=name, email=email,mobile_no=mobile_no,coverletter=coverletter)
        ticket.save()
        alert = True
    return redirect('/job_detail/'+str(joblisting_id))



def appliedJob(request):
    if not request.user.is_authenticated:
        return redirect("/Login")
    user = User.objects.get(id = request.user.id)
    joblisting = JobListing.objects.all()
    apply = ApplyJob.objects.filter(joblisting_id__in = joblisting,user_id=user,status = 0)
    paginator = Paginator(apply,7)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'applied_jobs.html',{'apply':page_obj,'joblisting':joblisting})


def applied_user_details(request):
    if not request.user.is_authenticated:
        return redirect("/Login")
    user = User.objects.get(id = request.user.id)
    joblisting = JobListing.objects.filter(user=user)
    ticket = ApplyJob.objects.filter(joblisting_id__in = joblisting,status = 0)
    paginator = Paginator(ticket,5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'appliedUserDetails.html',{'ticket':page_obj,'joblisting':joblisting})

def shortlisted(request):
    if not request.user.is_authenticated:
        return redirect("/Login")
    
    user = User.objects.get(id = request.user.id)
    joblisting = JobListing.objects.filter(user=user)
    ticket = ApplyJob.objects.filter(joblisting_id__in = joblisting , status = 1)
    paginator = Paginator(ticket,5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'appliedUserDetails.html',{'ticket':page_obj,'joblisting':joblisting})



def job_list(request):
    return render(request,'job-list.html')


