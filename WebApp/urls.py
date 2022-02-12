from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.appindex,name="app-index"),
    path('test',views.test,name="test"),
   path('result',views.result,name="result"),
    path('predict',views.predict,name="result"),
]
