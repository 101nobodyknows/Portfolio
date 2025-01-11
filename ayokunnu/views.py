from django.shortcuts import render, redirect, get_object_or_404
from .models import new_message, education, image_gallery, about
from django.urls import reverse
import random
from django.db.models import Q
from django.http import HttpResponse
import requests

#pages
def home(request):
    edu_list = education.objects.all()
    about_list = list(about.objects.all())
    default_about = ""

    my_about = about_list[-1] if about_list else default_about
    context = {
        'edu_list':edu_list,
        'about':my_about
    }
    return render(request, 'ayokunnu/index.html', context)

def projects(request):
    #getting the images
    images = image_gallery.objects.all()
    about_list = list(about.objects.all())
    default_about = ""

    my_about = about_list[-1] if about_list else default_about
    
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
            'about':my_about
        }
    else:
        context = {
            'website_list':website_list,
            'graphics_list':graphics_list,
            'image_length':image_length,
            'website_length':website_length,
            'graphics_length':graphics_length,
            'about':my_about
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

#download system
def download_file(request):
    # Get the file_url from query parameters
    file_url = request.GET.get('file_url')
    if not file_url:
        return HttpResponse("File URL is missing", status=400)

    # Fetch the file from the provided URL
    response = requests.get(file_url, stream=True)
    if response.status_code != 200:
        return HttpResponse("Error fetching the file", status=response.status_code)

    # Force the filename to be "ay_react_gallery_image.jpg"
    filename = "ay_react_img.jpg"

    # Prepare the HTTP response with the forced filename and `.jpg` extension
    download_response = HttpResponse(response.content, content_type="image/jpeg")
    download_response['Content-Disposition'] = f'attachment; filename="{filename}"'

    return download_response
