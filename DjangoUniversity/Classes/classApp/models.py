from django.db import models

class DjangoClasses(models.Model):
    Title = models.CharField(max_length=60)
    Course_Number = models.IntegerField(blank=True, null=True)
    Instructor_Name = models.CharField(max_length=60)
    Duration = models.DurationField()


    objects = models.Manager()

    def __str__(self):
        return self.Title
