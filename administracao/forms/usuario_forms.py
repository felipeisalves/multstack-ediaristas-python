from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

# Class herdando de UserCreationForm
class CadastroUsuarioForm(UserCreationForm):
    # Classe altera os campos obrigatorios do model
    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        # instancia o usuario que estamas criando
        user = super(UserCreationForm, self).save(commit=False)
        # altera o is_superuser para 1
        user.is_superuser = True
        user.set_password(self.cleaned_data['password1'])
        # e salva
        if commit:
            user.save()
        return user

class EditarUsuarioForm(UserChangeForm):
    password = None
    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'email']

