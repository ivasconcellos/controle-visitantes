from dataclasses import field
from django import forms
from .models import Visitante

class VisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante
        fields = ["nome_completo", "cpf", "data_nascimento", "numero_casa", "placa_veiculo"]
        error_messages = {
            "nome_completo": {
                "required": "O nome completo do visitante é obrigatório!"
            },
            "cpf": {
               "required": "O CPF do visitante é obrigatório!" 
            },
            "data_nascimento": {
               "required": "A data de nascimento do visitante é obrigatória!",
               "invalid": "Por favor, informe um formato válido para a data de nascimento (DD/MM/AAAA)!"
            },
            "numero_casa": {
               "required": "O númnero da casa obrigatório!" 
            },
            
        }
