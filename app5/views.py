from django.shortcuts import render

# Create your views here.
def hai(request):
    return render(request,'hai.html',context={'a':155,'b':1240,'c':1458})