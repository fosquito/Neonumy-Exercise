from django.db import models

class Image(models.Model):
    img = models.ImageField(blank=True, null=True, upload_to='images')
    
    class Meta:
        managed = True
        db_table = 'Image'
