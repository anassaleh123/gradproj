from django.shortcuts import render

# Create your views here.

def index(request):
    #dict x= {'name':'ali'}
    return render(request, 'pages/index.html')


def add_acc(request):
    return render(request, 'pages/add-acc.html') 


def add_bracelet(request):
    return render(request, 'pages/add-bracelet.html')


def add_faq(request):
    return render(request, 'pages/add-faq.html')                    


def add_users(request):
    return render(request, 'pages/add-users.html')


def add(request):
    return render(request, 'pages/add.html')             


def show(request):
    return render(request, 'pages/show.html')             


def show_bracelet(request):
    return render(request, 'pages/show-bracelet.html')   



def show_faq(request):
    return render(request, 'pages/show-faq.html')                    


def show_users(request):
    return render(request, 'pages/show-users.html')


def show_users(request):
    return render(request, 'pages/show-users.html')


def show_acc(request):
    return render(request, 'pages/show-acc.html')     