from django.shortcuts import render
import random

def home(request):
    return render(request, 'lottoapp/home.html')

def result(request):
    num = random.sample(range(1,47),6)

    list = ('사과', '딸기', '포도', '배', '키위', '복숭아')
    fruits = random.sample(list, 2)

    return render(request, 'lottoapp/result.html', {'num': num, 'fruits': fruits})

# Create your views here.
