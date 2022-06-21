from django.http import HttpResponse
from django.shortcuts import render
import paho.mqtt.client as mqtt
import json

def control(request):

    return render(request, 'control.html')


def pub(request):
    message = request.POST.get('message')
    client = mqtt.Client(transport="websockets")
    client.connect('13.125.175.118', 1883)
    client.loop_start()
    client.publish('/upi/control', message, 1)

    return HttpResponse("return this string")


