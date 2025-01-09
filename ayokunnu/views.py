from django.shortcuts import render, redirect, get_object_or_404
from .models import new_message, education, image_gallery, about
from django.urls import reverse
import random
from django.db.models import Q

#pages
def home(request):
    edu_list = education.objects.all()
    about_list = list(about.objects.all())
    context = {
        'edu_list':edu_list,
        'about':about_list[-1]
    }
    return render(request, 'ayokunnu/index.html', context)

def projects(request):
    #getting the images
    images = image_gallery.objects.all()
    about_list = list(about.objects.all())
    
    #search feature
    query = request.GET.get('query')
    results = []
    if query:
        results = list(
            image_gallery.objects.filter(
                Q(img_name__icontains = query) |
                Q(img_desc__icontains = query) |
                Q(img_category__icontains = query)
            )
        )
        image_list = results
    else:
        image_list = images
    
    #empty lists created to hold websites and graphics individually
    website_list = []
    graphics_list = []
    
    #system to seperate the images into different lists
    for image in image_list:
        if image.img_category.lower() == 'website':
            website_list.append(image)
        else:
            graphics_list.append(image)
    
    #shuffling the iamges
    random.shuffle(website_list)
    random.shuffle(graphics_list)
    
    #taking the length of the lists
    image_length = len(image_list)
    website_length = len(website_list)
    graphics_length = len(graphics_list)
    
    #passing all needed variables to the template through context
    if query != '':
        context = {
            'query':query,
            'website_list':website_list,
            'graphics_list':graphics_list,
            'image_length':image_length,
            'website_length':website_length,
            'graphics_length':graphics_length,
            'about':about_list
        }
    else:
        context = {
            'website_list':website_list,
            'graphics_list':graphics_list,
            'image_length':image_length,
            'website_length':website_length,
            'graphics_length':graphics_length,
            'about':about_list
        }
    return render(request, 'ayokunnu/project.html', context)

#messages system
def sub_message(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        
        NewMessage = new_message.objects.create(name=name, email=email, message=message)
        NewMessage.save()
        
        message_id = NewMessage.id
        return redirect(reverse('message_submitted', kwargs={'message_id':message_id}))
    return render(request, 'ayokunnu/index.html')

def message_sub(request, message_id):
    user_message = get_object_or_404(new_message, id=message_id)
    
    context = {
        'user_message':user_message
    }
    return render(request, 'ayokunnu/success.html', context)