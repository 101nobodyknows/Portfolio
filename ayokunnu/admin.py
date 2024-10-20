from django.contrib import admin
from .models import new_message, education, image_gallery, about

class NewMessageAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'email', 'message')
    search_fields = ('id', 'email')
    list_filter = ('email',)

class EducationAdmin(admin.ModelAdmin):
    list_display = ('id','location', 'cert', 'start_date', 'end_date')
    search_fields = ('id', 'cert')
    list_filter = ('cert',)
    
class ImageGalleryAdmin(admin.ModelAdmin):
    list_display = ('id','img_name', 'img_category', 'main_img')
    search_fields = ('id', 'img_name', 'img_category')
    list_filter = ('img_category',)
    
admin.site.register(new_message, NewMessageAdmin)
admin.site.register(education, EducationAdmin)
admin.site.register(image_gallery, ImageGalleryAdmin)
admin.site.register(about)