from django.shortcuts import render

def home(request):
    return render(request, 'dev/home.html', {'test':'TEST'})

def test(request, text):
    return render(request, 'dev/home.html', {'test':text})
