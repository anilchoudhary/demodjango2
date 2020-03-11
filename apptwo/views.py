from django.shortcuts import render
from django.http import HttpResponse
from apptwo.models import User
# Create your views here.


def help(request):
    my_dict = {'insert_me': "please use users/ in URL "}
    return render(request, 'apptwo/help.html', context=my_dict)


def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'user': user_list}
    return render(request, 'apptwo/user.html', context=user_dict)
