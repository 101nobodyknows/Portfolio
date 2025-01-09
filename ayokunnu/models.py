from django.db import models

category_choice = [
    ('Website', 'Website'),
    ('Graphics', 'Graphics')
]

class new_message(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    message = models.TextField()
    
    def str(self):
        return self.name
    
class education(models.Model):
    location = models.TextField()
    cert = models.TextField()
    start_date = models.IntegerField()
    end_date = models.IntegerField(default=True)
    
    def str(self):
        return self.cert
    
class image_gallery(models.Model):
    main_img = models.ImageField(upload_to="gallery_images/")
    img_name = models.TextField(blank=True)
    img_desc = models.TextField()
    img_category = models.CharField(
        max_length=10,
        choices=category_choice
    )
    img_link = models.TextField(blank=True)
    
    def str(self):
        return self.img_name
    
class about(models.Model):
    name = models.TextField(default="AY_REACT")
    my_desc = models.TextField()
    my_img = models.ImageField(upload_to="gallery_images/", blank=True)
    x_link = models.TextField(blank=True)
    git_link = models.TextField(blank=True)
    insta_link = models.TextField(blank=True)
    email = models.TextField(blank=True)
    wa_link = models.TextField(blank=True)
    
    def str(self):
        return self.my_desc