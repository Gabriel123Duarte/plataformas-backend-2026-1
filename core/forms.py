from django import forms

from core.models import Aluno


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ["nome", "idade", "email", "curso"]

    def clean_idade(self):
        idade = self.cleaned_data.get("idade")

        if idade <= 0:
            raise forms.ValidationError("Idade não pode ser menor ou igual a zero.")

        return idade
