from django.shortcuts import render
from .models import Chain
from django.http import Http404


# Create your views here.
def index(request):
    chain_list = Chain.objects.order_by('-reg_date')
    context = {'chain_list': chain_list}
    return render(request, 'psw/index.html', context)


def view(request, chain_id):
    try:
        chain = Chain.objects.get(pk=chain_id)
        context = {'chain': chain}
    except Chain.DoesNotExist:
        raise Http404("Chain does not exist")
    return render(request, 'psw/index.html', context)


def reg():
    pass


def add():
    pass


def edit():
    pass


