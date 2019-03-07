from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main.html')

def wordcount(request):
    return render(request, 'wordcount.html')