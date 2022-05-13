from django.contrib.auth.forms import UserCreationForm

# Class herdando de UserCreationForm
class UsuarioForm(UserCreationForm):
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