from django.forms import forms
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView
from example.models import GiftList, Gift
from example.forms import GiftListForm

def hello_world(request):
    return render(request, 'example/index.html', {})
    # return HttpResponse('Hello World!')


def hello_name(request, name):
    return HttpResponse('Hello, {name}!'.format(name=name))


def simple_list_view(request):
    gfl_entries = GiftList.objects.all()
    return render(
        request,
        'example/list.html',
        {'gfl_entries': gfl_entries}
    )


class GiftListView(ListView):
    model = GiftList
    template_name = 'example/list.html'
    context_object_name = 'gfl_entries'


def GiftView(request, giftlist_id):
    gfl_gifts = Gift.objects.filter(gift_list=giftlist_id)
    return render(
        request,
        'example/gift.html',
        {'gfl_gifts': gfl_gifts}
    )


class PostCreateView(CreateView):
    model = GiftList
    form_class = GiftListForm
    success_url = '/gift_list'
    template_name = 'example/add.html'


class RemoveView(DeleteView):
    model = GiftList
    form_class = GiftListForm
    success_url = '/gift_list'
    template_name = 'example/remove.html'


class PostCreateGiftView(CreateView):
    model = Gift
    form_class = GiftListForm
    success_url = '/gift_list/add'
    template_name = 'example/add.html'


class RemoveGiftView(DeleteView):
    model = Gift
    form_class = GiftListForm
    success_url = '/gift_list'
    template_name = 'example/remove.html'


