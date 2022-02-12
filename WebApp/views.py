from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from .forms import UploadForm
from .models import FormModel,SaveModel
from django.contrib import messages
from django.http import JsonResponse

from django.core.files import File

import numpy as np
import os















#[top left x position, top left y position, width, height].





def appindex(request):
     return render(request,"index.html")


# x=[]
def test(request):
    context = {}
   
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid() and request.POST.get('cars') and request.POST.get('cars1'):
            img = form.cleaned_data.get("Image")
            obj =FormModel.objects.create(img = img,)
            obj.save()
            print(obj)
            data=SaveModel()
            data.modeltype =request.POST.get('cars')
            data.task=request.POST.get('cars1')
            data.save()
            img = FormModel.objects.all()
            image = np.array(img)
            print(image.shape)
            form_data_values=SaveModel.objects.last()
            print(form_data_values)
            # x.append(a)
            # print(Dirs(a))
            print("Hello",form_data_values.modeltype)
            print("Hi",form_data_values.task)
            # print("Hello",a.choices)
            global selection_type
            selection_type=MODEL_TYPE[form_data_values.modeltype]
            return redirect('result')    


            
    else:
        form = UploadForm()
    
    context['form']= form
    return render( request, "upload.html", context)  

def predict(request):
    if request.method =='GET':
        images = FormModel.objects.last() # all()
        # print("Image Type :", type(images.__class__.__name__))
        # print("Direc :", dir(images))
        print("Image Path :", images.img)
        print("IDs :", images.id)
        image_path = os.path.join(CURRENT_FOLDER, "media", str(images.img))
        image_id = images.id
        if selection_type==1:
            r, output = runPointrendModel(image_path)
            newdict = createDict(r)
            writeJSON(simpleDict(r), os.path.join(CURRENT_FOLDER,"WebApp", "static","demo.json"))
            # images = os.path.join(CURRENT_FOLDER, "media", "images",  "out.png") 
            # G:\GitLab\Manthan21\WebApp\static\images
            images = os.path.join(CURRENT_FOLDER, "WebApp", "static", "images", "out.png") 
            print("Saving Image to : ",images)
            saveImg(filename = images, img = output)
            images = os.path.join("media", "images",  "out.png") 

        elif selection_type==2 or selection_type==3:
            colorized=insegmentation(image_path)
            images = os.path.join(CURRENT_FOLDER, "WebApp", "static", "images", "out.png") 
            print("Saving Image to : ",images)
            print(type(colorized))
            colorized_array=np.asarray(colorized).astype("uint8")
            saveImg(filename = images, img = colorized_array,cvtColor=False)
            images = os.path.join("media", "images",  "out.png")
        else:
            # for image in images:
            #     new_images = image.img.url
            # images = new_images
            print("Image Type :", type(images.__class__.__name__))
            print("Direc :", dir(images))
            images = [images]
        #     {% for image in images %}
        # <img src="{{image.img.url}}" />
        # {%endfor%}
        # "{%url_for('static', filename='od.png' )%}"
        print("Output Image Path :", images)
        return render(request, 'predict.html',{'images' : images})    
    
            #   print("Image Type :", type(img.__class__.__name__))
            #   print("Direc :", dir(img))
            
            
    return render(request, 'index.html')



def result(request):
    return render(request, "result.html")

# G:\GitLab\Manthan21\media\images\out.png