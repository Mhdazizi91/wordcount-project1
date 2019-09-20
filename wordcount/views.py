from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return HttpResponse('hello')
def homepage(request):
    return render(request,'homepage.html')  # how to call an html page in separate folder
def count(request):
    fulltext = request.GET['fulltext']
    x = fulltext.split()
    worddic = {}
    for word in x:
        if word in worddic:
            worddic[word] += 1
        else:
            worddic[word] = 1
    sortedwords = sorted(worddic.items(), key=operator.itemgetter(1), reverse=True)
    return render(request,'count.html', {'fulltext':fulltext,'count':len(x), 'worddic' : sortedwords})  # how to call an html page in separate folder
def about(request):
    return render(request,'about.html')  # how to call an html page in separate folder