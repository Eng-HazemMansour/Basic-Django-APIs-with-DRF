from django.db import models


#Table fields
class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=50)
    picture = models.ImageField(blank = True)


#This function is to view the note with its title in the Django admin notes list
    def __str__(self):
        return self.title