from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    dob = models.DateField(auto_now=False, auto_now_add=False)
    state = models.CharField(choices=(("T", "Telangana"),("AP","Andhra Pradesh"),("M","Maharashtra"),("K","Karnataka"),("Tm","Tamil Nadu")),max_length=100)
    gender = models.CharField(choices=(("M", "Male"),("F","Female")), max_length=100)
    pimage = models.ImageField(upload_to='pimages', blank = True)
    rdoc = models.FileField(upload_to="rdocs", blank=True)
    
    def __str__(self):
        return self.name