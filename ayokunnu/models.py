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
    main_img = models.ImageField(upload_to="static/gallery_images")
    img_name = models.TextField()
    img_desc = models.TextField()
    img_category = models.CharField(
        max_length=10,
        choices=category_choice
    )
    img_link = models.TextField(blank=True)
    
    def str(self):
        return self.img_name
    
class about(models.Model):
    my_desc = models.TextField()
    my_img = models.ImageField(upload_to="static/gallery_images", blank=True)
    
    def str(self):
        return self.my_desc