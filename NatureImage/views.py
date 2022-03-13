from django.shortcuts import render, redirect
from .models import NatureImage
from django.core.mail import send_mail
from django.http import HttpResponse
from random import randint

# Create your views here.

def main(request):
    return render(request, 'NatureImage/main.html')


def save(request):
    width = request.POST.get("width")
    height = request.POST.get("height")
    id = randint(0,999)
    url = f'https://picsum.photos/id/{id}/{height}/{height}'

    request.session['width'] = width
    request.session['height'] = height
    request.session['url'] = url

    data = {'width': width,
            'height': height,
            'url': url}

    return render(request, 'NatureImage/save.html', data)


def saveimage(request):
    if request.method == 'POST':
        width = request.session['width']
        height = request.session['height']
        url = request.session['url']
        description = request.POST.get('description')
        image = NatureImage(width=width, height=height, url=url, description=description)
        try:
            image.save()
            return redirect('send')
        except Exception as err:
            print(err)
            return HttpResponse(status=409)


def send(request):
    return render(request, 'NatureImage/send.html')


def thanks(request):
    url = request.session['url']
    user_email = request.POST.get('email')
    send_mail('Link for image!', f'Here is your image: {url}', "aliaksei.severyn.work@gmail.com", [f'{user_email}'])
    return render(request, 'NatureImage/thanks_page.html')