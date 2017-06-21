from django.db import models

# Create your models here.
class Phonebook(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    phone_num = models.CharField(max_length=11)
    email = models.EmailField()
    city = models.CharField(max_length = 10)
    zip_code = models.CharField(max_length =5)

    def __unicode__(self):
        return '%s %s' %(self.f_name, self.l_name)

    class Meta:
        ordering = ['l_name']
