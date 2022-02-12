import numpy as np
import os
import pixellib
from pixellib.torchbackend.instance import instanceSegmentation
ins = instanceSegmentation()
ins.load_model(POINTREND_MODEL_PATH)

def runPointrendModel(picture_path = os.path.join(os.path.dirname(__file__),  "images", "art.jpg"), 
                        output_image_name="media/images/output11.png"):
    r , output = ins.segmentImage(picture_path, show_bboxes=True, output_image_name=output_image_name)
    return r, output

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
