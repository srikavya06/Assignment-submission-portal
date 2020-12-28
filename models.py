from django.db import models

# Create your models here.
class logindata(models.Model):
	branches=(
		("ECE","ece"),
		("CSE","cse"),
		("IT","it")
	)
	Name=models.CharField(max_length=50)
	Branch=models.CharField(max_length=10,choices=branches)
	Email=models.EmailField(blank=True)
	password=models.CharField(max_length=10
		)
	Rollno=models.CharField(max_length=15)
	Year=models.CharField(max_length=3,default="3")
	Semester=models.CharField(max_length=3,default="1")
	def __str__(self):
		return self.Name+" "+self.Branch
class assignments(models.Model):
	subjects=(
		("cd","CD"),
		("DBMS","dbms"),
		("up","UP"),
		("ooad","OAAD"),
		("os","OS"),
		)
	status=(
			("YES","yes"),
			("No","NO"),
			)
	Name=models.CharField(max_length=50)
	AssignmentName=models.CharField(max_length=50)
	Branch=models.CharField(max_length=10)
	Subjects=models.CharField(max_length=50,choices=subjects)
	Rollno=models.CharField(max_length=15)
	file=models.FileField(upload_to='uploads/')
	status=models.CharField(max_length=3,choices=status,default="no")

  


