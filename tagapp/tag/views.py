from django.shortcuts import render

# Create your views here.

def index(request):
    scores = [78, 83, 90, 87, 62, 71]
    return render(request, 'index.html', locals())

def tag(request):
    subjects = ['國文', '英文', '數學', '自然','社會']
    scores = [78, 83, 90, 62, 87]
    return render(request, 'tag.html', locals())
