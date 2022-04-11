from django import forms
from linkedlist_completo import LinkedList


class FormLinkedList(forms.Form):
    opcao = {
        (1, 'insert'),
        (2, 'append'),
        (3, 'removeFirst')
    }
    linked_list = forms.IntegerField(label='Linked List', required=False)
    escolhe_acao = forms.ChoiceField(label='Escolha a opcao', choices=opcao)
    lista_atual = forms.CharField(
        label='Lista Atual',
        required=False,
        )

    def clean(self):
        escolhe_acao = self.cleaned_data.get('escolhe_acao')
        print('esolhoeas pdfa')
        if escolhe_acao != '3':
            
            self.add_error('linked_list', 'Campo não poder ser vazio')
        
        return self.cleaned_data