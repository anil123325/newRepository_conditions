from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'a':10,'b':5,'c':3}
    d1={'name':'anil'}
    return render(request,'condition.html',d1)
