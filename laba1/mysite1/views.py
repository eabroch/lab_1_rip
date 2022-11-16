from django.shortcuts import render, redirect
from django.http import HttpResponse
def index(request):
    return render(request, 'index.html')

macbooks_list = [
    {
        'id': 0,
        'name': 'Macbook Pro',
        'text': '''Подойдет для всего'''
    },
    {
        'id': 1,
        'name': 'Macbook Air',
        'text': '''Для просмотра кино и небольших задач'''
    }
]

ipads_list = [
    {
        'id': 0,
        'name': 'Ipad Pro',
        'text': '''Идеальный Ipad для всего'''
    },
    {
        'id': 1,
        'name': 'Ipad Air',
        'text': '''Хороший Ipad'''
    },
    {
        'id': 2,
        'name': 'Ipad Mini',
        'text': '''Тоже хороший, но лучше Air'''
    },
]

def macbooks(request):
    return render(request, 'macbooks.html', {
        'macbooks': macbooks_list
    })

def ipads(request):
    return render(request, 'ipads.html', {
        'ipads': ipads_list
    })

def catalog_macbooks(request, number):
    if number < len(macbooks_list):
        return render(request, 'catalog_macbooks.html', macbooks_list[number])
    else:
        return redirect('/')

def catalog_ipads(request, number):
     if number < len(ipads_list):
        return render(request, 'catalog_macbooks.html', ipads_list[number])
     else:
         return redirect('/')

# Create your views here.