from django.db import models
from projects.models import Project, Employee
# from employees.models import Employee




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
