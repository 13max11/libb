from django.db import models

# Create your models here.

class LibraryBook(models.Model):
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    isbn = models.CharField(max_length=13, primary_key=True)
    available = models.BooleanField()

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['author', 'title']
        #db_table - змінити назву таблички
        #verbose_name - в адмінці
        #verbose_name_plural - в множині
        #unique_together - унікальні разом