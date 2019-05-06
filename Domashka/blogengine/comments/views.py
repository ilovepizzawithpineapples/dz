from django.shortcuts import render

from .models import COMMENTS
# Create your views here.


def comments_list(request):
    comments = COMMENTS.objects.all()
    return render(request, 'comments/comments_detail.html', context={'comments ': comments  })
