from ast import Module
from django.db import models

# Create your models here.

class faculty(models.Model) :
    name = models.CharField(max_length=200, help_text="Введите наименование факультета")
    def __str__(self) :
        return self.name
    
from django.urls import reverse

class course (models.Model) :
    title = models.CharField(max_length=200)
    teacher = models.ForeignKey('teacher', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text="Введите описание учебного корпуса")
    faculty = models.ManyToManyField(faculty, help_text="Выберите факультет")
    def __str__(self) :
        return self.title
    def get_absolute_url(self):
        return reverse('Данные о курсе', args=[str(self.id)])
    
    def display_faculty(self):
        return ', '.join([ faculty.name for faculty in self.faculty.all()[:3] ])
    display_faculty.short_description = 'Faculty'

class teacher(models.Model) :
    first_name = models.CharField(max_length=100, help_text="Введите имя преподавателя")
    last_name = models.CharField(max_length=100, help_text="Введите фамилию")
    date_of_birth = models.DateField(null=True, blank=True)

    def get_absolute_url(self) :
        return reverse('Данные о преподавателе', args=[str(self.id)])
    
    def __str__(self) :
        return '%s, %s' % (self.last_name, self.first_name)