from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import logindata
from .models import assignments
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import DocumentForm
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def register(request):
  if request.method=='POST':
        name=request.POST['name']
        branch=request.POST['branch']
        email=request.POST['mail']
        password=request.POST['password']
        Rollno=request.POST['Rollno']
        year=request.POST['year']
        Semester=request.POST['Semester']
        user=User.objects.create_user(username=name,password=password)
        user.save()
        data=logindata(Name=name,Branch=branch,Email=email,password=password,Rollno=Rollno,Year=year,Semester=Semester)
        data.save()
        return HttpResponse("registeration  sucessfull")
  return render(request,'register.html')


def login(request):
	return render(request,'login.html')

def studentlogin(request):
	if request.method == 'POST':
          name=request.POST['name']
          mail = request.POST['mail']
          password = request.POST['password']
          user=authenticate(request,username=name,password=password)
          if user is not None:
            if user.is_active:
                  form=login(request)
                  return HttpResponseRedirect("StudentDashboard/")
            else:
                  messages.error(request,'invalid credentials')
                  return redirect(request,login.html)
          else:
            messages.error(request, "invalid login details " + mail + " " + password)
            return render(request,'Studentlogin.html')
	return render(request,'studentlogin.html') 

def fileupload(request):
  if request.method == 'POST':
    form=DocumentForm(request.POST,request.FILES)
    if form.is_valid():
      form.save()
      return HttpResponse('assignment submitted')
  else :
    form=DocumentForm()
  return render(request,'upload.html',{'form':form})

def facultylogin(request):
    if request.method == 'POST':
          name = request.POST['name']
          mail = request.POST['mail']
          password = request.POST['password']
          user=authenticate(request,username=name,password=password)
          if user is not None:
              if user.is_active:
                  form=login(request)
                  # Redirect to index page.
                  return HttpResponseRedirect("FacultyDashboard/")
              else:
                  # Return a 'disabled account' error message
                  return HttpResponse("You're account is disabled.")
          else:
              # Return an 'invalid login' error message.
              print ( "invalid login details " + mail + " " + password)
              return render(request,'facultylogin.html')
    return render(request,'facultylogin.html')

def FacultyDashboard(request):
	return render(request,'FacultyDashboard.html') 

def StudentDashboard(request):
	return render(request,'StudentDashboard.html')
	
def Home(request):
	return render(request,'Home.html')
#def openassignment(request,name):
 # image_data = open(“upload/”, “rb”).read()
  #return HttpResponse(image_data, mimetype=”application/pdf”)

def subjectslist(request):
    return render(request,'subjectslist.html')

def delete(request,id):
  data=logindata.objects.get(id=id)
  data.delete()
  return redirect('/display')

def update(request,name):
  data=logindata.objects.get(Name=name)
  if request.method=="POST":
    c=request.POST['name']
    n=request.POST['Rollno']
    r=request.POST['Semester']
    b=request.POST['Branch']
    y=request.POST['Year']
    data.Name=c
    data.Rollno=n
    data.Semester=r
    data.Branch=b
    data.Year=y
    data.save()
    return render(request,'display.html')
  return render(request,'update.html',{'info':data})

def display(request):
  data=logindata.objects.all()
  return render(request,'display.html',{'info':data})  
def viewassignments(request):
  data=assignments.objects.all()
  return render(request,'viewassignments.html',{'info':data})


