from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import People
from django.http import Http404
from django.views.decorators import csrf


# Create your views here.


def index(request):
    people_list = People.objects.order_by('-pub_date')[:5]
    template = loader.get_template('contact/index.html')
    context = {
        'people_list': people_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, people_id):
    try:
        people = People.objects.get(pk=people_id)
    except People.DoesNotExist:
        raise Http404('该人不在通讯录')
    return render(request, 'contact/detail.html', {'people': people})


def search(request):
    ctx = {}

    if request.POST:
        ctx['rlt'] = request.POST['q']
        name = request.POST['q']
        print(request.POST['q'])
        try:
            people = People.objects.get(name_text=name)
        except:
            raise Http404("该人不在通讯录")

    return render(request, 'contact/detail.html', {'people': people})
