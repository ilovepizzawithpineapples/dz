from django.shortcuts import render

from .models import POST

from comments.models import COMMENTS


# Create your views here.
def posts_list(request):
    posts = POST.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts })

def post_detail(request, id):
    post = POST.objects.get(id=id)
    c_ = COMMENTS.get_id_comments(id)
 
    print()
    print()
    print(c_)
    print()
    print()
 


    return render(request, 'blog/post_detail.html', context={'post': post, 'c_': c_})