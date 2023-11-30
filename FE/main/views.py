import json
import requests
from django.conf import settings
from django.shortcuts import render


def index(request):
    requestPosts = requests.get(
        f'http://{settings.BACK_END_URL}/rounge/api/')
    postdata = json.loads(requestPosts.text)
    context = {"postdata": postdata}

    return render(request, 'main/index.html', context)
