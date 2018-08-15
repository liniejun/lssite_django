from django.shortcuts import render
from tutorial import models

# Create your views here.

def index(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        print(username, password)
        # 添加数据到数据库
        temp = {'user':username, 'pwd':password}
        models.UserInfo.objects.create(user=username, pwd=password)

    #从数据库取出所有用户用于展示
    user_list = models.UserInfo.objects.all()
    return render(request, 'tutorial/index.html', {'data': user_list})