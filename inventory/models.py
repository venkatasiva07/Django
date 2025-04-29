from django.db import models
    
class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True, verbose_name='Name')
    brand = models.CharField(max_length=30, verbose_name='Brand')  # <-- New field
    quantity = models.IntegerField(default=1)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
	    return self.name