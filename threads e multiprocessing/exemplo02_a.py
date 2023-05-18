import random

def append_to_list(lst, num_items):
    'Adiciona num_items dentro de uma faixa de números entre 0-20000000'
    for n in random.sample(range(20000000), num_items):        
        lst.append(n)
    #print(lst)


if __name__ == "__main__":
    for i in range(2):
        append_to_list([], 10000000)