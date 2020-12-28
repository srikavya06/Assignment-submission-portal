from django.urls import path
from portal import views
urlpatterns=[
	path('Home/register/',views.register,name='register'),
	path('Home/login/',views.login,name='login'),
	path('Home/login/studentlogin',views.studentlogin,name='studentlogin'),
	path('Home/login/facultylogin',views.facultylogin,name='facultylogin'),
	path('Home/login/StudentDashboard/',views.StudentDashboard,name='StudentDashboard'),
	path('Home/login/StudentDashboard/upload/',views.fileupload,name='StudentDashboard'),
	path('Home/',views.Home,name='Home'),
	path('Home/login/Home',views.Home,name="Home"),
	path('Home/login/FacultyDashboard/',views.FacultyDashboard,name="FacultyDashboard"),
	path('Home/login/facultylogin/assignments',views.assignments,name="assignments"),
	path('Home/login/subjectslist',views.subjectslist,name="subjectslist"),
	path('Home/login/register',views.register,name="addusers"),
	path('Home/display',views.display,name="display"),
	path('Home/delete/<int:id>/',views.delete,name='del'),
    path('Home/update/<str:name>/',views.update,name='up'),
    path('display/',views.display,name="display"),
    path('Home/login/FacultyDashboard/register',views.register,name='register'),
    path('Home/login/FacultyDashboard/display',views.display,name='display'),
    path('Home/login/FacultyDashboard/viewassignments',views.viewassignments,name='viewassignments'),
    path('Home/login/StudentDashboard/assignments',views.viewassignments,name='assignments')
    #path('Home/login/FacultyDashboard/uploads/uploads/<str:name',views.openassignment,name='openassignment'),
	]

