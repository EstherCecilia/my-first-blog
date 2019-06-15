from django.db import models
from django.utils import timezone


class Task(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Label(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name




class Document(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    label = models.ForeignKey(Label, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.label
    
class Term(models.Model):
    name = models.CharField(max_length=200)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class OcorrenciaTermo(models.Model):
    term = models.ForeignKey(Term, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.term

