from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
import json
from johnPiCar import picar

pc = picar.Picar(11,12,13,15,37,38,50)
cf = 'cfpd'
 
#主控页面
def mainPage(request):
    context = {}
    return render(request,'Control.html',context)
 

# 接收请求数据
def control(request):
    request.encoding='utf-8'
    if 'direction' in request.GET and request.GET['direction']:
        jianwei = request.GET['direction']
        global cf
        if cf != jianwei:
            print('进入')
            print('重复：'+cf)
            print('键位：'+jianwei)
            print(cf != jianwei)
            cf = jianwei
            if jianwei == 'kup':
                pc.stop()
            else:
                if jianwei == 'W':
                    pc.forward(0)
                elif jianwei == 'S':
                    pc.backwards(0)
                elif jianwei == 'A':
                    pc.turnLeft(0)
                elif jianwei == 'D':
                    pc.turnRight(0)
                elif jianwei == 'Q':
                    pc.anticlockwise(0)
                elif jianwei == 'E':
                    pc.clockwise(0)
                elif jianwei == '1':
                    pc.speed = 30
                elif jianwei == '2':
                    pc.speed = 50
                elif jianwei == '3':
                    pc.speed = 100

    data = {}
    data['mes'] = jianwei
    return HttpResponse(json.dumps(data))

