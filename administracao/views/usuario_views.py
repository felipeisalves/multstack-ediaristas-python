from ..forms.usuario_forms import UsuarioForm
from django.shortcuts import render

def  cadastrar_usuario(request):
    if request.method == "POST":
        # Cria o form com os dados passados pelo POST
        form_usuario = UsuarioForm(request.POST)
        # Só salva se os dados forem validos
        if form_usuario.is_valid():
            form_usuario.save()
    else:
        # Cria um formulario vazio
        form_usuario = UsuarioForm()
    return render(request, 'usuarios/form_usuario.html', {'form_usuario': form_usuario})
