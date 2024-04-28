from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotFound, JsonResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth.decorators import login_required

from .models import Exercise
from core.models import Profile
from . import methods
from . import views_data
import json

from django.template.defaulttags import register


@register.filter
def get_item(dictionary, key):
    if key in dictionary:
        return 'Sí'
    else:
        return 'No'


# Create your views here.
POWER_TITLE = 'Potencia'
ADD_LIST_TITLE = 'Sumar los elementos de una lista'
SAME_STRING_TITLE = 'Dos string iguales'
DECIMAL_TO_BINARY_TITLE = 'Decimal a binario'
DIGIT_IN_NUMBER_TITLE = 'Número contine un dígito'
PALINDROME_TITLE = 'Palíndromo'
DECIMAL_TO_N_ARY_TITLE = 'Decimal a base N'
FACTORIAL_TITLE = 'Factorial'
GREATER_IN_LIST_TITLE = 'Mayor elemento en una lista'
INVERSE_STRING_TITEL = 'Invertir un string'
MERGE_SORT = 'Ordenar lista: Merge sort'
INSER_SORT = 'Ordenar lista: Insert sort'
QUICK_SORT = 'Ordenar lista: Quick sort'
SELECT_SORT = 'Ordenar lista: Select sort'


@login_required
def searcher(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    exercises_user = profile.exercises.all()
    exercise_set = set()
    for exercise in exercises_user:
        exercise_set.add(exercise.name)

    query_done = request.GET.get('query_done', '')
    query_name = request.GET.get('query_name', '')
    exercises = Exercise.objects.filter()
    percentage = int(len(exercises_user) / len(exercises) * 100)

    if query_name:
        exercises = exercises.filter(name__icontains=query_name)

    data = {
        'exercises': exercises,
        'query_name': query_name,
        'exercise_set': exercise_set,
        'query_done': query_done,
        'percentage': percentage,
        'stars': [1, 2, 3, 4, 5],
    }
    return render(request, 'searcher.html', data)


def _replace_list(lis, type_convert):
    lis = lis.replace('[', '')
    lis = lis.replace(']', '')
    if lis.isspace() or lis == '':
        return []
    try:
        return [type_convert(s) for s in lis.split(',')]
    except:
        return -1


def _positive_int(input):
    try:
        number = int(input)
        if number >= 0:
            return number
        else:
            return ''
    except:
        return ''


def _int(input):
    try:
        number = int(input)
        return number
    except:
        return ''


@csrf_exempt
def getResults(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        titulo = body.get('title')
        if titulo == POWER_TITLE:
            input1 = body.get('first')
            input2 = body.get('second')
            input1 = _positive_int(input1)
            input2 = _int(input2)
            number = body.get('number')

            if input1 == '' or input2 == '':
                return JsonResponse({'error': 'Formato incorrecto. Formato ejemplo:\nbase: 5\nexponente: 3'})
            if number == 3:
                if body.get('aux_counter') == 0:
                    if input2 % 2 == 1:
                        return JsonResponse({'error': 'El número recibido es impar cuando a de ser par'})
                else:
                    if input2 % 2 == 0:
                        return JsonResponse({'error': 'El número recibido es par cuando a de ser impar'})

            return JsonResponse(methods.power_dummy(input1, input2, number))

        elif titulo == ADD_LIST_TITLE:
            input1 = body.get('first')
            input1 = _replace_list(input1, int)

            if input1 == -1:
                return JsonResponse({'error': 'Formato incorrecto. Formato ejemplo:\n[5, 3, 2, -1]'})

            return JsonResponse(methods.add_list_dummy(input1, body.get('number')))

        elif titulo == SAME_STRING_TITLE:
            input1 = body.get('first')
            input2 = body.get('second')

            if input1.isalnum() and input2.isalnum():
                return JsonResponse(methods.same_string_dummy(input1, input2, body.get('number')))
            else:
                return JsonResponse({'error': 'Tienen que ser string alfanuméricos. Formato ejemplo:\nhola123'})

        elif titulo == DECIMAL_TO_BINARY_TITLE:
            input1 = body.get('first')
            input1 = _positive_int(input1)

            if input1 == '':
                return JsonResponse({'error': 'Formato incorrecto. Formato ejemplo:\nnumber: 15'})
            else:
                return JsonResponse(methods.decimal_to_binary_dummy(input1))

        elif titulo == DIGIT_IN_NUMBER_TITLE:
            input1 = body.get('first')
            input2 = body.get('second')
            input1 = _positive_int(input1)
            input2 = _positive_int(input2)

            if input1 == '' or input2 == '':
                return JsonResponse({'error': 'Formato incorrecto. Formato ejemplo:\nnumero: 82559\ndigito: 3'})
            if input2 > 10:
                return JsonResponse({'error': 'El dígito recibido es mayor que 10, tiene que ser un número entre 0 y 9'})

            return JsonResponse(methods.digit_in_number_dummy(input1, input2))

        elif titulo == PALINDROME_TITLE:
            input1 = body.get('first')

            if input1.isalpha() and input1.islower():
                return JsonResponse(methods.palindrome_dummy(input1))
            else:
                return JsonResponse({'error': 'Tienen que ser string alfábetico, solo letras minúsculas. Formato ejemplo:\ngresyla'})

        elif titulo == DECIMAL_TO_N_ARY_TITLE:
            input1 = body.get('first')
            input2 = body.get('second')
            input1 = _positive_int(input1)
            input2 = _positive_int(input2)

            if input1 == '' or input2 == '':
                return JsonResponse({'error': 'Formato incorrecto. Formato ejemplo:\nnumber: 23\nbase: 3'})
            if input2 > 10 or input2 < 2:
                return JsonResponse({'error': 'La base recibida no está comprendida entre 2 y 9, tiene que ser un número entre 2 y 9'})

            return JsonResponse(methods.decimal_to_n_ary_dummy(input1, input2))

        elif titulo == FACTORIAL_TITLE:
            input1 = body.get('first')
            input1 = _positive_int(input1)

            if input1 == '':
                return JsonResponse({'error': 'Formato incorrecto. Formato ejemplo:\nnumber: 7'})
            else:
                return JsonResponse(methods.factorial_dummy(input1))

        elif titulo == GREATER_IN_LIST_TITLE:
            input1 = body.get('first')
            input1 = _replace_list(input1, int)

            if input1 == -1:
                return JsonResponse({'error': 'Formato incorrecto. Formato ejemplo:\n[5, 3, 2, -1]'})

            if len(input1) == 1:
                return JsonResponse({'error': 'No vale una lista vacia'})

            return JsonResponse(methods.greater_in_list_dummy(input1, body.get('number')))

        elif titulo == INVERSE_STRING_TITEL:
            input1 = body.get('first')

            if input1.isalnum():
                return JsonResponse(methods.inverse_string_dummy(input1, body.get('number')))
            else:
                return JsonResponse({'error': 'Tienen que ser string alfábetico. Formato ejemplo:\nnumero'})

        elif titulo == MERGE_SORT:
            input1 = body.get('first')
            input1 = _replace_list(input1, int)

            if input1 == -1:
                return JsonResponse({'error': 'Formato incorrecto. Formato ejemplo:\n[5, 3, 2, -1]'})

            return JsonResponse(methods.merge_sort_dummy(input1))

        elif titulo == INSER_SORT:
            input1 = body.get('first')
            input1 = _replace_list(input1, int)

            if input1 == -1:
                return JsonResponse({'error': 'Formato incorrecto. Formato ejemplo:\n[5, 3, 2, -1]'})

            return JsonResponse(methods.insert_sort_dummy(input1))

        elif titulo == QUICK_SORT:
            input1 = body.get('first')
            input1 = _replace_list(input1, int)

            if input1 == -1:
                return JsonResponse({'error': 'Formato incorrecto. Formato ejemplo:\n[5, 3, 2, -1]'})

            return JsonResponse(methods.quick_sort_dummy(input1))

        elif titulo == SELECT_SORT:
            input1 = body.get('first')
            input1 = _replace_list(input1, int)

            if input1 == -1:
                return JsonResponse({'error': 'Formato incorrecto. Formato ejemplo:\n[5, 3, 2, -1]'})

            return JsonResponse(methods.select_sort_dummy(input1))

        else:
            return JsonResponse({'error': 'No existe este ejercicio'})


@csrf_protect
@login_required
def exercise(request, pk):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    exercises_user = profile.exercises.filter(pk=pk)
    exercise = get_object_or_404(Exercise, pk=pk)
    if request.method == 'POST':
        if not exercises_user:
            profile.exercises.add(exercise)
        return redirect('exercises:searcher')
    render_data = selector(request, exercise)
    context = render_data.get('data')
    if not context:
        return render_data
    if exercises_user:
        context['done'] = 'yes'
    return render(render_data.get('request'), 'exercise/exercise.html', context)


def selector(request, exercise):
    name = exercise.name
    if name == POWER_TITLE:
        return views_data.power(request, exercise)
    elif name == ADD_LIST_TITLE:
        return views_data.add_list(request, exercise)
    elif name == SAME_STRING_TITLE:
        return views_data.same_string(request, exercise)
    elif name == DECIMAL_TO_BINARY_TITLE:
        return views_data.decimal_to_binary(request, exercise)
    elif name == DIGIT_IN_NUMBER_TITLE:
        return views_data.digit_in_number(request, exercise)
    elif name == PALINDROME_TITLE:
        return views_data.palindrome(request, exercise)
    elif name == DECIMAL_TO_N_ARY_TITLE:
        return views_data.decimal_to_n_ary(request, exercise)
    elif name == FACTORIAL_TITLE:
        return views_data.factorial(request, exercise)
    elif name == GREATER_IN_LIST_TITLE:
        return views_data.greater_in_list(request, exercise)
    elif name == INVERSE_STRING_TITEL:
        return views_data.inverse_string(request, exercise)
    elif name == MERGE_SORT:
        return views_data.merge_sort(request, exercise)
    elif name == INSER_SORT:
        return views_data.insert_sort(request, exercise)
    elif name == QUICK_SORT:
        return views_data.quick_sort(request, exercise)
    elif name == SELECT_SORT:
        return views_data.select_sort(request, exercise)
    else:
        return HttpResponseNotFound('Ejercicio no encontrado')
