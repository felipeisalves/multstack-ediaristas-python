import re
from ..forms.usuario_forms import UsuarioForm
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model

def  cadastrar_usuario(request):
    if request.method == "POST":
        # Cria o form com os dados passados pelo POST
        form_usuario = UsuarioForm(request.POST)
        # Só salva se os dados forem validos
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect(listar_usuarios)
    else:
        # Cria um formulario vazio
        form_usuario = UsuarioForm()
    return render(request, 'usuarios/form_usuario.html', {'form_usuario': form_usuario})

def listar_usuarios(request):
    # Instancia o model de usuario do django
    User = get_user_model()
    # seleciona os usuario (Select)
    usuarios = User.objects.filter(is_superuser=True)
    return render(request, 'usuarios/lista_usuario.html', {'usuarios': usuarios})