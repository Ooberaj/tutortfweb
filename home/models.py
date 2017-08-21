from django.db import models

class student_form(models.Model):
	first_name=models.CharField(max_length=100)
	middle_name=models.CharField(max_length=100)
	last_name=models.CharField(max_length=100)
	birthday=models.DateField(max_length=50)
	gender=models.CharField(max_length=50)
	school=models.CharField(max_length=100)
	grade=models.IntegerField(max_length=1)
	email=models.EmailField()
	phone=models.IntegerField(max_length=12)
	program=models.CharField(max_length=50)


class teacher_form(models.Model):
	first_name=models.CharField(max_length=100)
	middle_name=models.CharField(max_length=100)
	last_name=models.CharField(max_length=100)
	birthday=models.DateField(max_length=50)
	gender=models.CharField(max_length=50)
	school=models.CharField(max_length=100)
	grade=models.IntegerField(max_length=1)
	email=models.EmailField()
	phone=models.IntegerField(max_length=12)
	program=models.CharField(max_length=50)
	reason=models.CharField(max_length=1000)
	qualifications=models.CharField(max_length=1000)
	methods=models.CharField(max_length=1000)