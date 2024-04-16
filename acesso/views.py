from django.shortcuts import render, redirect
from .models import Professor
from .forms import Cad
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.
def Professor(request):
    if request.method == 'POST':
        djangoForm = Cad(request.POST)
        if djangoForm.is_valid():
            user = User.objects.create_user(
                username= request.POST['username'],
                email= request.POST['email'],
                password= request.POST['password']
            )
            novo_professor = djangoForm.save(commit=False)
            novo_professor.user = user
            novo_professor.save()
            return HttpResponse('Sucesso')
        else:
            return HttpResponse('Erro')
    else:
        form = Cad()
        return render(request, 'cadastro.html', {'form': form})