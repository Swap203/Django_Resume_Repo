from django.urls import path
from . import views

urlpatterns = [
	path('',views.view_HomePage, name="index"),
	path('login/',views.login, name="login"),
	path('check_login/',views.check_login, name="check_login"),
	path('logout/',views.logout, name="logout"),
	path('user_index/',views.user_index, name="user_index"),
	#HomePage :::
    path('update_HomePage/',views.update_HomePage, name="update_HomePage"),
	path('DeleteHomePage/',views.DeleteHomePage, name="DeleteHomePage"),
    path('add_HomePage/',views.add_HomePage, name="add_HomePage"),
    path('view_HomePage/',views.view_HomePage, name="view_HomePage"),
	#Experience Mode::::
	path('editMode_Experience/',views.editMode_Experience, name="editMode_Experience"),
	path('DeleteExperience/<int:id>/',views.DeleteExperience, name="DeleteExperience"),
	path('update_Experience/<int:id>/',views.update_Experience, name="update_Experience"),
	path('add_Experience/',views.add_Experience, name="add_Experience"),
	path('view_Experience/',views.view_Experience, name="view_Experience"),
	#About Me :::
	path('update_AboutMe/',views.update_AboutMe, name="update_AboutMe"),
	path('DeleteAboutMe/',views.DeleteAboutMe, name="DeleteAboutMe"),
	path('add_AboutMe/',views.add_AboutMe, name="add_AboutMe"),
	path('view_aboutMe/',views.view_aboutMe, name="view_aboutMe"),
	#Education :::
	path('editMode_Education/',views.editMode_Education, name="editMode_Education"),
	path('DeleteEducation/<int:id>/',views.DeleteEducation, name="DeleteEducation"),
	path('update_Education/<int:id>/',views.update_Education, name="update_Education"),
	path('add_Education/',views.add_Education, name="add_Education"),
	path('view_Education/',views.view_Education, name="view_Education"),
	#Projects :::
	path('editMode_Projects/',views.editMode_Projects, name="editMode_Projects"),
	path('DeleteProjects/<int:id>/',views.DeleteProjects, name="DeleteProjects"),
	path('update_Projects/<int:id>/',views.update_Projects, name="update_Projects"),
	path('add_Projects/',views.add_Projects, name="add_Projects"),
	path('view_Projects/',views.view_Projects, name="view_Projects"),
	#View Contact :::
	path('view_Contact/',views.view_Contact, name="view_Contact"),

]
