# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 17:31:36 2021

@author: info
"""

#I HAVE CREATED THIS FILE -RAJAT GARG
from django.http import HttpResponse

def index(request):
    return HttpResponse('''Hello who are you<a href ="https://www.linkedin.com/mynetwork/"> MYProfile linkedin</a>''')

def about(request):
    return HttpResponse('''<h1>RAJAT GARG</h1><a href="https://www.youtube.com/results?search_query=Rajat+garg+a+simple+magic+trick">Django with Rajat</a>''')
def also(request):
    file=open("1.txt")
    return HttpResponse(file.read())