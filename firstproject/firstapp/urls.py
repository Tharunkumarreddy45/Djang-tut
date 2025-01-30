from django.urls import path
from . import views

urlpatterns=[
    path('',views.functioncall,name="name"),
    path('about/<str:name>/<int:age>',views.about,name="about"),
    path('welcome/<str:name>/<num>',views.call,name='call'),
    path('page',views.page,name='page'),
    path('second',views.second,name='second'),
    path('third',views.third,name='third'),
    path("image/<str:name>",views.image,name='image'),
    path('form',views.form,name='form'),
    path('submit',views.submit,name="submit"),
    path('reactrendering',views.reactrendering,name="reactrendering")

]