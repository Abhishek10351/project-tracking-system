from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

    def get_employee_count(self):
        return Employee.objects.filter(project=self).count()

    class Meta:
        ordering = ["name"]


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_project_name(self):
        return self.project.name

    class Meta:
        ordering = ["name"]
