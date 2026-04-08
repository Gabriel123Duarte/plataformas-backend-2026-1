from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        return HttpResponse(nome)

    return render(request, 'homepage.html')