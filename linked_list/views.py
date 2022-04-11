from django.shortcuts import render
from linked_list.form import FormLinkedList
from linkedlist_completo import LinkedList
from django.core.cache import cache


def index(request):
    if request.method == 'POST':
        form = FormLinkedList(request.POST)
        lista_encadeada = cache.get('lista_encadeada')
        if form.is_valid():
            opcao = int(request.POST['escolhe_acao'])
            if opcao == 1:
                lista_encadeada.insert(request.POST['linked_list'])
            elif opcao == 2:
                lista_encadeada.append(request.POST['linked_list'])
            elif opcao == 3:
                lista_encadeada.removeFirst()
            data = {'lista_atual': lista_encadeada.toList()}
            
            form = FormLinkedList(data)
            cache.set('lista_encadeada', lista_encadeada)
            
    else:
        form = FormLinkedList()
        lista_encadeada = LinkedList()
        cache.set('lista_encadeada', lista_encadeada)

    return render(request, 'index.html', {'form': form})


  