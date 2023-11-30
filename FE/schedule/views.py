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


def scheduleList(request):
    requestData = requests.get(
        f'http://{settings.BACK_END_URL}/schedule/api/')
    data = json.loads(requestData.text)
    context = {'data': data}
    return render(request, 'schedule/index.html', context)


def scheduleDetail(request, pk):
    requestData = requests.get(
        f'http://{settings.BACK_END_URL}/schedule/api/{pk}/')
    data = json.loads(requestData.text)
    context = {'data': data, 'pk': pk}
    return render(request, 'schedule/post.html', context)


def scheduleCreate(request):
    return render(request, 'schedule/create.html')


def scheduleUpdate(request, pk):
    requestData = requests.get(
        f'http://{settings.BACK_END_URL}/schedule/api/{pk}/')
    data = json.loads(requestData.text)
    context = {'schedule': data, 'pk': pk}
    return render(request, 'schedule/update.html', context)
