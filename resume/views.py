#from django.shortcuts import render

from django.shortcuts import render,get_object_or_404,reverse,redirect
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from .models import About_Me,Home_Page,Education,Experience,Projects,Login
from dateutil.relativedelta import relativedelta
from .forms import ExperienceForm,About_MeForm,EducationForm,HomePageForm,ProjectsForm


def index(request):
    return render(request,'resume/menu.html')

def login(request):
    if 'username' not in request.session:
        return render(request,'resume/userIndex/user_login.html')
    else:
        return HttpResponseRedirect(reverse('user_index'))

def check_login(request):
    userName=request.POST.get('userName')
    password=request.POST.get('password')
    try:
        login1=Login.objects.get(userName=userName, password=password)
        if login1:
            request.session['username'] = login1.userEmail
    except:
        return HttpResponseRedirect(reverse('login'))

    return HttpResponseRedirect(reverse('user_index'))

#@login_required(login_url='login/')



def view_HomePage(request):
    try:
        abt_me=About_Me.objects.get()
        Home_Page1=Home_Page.objects.get()
        context = {"Home_Page":Home_Page1,"abt_me":abt_me}
        return render(request, 'resume/userIndex/Home_Page.html',context)
    except:
        return render(request, 'resume/userIndex/NothingToDisplay.html')


###################### User Edit Mode Begin #########################

def user_index(request):
    if 'username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
    else:
        try:
            abt_me=About_Me.objects.get()
            Home_Page1=Home_Page.objects.get()
            context = {"Home_Page":Home_Page1,"abt_me":abt_me}
            return render(request, 'resume/userEditMode/user_index.html',context)
        except:
            if abt_me is None:
                return redirect('add_AboutMe')
            else:
                return redirect('add_HomePage')


###################### Experience Section CRUD #########################

def editMode_Experience(request):
    if 'username' in request.session:
        Experience1=Experience.objects.all().order_by('-resign_date')
        context={"Experience":Experience1}
        return render(request, 'resume/userEditMode/Experience.html',context)
    else:
        return HttpResponseRedirect(reverse('login'))

def DeleteExperience(request,id):
    if 'username' in request.session:
        Experience1=Experience.objects.get(id=id)
        Experience1.delete()
        return HttpResponseRedirect(reverse('editMode_Experience'))
    else:
        return HttpResponseRedirect(reverse('login'))

def add_Experience(request):
    if 'username' in request.session:
        if request.method == "POST":
            form = ExperienceForm(request.POST)
            if form.is_valid():
                model_instance = form.save(commit=False)
                model_instance.save()
                return redirect('editMode_Experience')
        else:
            form = ExperienceForm()
        return render(request,'resume/myEntry/addExperience.html',{'form':form})
    else:
        return HttpResponseRedirect(reverse('login'))

#@login_required(login_url='login/')
def update_Experience(request,id,template_name='resume/myEntry/UpdateExperience.html'):
    if 'username' in request.session:
        exp = get_object_or_404(Experience, id=id)
        form = ExperienceForm(request.POST or None, instance=exp)
        if form.is_valid():
            form.save()
            return redirect('editMode_Experience')
        return render(request, template_name , {'form':form})
    else:
        return HttpResponseRedirect(reverse('login'))

def view_Experience(request):
    Experience1=Experience.objects.all().order_by('-resign_date')
    if not Experience1:
        message="Please Add Experience"
        #context={"message":message,}
        return render(request, 'resume/userIndex/NothingToDisplay.html')
        #return HttpResponseRedirect(reverse('NothingToDisplay'),context)
        #return redirect('login',context)
    experienceCount={}
    for exp in Experience1:
        j_date,r_date=(exp.joining_date,exp.resign_date) if exp.joining_date > exp.resign_date else (exp.resign_date,exp.joining_date)
        rd=relativedelta(j_date,r_date)
        difference_in_years_months = rd.years,rd.months
        experienceCount[exp.id]=difference_in_years_months
    context = {"Experience" : Experience1, "experienceCount" : experienceCount}
    return render(request, 'resume/userIndex/Experience.html',context)



######################################################################################

def logout(request,):
    del request.session['username']
    return HttpResponseRedirect(reverse('login'))

#def NothingToDisplay(request,):
#    return HttpResponseRedirect(reverse('NothingToDisplay'))

####################### About Me Section CRUD #######################

def DeleteAboutMe(request):
    if 'username' in request.session:
        ins=About_Me.objects.get()
        About_Me1=About_Me.objects.get(id=ins.id)
        About_Me1.delete()
        return HttpResponseRedirect(reverse('update_AboutMe'))
    else:
        return HttpResponseRedirect(reverse('login'))

def add_AboutMe(request):
    if 'username' in request.session:
        if request.method == "POST":
            form = About_MeForm(request.POST)
            if form.is_valid():
                model_instance = form.save(commit=False)
                model_instance.save()
                return redirect('user_index')
        else:
            form = About_MeForm()
        return render(request,'resume/myEntry/addAboutMe.html',{'form':form})
    else:
        return HttpResponseRedirect(reverse('login'))

def update_AboutMe(request,template_name='resume/myEntry/addAboutMe.html'):
    if 'username' in request.session:
        try:
            ins=About_Me.objects.get()
        except:
            return redirect('add_AboutMe')
        exp = get_object_or_404(About_Me, id=ins.id)
        form = About_MeForm(request.POST or None, instance=exp)
        if form.is_valid():
            form.save()
            return redirect('user_index')
        return render(request, template_name , {'form':form})
    else:
        return HttpResponseRedirect(reverse('login'))

