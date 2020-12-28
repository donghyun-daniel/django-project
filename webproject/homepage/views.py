from django.shortcuts import HttpResponse, render
from .models import Coffee, Introduction
# render함수는 인자로 3개를 받는다
# render(request, '.html', {})
# template에서 쓸 변수는 view.py에 name처럼 선언되어있어야한다

# Create your views here.
def index(request):
    name = "Donghyun Sung"
    nums = [1, 2, 3, 4]
    return render(request, 'index.html', {"my_name" : name, "my_list" : nums})

def introduction_view(request):
    introduction_all = Introduction.objects.all() # 모두 가져온다
    return render(request, 'introduction.html', {})
# return문: 모델에서 가져온 introduction_list를 가져와서 introduction.html에 받아온다

def coffee_view(request):
    coffee_all = Coffee.objects.all() # 모두 가져온다
    return render(request, 'coffee.html', {"coffee_list" : coffee_all})
# return문: 모델에서 가져온 coffee_list를 가져와서 coffee.html에 받아온다