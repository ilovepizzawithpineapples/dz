from django.urls import path


from .views import *


urlpatterns = [
    path('', posts_list, name='post_list_url'), #чтобы просто открыть в других частях проекта
    path('post/<id>/', post_detail, name='post_detail_url')
#
]