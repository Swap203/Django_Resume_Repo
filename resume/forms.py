from django import forms
from django.views.generic import UpdateView
from django.contrib.auth.forms import AuthenticationForm


from .models import Experience,About_Me,Projects,Education,Home_Page

class DateInput(forms.DateInput):
    input_type = 'date'

# class LoginForm(AuthenticationForm):


class ExperienceForm(forms.ModelForm):
    description=forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'cols':21}))
    class Meta:
        model=Experience
        widgets = {
            'joining_date': DateInput(),'resign_date': DateInput()
        }
        fields=('employer','designation','description','joining_date','resign_date')


class About_MeForm(forms.ModelForm):
    objective=forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'cols':21}))
    whatIDo=forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'cols':21}))
    class Meta:
        model=About_Me
        widgets ={'birthDate': DateInput()}
        fields=('firstName','middleName','lastName','email','mobile_no','City','Street',
            'State','Pincode','birthDate','objective','whatIDo')


class EducationForm(forms.ModelForm):

    class Meta:
        model=Education
        fields=('degree','college','university','description','start_year','end_year')



class ProjectsForm(forms.ModelForm):
    description=forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'cols':21}))
    class Meta:
        model=Projects
        fields=('projects_name','technologies','description','time_required')


class HomePageForm(forms.ModelForm):
    someIntro=forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'cols':21}))
    class Meta:
        model=Home_Page
        fields=('proffesion','someIntro')
