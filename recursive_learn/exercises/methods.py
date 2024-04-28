############# power ##########################################

def power_dummy(base, exponent, number):
    if exponent == 0:
        return {
            'subproblem': '<div class="info red_border">Es un caso base</div>',
            'simple_solution': '<div class="info blue_border">Es un caso base</div>',
            'result': '<div class="info green_border">{x}</div>'.format(x=1),
        }
    else:
        if number == 1:
            res = power_method(base, exponent - 1)
            return {
                'subproblem': '<div class="info red_border">{x}</div>'.format(x=(exponent - 1)),
                'simple_solution': '<div class="info blue_border">{x}</div>'.format(x=res),
                'result': '<div class="info green_border">{x}</div>'.format(x=(base * res)),
            }
        else:
            res = power_half(base, exponent//2)
            if exponent % 2 == 1:
                result = res ** 2 * base
            else:
                result = res ** 2
            return {
                'subproblem': '<div class="info red_border">{x}</div>'.format(x=(exponent // 2)),
                'simple_solution': '<div class="info blue_border">{x}</div>'.format(x=res),
                'result': '<div class="info green_border">{x}</div>'.format(x=result),
            }


def power_method(base, exponent):
    if exponent == 0:
        return 1
    return base * power_method(base, exponent-1)


def power_half(base, exponent):
    if exponent == 0:
        return 1
    else:
        if exponent % 2 == 1:
            return power_half(base, exponent//2) ** 2 * base
        else:
            return power_half(base, exponent//2) ** 2


############# add_list ##########################################

def add_list_dummy(lista, number):
    if len(lista) == 0:
        return {
            'subproblem': '<div class="info red_border">Es un caso base</div>',
            'simple_solution': '<div class="info blue_border">Es un caso base</div>',
            'result': '<div class="info green_border">{x}</div>'.format(x=0),
        }
    else:
        if number == 1:
            res = add_list_ini(lista[1:])
            return {
                'subproblem': '<div class="info red_border">{x}</div>'.format(x=lista[1:]),
                'simple_solution': '<div class="info blue_border">{x}</div>'.format(x=res),
                'result': '<div class="info green_border">{x}</div>'.format(x=(lista[0] + res)),
            }
        elif number == 2:
            res = add_list_fin(lista[:-1])
            return {
                'subproblem': '<div class="info red_border">{x}</div>'.format(x=lista[:-1]),
                'simple_solution': '<div class="info blue_border">{x}</div>'.format(x=res),
                'result': '<div class="info green_border">{x}</div>'.format(x=(lista[-1] + res)),
            }
        elif number == 3:
            if len(lista) == 1:
                return {
                    'subproblem': '<div class="info red_border">Es un caso base</div>',
                    'simple_solution': '<div class="info blue_border">Es un caso base</div>',
                    'result': '<div class="info green_border">{x}</div>'.format(x=lista[0]),
                }
            else:
                reduccion = len(lista)//2
                res1 = add_list_half(lista[:reduccion])
                res2 = add_list_half(lista[reduccion:])
                return {
                    'subproblem': '<div class="info red_border">{x}</div><div class="info red_border">{y}</div>'.format(x=lista[:reduccion], y=lista[reduccion:]),
                    'simple_solution': '<div class="info blue_border">{x}</div><div class="info blue_border">{y}</div>'.format(x=res1, y=res2),
                    'result': '<div class="info green_border">{x}</div>'.format(x=(res1 + res2)),
                }


def add_list_ini(lista):
    if len(lista) == 0:
        return 0
    return lista[0] + add_list_ini(lista[1:])


def add_list_fin(lista):
    if len(lista) == 0:
        return 0
    return lista[-1] + add_list_fin(lista[:-1])


def add_list_half(lista):
    if len(lista) == 0:
        return 0
    elif len(lista) == 1:
        return lista[0]
    return add_list_half(lista[:len(lista)//2]) + add_list_half(lista[len(lista)//2:])


############# same_string ##########################################

def same_string_dummy(first, second, number):
    if first == "" or second == "":
        return {
            'subproblem': '<div class="info red_border">Es un caso base</div>',
            'simple_solution': '<div class="info blue_border">Es un caso base</div>',
            'result': '<div class="info green_border">{x}</div>'.format(x=first == second),
        }
    else:
        if number == 1:
            res = same_string_ini(first[1:], second[1:])
            return {
                'subproblem': '<div class="info red_border">a* = {x}<br>b* = {y}</div>'.format(x=first[1:], y=second[1:]),
                'simple_solution': '<div class="info blue_border">{x}</div>'.format(x=res),
                'result': '<div class="info green_border">{x}</div>'.format(x=(first[0] == second[0] and res)),
            }
        elif number == 2:
            res = same_string_fin(first[:-1], second[:-1])
            return {
                'subproblem': '<div class="info red_border">a* = {x}<br>b* = {y}</div>'.format(x=first[:-1], y=second[:-1]),
                'simple_solution': '<div class="info blue_border">{x}</div>'.format(x=res),
                'result': '<div class="info green_border">{x}</div>'.format(x=(first[-1] == second[-1] and res)),
            }
        elif number == 3:
            if len(first) == 1 or len(second) == 1:
                return {
                    'subproblem': '<div class="info red_border">Es un caso base</div>',
                    'simple_solution': '<div class="info blue_border">Es un caso base</div>',
                    'result': '<div class="info green_border">{x}</div>'.format(x=first == second),
                }
            else:
                reduccion = len(first)//2
                reduccion2 = len(second)//2
                res1 = same_string_half(first[:reduccion], second[:reduccion2])
                res2 = same_string_half(first[reduccion:], second[reduccion2:])
                return {
                    'subproblem': '<div class="info red_border">a* = {x}<br>b* = {x2}</div><div class="info red_border">a* = {y}<br>b* = {y2}</div>'.format(x=first[:reduccion], x2=second[:reduccion2], y=first[reduccion:], y2=second[reduccion2:]),
                    'simple_solution': '<div class="info blue_border">{x}</div><div class="info blue_border">{y}</div>'.format(x=res1, y=res2),
                    'result': '<div class="info green_border">{x}</div>'.format(x=(res1 + res2)),
                }


def same_string_ini(first, second):
    if first == "" or second == "":
        return first == second
    return first[0] == second[0] and same_string_ini(first[1:], second[1:])


def same_string_fin(first, second):
    if first == "" or second == "":
        return first == second
    return first[-1] == second[-1] and same_string_fin(first[:-1], second[:-1])


def same_string_half(first, second):
    if first == "" or second == "":
        return first == second
    if len(first) == 1 or len(second) == 1:
        return first == second
    return same_string_half(first[:len(first)//2], second[:len(second)//2]) and same_string_half(first[len(first)//2:], second[len(second)//2:])


############# decimal_to_binary ##########################################

def decimal_to_binary_dummy(n):
    if n < 2:
        return {
            'subproblem': '<div class="info red_border">Es un caso base</div>',
            'simple_solution': '<div class="info blue_border">Es un caso base</div>',
            'result': '<div class="info green_border">{x}</div>'.format(x=n),
        }
    else:
        res = decimal_to_binary(n//2)
        return {
            'subproblem': '<div class="info red_border">{x}</div>'.format(x=(n // 2)),
            'simple_solution': '<div class="info blue_border">{x}</div>'.format(x=res),
            'result': '<div class="info green_border">{x}</div>'.format(x=(res*10+(n % 2))),
        }


def decimal_to_binary(n):
    if n < 2:
        return n
    else:
        return decimal_to_binary(n//2) * 10 + (n % 2)


############# digit_in_number ##########################################

def digit_in_number_dummy(numero, digito):
    if numero < 10:
        return {
            'subproblem': '<div class="info red_border">Es un caso base</div>',
            'simple_solution': '<div class="info blue_border">Es un caso base</div>',
            'result': '<div class="info green_border">{x}</div>'.format(x=digito == numero),
        }
    else:
        res = digit_in_number(numero//10, digito)
        return {
            'subproblem': '<div class="info red_border">{x}</div>'.format(x=(numero//10)),
            'simple_solution': '<div class="info blue_border">{x}</div>'.format(x=res),
            'result': '<div class="info green_border">{x}</div>'.format(x=(res or numero % 10 == digito)),
        }


def digit_in_number(numero, digito):
    if numero < 10:
        return numero == digito
    else:
        return digit_in_number(numero//10, digito) or numero % 10 == digito


############# palindromo ##########################################

def palindrome_dummy(palabra):
    if len(palabra) < 2:
        return {
            'subproblem': '<div class="info red_border">Es un caso base</div>',
            'simple_solution': '<div class="info blue_border">Es un caso base</div>',
            'result': '<div class="info green_border">{x}</div>'.format(x=True),
        }
    else:
        res = palindrome(palabra[1:-1])
        return {
            'subproblem': '<div class="info red_border">{x}</div>'.format(x=(palabra[1:-1])),
            'simple_solution': '<div class="info blue_border">{x}</div>'.format(x=res),
            'result': '<div class="info green_border">{x}</div>'.format(x=(res and palabra[0] == palabra[-1])),
        }


def palindrome(palabra):
    if len(palabra) <= 1:
        return True
    else:
        return palindrome(palabra[1:-1]) and palabra[0] == palabra[-1]


############# decimal_to_n_ary ##########################################

def decimal_to_n_ary_dummy(n, base):
    if n < base:
        return {
            'subproblem': '<div class="info red_border">Es un caso base</div>',
            'simple_solution': '<div class="info blue_border">Es un caso base</div>',
            'result': '<div class="info green_border">{x}</div>'.format(x=n),
        }
    else:
        res = decimal_to_n_ary(n//base, base)
        return {
            'subproblem': '<div class="info red_border">{x}</div>'.format(x=(n // base)),
            'simple_solution': '<div class="info blue_border">{x}</div>'.format(x=res),
            'result': '<div class="info green_border">{x}</div>'.format(x=(res*10+(n % base))),
        }


def decimal_to_n_ary(n, base):
    if n < base:
        return n
    else:
        return decimal_to_n_ary(n//base, base) * 10 + (n % base)


############# factorial ##########################################

def factorial_dummy(n):
    if n == 0:
        return {
            'subproblem': '<div class="info red_border">Es un caso base</div>',
            'simple_solution': '<div class="info blue_border">Es un caso base</div>',
            'result': '<div class="info green_border">{x}</div>'.format(x=1),
        }
    else:
        res = factorial(n-1)
        return {
            'subproblem': '<div class="info red_border">{x}</div>'.format(x=(n-1)),
            'simple_solution': '<div class="info blue_border">{x}</div>'.format(x=res),
            'result': '<div class="info green_border">{x}</div>'.format(x=(res*n)),
        }


def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n-1) * n


############# greater_in_list ##########################################

def greater_in_list_dummy(lista, number):
    if len(lista) == 1:
        return {
            'subproblem': '<div class="info red_border">Es un caso base</div>',
            'simple_solution': '<div class="info blue_border">Es un caso base</div>',
            'result': '<div class="info green_border">{x}</div>'.format(x=lista[0]),
        }
    else:
        if number == 1:
            res = greater_in_list_ini(lista[1:])
            return {
                'subproblem': '<div class="info red_border">{x}</div>'.format(x=lista[1:]),
                'simple_solution': '<div class="info blue_border">{x}</div>'.format(x=res),
                'result': '<div class="info green_border">{x}</div>'.format(x=(max(lista[0], res))),
            }
        elif number == 2:
            res = greater_in_list_fin(lista[:-1])
            return {
                'subproblem': '<div class="info red_border">{x}</div>'.format(x=lista[:-1]),
                'simple_solution': '<div class="info blue_border">{x}</div>'.format(x=res),
                'result': '<div class="info green_border">{x}</div>'.format(x=(max(lista[-1], res))),
            }
        else:
            reduccion = len(lista)//2
            res1 = greater_in_list_half(lista[:reduccion])
            res2 = greater_in_list_half(lista[reduccion:])
            return {
                'subproblem': '<div class="info red_border">{x}</div><div class="info red_border">{y}</div>'.format(x=lista[:reduccion], y=lista[reduccion:]),
                'simple_solution': '<div class="info blue_border">{x}</div><div class="info blue_border">{y}</div>'.format(x=res1, y=res2),
                'result': '<div class="info green_border">{x}</div>'.format(x=max(res1, res2)),
            }


def greater_in_list_ini(lista):
    if len(lista) == 1:
        return lista[0]
    return max(lista[0], greater_in_list_ini(lista[1:]))


def greater_in_list_fin(lista):
    if len(lista) == 1:
        return lista[0]
    return max(lista[-1], greater_in_list_fin(lista[:-1]))


def greater_in_list_half(lista):
    if len(lista) == 1:
        return lista[0]
    return max(greater_in_list_half(lista[:len(lista)//2]), greater_in_list_half(lista[len(lista)//2:]))


############# inverse_string ##########################################

def inverse_string_dummy(word, number):
    if len(word) == 0:
        return {
            'subproblem': '<div class="info red_border">Es un caso base</div>',
            'simple_solution': '<div class="info blue_border">Es un caso base</div>',
            'result': '<div class="info green_border">""</div>',
        }
    else:
        if number == 1:
            res = inverse_string_ini(word[1:])
            return {
                'subproblem': '<div class="info red_border">{x}</div>'.format(x=word[1:]),
                'simple_solution': '<div class="info blue_border">{x}</div>'.format(x=res),
                'result': '<div class="info green_border">{x}</div>'.format(x=(res + word[0])),
            }
        elif number == 2:
            res = inverse_string_fin(word[:-1])
            return {
                'subproblem': '<div class="info red_border">{x}</div>'.format(x=word[:-1]),
                'simple_solution': '<div class="info blue_border">{x}</div>'.format(x=res),
                'result': '<div class="info green_border">{x}</div>'.format(x=(word[-1] + res)),
            }
        else:
            reduccion = len(word)//2
            res1 = inverse_string_half(word[:reduccion])
            res2 = inverse_string_half(word[reduccion:])
            return {
                'subproblem': '<div class="info red_border">{x}</div><div class="info red_border">{y}</div>'.format(x=word[:reduccion], y=word[reduccion:]),
                'simple_solution': '<div class="info blue_border">{x}</div><div class="info blue_border">{y}</div>'.format(x=res1, y=res2),
                'result': '<div class="info green_border">{x}</div>'.format(x=res2 + res1),
            }


def inverse_string_ini(word):
    if len(word) <= 1:
        return word
    return inverse_string_ini(word[1:]) + word[0]


def inverse_string_fin(word):
    if len(word) <= 1:
        return word
    return word[-1] + inverse_string_fin(word[:-1])


def inverse_string_half(word):
    if len(word) <= 1:
        return word
    return inverse_string_half(word[len(word)//2:]) + inverse_string_half(word[:len(word)//2])


############# merge_sort ##########################################

def merge_sort_dummy(int_list):
    if len(int_list) <= 1:
        return {
            'subproblem': '<div class="info red_border">Es un caso base</div>',
            'simple_solution': '<div class="info blue_border">Es un caso base</div>',
            'result': '<div class="info green_border">{x}</div>'.format(x=int_list),
        }
    else:
        reduccion = len(int_list)//2
        res1 = merge_sort(int_list[:reduccion])
        res2 = merge_sort(int_list[reduccion:])
        return {
            'subproblem': '<div class="info red_border">{x}</div><div class="info red_border">{y}</div>'.format(x=int_list[:reduccion], y=int_list[reduccion:]),
            'simple_solution': '<div class="info blue_border">{x}</div><div class="info blue_border">{y}</div>'.format(x=res1, y=res2),
            'result': '<div class="info green_border">{x}</div>'.format(x=mezclar(res2, res1)),
        }


def mezclar(lista1, lista2):
    lista_final = []
    while len(lista1) > 0 and len(lista2) > 0:
        if lista1[0] > lista2[0]:
            lista_final.append(lista2.pop(0))
        else:
            lista_final.append(lista1.pop(0))
    lista_final = lista_final + lista1 + lista2
    return lista_final


def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        return mezclar(merge_sort(lista[:len(lista)//2]), merge_sort(lista[len(lista)//2:]))


############# insert_sort ##########################################

def insert_sort_dummy(int_list):
    if len(int_list) <= 1:
        return {
            'subproblem': '<div class="info red_border">Es un caso base</div>',
            'simple_solution': '<div class="info blue_border">Es un caso base</div>',
            'result': '<div class="info green_border">{x}</div>'.format(x=int_list),
        }
    else:
        res = insert_sort(int_list[:-1])
        return {
            'subproblem': '<div class="info red_border">{x}</div>'.format(x=int_list[:-1]),
            'simple_solution': '<div class="info blue_border">{x}</div>'.format(x=res),
            'result': '<div class="info green_border">{x}</div>'.format(x=(colocar(int_list[-1], res))),
        }


def insert_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        listado = insert_sort(lista[:-1])
        return colocar(lista[-1], listado)


def colocar(numero, lista):
    i = len(lista)
    lista.append(numero)
    while i > 0 and numero < lista[i-1]:
        lista[i] = lista[i-1]
        lista[i-1] = numero
        i -= 1
    return lista


############# insert_sort ##########################################
def quick_sort_dummy(int_list):
    if len(int_list) <= 1:
        return {
            'subproblem': '<div class="info red_border">Es un caso base</div>',
            'simple_solution': '<div class="info blue_border">Es un caso base</div>',
            'result': '<div class="info green_border">{x}</div>'.format(x=int_list),
        }
    else:
        indice_pivote = particion_Hoare(int_list, 0, len(int_list) - 1)
        subproblem = int_list.copy()
        quick_sort_index(int_list, 0, indice_pivote - 1)
        res1 = int_list.copy()
        quick_sort_index(int_list, indice_pivote + 1, len(int_list) - 1)
        return {
            'subproblem': '<div class="info red_border">{x}</div><div class="info red_border">{y}</div>'.format(x=subproblem, y=subproblem),
            'simple_solution': '<div class="info blue_border">{x}</div><div class="info blue_border">{y}</div>'.format(x=res1, y=int_list),
            'result': '<div class="info green_border">{x}</div>'.format(x=int_list),
        }


def quick_sort(a):
    quick_sort_index(a, 0, len(a) - 1)


def particion_Hoare(a, ini, fin):
    if fin >= 0:
        mitad = (ini + fin) // 2
        pivote = a[mitad]
        a[mitad] = a[ini]
        a[ini] = pivote

        izqa = ini + 1
        dcha = fin

        ha_terminado = False
        while not ha_terminado:

            while izqa <= fin and a[izqa] <= pivote:
                izqa = izqa + 1

            while a[dcha] > pivote:
                dcha = dcha - 1

            if izqa < dcha:
                aux = a[izqa]
                a[izqa] = a[dcha]
                a[dcha] = aux

            ha_terminado = izqa > dcha

        a[ini] = a[dcha]
        a[dcha] = pivote
        return dcha


def quick_sort_index(a, ini, fin):
    if ini < fin:
        indice_pivote = particion_Hoare(a, ini, fin)
        quick_sort_index(a, ini, indice_pivote - 1)
        quick_sort_index(a, indice_pivote + 1, fin)


def quicksort(int_list):
    if len(int_list) <= 1:
        return int_list
    return quicksort(list(filter((lambda y: y < int_list[0]), int_list[1:]))) + [int_list[0]] + quicksort(list(filter((lambda y: y >= int_list[0]), int_list[1:])))


############# insert_sort ##########################################
def select_sort_dummy(int_list):
    if len(int_list) <= 1:
        return {
            'subproblem': '<div class="info red_border">Es un caso base</div>',
            'simple_solution': '<div class="info blue_border">Es un caso base</div>',
            'result': '<div class="info green_border">{x}</div>'.format(x=int_list),
        }
    else:
        min_int = min(int_list)
        int_list.remove(min_int)
        int_list_whitout_min = int_list.copy()
        res1 = select_sort(int_list)
        return {
            'subproblem': '<div class="info red_border">{x}</div>'.format(x=int_list_whitout_min),
            'simple_solution': '<div class="info blue_border">{x}</div>'.format(x=res1),
            'result': '<div class="info green_border">{x}</div>'.format(x=[min_int] + res1),
        }


def select_sort(int_list):
    if len(int_list) <= 1:
        return int_list
    int_list.remove(min(int_list))
    return [min(int_list)] + select_sort(int_list)
