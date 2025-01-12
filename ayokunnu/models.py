from django.db import models
from cloudinary.models import CloudinaryField

# Choices for categories
category_choice = [
    ('Website', 'Website'),
    ('Graphics', 'Graphics'),
]

class NewMessage(models.Model):  # Class names should use PascalCase (best practice)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    message = models.TextField()
    
    def __str__(self):  # Fixed the method name to `__str__`
        return self.name
    
class Education(models.Model):  # Updated class name for consistency
    location = models.TextField()
    cert = models.TextField()
    start_date = models.TextField()
    end_date = models.TextField(default=True)
    
    def __str__(self):  # Fixed the method name to `__str__`
        return self.cert
    
class ImageGallery(models.Model):  # Updated class name for consistency
    main_img = CloudinaryField('image')  # Replaced with CloudinaryField
    img_name = models.TextField(blank=True)
    img_desc = models.TextField()
    img_category = models.CharField(
        max_length=10,
        choices=category_choice
    )
    img_link = models.TextField(blank=True)
    
    def __str__(self):  # Fixed the method name to `__str__`
        return self.img_name
    
class About(models.Model):  # Updated class name for consistency
    name = models.TextField(default="AY_REACT")
    my_desc = models.TextField()
    my_img = CloudinaryField('image', blank=True)  # Replaced with CloudinaryField
    my_cv = CloudinaryField('image', blank=True)  # Replaced with CloudinaryField
    x_link = models.TextField(blank=True)
    git_link = models.TextField(blank=True)
    insta_link = models.TextField(blank=True)
    email = models.TextField(blank=True)
    wa_link = models.TextField(blank=True)
    phone = models.TextField(blank=True, default='07044584688')
    
    def __str__(self):  # Fixed the method name to `__str__`
        return self.my_desc
