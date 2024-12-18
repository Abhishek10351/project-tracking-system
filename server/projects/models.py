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


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    due_date = models.DateField()

    def __str__(self):
        return self.title

    def get_project_name(self):
        return self.project.name

    def get_employee_name(self):
        return self.employee.name

    class Meta:
        ordering = ["due_date"]
