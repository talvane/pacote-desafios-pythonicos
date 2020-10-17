"""
12. linear_merge

Dada duas listas ordenadas em ordem crescente, crie e retorne uma lista
com a combinação das duas listas, também em ordem crescente. Você pode
modificar as listas recebidas.

A sua solução deve rodar em tempo linear, ou seja, deve fazer uma
única passagem em cada uma das listas.
"""

# import itertools
from heapq import merge

def linear_merge(list1, list2):

    # listMerged = []
    # for a, b in itertools.zip_longest(list1, list2):
    #     if a != None and b != None and a < b:
    #         listMerged.append(a)
    #         listMerged.append(b)
    #     elif a != None and b != None and a > b:
    #         listMerged.append(b)
    #         listMerged.append(a)
    #     elif a == None:
    #         listMerged.append(b)
    #     elif b == None:
    #         listMerged.append(a)
    #     else:
    #         listMerged.append(a)
    #         listMerged.append(b)
    #
    # return listMerged

    # linear_merged = [ ]
    # for i in range(len(list1) + len(list2)):
    #     if list1[ -1: ] > list2[ -1: ]:
    #         linear_merged.append(list1[ -1 ])
    #         list1.pop(-1)
    #     else:
    #         linear_merged.append(list2[ -1 ])
    #         list2.pop(-1)
    #
    # linear_merged.sort()
    # return linear_merged

    return list(merge(list1, list2))


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}{in_!r} retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(linear_merge, (['aa', 'xx', 'zz'], ['bb', 'cc']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge, (['aa', 'xx'], ['bb', 'cc', 'zz']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge, (['aa', 'aa'], ['aa', 'bb', 'bb']),
         ['aa', 'aa', 'aa', 'bb', 'bb'])
