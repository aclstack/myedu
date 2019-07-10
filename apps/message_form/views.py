from django.shortcuts import render
from apps.message_form.models import Message

# Create your views here.

def message_form(request):
    # 拼凑SQL语句
    # all_message = Message.objects.all()

    # # 真正执行SQL语句
    # for message in all_message:
    #      print(message.name)

    # filter 语句，查不到返回空
    # all_message = Message.objects.filter(name="bobby")

    # get 返回的是一个对象，数据不存在货多个则会报错,此操作会立即执行，而不再拼凑SQL
    # message = Message.objects.get(name="bobby1")
    # 删除操作
    # message.delete()

    # 数据插入,如果存在则覆盖
    # message = Message()
    # message.name ='ZS'
    # message.email = 'zs@qq.com'
    # message.address ='北京'
    # message.message = '咱也不知道，咱也不敢问'
    # message.save()

    # 请求提交时，request为uwsgi对象
    var_dict = {}
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        address = request.POST.get("address", "")
        message_text = request.POST.get("message", "")

        message = Message()
        message.name = name
        message.email = email
        message.address = address
        message.message = message_text
        message.save()
    elif request.method == "GET":
        all_message = Message.objects.filter()
        if all_message:
            message = all_message[0]
            var_dict = {"message": message}
    return render(request, 'message_form.html', var_dict)
