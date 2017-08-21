from django.contrib import admin

from .models import student_form
from .models import teacher_form

class studentData(admin.ModelAdmin):
	list_display=['first_name','middle_name','last_name','birthday','gender','school','grade','email','phone','program']

	class Meta:
		model=student_form

admin.site.register(student_form, studentData)

class teacherData(admin.ModelAdmin):
	list_display=['first_name','middle_name','last_name','birthday','gender','school','grade','email','phone','program','reason','qualifications','methods']

	class Meta:
		model=teacher_form

admin.site.register(teacher_form, teacherData)
