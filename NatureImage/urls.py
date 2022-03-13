from django.urls import path

from .views import main, save, send, thanks, saveimage

urlpatterns = [
    path('', main, name='main'),
    path('save/', save, name='save'),
    path('send/', send, name='send'),
    path('thanks/', thanks, name='thanks'),
    path('saveimg/', saveimage, name='saveimg')
]