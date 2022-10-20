from django.urls import path
from . import views

# This is a URLConf module
urlpatterns = [
    # path functions return URLPattern objects

    # because we added 'playground/' in the main project's url.py file
    # and linked it to the urls.py file here through the include module
    # the path here should be changed from 'playground/hello' to simply
    # 'hello/'
    path('hello/', views.say_hello),
    path('hellov2/', views.say_hello_v2)
]