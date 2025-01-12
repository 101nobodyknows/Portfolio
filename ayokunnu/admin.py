from django.contrib import admin
from .models import NewMessage, Education, ImageGallery, About

class NewMessageAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'email', 'message')
    search_fields = ('id', 'email')
    list_filter = ('email',)

class EducationAdmin(admin.ModelAdmin):
    list_display = ('id','location', 'cert', 'start_date', 'end_date')
    search_fields = ('id', 'cert')
    list_filter = ('cert',)
    
class ImageGalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'img_category', 'main_img')
    search_fields = ('id', 'img_name', 'img_category')
    list_filter = ('img_category',)

class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'my_img')
    
admin.site.register(NewMessage, NewMessageAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(ImageGallery, ImageGalleryAdmin)
admin.site.register(About, AboutAdmin)