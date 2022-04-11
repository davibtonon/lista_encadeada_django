from django import forms


class FormLinkedList(forms.Form):
    """Classe responsavel por cria o formulario html"""

    opcao = {
        (1, 'insert'),
        (2, 'append'),
        (3, 'removeFirst')
    }
   
    linked_list = forms.CharField(label='Adicionar elemento', required=False)
    escolhe_acao = forms.ChoiceField(
        label='Escolha a opcao',
        choices=opcao,
        required=False,
        )
    lista_atual = forms.CharField(
        label='Lista Atual',
        required=False,
        )