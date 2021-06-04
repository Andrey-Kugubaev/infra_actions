from django.http import HttpResponse


def index(request):
    return HttpResponse('Хм, а где: У меня получилось!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
