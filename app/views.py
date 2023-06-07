from django.shortcuts import render

# Create your views here.
def cdn_specific_static(request):
    return render(request,'cdn_specific_static.html')