from django import forms
from .models import student_form
from .models import teacher_form

GENDERS=(
	("Male", "Male"),
	("Female", "Female"),
	("Other", "Other"),
)

PROGRAMS=(
	("Tutoring","Tutoring"),
	("Debate","Debate"),
	("Programming","Programming"),
)

class student_form(forms.ModelForm):
	first_name=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	middle_name=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_name=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	birthday=forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
	gender=forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'choice'}),choices=GENDERS)
	school=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	grade=forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	email=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
	phone=forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	program=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=PROGRAMS)

	class Meta:
		model=student_form
		fields=['first_name','middle_name','last_name','birthday','gender','school','grade','email','phone','program']

class teacher_form(forms.ModelForm):
	first_name=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	middle_name=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_name=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	birthday=forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
	gender=forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'choice'}),choices=GENDERS)
	school=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	grade=forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	email=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
	phone=forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	program=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=PROGRAMS)
	reason=forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}),label="Why do you want to tutor, teach debate, or teach programming?")
	qualifications=forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}),label="What are you qualifications to tutor, teach debate, or teach programming?")
	methods=forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}),label="In your opinion, what is the best way for students to learn? How can you apply this while teaching in Tutoring the Future? ")

	class Meta:
		model=teacher_form

		fields=['first_name','middle_name','last_name','birthday','gender','school','grade','email','phone','program','reason','qualifications','methods']










