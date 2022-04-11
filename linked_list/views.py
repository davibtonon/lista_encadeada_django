from ast import Global
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from linked_list.form import FormLinkedList
from linkedlist_completo import LinkedList

global lista_encadeada
lista_encadeada = LinkedList()
# Create your views here.

def index(request):
    if request.method == 'POST':
        opcao = int(request.POST['escolhe_acao'])
        if opcao == 1:
            lista_encadeada.insert(request.POST['linked_list'])
        elif opcao == 2:
            lista_encadeada.append(request.POST['linked_list'])
        elif opcao == 3:
            lista_encadeada.removeFirst()

        data = {'lista_atual': lista_encadeada.toList()}
        form = FormLinkedList(data)

        return render(request, 'index.html', {'form': form})
    else:
        
        form = FormLinkedList({ 'lista_atual': lista_encadeada.toList()})
        return render(request, 'index.html', {'form': form})


  