def view_aboutMe(request):
    abt_me=About_Me.objects.get()
    if not abt_me:
        return render(request, 'resume/userIndex/NothingToDisplay.html')
    context = {"abt_me":abt_me}
    return render(request, 'resume/userIndex/about_Me.html',context)


######################################################################################


####################### HOME Section CRUD #######################

def DeleteHomePage(request):
    if 'username' in request.session:
        ins=Home_Page.objects.get()
        Home_Page1=Home_Page.objects.get(id=ins.id)
        Home_Page1.delete()
        return HttpResponseRedirect(reverse('update_HomePage'))
    else:
        return HttpResponseRedirect(reverse('login'))

def add_HomePage(request):
    if 'username' in request.session:
        if request.method == "POST":
            form = HomePageForm(request.POST)
            if form.is_valid():
                model_instance = form.save(commit=False)
                model_instance.save()
                return redirect('user_index')
        else:
            form = HomePageForm()
        return render(request,'resume/myEntry/addHomePage.html',{'form':form})
    else:
        return HttpResponseRedirect(reverse('login'))

def update_HomePage(request,template_name='resume/myEntry/addHomePage.html'):
    if 'username' in request.session:
        try:
            ins=Home_Page.objects.get()
        except:
            return redirect('add_HomePage')
        exp = get_object_or_404(Home_Page, id=ins.id)
        form = HomePageForm(request.POST or None, instance=exp)
        if form.is_valid():
            form.save()
            return redirect('user_index')
        return render(request, template_name , {'form':form})
    else:
        return HttpResponseRedirect(reverse('login'))

    #####################################################

###################### Education Section CRUD #########################

def editMode_Education(request):
    if 'username' in request.session:
        Education1=Education.objects.all().order_by('-end_year')
        context={"Education":Education1}
        return render(request, 'resume/userEditMode/Education.html',context)
    else:
        return HttpResponseRedirect(reverse('login'))
def DeleteEducation(request,id):
    if 'username' in request.session:
        Education1=Education.objects.get(id=id)
        Education1.delete()
        return HttpResponseRedirect(reverse('editMode_Education'))
    else:
        return HttpResponseRedirect(reverse('login'))


def add_Education(request):
    if 'username' in request.session:
        if request.method == "POST":
            form = EducationForm(request.POST)
            if form.is_valid():
                model_instance = form.save(commit=False)
                model_instance.save()
                return redirect('editMode_Education')
        else:
            form = EducationForm()
        return render(request,'resume/myEntry/addEducation.html',{'form':form})
    else:
        return HttpResponseRedirect(reverse('login'))

def update_Education(request,id,template_name='resume/myEntry/UpdateEducation.html'):
    if 'username' in request.session:
        edu = get_object_or_404(Education, id=id)
        form = EducationForm(request.POST or None, instance=edu)
        if form.is_valid():
            form.save()
            return redirect('editMode_Education')
        return render(request, template_name , {'form':form})
    else:
        return HttpResponseRedirect(reverse('login'))
def view_Education(request):
    Education1=Education.objects.all().order_by('-end_year')
    if not Education1:
        return render(request, 'resume/userIndex/NothingToDisplay.html')
    context = {"Education":Education1}
    return render(request, 'resume/userIndex/Education.html',context)





######################################################################################





###################### Projects Section CRUD #########################

def editMode_Projects(request):
    if 'username' in request.session:
        Projects1=Projects.objects.all()
        context={"Projects":Projects1}
        return render(request, 'resume/userEditMode/Projects.html',context)
    else:
        return HttpResponseRedirect(reverse('login'))

def DeleteProjects(request,id):
    if 'username' in request.session:
        Projects1=Projects.objects.get(id=id)
        Projects1.delete()
        return HttpResponseRedirect(reverse('editMode_Projects'))
    else:
        return HttpResponseRedirect(reverse('login'))

def add_Projects(request):
    if 'username' in request.session:
        if request.method == "POST":
            form = ProjectsForm(request.POST)
            if form.is_valid():
                model_instance = form.save(commit=False)
                model_instance.save()
                return redirect('editMode_Projects')
        else:
            form = ProjectsForm()
        return render(request,'resume/myEntry/addProjects.html',{'form':form})
    else:
        return HttpResponseRedirect(reverse('login'))

def update_Projects(request,id,template_name='resume/myEntry/UpdateProjects.html'):
    if 'username' in request.session:
        edu = get_object_or_404(Projects, id=id)
        form = ProjectsForm(request.POST or None, instance=edu)
        if form.is_valid():
            form.save()
            return redirect('editMode_Projects')
        return render(request, template_name , {'form':form})
    else:
        return HttpResponseRedirect(reverse('login'))
def view_Projects(request):
    Projects1=Projects.objects.all()
    if not Projects1:
        return render(request, 'resume/userIndex/NothingToDisplay.html')
    context = {"Projects" : Projects1}
    return render(request, 'resume/userIndex/Projects.html',context)

######################################################################################

def view_Contact(request):
    abt_me=About_Me.objects.get()
    if not abt_me:
        return render(request, 'resume/userIndex/NothingToDisplay.html')
    context = {"abt_me":abt_me}
    #return render(request, 'resume/userIndex/about_Me.html',context)
    return render(request, 'resume/userIndex/Contact.html',context)







######################################################################################

def check_Session():
    if 'username' in request.session:
        return True
    else:
        return False

# Create your views here.
