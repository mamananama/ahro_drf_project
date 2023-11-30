from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DeleteView
from django.conf import settings
import requests
import json

import utils.context_process


# class PostListView(ListView):
#     template_name = "rounge/index.html"

#     def get_context_data(self, **kwargs):
#         print(self)


def postlist(request):
    requestData = requests.get(
        f'http://{settings.BACK_END_URL}/rounge/api/')
    data = json.loads(requestData.text)
    context = {'data': data}
    return render(request, 'rounge/index.html', context)


def postdetail(request, pk):
    requestData = requests.get(
        f'http://{settings.BACK_END_URL}/rounge/api/{pk}/')
    data = json.loads(requestData.text)
    
    context = {'data': data, 'pk': pk, 'user': request.user}
    return render(request, 'rounge/post.html', context)


def postcreate(request):
    return render(request, 'rounge/create.html')


def postupdate(request, pk):
    requestData = requests.get(
        f'http://{settings.BACK_END_URL}/rounge/api/{pk}/')
    data = json.loads(requestData.text)
    context = {'post': data, 'pk': pk}
    return render(request, 'rounge/update.html', context)
