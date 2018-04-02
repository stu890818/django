# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django import template

def here(request):
    return HttpResponse('媽，我在這！')

def math(request, a, b):
    a = int(a)
    b = int(b)
    s = a + b
    d = a - b
    p = a * b
    q = a / b
    # t = get_template('math.html')
    # c = template.Context({'s':s, 'd':d, 'p':p, 'q':q})
    # return HttpResponse(t.render(c))
    return render_to_response('math.html',{'s':s, 'd':d, 'p':p, 'q':q})

def menu(request):
    food = { 'name':'番茄炒蛋', 'price':60, 'comment':'好吃', 'is_spicy':False }
    food2 = { 'name':'蒜泥白肉', 'price':100, 'comment':'人氣推薦', 'is_spicy':True }
    foods = [food, food2]
    return render_to_response('menu.html',locals())
    