from django.shortcuts import render,redirect
from .forms import student_form
from .forms import teacher_form

def home(request):
	return render(request,'home.html')

def programs(request):
	return render(request, 'programs.html')

def team(request):
	return render(request, 'team.html')

def about(request):
	return render(request, 'about.html')

def student_forms(request):

	if request.method == 'POST':
		form = student_form(request.POST)

		if form.is_valid():
			form.save(commit=False)
			first_name=form.cleaned_data.get('first_name')
			middle_name=form.cleaned_data.get('middle_name')
			last_name=form.cleaned_data.get('last_name')
			birthday=form.cleaned_data.get('birthday')
			gender=form.cleaned_data.get('gender')
			school=form.cleaned_data.get('school')
			grade=form.cleaned_data.get('grade')
			email=form.cleaned_data.get('email')
			phone=form.cleaned_data.get('phone')
			program=form.cleaned_data.get('program')

			form.save()
			return redirect('http://localhost:8000')
	else:
		form=student_form(request.POST)

	return render(request, 'student_signup.html', {'form': form})

def teacher_forms(request):

	if request.method == 'POST':
		form = teacher_form(request.POST)

		if form.is_valid():
			form.save(commit=False)
			first_name=form.cleaned_data.get('first_name')
			middle_name=form.cleaned_data.get('middle_name')
			last_name=form.cleaned_data.get('last_name')
			birthday=form.cleaned_data.get('birthday')
			gender=form.cleaned_data.get('gender')
			school=form.cleaned_data.get('school')
			grade=form.cleaned_data.get('grade')
			email=form.cleaned_data.get('email')
			phone=form.cleaned_data.get('phone')
			program=form.cleaned_data.get('program')
			reasons=form.cleaned_data.get('reasons')
			qualifications=form.cleaned_data.get('qualifications')
			methods=form.cleaned_data.get('methods')

			form.save();
			return redirect('http://localhost:8000')
	else:
		form=teacher_form(request.POST)

	return render(request, 'teacher_signup.html', {'form': form})


