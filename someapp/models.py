from django.db import models

class Author(models.Model):
    full_name = models.CharField(max_length=100)
    birth_year = models.IntegerField(null=True, blank=True)
    bio = models.TextField(blank=True)
    
    def __str__(self):
        return self.full_name

class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    
    def __str__(self):
        return self.name