from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from .forms import UploadForm
from .models import FormModel,SaveModel
from django.contrib import messages
from django.http import JsonResponse

from django.core.files import File

from fastseg import MobileV3Large
from fastseg.image import colorize, blend


import torch

import json
import numpy as np
import os
import cv2


MODEL_TYPE = {
    "PointRend" : 1,
    "MobileNetV3Large" : 2,
    "MobileNetV3Small" : 3
}

TASK_TYPE = {
    "Object Detection" : 1,
    "Instance Segmentation (Map)" : 2,
    "Instance Segmentation (Blend)" : 3
}
global ins

#POINTREND_MODEL_PATH =  "G:\GitLab\Objectify\LabelMeData\pointrend_resnet50.pkl" #  "D:\GITHUB MLXTREME\ML\LabelMeData\pointrend_resnet50.pkl"
global selection_type
selection_type = 2



"""
0 : No Ml model to run 
1 : Object Detection : PointRend
2 : Instance Detection (Map) : MobileV3Large 
3 : Instance Detection (Blend) : MobileV3Large 
"""


global form_data_values
form_data_values=0
BASE_FOLDER = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CURRENT_FOLDER = BASE_FOLDER
print("Current Directory :",CURRENT_FOLDER)

MODEL_FOLDER=os.path.join(BASE_FOLDER,"models")

POINTREND_MODEL_PATH=os.path.join(MODEL_FOLDER,"pointrend_resnet50.pkl")

print(POINTREND_MODEL_PATH)


if torch.cuda.is_available():
    model = MobileV3Large.from_pretrained().cuda().eval()
else:
    model = MobileV3Large.from_pretrained().eval()

import pixellib
from pixellib.torchbackend.instance import instanceSegmentation

ins = instanceSegmentation()
ins.load_model(POINTREND_MODEL_PATH)

def insegmentation(imgpath):
    # read the image , convert BGR2RGB , perform mxnet prediction return mask result 
    imgvar=cv2.imread(imgpath)
    image = cv2.cvtColor(imgvar, cv2.COLOR_BGR2RGB )
    labels = model.predict_one(image)
    colorized = colorize(labels)
    return colorized


def saveImg(filename, img, cvtColor=True):
    if cvtColor:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.imwrite(filename, img)
    return True


class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        
        return super(NpEncoder, self).default(obj)

def writeJSON(newdict, json_path = 'static/result.json'):
    x = json.dumps(newdict, cls=NpEncoder,indent=4)
    # print(x)
    with open(json_path, 'w') as fp:
        fp.write(x)
    return True

def runPointrendModel(picture_path = os.path.join(os.path.dirname(__file__),  "images", "art.jpg"), 
                        output_image_name="media/images/output11.png"):
    r , output = ins.segmentImage(picture_path, show_bboxes=True, output_image_name=output_image_name)
    return r, output

#[top left x position, top left y position, width, height].
def createDict(r):
    newdict={}
    for i,(bbox, cname, sc) in enumerate(zip(r["boxes"] , r["class_names"], np.array(r["scores"]))): 
        newdict[i+1]=cname,bbox,sc
    return newdict

def simpleDict(r):
    cnames = []
    for cname in r["class_names"]:
        cnames.append(cname)
    cnames = list(set(cnames))
    return [{"label" : cnames}]





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