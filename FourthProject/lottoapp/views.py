from django.shortcuts import render
import random

def home(request):
    return render(request, 'lottoapp/home.html')

def result(request):
    list = ['김유진', '박혜준', '노은성', '김소은', '강연우', '김정운', '김서영', '이연수', '오예림', '장한빛', '황서경', '안현주', '문다연', '박경나', '이민정', '조원아']
    partner = random.sample(list, 1)
    partner = "".join(partner)

    return render(request, 'lottoapp/result.html', {'partner': partner})

# Create your views here.
