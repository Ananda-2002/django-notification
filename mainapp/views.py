from django.shortcuts import render
from .models import percentage
# Create your views here.


def home(request):
    print(id)
    percentage_objs = percentage.objects.all()
    return render(request, 'index.html', {
        'percentages': percentage_objs
    })


def post(request, id):
    percentage_objs = percentage.objects.filter(id=id)
    return render(request, 'post.html', {
        'percentage': percentage_objs
    })
