from . import forms


def power(request, exercise):
    description = 'Dados dos números enteros no negativos, una <i>base</i> y un <i>exponente</i>. Se desea calcular el resultado de la potencia <i>base</i> elevada a <i>exponente</i>. por ejemplo, para <span class="focus-wraper"><span class="outline o1"><i>base</i> = 5 y <i>exponente</i> = 3</span><span class="ring r1"></span><span class="stick s1"></span></span> el resultado sería 125 ya que 5<sup>3</sup> = 125 = 5·5·5'
    form = forms.powerForm()
    paragraph = [
        ['Siguiendo el ejemplo marcado seleccionaremos el <strong>tamaño del problema</strong>:'],
        ['La base no nos ayuda a determinar la complejidad del problema, dado que la base es el factor multiplicativo.',
            '¡Correcto! El exponente es la medida a utilizar, dado que es el número de veces que multiplicamos la base.'],
        ['A continuación tendremos que elegir el <strong>caso base</strong> que se ajuste al problema.'],
        ['Como hemos dicho antes, no podemos utilizar la base como <strong>caso base</strong> dado que es el factor multiplicativo.',
            'Podría ser el <strong>caso base</strong> pero como tienen que ser no negativos no estamos contemplando el 0.', '¡Correcto! Tenemos que llegar a que el exponente sea 0.'],
        ['Ahora elegiremos el valor de retorno una vez lleguemos al <strong>caso base</strong>.'],
        ['La base es una idea interesante, pero no funcionaría debido a que un número elevado a 0 no es el propio número.', '¡Correcto! Una potencia elevada a 0 siempre es 1.',
            'El exponente podría ser una solución válida, pero falla un caso. Con exponente == 0 debería devolver un 1, no un 0.'],
        ['¿Nos hacen falta más <strong>casos base</strong>?'],
        ['¿Qué <strong>caso/s base/s</strong> necesitamos para continuar?'],
        ['Nos da igual que el exponente sea negativo o positivo. En realidad es una buena observación pero se resolverá facilmente con una <strong>descomposición</strong> acertada.',
            '¡En efecto! Dependiendo de si el resultado es par o impar la operación será distinta.', 'Este caso solo sería válido para una descomposición de exponente - 2, la cual os animo a intentar pero no exploraremos aquí porque es muy similar a exponente - 1.'],
        ['Ahora tendremos que elegir la <strong>descomposición</strong> que usaremos para resolver el ejercicio.'],
        ['No podemos tan solo dividir. Nos quedaría como resultado un real, que no es una entrada válida para la función.',
            '¡Correcto! Si dividimos a la mitad el resultado podemos resolver el ejercicio en tiempo logarítmico.', 'En efecto funcionaría, pero no sería necesarío este caso base. Por tanto vamos a explorar otras opciones.'],
        ['Ahora introduce unos valores de ejemplo en los recuadros de entrada, el exponente a de ser par. Puedes utilizar el siguiente ejemplo: base = 5 | exponente = 6'],
        ['El <strong>subproblema</strong> se resuelve automáticamente al hacer la llamada recursiva. Queda componer el resultado del mismo con el valor de la descomposición para el caso par.'],
        ['Si solo multiplicamos por el exponente la <strong>descomposición</strong> habría sido exponente - 1.', 'Sería correcto si fuese el caso impar.',
            '¡Correcto! Dado que hemos dividido el exponente en 2 y hemos calculado el resultado, ahora solo queda elevar al cuadrado.'],
        ['Para el caso impar, vuelve a introducir valores de ejemplo en los recuadros de entrada, el exponente a de ser impar. Puedes utilizar el siguiente ejemplo: base = 5 | exponente = 6'],
        ['Ahora solo nos falta elegir la/s operación/es para completar el caso impar.'],
        ['¡Correcto! Solo nos falta multiplicar por el exponente después de elevar al cuadrado si es un caso impar.',
            'No podemos multiplicar por el exponente solo, nos falta también elevar al cuadrado como en el caso par.', 'Sería el mismo caso y estarían juntos, pero está muy cerca de la solución real'],
        ['¡Enhorabuena! Con esto habriamos terminado el ejercicio de potencias.']
    ]

    options = [
        ['<div class="option-content next2">exponente</div> <div class="option-content next1">base</div>'],
        ['<div class="next back">Volver a intentar</div>',
            '<div class="next next1">Seguir</div>'],
        ['<div class="option-content next1">base==0</div> <div class="option-content next2">exponente==1</div> <div class="option-content next3">exponente==0</div>'],
        ['<div class="next back">Volver a intentar</div>',
            '<div class="next back">Volver a intentar</div>', '<div class="next next1">Seguir</div>'],
        ['<div class="option-content next2">1</div> <div class="option-content next1">base</div> <div class="option-content next3">exponente</div>'],
        ['<div class="next back">Volver a intentar</div>', '<div class="next next1">Seguir</div>',
            '<div class="next back">Volver a intentar</div>'],
        ['<div class="option-content hardnext1">No</div> <div class="option-content next1">Sí</div>'],
        ['<div class="option-content next2">exponente par/impar</div> <div class="option-content next3">exponente == 1</div> <div class="option-content next1">base < 0</div>'],
        ['<div class="next back">Volver a intentar</div>',
            '<div class="next next1">Seguir</div>', '<div class="next back">Volver a intentar</div>'],
        ['<div class="option-content next2">exponente // 2</div> <div class="option-content next3">exponente - 1</div> <div class="option-content next1">exponente / 2</div>'],
        ['<div class="next back">Volver a intentar</div>', '<div class="next next1">Seguir</div>',
            '<div class="next back">Volver a intentar</div>'],
        ['<div class="next evaluate">Calcular</div>'],
        ['<div class="option-content next3">** 2</div> <div class="option-content next1">* exponente</div> <div class="option-content next2">** 2 * exponente</div>'],
        ['<div class="next back">Volver a intentar</div>',
            '<div class="next back">Volver a intentar</div>', '<div class="next next1">Seguir</div>'],
        ['<div class="next evaluate">Calcular</div>'],
        ['<div class="option-content next3">** 2</div> <div class="option-content next2">* exponente</div> <div class="option-content next1">** 2 * exponente</div>'],
        ['<div class="next next1">Seguir</div>',
            '<div class="next back">Volver a intentar</div>', '<div class="next back">Volver a intentar</div>'],
        ['<div class="next end_exercise">Finalizar ejercicio</div>']
    ]

    code = [
        [''],
        ['', 'def potencia(base, exponente):<br>'],
        [''],
        ['', '', '&nbsp&nbsp&nbspif exponente==0:<br>'],
        [''],
        ['', '&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn 1<br>'],
        [''],
        ['<span class="delete">&nbsp&nbsp&nbspelif ____:<br></span>'],
        ['', '&nbsp&nbsp&nbspelif exponenente % 2 == 0:<br>'],
        [''],
        ['',
            '<span class="delete">&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn <span class="step_simpler">potencia(<span class="step_subproblem">base, exponent//2</span>)</span></span>'],
        [''],
        [''],
        ['', '',
            '&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn <span class="step_solution"><span class="step_simpler">potencia(<span class="step_subproblem">base, exponent//2</span>)</span> ** 2</span><br>'],
        ['&nbsp&nbsp&nbspelse:<br>'],
        [''],
        ['&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn <span class="step_solution"><span class="step_simpler">potencia(<span class="step_subproblem">base, exponent//2</span>)</span> ** 2 * exponente</span>'],
        ['']
    ]

    '''false no tiene varias opciones (solo continuar o retroceder)
    true tiene varias opciones (a elegir)'''
    optionsChange = [
        True,
        False,
        True,
        False,
        True,
        False,
        True,
        True,
        False,
        True,
        False,
        False,
        True,
        False,
        False,
        True,
        False,
        False
    ]

    paragraph1 = [
        ['¡Perfecto! Ahora tenemos que elegir una descomposición'],
        ['En efecto. Es una <strong>descomposición</strong> válida y suficiente, reducimos el problema a una potencia más simple.',
            'Es una <strong>descomposición</strong> correcta. Pero solo con un caso base es imposible de resolver.', 'Dividir a la mitad es una opción posible, pero una división simple da como salida un número real.'],
        ['Ahora introduce unos valores de ejemplo en los recuadros de entrada. Puedes utilizar el siguiente ejemplo: base = 5 | exponente = 6'],
        ['Ahora nos queda componer el <strong>subproblema</strong> con el valor de la descomposición.'],
        ['¡Muy bien! si multiplicamos el resultado del <strong>subproblema</strong> por la base obtenemos el resultado desado.',
            'El resultado del subproblema no es el resultado esperado, por tanto tenemos que realizar una operación.', 'Muy cerca, pero el exponente lo utilizamos para el tamaño, no para el de la solución.'],
        ['¡Enhorabuena! Con esto habriamos terminado el ejercicio de sumar los elementos de una lista.']
    ]

    options1 = [
        ['<div class="option-content next2">exponente // 2</div> <div class="option-content next3">exponente / 2</div> <div class="option-content next1">exponente - 1</div>'],
        ['<div class="next next1">Seguir</div>', '<div class="next back">Volver a intentar</div>',
            '<div class="next back">Volver a intentar</div>'],
        ['<div class="next evaluate">Calcular</div>'],
        ['<div class="option-content next2">Nada, ya debería de estar el resultado</div> <div class="option-content next3">* exponente</div> <div class="option-content next1">* base</div>'],
        ['<div class="next next1">Seguir</div>', '<div class="next back">Volver a intentar</div>',
            '<div class="next back">Volver a intentar</div>',],
        ['<div class="next end_exercise">Finalizar ejercicio</div>']
    ]

    code1 = [
        ['&nbsp&nbsp&nbspelse:<br>'],
        ['<span class="delete">&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn <span class="step_simpler">potencia(<span class="step_subproblem">base, exponent - 1</span>)</span></span>'],
        [''],
        [''],
        [''],
        ['&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn <span class="step_solution"><span class="step_simpler">potencia(<span class="step_subproblem">base, exponent - 1</span>)</span> * base</span>'],
        ['']
    ]

    '''false no tiene varias opciones (solo continuar o retroceder)
    true tiene varias opciones (a elegir)'''
    optionsChange1 = [
        True,
        False,
        False,
        True,
        False,
        False
    ]

    data = {
        'exercise': exercise,
        'description': description,
        'form': form,
        'paragraph': paragraph,
        'paragraph1': paragraph1,
        'options': options,
        'options1': options1,
        'code': code,
        'code1': code1,
        'optionsChange': optionsChange,
        'optionsChange1': optionsChange1,
    }

    return {'data': data, 'request': request}


def add_list(request, exercise):
    description = 'Dada una lista de enteros positivos <strong>a</strong>. Se desea calcular el resultado de la suma de todos los elementos de <strong>a</strong>. Por ejemplo, para <span class="focus-wraper"><span class="outline o1"><strong>a</strong> = [4, -5, 7]</span><span class="ring r1"></span><span class="stick s1"></span></span> el resultado sería 6 ya que 6 = 4 + 5 + 7.'
    form = forms.listForm()
    paragraph = [
        ['Siguiendo el ejemplo marcado seleccionaremos el <strong>tamaño del problema</strong>:'],
        ['¡Correcto! Lo más habitual al trabajar con listas es usar la longitud para determinar el tamaño del problema.',
            'La a podría ser una solución posible; en muchos lenguajes las listas no son tipos primitivos y es más difícil usarlas en condicionales. Habitualmente se utiliza el tamaño de la lista dado que es más sencillo. ¡Os animo a intentarlo!'],
        ['A continuación tendremos que elegir el <strong>caso base</strong> que se ajuste al problema.'],
        ['¡Correcto! Cuando el tamaño de la lista alcance 0 tendremos una lista vacia, momento en el que podemos resolver el problema.', 'Una lista con un solo elemento podría ser un caso base. Sin embargo es altamente probable recibir una lista vacia, en cuyo caso nos daría un error de ejecución; para evitarlo también contemplaremos este caso.',
            'Si utilizamos la a==0 nos dará un error de ejecución, dado que un elemento tipo lista no es comparable a un elemento tipo entero.'],
        ['Ahora elegiremos el valor de retorno una vez lleguemos al <strong>caso base</strong>.'],
        ['¡Correcto! Al tener una lista vacia, no hay elementos, por tanto el resultado que devolveremos es 0.', 'No podemos devolver una lista vacia dado que no se puede sumar un entero con una lista, además el valor de retorno que se espera es un entero.',
            'En caso de utilizar la a estariamos devolviendo una lista vacia que al sumar con enteros genera un error de tipos, además el valor de retorno que se espera es un entero.'],
        ['¿Con un <strong>caso base</strong> es suficiente?'],
        ['A continuación tendremos que elegir el otro <strong>caso base</strong>.'],
        ['¡Correcto! Si la lista alcanza tamaño 1 es muy sencillo indicar el resultado. Para las ocasiones en las que no se contemple la lista vacia, el caso base suele ser la longitud igual a 1.',
            'Si utilizamos la a==1 nos dará un error de ejecución, dado que una lista no es comparable a un entero.'],
        ['Ahora elegiremos el valor de retorno una vez lleguemos a este <strong>caso base</strong>.'],
        ['¡Correcto! Debemos devolver el valor restante de la lista dado que solo queda 1 elemento.', 'En caso de utilizar la a estariamos devolviendo la lista con 1 elemento, es un error de tipos porque no es un entero.',
            'No podemos devolver un 0 dado que una lista con un elemento debería devolver el elemento, no un 0.']
    ]

    options = [
        ['<div class="option-content next1">len(a)</div> <div class="option-content next2">a</div>'],
        ['<div class="next next1">Seguir</div>',
            '<div class="next back">Volver a intentar</div>'],
        ['<div class="option-content next1">len(a)==0</div> <div class="option-content next2">len(a)==1</div> <div class="option-content next3">a==0</div>'],
        ['<div class="next next1">Seguir</div>', '<div class="next next1">Seguir</div>',
            '<div class="next back">Volver a intentar</div>'],
        ['<div class="option-content next2">[]</div> <div class="option-content next1">0</div> <div class="option-content next3">a</div>'],
        ['<div class="next next1">Seguir</div>', '<div class="next back">Volver a intentar</div>',
            '<div class="next back">Volver a intentar</div>'],
        ['<div class="option-content hardnext1">Sí</div> <div class="option-content next1">No</div>'],
        ['<div class="option-content next2">a==1</div> <div class="option-content next1">len(a)==1</div>'],
        ['<div class="next next1">Seguir</div>',
            '<div class="next back">Volver a intentar</div>'],
        ['<div class="option-content next2">a</div> <div class="option-content next1">a[0]</div> <div class="option-content next3">0</div>'],
        ['<div class="next hardnext2">Seguir</div>', '<div class="next back">Volver a intentar</div>',
            '<div class="next back">Volver a intentar</div>']
    ]

    code = [
        [''],
        ['def sumar_lista(a):<br>'],
        [''],
        ['&nbsp&nbsp&nbspif len(a)==0:<br>',
         '&nbsp&nbsp&nbspif len(a)==0:<br>'],
        [''],
        ['&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn 0<br>'],
        [''],
        [''],
        ['&nbsp&nbsp&nbspelif len(a)==1:<br>'],
        [''],
        ['&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn a[0]<br>']
    ]

    '''false no tiene varias opciones (solo continuar o retroceder)
    true tiene varias opciones (a elegir)'''
    optionsChange = [
        True,
        False,
        True,
        False,
        True,
        False,
        True,
        True,
        False,
        True,
        False
    ]

    place = 4

    code_recursive = [
        ['&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn <span class="step_solution">a[0] + <span class="step_simpler">sumar_lista(<span class="step_subproblem">a[1:]</span>)</span></span><br>'],
        ['&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn <span class="step_solution">a[-1] + <span class="step_simpler">sumar_lista(<span class="step_subproblem">a[:-1]</span>)</span></span><br>'],
        ['&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn <span class="step_solution"><span class="step_simpler">sumar_lista(<span class="step_subproblem">a[len(a)//2:]</span>)</span> + <span class="step_simpler">sumar_lista(<span class="step_subproblem">a[:len(a)//2]</span>)</span></span><br>']
    ]

    paragraph1 = [
        ['Ahora tendremos que elegir la <strong>descomposición</strong> que usaremos para resolver el ejercicio.'],
        ['Es una <strong>descomposición</strong> válida, al quitar el primer elemento el tamaño del problema es más pequeño (len(a-1)).', 'Es una <strong>descomposición</strong> válida, al quitar el último elemento el tamaño del problema es más pequeño (len(a-1)).',
         'Es una <strong>descomposición</strong> válida, sin embargo al dividir a la mitad una lista de 1 elemento nos dan una lista de 0 elementos y de 1 elemento, pero no funcionaría en este caso dado que solo con len(a)==0 no contemplamos el caso de 1 único elemento, por lo que continuaría dividiendo la lista haciendo un bucle infinito.'],
        ['Ahora introduce unos valores de ejemplo en el recuadro de entrada. Puedes utilizar el siguiente ejemplo: [1, 3, 5, -2, -3]'],
        ['El <strong>subproblema</strong> se resuelve automáticamente al hacer la llamada recursiva. Queda componer el resultado del mismo con el valor de la descomposición.'],
        ['En efecto, dado que el objetivo es sumar todos los valores solo nos queda sumar el elemento con el resto de la lista.',
            'No podemos no hacer nada dado que en ese caso no se modificaría el retorno en ningún momento.', 'No es una lista, por tanto nos daría un error de tipos.',],
        ['¡Enhorabuena! Con esto habriamos terminado el ejercicio de sumar los elementos de una lista.']
    ]

    options1 = [
        ['<div class="option-content next1">Quitar el primer elemento</div> <div class="option-content next2">Quitar el último elemento</div> <div class="option-content next3">Partirlo a la mitad</div>'],
        ['<div class="next nextstage1">Seguir</div>', '<div class="next nextstage2">Seguir</div>',
            '<div class="next back">Volver a intentar</div>'],
        ['<div class="next evaluate">Calcular</div>'],
        ['<div class="option-content next2">Nada, ya debería de estar el resultado</div> <div class="option-content next3">++</div> <div class="option-content next1">+</div>'],
        ['<div class="next next1">Seguir</div>', '<div class="next back">Volver a intentar</div>',
            '<div class="next back">Volver a intentar</div>',],
        ['<div class="next end_exercise">Finalizar ejercicio</div>']
    ]

    code1 = [
        ['&nbsp&nbsp&nbspelse:<br>'],
        ['<span class="delete">&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn <span class="step_simpler">sumar_lista(<span class="step_subproblem">a[1:]</span>)</span><br></span>',
         '<span class="delete">&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn <span class="step_simpler">sumar_lista(<span class="step_subproblem">a[:-1]</span>)</span><br></span>'],
        [''],
        [''],
        [''],
        ['']
    ]

    '''false no tiene varias opciones (solo continuar o retroceder)
    true tiene varias opciones (a elegir)'''
    optionsChange1 = [
        True,
        False,
        False,
        True,
        False,
        False
    ]

    paragraph2 = [
        ['Ahora tendremos que elegir la <strong>descomposición</strong> que usaremos para resolver el ejercicio.'],
        ['Es una <strong>descomposición</strong> válida, al quitar el primer elemento el tamaño del problema es más pequeño (len(a-1)). En este caso no es eficiente utilizar el elif, dado que pararas cuando llegues a [].', 'Es una <strong>descomposición</strong> válida, al quitar el último elemento el tamaño del problema es más pequeño (len(a-1)), dado que ese caso ya se resuelve cuando llegue a 0.',
         'Es una <strong>descomposición</strong> válida, no funcionaría si no tenemos el elif, dado que sin ese caso al intentar descomponer una lista de 1 elemento en 2, nos queda una de 1 y una de 0, tras lo que volveriamos al mismo paso y sería un bucle infinito.'],
        ['Ahora introduce unos valores de ejemplo en el recuadro de arriba. Puedes utilizar el siguiente ejemplo: [1, 3, 5, -2, -3]'],
        ['El <strong>subproblema</strong> se resuelve automáticamente al hacer la llamada recursiva. Queda componer el resultado del mismo con el valor de la descomposición.'],
        ['En efecto, dado que el objetivo es sumar todos los valores solo nos queda sumar el valor de la <strong>descomposición</strong> con la solución simple.',
            'Hacer nada no es un opción dado que mantendrías el valor de la solución simple, no avanzando hacia la solución final.', 'No es una lista, por tanto nos daría un error de tipos.',],
        ['¡Enhorabuena! Con esto habriamos terminado el ejercicio de sumar los elementos de una lista.']
    ]

    options2 = [
        ['<div class="option-content next1">Quitar el primer elemento</div> <div class="option-content next2">Quitar el último elemento</div> <div class="option-content next3">Partirlo a la mitad</div>'],
        ['<div class="next nextstage1">Seguir</div>', '<div class="next nextstage2">Seguir</div>',
            '<div class="next nextstage3">Seguir</div>'],
        ['<div class="next evaluate">Calcular</div>'],
        ['<div class="option-content next2">Nada, ya debería de estar el resultado</div> <div class="option-content next3">++</div> <div class="option-content next1">+</div>'],
        ['<div class="next next1">Seguir</div>', '<div class="next back">Volver a intentar</div>',
            '<div class="next back">Volver a intentar</div>',],
        ['<div class="next end_exercise">Finalizar ejercicio</div>']
    ]

    code2 = [
        ['&nbsp&nbsp&nbspelse:<br>'],
        ['<span class="delete">&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn <span class="step_simpler">sumar_lista(<span class="step_subproblem">a[1:]</span>)</span><br></span>', '<span class="delete">&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn <span class="step_simpler">sumar_lista(<span class="step_subproblem">a[:-1]</span>)</span><br></span>',
         '<span class="delete">&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn <span class="step_simpler">sumar_lista(<span class="step_subproblem">a[len(a)//2:]</span>)</span> <span class="step_simpler">sumar_lista(<span class="step_subproblem">a[:len(a)//2]</span>)</span><br></span>'],
        [''],
        [''],
        [''],
        ['']
    ]

    '''false no tiene varias opciones (solo continuar o retroceder)
    true tiene varias opciones (a elegir)'''
    optionsChange2 = [
        True,
        False,
        False,
        True,
        False,
        False
    ]

    data = {
        'exercise': exercise,
        'description': description,
        'form': form,
        'paragraph': paragraph,
        'paragraph1': paragraph1,
        'paragraph2': paragraph2,
        'options': options,
        'options1': options1,
        'options2': options2,
        'code': code,
        'code1': code1,
        'code2': code2,
        'optionsChange': optionsChange,
        'optionsChange1': optionsChange1,
        'optionsChange2': optionsChange2,
        'place': place,
        'code_recursive': code_recursive,
    }

    return {'data': data, 'request': request}


def same_string(request, exercise):
    description = 'Dados dos String <i>a</i> y <i>b</i> compuestos de letras mayúsculas, minúsculas y números. Se desea averiguar si son iguales. Por ejemplo, para <span class="focus-wraper"><span class="outline o1"><i>a</i> = hola y <i>b</i> = hello</span><span class="ring r1"></span><span class="stick s1"></span></span> el resultado sería False ya que hola != hello'
    form = forms.sameStringForm()
    paragraph = [
        ['Siguiendo el ejemplo marcado seleccionaremos el <strong>tamaño del problema</strong>:'],
        ['¡Correcto! Como en las listas tendremos que utilizar la longitud para el tamaño, los Strings al fin y al cabo son listas de caracteres.',
            'Se podría llegar a utilizar. Pero dado que es una lista de caracteres lo recomendable sería pensar en la longitud para el tamaño.'],
        ['A continuación tendremos que elegir el <strong>caso base</strong> que se ajuste al problema.'],
        ['¡Correcto! Cuando el tamaño de uno de los string alcance 0 será un vacio, en el que la resolución es trivial.', 'Es correcto. Es lo mismo que decir que la longitud es 0, caso trivial de resolver.',
            'Casi es correcto. El problema estará en la descomposición, porque en cuanto uno llegue a 0 e intentes descomponer tendrás un error de ejecución si no acaban a la vez.'],
        ['Ahora elegiremos el valor de retorno una vez lleguemos al <strong>caso base</strong>.'],
        ['¡Correcto! Devolveremos el valor de verdad de si ambos son vacios, si no lo son será False.', '¡Correcto! Dado que uno ya es 0, si ambos son 0 será True, si no será False porque el otro tendría mayor longitud.',
            'Es un buen pensamiento, pero en realidad con el or en el if no sabemos si ambas listas son vacias en este momento.'],
        ['¿Con un <strong>caso base</strong> es suficiente?'],
        ['A continuación tendremos que elegir el otro <strong>caso base</strong>.'],
        ['¡Correcto! En caso de que uno de los valores llegue a 1 debería ser suficiente la resolución ya es trivial.',
            'Este es un caso trampa, en caso de que pusiesemos está comprobación ya sabriamos el resultado porque python lo haría por nosotros, pero estamos aprendiendo recursividad.', 'Es casi correcto. El problema es que podriamos tener tamaño mayor en la a y b nos daría un fallo de descomposición.'],
        ['Ahora elegiremos el valor de retorno una vez lleguemos a este <strong>caso base</strong>.'],
        ['¡Correcto! Si comprobamos que sean iguales los String será True, en cualquier otro caso False.', 'Esta vez no es correcto, porque aunque tengan el mismo tamaño también tiene que coincidir el valor del elemento, por ejemplo z != 3.',
            'Devolver False no es una opción, solo sería cierto si el tamaño o el valor son distintos.']
    ]

    options = [
        ['<div class="option-content next1">len()</div> <div class="option-content next2">a</div>'],
        ['<div class="next next1">Seguir</div>',
            '<div class="next back">Volver a intentar</div>'],
        ['<div class="option-content next1">len(a)==0 or len(b)==0</div> <div class="option-content next2">a=="" or b==""</div> <div class="option-content next3">len(a)<=0 and len(b)<=0</div>'],
        ['<div class="next next1">Seguir</div>', '<div class="next next1">Seguir</div>',
            '<div class="next back">Volver a intentar</div>'],
        ['<div class="option-content next2">len(a)==len(b)</div> <div class="option-content next1">a == b</div> <div class="option-content next3">True</div>'],
        ['<div class="next next1">Seguir</div>', '<div class="next next1">Seguir</div>',
            '<div class="next back">Volver a intentar</div>'],
        ['<div class="option-content hardnext1">Sí</div> <div class="option-content next1">No</div>'],
        ['<div class="option-content next2">a==b</div> <div class="option-content next1">len(a)==1 or len(b)==1</div> <div class="option-content next3">len(a)==1</div>'],
        ['<div class="next next1">Seguir</div>',
            '<div class="next back">Volver a intentar</div>', '<div class="next back">Volver a intentar</div>'],
        ['<div class="option-content next2">len(a) == len(b)</div> <div class="option-content next1">a==b</div> <div class="option-content next3">False</div>'],
        ['<div class="next hardnext2">Seguir</div>', '<div class="next back">Volver a intentar</div>',
            '<div class="next back">Volver a intentar</div>']
    ]

    code = [
        [''],
        ['def strings_iguales(a, b):<br>'],
        [''],
        ['&nbsp&nbsp&nbspif len(a)==0 or len(b)==0:<br>',
         '&nbsp&nbsp&nbspif a=="" or b=="":<br>'],
        [''],
        ['&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn a == b<br>',
            '&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn len(a)==len(b)<br>'],
        [''],
        [''],
        ['&nbsp&nbsp&nbspelif len(a)==1 or len(b)==1:<br>'],
        [''],
        ['&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn a==b<br>']
    ]

    '''false no tiene varias opciones (solo continuar o retroceder)
    true tiene varias opciones (a elegir)'''
    optionsChange = [
        True,
        False,
        True,
        False,
        True,
        False,
        True,
        True,
        False,
        True,
        False
    ]

    place = 4

    code_recursive = [
        ['&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn <span class="step_solution">a[0] == b[0] and <span class="step_simpler">strings_iguales(<span class="step_subproblem">a[1:], b[1:]</span>)</span></span><br>'],
        ['&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn <span class="step_solution">a[-1] == b[-1] and <span class="step_simpler">strings_iguales(<span class="step_subproblem">a[:-1], b[:-1]</span>)</span></span><br>'],
        ['&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn <span class="step_solution"><span class="step_simpler">strings_iguales(<span class="step_subproblem">a[len(b)//2:], b[len(b)//2:]</span>)</span> and <span class="step_simpler">strings_iguales(<span class="step_subproblem">a[:len(a)//2], b[:len(b)//2]</span>)</span></span><br>']
    ]

    paragraph1 = [
        ['Ahora tendremos que elegir la <strong>descomposición</strong> que usaremos para resolver el ejercicio.'],
        ['Es una <strong>descomposición</strong> válida, al quitar el primer caracter de ambos el tamaño del problema es más pequeño.', 'Es una <strong>descomposición</strong> válida, al quitar el último caracter el tamaño del problema es más pequeño.',
         'Es una <strong>descomposición</strong> válida. Al dividir a la mitad un string de 1 caracter nos dan un string vacio y otro de 1 caracter. Necesitas dos <strong>casos base</strong>, sin un <strong>caso base</strong> de un único carácter se repetiría la llamada haciendo un bucle infinito.'],
        ['Ahora introduce unos valores de ejemplo en el recuadro de entrada. Puedes utilizar el siguiente ejemplo: a=hola b=hello'],
        ['El <strong>subproblema</strong> se resuelve automáticamente al hacer la llamada recursiva. Queda componer el resultado del mismo con el valor de la descomposición.'],
        ['¡En efecto! Solo será igual si el subproblema es verdadero y la combinación de letras también.',
            'No podemos no hacer nada dado que en ese caso no se modificaría el retorno en ningún momento.', 'No sería correcto, dado que en ese caso en cuanto una comparación sea correcta se asumiría que las palabras son correctas con una sola letra igual.',],
        ['¡Enhorabuena! Con esto habriamos terminado el ejercicio de sumar los elementos de una lista.']
    ]

    options1 = [
        ['<div class="option-content next1">Quitar el primer caracter</div> <div class="option-content next2">Quitar el último caracter</div> <div class="option-content next3">Partirlo a la mitad</div>'],
        ['<div class="next nextstage1">Seguir</div>', '<div class="next nextstage2">Seguir</div>',
            '<div class="next back">Volver a intentar</div>'],
        ['<div class="next evaluate">Calcular</div>'],
        ['<div class="option-content next2">Nada, ya debería de estar el resultado</div> <div class="option-content next3">or</div> <div class="option-content next1">and</div>'],
        ['<div class="next next1">Seguir</div>', '<div class="next back">Volver a intentar</div>',
            '<div class="next back">Volver a intentar</div>',],
        ['<div class="next end_exercise">Finalizar ejercicio</div>']
    ]

    code1 = [
        ['&nbsp&nbsp&nbspelse:<br>'],
        ['<span class="delete">&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn <span class="step_simpler">strings_iguales(<span class="step_subproblem">a[1:], b[1:]</span>)</span><br></span>',
         '<span class="delete">&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn <span class="step_simpler">strings_iguales(<span class="step_subproblem">a[:-1], b[:-1]</span>)</span><br></span>'],
        [''],
        [''],
        [''],
        ['']
    ]

    '''false no tiene varias opciones (solo continuar o retroceder)
    true tiene varias opciones (a elegir)'''
    optionsChange1 = [
        True,
        False,
        False,
        True,
        False,
        False
    ]

    paragraph2 = [
        ['Ahora tendremos que elegir la <strong>descomposición</strong> que usaremos para resolver el ejercicio.'],
        ['Es una <strong>descomposición</strong> válida, al quitar el primer caracter el tamaño del problema es más pequeño. En este caso no es muy eficiente utilizar el elif, dado que añades un poco de complejidad en cada llamada.', 'Es una <strong>descomposición</strong> válida, al quitar el último caracter el tamaño del problema es más pequeño. En este caso no es muy eficiente utilizar el elif, dado que añades un poco de complejidad en cada llamada.',
         'Es una <strong>descomposición</strong> válida. Esta descomposición podría aparentar que es O(n), pero solo el tamaño del árbol lo sería, no el número de nodos.'],
        ['Ahora introduce unos valores de ejemplo en el recuadro de entrada. Puedes utilizar el siguiente ejemplo: a=hola b=hello'],
        ['El <strong>subproblema</strong> se resuelve automáticamente al hacer la llamada recursiva. Queda componer el resultado del mismo con el valor de la descomposición.'],
        ['¡En efecto! Solo será igual si el subproblema es verdadero y la combinación de letras también.',
            'No podemos no hacer nada dado que en ese caso no se modificaría el retorno en ningún momento.', 'No sería correcto, dado que en ese caso en cuanto una comparación sea correcta se asumiría que las palabras son correctas con una sola letra igual.',],
        ['¡Enhorabuena! Con esto habriamos terminado el ejercicio de sumar los elementos de una lista.']
    ]

    options2 = [
        ['<div class="option-content next1">Quitar el primer elemento</div> <div class="option-content next2">Quitar el último elemento</div> <div class="option-content next3">Partirlo a la mitad</div>'],
        ['<div class="next nextstage1">Seguir</div>', '<div class="next nextstage2">Seguir</div>',
            '<div class="next nextstage3">Seguir</div>'],
        ['<div class="next evaluate">Calcular</div>'],
        ['<div class="option-content next2">Nada, ya debería de estar el resultado</div> <div class="option-content next3">or</div> <div class="option-content next1">and</div>'],
        ['<div class="next next1">Seguir</div>', '<div class="next back">Volver a intentar</div>',
            '<div class="next back">Volver a intentar</div>',],
        ['<div class="next end_exercise">Finalizar ejercicio</div>']
    ]

    code2 = [
        ['&nbsp&nbsp&nbspelse:<br>'],
        ['<span class="delete">&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn <span class="step_simpler">strings_iguales(<span class="step_subproblem">a[1:]</span>)</span><br></span>', '<span class="delete">&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn <span class="step_simpler">strings_iguales(<span class="step_subproblem">a[:-1]</span>)</span><br></span>',
         '<span class="delete">&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn <span class="step_simpler">strings_iguales(<span class="step_subproblem">a[len(a)//2:], b[len(b)//2:]</span>)</span> <span class="step_simpler">strings_iguales(<span class="step_subproblem">a[:len(a)//2], b[:len(b)//2]</span>)</span><br></span>'],
        [''],
        [''],
        [''],
        ['']
    ]

    '''false no tiene varias opciones (solo continuar o retroceder)
    true tiene varias opciones (a elegir)'''
    optionsChange2 = [
        True,
        False,
        False,
        True,
        False,
        False
    ]

    data = {
        'exercise': exercise,
        'description': description,
        'form': form,
        'paragraph': paragraph,
        'paragraph1': paragraph1,
        'paragraph2': paragraph2,
        'options': options,
        'options1': options1,
        'options2': options2,
        'code': code,
        'code1': code1,
        'code2': code2,
        'optionsChange': optionsChange,
        'optionsChange1': optionsChange1,
        'optionsChange2': optionsChange2,
        'place': place,
        'code_recursive': code_recursive,
    }

    return {'data': data, 'request': request}


def decimal_to_binary(request, exercise):
    description = 'Dado un número no negativo <i>numero</i>. Se desea calcular la representación de <i>numero</i> en base 2. Por ejemplo, para <span class="focus-wraper"><span class="outline o1"><i>numero</i> = 13</span><span class="ring r1"></span><span class="stick s1"></span></span> el resultado sería 1101 ya que 13<sub>10</sub> = 1101<sub>2</sub> = 1·2<sup>3</sup> + 1·2<sup>2</sup> + 0·2<sup>1</sup> + 1·2<sup>0</sup>'
    form = forms.decimalBinaryForm()
    paragraph = [
        ['Siguiendo el ejemplo marcado seleccionaremos el <strong>tamaño del problema</strong>:'],
        ['¡Correcto! El <strong>tamaño del problema</strong> es el número de bits de la solución, aunque no lo necesitamos saber para resolver el ejercicio.', '¡En efecto! Es el logaritmo del número, en específico el logaritmo en base 2 dado que lo estamos pasando a binario.',
            'No podemos utilizar el número porque la reducción no es tan sencilla dado que necesitariamos una clase de representación en base 2. Nos daría una complejidad mayor O(n<sup>2</sup>) pero te animo a intentarlo.'],
        ['A continuación tendremos que elegir el <strong>caso base</strong> que se ajuste al problema.'],
        ['En casi todos los casos es correcto, dado que en la descomposición de un caso complejo siempre acabamos en 1, pero tenemos que contemplar que nos introduzcan el 0.',
            '¡Muy bien! Con ello vamos a contemplar el caso de 1 y el de 0 en un solo <strong>caso base</strong>.', '¡Correcto! Con ello vamos a contemplar el caso de 1 y el de 0 en un solo <strong>caso base</strong>.'],
        ['Ahora elegiremos el valor de retorno una vez lleguemos al <strong>caso base</strong>.'],
        ['Casi es correcto. El único problema es que si introducen un 0 deberiamos devolver un 0 no un 1.', '¡Muy bien! En caso de recibir un 1 devolvemos un 1 y con un 0 un 0.',
            'No es del todo correcto. Si solo devuelves un 0 el principio de la representación binario siempre será incorrecto.'],
        ['¿Nos hacen falta más <strong>casos base</strong>?'],
        ['No nos hacen falta más casos base. Con uno ya es suficiente.',
            '¡Efectivamente! Ya tenemos todos los casos posibles contemplados.'],
        ['Ahora tendremos que elegir la <strong>descomposición</strong> que usaremos para resolver el ejercicio.'],
        ['¡Correcto! Al hacer la división entera nos queda el cociente.', 'No podemos tan solo dividir. Nos quedaría como resultado un real, que no es una entrada válida para la función. Además de que matemáticamente necesitamos el cociente.',
            'Podría llegar a ser una solución posible. El problema es que tiene una complejidad mucho mayor y es un pensamiento más iterativo que recursivo.'],
        ['Ahora introduce unos valores de ejemplo en el recuadro de entrada. Puedes utilizar el siguiente ejemplo: numero = 7'],
        ['El <strong>subproblema</strong> se resuelve automáticamente al hacer la llamada recursiva. Queda componer el resultado.'],
        ['Sería una opción si fuese una clase de número binario en vez de un entero la resolución.', 'Saldría el resultado a la inversa y si hubiese ceros al final no se verían porque los ceros a la izquierda no se ponen en los enteros.',
            '¡Correcto! Tenemos que aumentar el número de las unidades y añadir el resto al final.'],
        ['¡Enhorabuena! Con esto habriamos terminado el ejercicio de decimal a binario.']
    ]

    options = [
        ['<div class="option-content next2">log(numero)</div> <div class="option-content next1">número de bits</div> <div class="option-content next3">numero</div>'],
        ['<div class="next next1">Seguir</div>', '<div class="next next1">Seguir</div>',
            '<div class="next back">Volver a intentar</div>'],
        ['<div class="option-content next1">numero==1</div> <div class="option-content next2">numero<2</div> <div class="option-content next3">numero<=1</div>'],
        ['<div class="next back">Volver a intentar</div>',
            '<div class="next next1">Seguir</div>', '<div class="next next1">Seguir</div>'],
        ['<div class="option-content next2">numero</div> <div class="option-content next1">1</div> <div class="option-content next3">0</div>'],
        ['<div class="next back">Volver a intentar</div>', '<div class="next next1">Seguir</div>',
            '<div class="next back">Volver a intentar</div>'],
        ['<div class="option-content next2">No</div> <div class="option-content next1">Sí</div>'],
        ['<div class="next back">Volver a intentar</div>',
            '<div class="next next1">Seguir</div>'],
        ['<div class="option-content next1">numero // 2</div> <div class="option-content next3">numero - 1</div> <div class="option-content next2">numero / 2</div>'],
        ['<div class="next next1">Seguir</div>', '<div class="next back">Volver a intentar</div>',
            '<div class="next back">Volver a intentar</div>'],
        ['<div class="next evaluate">Calcular</div>'],
        ['<div class="option-content next3">* 10 + (numero%2)</div> <div class="option-content next1">+ (numero%2)</div> <div class="option-content next2">+ (numero%2) * 10</div>'],
        ['<div class="next back">Volver a intentar</div>',
            '<div class="next back">Volver a intentar</div>', '<div class="next next1">Seguir</div>'],
        ['<div class="next end_exercise">Finalizar ejercicio</div>']
    ]

    code = [
        [''],
        ['def decimal_a_binario(numero):<br>',
         'def decimal_a_binario(numero):<br>'],
        [''],
        ['', '&nbsp&nbsp&nbspif numero < 2:<br>',
            '&nbsp&nbsp&nbspif numero <= 1:<br>'],
        [''],
        ['', '&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn numero<br>'],
        [''],
        ['', '&nbsp&nbsp&nbspelse:<br>'],
        [''],
        ['<span class="delete">&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn <span class="step_simpler">decimal_a_binario(<span class="step_subproblem">numero//2</span>)</span></span>'],
        [''],
        [''],
        ['', '',
            '&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn <span class="step_solution"><span class="step_simpler">decimal_a_binario(<span class="step_subproblem">numero//2</span>)</span> * 10 + (numero%2)</span>'],
        ['']
    ]

    '''false no tiene varias opciones (solo continuar o retroceder)
    true tiene varias opciones (a elegir)'''
    optionsChange = [
        True,
        False,
        True,
        False,
        True,
        False,
        True,
        False,
        True,
        False,
        False,
        True,
        False,
        False
    ]

    data = {
        'exercise': exercise,
        'description': description,
        'form': form,
        'paragraph': paragraph,
        'options': options,
        'code': code,
        'optionsChange': optionsChange,
    }

    return {'data': data, 'request': request}


def digit_in_number(request, exercise):
    description = 'Dados dos números enteros no negativos, <i>numero</i> y <i>digito</i> comprendido entre [0,9]. Se desea averiguar si el <i>digito</i> aparece en el <i>numero</i>. Por ejemplo, para <span class="focus-wraper"><span class="outline o1"><i>numero</i> = 658756 y <i>digito</i> = 5</span><span class="ring r1"></span><span class="stick s1"></span></span> el resultado sería True, dado que aparece 2 veces.'
    form = forms.digitInNumberForm()
    paragraph = [
        ['Siguiendo el ejemplo marcado seleccionaremos el <strong>tamaño del problema</strong>:'],
        ['Es una descripción muy vaga. Sí depende del número, pero tendriamos que poner una propiedad más específica.', '¡Correcto! Aunque no sea una lista el tamaño del problema viene dado por cuantos digitos tenga el número, aunque si pusiesemos la longitud de un entero fallaría en ejecución por el tipo.',
            'El digito que sea no importa de cara a conocer el tamaño del problema, nos da igual el valor de cara a descomponer.'],
        ['A continuación tendremos que elegir el <strong>caso base</strong> que se ajuste al problema.'],
        ['¡Correcto! Al ser el dígito menor que 10 sabes que su "tamaño" es 1, dado que es un número positivo.', 'Hay que estar un poco más atento, como ya hemos dicho va a dar un error en ejecución de tipos. ¡Los enteros no tienen propiedad len!.',
            'El digito no afecta al caso base.'],
        ['Ahora elegiremos el valor de retorno una vez lleguemos al <strong>caso base</strong>.'],
        ['¡En efecto! Tenemos que comprobar si el valor el digito es igual al número de un digito.', 'Casi, pero si hiciesemos una división entera sería como poner un 0 directamente.',
            'Es justo lo contrario, con eso comprobariamos si es distinto el valor y queremos que sea igual.'],
        ['¿Con un <strong>caso base</strong> es suficiente?'],
        ['No nos hacen falta más casos base. Con uno ya es suficiente.',
            '¡Efectivamente! Ya tenemos todos los casos posibles contemplados.'],
        ['Ahora tenemos que elegir una descomposición'],
        ['En efecto. Es una <strong>descomposición</strong> con la que obtenemos un número con un dígito menos.',
            'No sería una descomposición correcta dado que estariamos pasando un número real al subproblema.', 'Sería incorrecto porque si pasamos el resto solo conoceriamos la solución del resto, no de los demás dígitos.'],
        ['Ahora introduce unos valores de ejemplo en los recuadros de entrada. Puedes utilizar el siguiente ejemplo: base = 5 | exponente = 6'],
        ['El <strong>subproblema</strong> se resuelve automáticamente al hacer la llamada recursiva. Queda componer el resultado del mismo con el valor de la descomposición.'],
        ['Casi, pero si hacemos un and y ya era verdadero y ahora añadimos un falso estariamos diciendo que no está el digito cuando si está, en el subproblema.',
            '¡Efectivamente! Si hacemos el or con el elemento ya lo habiamos encontrado se mantendrá el resultado y si no dependerá de la igualdad de ahora.', 'Hacer nada no es una opción. Solo comprobariamos si el primer número es igual al digito, no el resto.',],
        ['¡Enhorabuena! Con esto habriamos terminado el ejercicio de sumar los elementos de una lista.']
    ]

    options = [
        ['<div class="option-content next1">numero</div> <div class="option-content next2">len(numero)</div> <div class="option-content next3">digito</div>'],
        ['<div class="next back">Volver a intentar</div>', '<div class="next next1">Seguir</div>',
            '<div class="next back">Volver a intentar</div>'],
        ['<div class="option-content next2">len(numero)==1</div> <div class="option-content next1">numero < 10</div> <div class="option-content next3">numero==digito</div>'],
        ['<div class="next next1">Seguir</div>', '<div class="next back">Volver a intentar</div>',
            '<div class="next back">Volver a intentar</div>'],
        ['<div class="option-content next2">numero//10==digito</div> <div class="option-content next3">numero != digito</div> <div class="option-content next1">numero == digito</div>'],
        ['<div class="next next1">Seguir</div>', '<div class="next back">Volver a intentar</div>',
            '<div class="next back">Volver a intentar</div>'],
        ['<div class="option-content next2">Sí</div> <div class="option-content next1">No</div>'],
        ['<div class="next back">Volver a intentar</div>',
            '<div class="next next1">Seguir</div>'],
        ['<div class="option-content next2">numero / 10</div> <div class="option-content next3">numero % 10</div> <div class="option-content next1">numero // 10</div>'],
        ['<div class="next next1">Seguir</div>', '<div class="next back">Volver a intentar</div>',
            '<div class="next back">Volver a intentar</div>'],
        ['<div class="next evaluate">Calcular</div>'],
        ['<div class="option-content next3">Nada, ya debería de estar el resultado</div> <div class="option-content next2">or numero%10 == digito</div> <div class="option-content next1">and numero%10 == digito</div>'],
        ['<div class="next back">Volver a intentar</div>', '<div class="next next1">Seguir</div>',
            '<div class="next back">Volver a intentar</div>',],
        ['<div class="next end_exercise">Finalizar ejercicio</div>']
    ]

    code = [
        [''],
        ['', 'def digito_en_numero(numero, digito):<br>'],
        [''],
        ['&nbsp&nbsp&nbspif numero < 10:<br>'],
        [''],
        ['&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn numero == digito<br>'],
        [''],
        ['', '&nbsp&nbsp&nbspelse:<br>'],
        [''],
        ['<span class="delete">&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn <span class="step_simpler">digito_en_numero(<span class="step_subproblem">numero // 10, digito</span>)</span></span>'],
        [''],
        [''],
        ['',
            '&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn <span class="step_solution"><span class="step_simpler">digito_en_numero(<span class="step_subproblem">numero // 10, digito</span>)</span> or numero%10 == digito</span>'],
        ['']
    ]

    '''false no tiene varias opciones (solo continuar o retroceder)
    true tiene varias opciones (a elegir)'''
    optionsChange = [
        True,
        False,
        True,
        False,
        True,
        False,
        True,
        False,
        True,
        False,
        False,
        True,
        False,
        False
    ]

    data = {
        'exercise': exercise,
        'description': description,
        'form': form,
        'paragraph': paragraph,
        'options': options,
        'code': code,
        'optionsChange': optionsChange,
    }

    return {'data': data, 'request': request}


def palindrome(request, exercise):
    description = 'Dada un string <i>palabra</i> compuesto de letras minúsculas. Se desea averiguar si <i>palabra</i> es palíndromo, es decir se lee igual al derecho que al revés. Por ejemplo, para <span class="focus-wraper"><span class="outline o1"><i>palabra</i> = recocer</span><span class="ring r1"></span><span class="stick s1"></span></span> el resultado es True dado que recocer = recocer'
    form = forms.palindromeForm()
    paragraph = [
        ['Siguiendo el ejemplo marcado seleccionaremos el <strong>tamaño del problema</strong>:'],
        ['Es un razonamiento vago. Lo que tenemos que elegir es una propiedad de la palabra.', 'Creo que se por dónde vas. Hacerlo en la mitad de tiempo no es logarítmico, es un factor de n.',
            '¡Muy bien! En efecto es la longitud de la palabra la que va a dar el tamaño del problema.'],
        ['A continuación tendremos que elegir el <strong>caso base</strong> que se ajuste al problema.'],
        ['Podría ser una opción, pero dado que luego vamos a necesitar otro <strong>caso base</strong> podemos comprimirlo ya de antemano.', '¡Correcto! Dado que puede resultar que la palabra tenga longitud par o impar, pero en ambos casos la solución es la misma.',
            'Podría ser una opción, pero dado que luego vamos a necesitar otro <strong>caso base</strong> podemos comprimirlo ya de antemano.'],
        ['Ahora elegiremos el valor de retorno una vez lleguemos al <strong>caso base</strong>.'],
        ['¡En efecto! Siempre que tengamos una o ninguna letra el resultado es verdadero.', 'La idea es interesante, pero dado que la longitud == 0 es un caso posible sería un error out of bounds.',
            'Al contrario, por ejemplo una palabra de una única letra es palíndroma.'],
        ['¿Con un <strong>caso base</strong> es suficiente?'],
        ['No nos hacen falta más casos base. Con uno ya es suficiente.',
            '¡Efectivamente! Ya tenemos todos los casos posibles contemplados.'],
        ['Ahora tenemos que elegir una descomposición'],
        ['¡En efecto! Es una <strong>descomposición</strong> con la que iremos quitando el primer y último elmento haciendo que el tiempo no sea n si no n/2, aunque sigue siendo O(n).',
            'Si solo quitamos el primer caracter estariamos reduciendo el problema a una palabra no palíndroma y luego sería más difícil de controlar la composición de la solución. ¡Te animo a intentarlo de todos modos!', 'Si solo quitamos el último caracter estariamos reduciendo el problema a una palabra no palíndroma y luego sería más difícil de controlar la composición de la solución. ¡Te animo a intentarlo de todos modos!'],
        ['Ahora introduce unos valores de ejemplo en los recuadros de entrada. Puedes utilizar el siguiente ejemplo: palabra = corbeta'],
        ['El <strong>subproblema</strong> se resuelve automáticamente al hacer la llamada recursiva. Queda componer el resultado del mismo con el valor de la descomposición.'],
        ['Casi, pero si hacemos un or diriamos que en cuanto una coincide coinciden todas y eso no sería cierto.',
            '¡Efectivamente! Si hacemos el and con el resultado del <strong>subproblema</strong> sabremos si el resultado se mantiene palíndromo en caso de que lo fuese y si no deja de serlo.', 'Hacer nada no es una opción. Tenemos que saber si las letras de la descomposición son iguales o no.',],
        ['¡Enhorabuena! Con esto habriamos terminado el ejercicio de sumar los elementos de una lista.']
    ]

    options = [
        ['<div class="option-content next3">len(palabra)</div> <div class="option-content next1">palabra</div> <div class="option-content next2">log(palabra)</div>'],
        ['<div class="next back">Volver a intentar</div>',
            '<div class="next back">Volver a intentar</div>', '<div class="next next1">Seguir</div>'],
        ['<div class="option-content next3">len(palabra) == 0</div> <div class="option-content next1">palabra==""</div> <div class="option-content next2">len(palabra) <= 1</div>'],
        ['<div class="next back">Volver a intentar</div>', '<div class="next next1">Seguir</div>',
            '<div class="next back">Volver a intentar</div>'],
        ['<div class="option-content next1">True</div> <div class="option-content next3">False</div> <div class="option-content next2">palabra[0]==palabra[-1]</div>'],
        ['<div class="next next1">Seguir</div>', '<div class="next back">Volver a intentar</div>',
            '<div class="next back">Volver a intentar</div>'],
        ['<div class="option-content next2">Sí</div> <div class="option-content next1">No</div>'],
        ['<div class="next back">Volver a intentar</div>',
            '<div class="next next1">Seguir</div>'],
        ['<div class="option-content next2">palabra[1:]</div> <div class="option-content next1">palabra[1:-1]</div> <div class="option-content next3">len(palabra)//2</div>'],
        ['<div class="next next1">Seguir</div>', '<div class="next back">Volver a intentar</div>',
            '<div class="next back">Volver a intentar</div>'],
        ['<div class="next evaluate">Calcular</div>'],
        ['<div class="option-content next2">and palabra[0] == palabra[-1]</div> <div class="option-content next3">Nada, ya debería de estar el resultado</div> <div class="option-content next1">or palabra[0] == palabra[-1]</div>'],
        ['<div class="next back">Volver a intentar</div>', '<div class="next next1">Seguir</div>',
            '<div class="next back">Volver a intentar</div>',],
        ['<div class="next end_exercise">Finalizar ejercicio</div>']
    ]

    code = [
        [''],
        ['', 'def palindromo(palabra):<br>'],
        [''],
        ['', '', '&nbsp&nbsp&nbspif palabra <= 1:<br>'],
        [''],
        ['&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn True<br>'],
        [''],
        ['', '&nbsp&nbsp&nbspelse:<br>'],
        [''],
        ['<span class="delete">&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn <span class="step_simpler">palindromo(<span class="step_subproblem">palabra[1:-1]</span>)</span></span>'],
        [''],
        [''],
        ['',
            '&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn <span class="step_solution"><span class="step_simpler">palindromo(<span class="step_subproblem">palabra[1:-1]</span>)</span> and palabra[0] == palabra[-1]</span>'],
        ['']
    ]

    '''false no tiene varias opciones (solo continuar o retroceder)
    true tiene varias opciones (a elegir)'''
    optionsChange = [
        True,
        False,
        True,
        False,
        True,
        False,
        True,
        False,
        True,
        False,
        False,
        True,
        False,
        False
    ]

    data = {
        'exercise': exercise,
        'description': description,
        'form': form,
        'paragraph': paragraph,
        'options': options,
        'code': code,
        'optionsChange': optionsChange,
    }

    return {'data': data, 'request': request}


def decimal_to_n_ary(request, exercise):
    description = 'Dados un número no negativo <i>numero</i>, y otro entero <i>base</i> comprendido entre [2,9]. Se desea calcular la representación de <i>numero</i> en base <i>base</i>. Por ejemplo, para <span class="focus-wraper"><span class="outline o1"><i>numero</i> = 24, y <i>base</i> = 3</span><span class="ring r1"></span><span class="stick s1"></span></span> el resultado sería 220 ya que 24<sub>10</sub> = 220<sub>3</sub> = 2·3<sup>2</sup> + 2·3<sup>1</sup> + 0·3<sup>0</sup>'
    form = forms.nAryForm()
    paragraph = [
        ['Siguiendo el ejemplo marcado seleccionaremos el <strong>tamaño del problema</strong>:'],
        ['¡Correcto! El <strong>tamaño del problema</strong> es el número de digitos de la solución, aunque no lo necesitamos saber para resolver el ejercicio.', '¡En efecto! Es el logaritmo del número, en específico el logaritmo en base "base".',
            'No podemos utilizar el número porque la reducción no es tan sencilla dado que necesitariamos una clase de representación en base "base". Nos daría una complejidad mayor O(n<sup>2</sup>), pero te animo a intentarlo.'],
        ['A continuación tendremos que elegir el <strong>caso base</strong> que se ajuste al problema.'],
        ['Si solo contemplamos cuando llegue a 1 nos pasariamos siempre en lo casos recursivos salvo que justo salga 1.',
            '¡Muy bien! Con ello vamos a contemplar el caso de que quede por debajo de la base en un solo <strong>caso base</strong>.', '¡Correcto! Con ello vamos a contemplar el caso de que quede por debajo de la base en un solo <strong>caso base</strong>.'],
        ['Ahora elegiremos el valor de retorno una vez lleguemos al <strong>caso base</strong>.'],
        ['Si devolvemos la base siempre va a ser el mismo resultado independientemente del numero, eso sería incorrecto.', '¡Muy bien! Siempre devolveremos el valor que debería ser.',
            'Si devolvemos un 1 el resultado siempre va a ser el mismo independientemente del numero, eso sería incorrecto.'],
        ['¿Nos hacen falta más <strong>casos base</strong>?'],
        ['No nos hacen falta más casos base. Con uno ya es suficiente.',
            '¡Efectivamente! Ya tenemos todos los casos posibles contemplados.'],
        ['Ahora tendremos que elegir la <strong>descomposición</strong> que usaremos para resolver el ejercicio.'],
        ['¡Correcto! Al hacer la división entera nos queda el cociente.', 'No podemos tan solo dividir. Nos quedaría como resultado un real, que no es una entrada válida para la función. Además de que matemáticamente necesitamos el cociente.',
            'Podría llegar a ser una solución posible. El problema es que tiene una complejidad mucho mayor y es un pensamiento más iterativo que recursivo.'],
        ['Ahora introduce unos valores de ejemplo en el recuadro de entrada. Puedes utilizar el siguiente ejemplo: numero=34 base=7'],
        ['El <strong>subproblema</strong> se resuelve automáticamente al hacer la llamada recursiva. Queda componer el resultado.'],
        ['Sería una opción si fuese una clase de número base "base" en vez de un entero la resolución.', 'Saldría el resultado a la inversa y si hubiese ceros al final no se verían porque los ceros a la izquierda no se ponen en los enteros.',
            '¡Correcto! Tenemos que aumentar el número de las unidades y añadir el resto al final.'],
        ['¡Enhorabuena! Con esto habriamos terminado el ejercicio de decimal a binario.']
    ]

    options = [
        ['<div class="option-content next2">log(numero)</div> <div class="option-content next1">número de dígitos solución</div> <div class="option-content next3">numero</div>'],
        ['<div class="next next1">Seguir</div>', '<div class="next next1">Seguir</div>',
            '<div class="next back">Volver a intentar</div>'],
        ['<div class="option-content next1">numero==1</div> <div class="option-content next2">numero < base</div> <div class="option-content next3">numero<=base-1</div>'],
        ['<div class="next back">Volver a intentar</div>',
            '<div class="next next1">Seguir</div>', '<div class="next next1">Seguir</div>'],
        ['<div class="option-content next2">numero</div> <div class="option-content next1">base</div> <div class="option-content next3">1</div>'],
        ['<div class="next back">Volver a intentar</div>', '<div class="next next1">Seguir</div>',
            '<div class="next back">Volver a intentar</div>'],
        ['<div class="option-content next2">No</div> <div class="option-content next1">Sí</div>'],
        ['<div class="next back">Volver a intentar</div>',
            '<div class="next next1">Seguir</div>'],
        ['<div class="option-content next1">numero // base</div> <div class="option-content next3">numero - 1</div> <div class="option-content next2">numero / base</div>'],
        ['<div class="next next1">Seguir</div>', '<div class="next back">Volver a intentar</div>',
            '<div class="next back">Volver a intentar</div>'],
        ['<div class="next evaluate">Calcular</div>'],
        ['<div class="option-content next3">* 10 + (numero%base)</div> <div class="option-content next1">+ (numero%base)</div> <div class="option-content next2">+ (numero%base) * 10</div>'],
        ['<div class="next back">Volver a intentar</div>',
            '<div class="next back">Volver a intentar</div>', '<div class="next next1">Seguir</div>'],
        ['<div class="next end_exercise">Finalizar ejercicio</div>']
    ]

    code = [
        [''],
        ['def decimal_a_n_ario(numero, base):<br>',
         'def decimal_a_binario(numero, base):<br>'],
        [''],
        ['', '&nbsp&nbsp&nbspif numero < base:<br>',
            '&nbsp&nbsp&nbspif numero <= base-1:<br>'],
        [''],
        ['', '&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn numero<br>'],
        [''],
        ['', '&nbsp&nbsp&nbspelse:<br>'],
        [''],
        ['<span class="delete">&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn <span class="step_simpler">decimal_a_n_ario(<span class="step_subproblem">numero//base</span>)</span></span>'],
        [''],
        [''],
        ['', '',
            '&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn <span class="step_solution"><span class="step_simpler">decimal_a_n_ario(<span class="step_subproblem">numero//base</span>)</span> * 10 + (numero%base)</span>'],
        ['']
    ]

    '''false no tiene varias opciones (solo continuar o retroceder)
    true tiene varias opciones (a elegir)'''
    optionsChange = [
        True,
        False,
        True,
        False,
        True,
        False,
        True,
        False,
        True,
        False,
        False,
        True,
        False,
        False
    ]

    data = {
        'exercise': exercise,
        'description': description,
        'form': form,
        'paragraph': paragraph,
        'options': options,
        'code': code,
        'optionsChange': optionsChange,
    }

    return {'data': data, 'request': request}


def factorial(request, exercise):
    description = 'Dado un número entero no negativo <i>numero</i>. El objetivo es calcular el resultado del factorial de <i>numero</i>. Por ejemplo, para <span class="focus-wraper"><span class="outline o1"><i>numero</i> = 6</span><span class="ring r1"></span><span class="stick s1"></span></span> el resultado sería 720 dado que 6! = 720 = 6·5·4·3·2·1'
    form = forms.factorialForm()

    paragraph = [
        ['Siguiendo el ejemplo marcado seleccionaremos el <strong>tamaño del problema</strong>:'],
        ['No se puede resolver en tiempo logarítmico, aunque se puede reducir un poco la complejidad de las multiplicaciones con el algoritmo de karatsuba.',
            '¡Correcto! El propio número nos indica el tamaño del problema.'],
        ['A continuación tendremos que elegir el <strong>caso base</strong> que se ajuste al problema.'],
        ['¡Correcto! En cuanto llegues a 1 o a 0 matemáticamente ya sabemos el resultado.',
            '¡Cierto! El 0 es un <strong>caso base</strong> muy reconocido en las matemáticas para los factoriales.', 'Casi, contemplas casi todos los casos salvo el propio 0.'],
        ['Ahora elegiremos el valor de retorno una vez lleguemos al <strong>caso base</strong>.'],
        ['La idea es interesante. El problema es que el factorial de 0 no es 0.',
            '¡En efecto! Lo más importante es que el factorial de 0 siempre es 1, momento en el que no hace falta reducir más. Cabe destacar que el factorial de 1 siempre es 1 también, lo cual hace el código más eficiente con numero <=1.', 'El problema es que el factorial de 0 no es 0.'],
        ['¿Nos hacen falta más <strong>casos base</strong>?'],
        ['No nos hacen falta más casos base. Con uno ya es suficiente.',
            '¡Efectivamente! Ya tenemos todos los casos posibles contemplados.'],
        ['Ahora tendremos que elegir la <strong>descomposición</strong> que usaremos para resolver el ejercicio.'],
        ['Si hacemos la raiz cuadrada nos dará una entrada incorrecta porque estariamos pasando un real y además no tiene sentido matemático para el factorial.',
            '¡Correcto! Al restar 1 el problema es el factorial del número anterior.', 'Si dividimos el numero a la mitad tendremos que pensar de forma iterativa para resolver luego el ejercicio, asi que no es la mejor opción. Puedes intentarlo para ver como saldría la <strong>derivación del caso recursivo</strong>.'],
        ['Ahora introduce unos valores de ejemplo en los recuadros de entrada. Puedes utilizar el siguiente ejemplo: numero = 7'],
        ['El <strong>subproblema</strong> se resuelve automáticamente al hacer la llamada recursiva. Queda componer el resultado del mismo con el valor de la descomposición.'],
        ['¡Por supuesto! Los factoriales son una secuencia de multiplicaciones.', 'Es un error de concepto, los factoriales no son una secuencia de sumas.',
            'Si multiplicamos por el valor inmediatamente más pequeño el resultado no sería el correcto.'],
        ['¡Enhorabuena! Con esto habriamos terminado el ejercicio de factoriales.']
    ]

    options = [
        ['<div class="option-content next2">numero</div> <div class="option-content next1">log(numero)</div>'],
        ['<div class="next back">Volver a intentar</div>',
            '<div class="next next1">Seguir</div>'],
        ['<div class="option-content next1">numero<=1</div> <div class="option-content next2">numero==0</div> <div class="option-content next3">numero==1</div>'],
        ['<div class="next next1">Seguir</div>', '<div class="next next1">Seguir</div>',
            '<div class="next back">Volver a intentar</div>'],
        ['<div class="option-content next2">1</div> <div class="option-content next1">numero</div> <div class="option-content next3">0</div>'],
        ['<div class="next back">Volver a intentar</div>', '<div class="next next1">Seguir</div>',
            '<div class="next back">Volver a intentar</div>'],
        ['<div class="option-content next2">No</div> <div class="option-content next1">Sí</div>'],
        ['<div class="next back">Volver a intentar</div>',
            '<div class="next next1">Seguir</div>'],
        ['<div class="option-content next3">numero // 2</div> <div class="option-content next2">numero - 1</div> <div class="option-content next1">numero ** 0.5</div>'],
        ['<div class="next back">Volver a intentar</div>',
            '<div class="next next1">Seguir</div>', '<div class="next back">Volver a intentar</div>'],
        ['<div class="next evaluate">Calcular</div>'],
        ['<div class="option-content next1">* numero</div> <div class="option-content next2">+ numero</div> <div class="option-content next3">* (numero - 1)</div>'],
        ['<div class="next next1">Seguir</div>', '<div class="next back">Volver a intentar</div>',
            '<div class="next back">Volver a intentar</div>'],
        ['<div class="next end_exercise">Finalizar ejercicio</div>']
    ]

    code = [
        [''],
        ['', 'def factorial(numero):<br>'],
        [''],
        ['&nbsp&nbsp&nbspif numero<=1:<br>', '&nbsp&nbsp&nbspif numero==0:<br>'],
        [''],
        ['', '&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn 1<br>'],
        [''],
        ['', '&nbsp&nbsp&nbspelse:<br>'],
        [''],
        ['',
            '<span class="delete">&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn <span class="step_simpler">factorial(<span class="step_subproblem">numero - 1</span>)</span></span>'],
        [''],
        [''],
        ['&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn <span class="step_solution"><span class="step_simpler">factorial(<span class="step_subproblem">numero - 1</span>)</span> * n</span><br>'],
        ['']
    ]

    '''false no tiene varias opciones (solo continuar o retroceder)
    true tiene varias opciones (a elegir)'''
    optionsChange = [
        True,
        False,
        True,
        False,
        True,
        False,
        True,
        False,
        True,
        False,
        False,
        True,
        False,
        False
    ]

    data = {
        'exercise': exercise,
        'description': description,
        'form': form,
        'paragraph': paragraph,
        'options': options,
        'code': code,
        'optionsChange': optionsChange,
    }

    return {'data': data, 'request': request}


def greater_in_list(request, exercise):
    description = 'Dada una lista de enteros no negativos no vacia <strong>a</strong>. Se desea averiguar el mayor número en <strong>a</strong>. Por ejemplo para <span class="focus-wraper"><span class="outline o1"><strong>a</strong> = [4, -5, 7]</span><span class="ring r1"></span><span class="stick s1"></span></span> el resultado sería 7 ya que -5 < 4 < 7.'
    form = forms.listForm()

    paragraph = [
        ['Siguiendo el ejemplo marcado seleccionaremos el <strong>tamaño del problema</strong>:'],
        ['¡Correcto! Lo más habitual al trabajar con listas es usar la longitud para determinar el tamaño del problema.',
            'La a podría ser una solución posible; en muchos lenguajes las listas no son tipos primitivos y es más difícil usarlas en condicionales. Habitualmente se utiliza el tamaño de la lista dado que es más sencillo. ¡Os animo a intentarlo!'],
        ['A continuación tendremos que elegir el <strong>caso base</strong> que se ajuste al problema.'],
        ['No aceptamos listas vacias dado que tendriamos que generar o una excepción o devolver un valor de error de algún tipo dado que no hay elementos que puedan ser más grandes que otros.', '¡Correcto! Cuando la lista solo tenga 1 elemento es trivial.',
            'Si utilizamos la a==1 nos dará un error de ejecución, dado que un elemento tipo lista no es comparable a un elemento tipo entero.'],
        ['Ahora elegiremos el valor de retorno una vez lleguemos al <strong>caso base</strong>.'],
        ['No es del todo correcto. Si devolvemos a estamos devolviendo una lista, el objetivo es devolver un entero.', 'Si devolvemos un 0 con una lista de un elemento estariamos obviando dicho valor.',
            '¡En efecto! El mayor elemento en una lista de un elemento es el propio elemento.'],
        ['¿Con un <strong>caso base</strong> es suficiente?'],
        ['No nos hacen falta más casos base. Con uno ya es suficiente.',
            '¡Efectivamente! Ya tenemos todos los casos posibles contemplados.'],
        ['Ahora tendremos que elegir la <strong>descomposición</strong> que usaremos para resolver el ejercicio.'],
        ['¡Correcto! Es una descomposición válida.'],
        ['Ahora introduce unos valores de ejemplo en los recuadros de entrada, el exponente a de ser par. Puedes utilizar el siguiente ejemplo: a = [-3, 4, 2, -1, 7, 6]'],
        ['El <strong>subproblema</strong> se resuelve automáticamente al hacer la llamada recursiva. Queda componer el resultado del mismo con el valor de la descomposición.'],
        ['¡Por supuesto! Tenemos que escoger el máximo entre las dos mitades.', 'Casi es correcto. El problema es que devuelve un valor booleano aunque se puede hacer con un if else. ¡Intenta hacerlo!.',
            'Casi es correcto. El problema es que devuelve un valor booleano aunque se puede hacer con un if else. ¡Intenta hacerlo!.'],
        ['¡Enhorabuena! Con esto habriamos terminado el ejercicio de potencias.']
    ]

    options = [
        ['<div class="option-content next1">len(a)</div> <div class="option-content next2">a</div>'],
        ['<div class="next next1">Seguir</div>',
            '<div class="next back">Volver a intentar</div>'],
        ['<div class="option-content next1">len(a)==0</div> <div class="option-content next2">len(a)==1</div> <div class="option-content next3">a==1</div>'],
        ['<div class="next back">Volver a intentar</div>', '<div class="next next1">Seguir</div>',
            '<div class="next back">Volver a intentar</div>'],
        ['<div class="option-content next2">0</div> <div class="option-content next1">a</div> <div class="option-content next3">a[0]</div>'],
        ['<div class="next back">Volver a intentar</div>',
            '<div class="next back">Volver a intentar</div>', '<div class="next next1">Seguir</div>'],
        ['<div class="option-content next2">Sí</div> <div class="option-content next1">No</div>'],
        ['<div class="next back">Volver a intentar</div>',
            '<div class="next next1">Seguir</div>'],
        ['<div class="option-content hardnext1">Quitar el primer elemento</div> <div class="option-content hardnext2">Quitar el último elemento</div> <div class="option-content next1">Dividir a la mitad</div>'],
        ['<div class="next next1">Seguir</div>'],
        ['<div class="next evaluate">Calcular</div>'],
        ['<div class="option-content next1">max</div> <div class="option-content next2">mayor</div> <div class="option-content next3">mayor o igual</div>'],
        ['<div class="next next1">Seguir</div>', '<div class="next back">Volver a intentar</div>',
            '<div class="next back">Volver a intentar</div>'],
        ['<div class="next end_exercise">Finalizar ejercicio</div>']
    ]

    code = [
        [''],
        ['def mayor_lista(a):<br>'],
        [''],
        ['', '&nbsp&nbsp&nbspif len(a)==1:<br>'],
        [''],
        ['', '', '&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn a[0]<br>'],
        [''],
        ['', '&nbsp&nbsp&nbspelse:<br>'],
        [''],
        ['<span class="delete">&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn <span class="step_simpler">mayor_lista(<span class="step_subproblem">a[:len(a)]//2]</span>)</span> <span class="step_simpler">mayor_lista(<span class="step_subproblem">a[len(a)]//2:]</span>)</span></span>'],
        [''],
        [''],
        ['&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn <span class="step_solution">max(<span class="step_simpler">mayor_lista(<span class="step_subproblem">a[:len(a)]//2]</span>)</span>, <span class="step_simpler">mayor_lista(<span class="step_subproblem">a[len(a)]//2:]</span>)</span>)</span><br>'],
        ['']
    ]

    '''false no tiene varias opciones (solo continuar o retroceder)
    true tiene varias opciones (a elegir)'''
    optionsChange = [
        True,
        False,
        True,
        False,
        True,
        False,
        True,
        False,
        True,
        False,
        False,
        True,
        False,
        False
    ]

    paragraph1 = [
        ['¡Muy bien! Al quitar el primer elemento reducimos el tamaño de la lista.'],
        ['Ahora introduce unos valores de ejemplo en el recuadro de entrada. Puedes utilizar el siguiente ejemplo: [-3, 4, 2, -1, 7, 6]'],
        ['El <strong>subproblema</strong> se resuelve automáticamente al hacer la llamada recursiva. Queda componer el resultado del mismo con el valor de la descomposición para el caso par.'],
        ['¡Por supuesto! Tenemos que escoger el máximo entre las dos mitades.', 'Casi es correcto. El problema es que devuelve un valor booleano aunque se puede hacer con un if else. ¡Intenta hacerlo!.',
            'Casi es correcto. El problema es que devuelve un valor booleano aunque se puede hacer con un if else. ¡Intenta hacerlo!.'],
        ['¡Enhorabuena! Con esto habriamos terminado el ejercicio de potencias.']
    ]

    options1 = [
        ['<div class="next next1">Seguir</div>'],
        ['<div class="next evaluate">Calcular</div>'],
        ['<div class="option-content next1">max</div> <div class="option-content next2">mayor</div> <div class="option-content next3">mayor o igual</div>'],
        ['<div class="next next1">Seguir</div>', '<div class="next back">Volver a intentar</div>',
            '<div class="next back">Volver a intentar</div>'],
        ['<div class="next end_exercise">Finalizar ejercicio</div>']
    ]

    code1 = [
        ['<span class="delete">&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn <span class="step_simpler">mayor_lista(<span class="step_subproblem">a[1:]</span>)</span></span>'],
        [''],
        [''],
        ['&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn <span class="step_solution">max(a[0], <span class="step_simpler">mayor_lista(<span class="step_subproblem">a[1:]</span>)</span>)</span><br>'],
        ['']
    ]

    '''false no tiene varias opciones (solo continuar o retroceder)
    true tiene varias opciones (a elegir)'''
    optionsChange1 = [
        False,
        False,
        True,
        False,
        False
    ]

    paragraph2 = [
        ['¡Muy bien! Al quitar el último elemento reducimos el tamaño de la lista.'],
        ['Ahora introduce unos valores de ejemplo en el recuadro de arriba. Puedes utilizar el siguiente ejemplo: [-3, 4, 2, -1, 7, 6]'],
        ['El <strong>subproblema</strong> se resuelve automáticamente al hacer la llamada recursiva. Queda componer el resultado del mismo con el valor de la descomposición para el caso par.'],
        ['¡Por supuesto! Tenemos que escoger el máximo entre las dos mitades.', 'Casi es correcto. El problema es que devuelve un valor booleano aunque se puede hacer con un if else. ¡Intenta hacerlo!.',
            'Casi es correcto. El problema es que devuelve un valor booleano aunque se puede hacer con un if else. ¡Intenta hacerlo!.'],
        ['¡Enhorabuena! Con esto habriamos terminado el ejercicio de potencias.']
    ]

    options2 = [
        ['<div class="next next1">Seguir</div>'],
        ['<div class="next evaluate">Calcular</div>'],
        ['<div class="option-content next1">max</div> <div class="option-content next2">mayor</div> <div class="option-content next3">mayor o igual</div>'],
        ['<div class="next next1">Seguir</div>', '<div class="next back">Volver a intentar</div>',
            '<div class="next back">Volver a intentar</div>'],
        ['<div class="next end_exercise">Finalizar ejercicio</div>']
    ]

    code2 = [
        ['<span class="delete">&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn <span class="step_simpler">mayor_lista(<span class="step_subproblem">a[:-1]</span>)</span></span>'],
        [''],
        [''],
        ['&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn <span class="step_solution">max(a[-1], <span class="step_simpler">mayor_lista(<span class="step_subproblem">a[:-1]</span>)</span>)</span><br>'],
        ['']
    ]

    '''false no tiene varias opciones (solo continuar o retroceder)
    true tiene varias opciones (a elegir)'''
    optionsChange2 = [
        False,
        False,
        True,
        False,
        False
    ]

    data = {
        'exercise': exercise,
        'description': description,
        'form': form,
        'paragraph': paragraph,
        'paragraph1': paragraph1,
        'paragraph2': paragraph2,
        'options': options,
        'options1': options1,
        'options2': options2,
        'code': code,
        'code1': code1,
        'code2': code2,
        'optionsChange': optionsChange,
        'optionsChange1': optionsChange1,
        'optionsChange2': optionsChange2,
    }

    return {'data': data, 'request': request}


def inverse_string(request, exercise):
    description = 'Dado un string alfanumérico <i>a</i>. Se desea calcular el string inverso de <i>a</i>. Por ejemplo, para <span class="focus-wraper"><span class="outline o1"><i>a</i> = caball0</span><span class="ring r1"></span><span class="stick s1"></span></span> el resultado sería 0llabac.'
    form = forms.palindromeForm()
    paragraph = [
        ['Siguiendo el ejemplo marcado seleccionaremos el <strong>tamaño del problema</strong>:'],
        ['Es un razonamiento vago. Lo que tenemos que elegir es una propiedad de la palabra.', 'Creo que se por dónde vas. Hacerlo en la mitad de tiempo no es logarítmico, es un factor de n.',
            '¡Muy bien! En efecto es la longitud de la palabra la que va a dar el tamaño del problema.'],
        ['A continuación tendremos que elegir el <strong>caso base</strong> que se ajuste al problema.'],
        ['¡Correcto! Un dado que resolver el caso de un string con 0 o ningún carácter es trivial.', '¡En efecto! Sería una opción válida, aunque vamos a mejorar un poco el <strong>caso base</strong>. Te animo aún así a hacer tu idea por tu cuenta y comparar.',
            'Tenemos que comprobar también la cadena vacia.'],
        ['Ahora elegiremos el valor de retorno una vez lleguemos al <strong>caso base</strong>.'],
        ['No es del todo correcto. Sería válido si solo fuese el caso len(a)==0.', '¡Correcto! Lo bueno de devolver el string es que será vacio si es 0 y el string con el caracter si es 1.',
            'No es del todo correcto. Dado que no contemplamos el caso de len(a)==0'],
        ['¿Con un <strong>caso base</strong> es suficiente?'],
        ['No nos hacen falta más casos base. Con uno ya es suficiente.',
            '¡Efectivamente! Ya tenemos todos los casos posibles contemplados.'],
        ['Ahora tendremos que elegir la <strong>descomposición</strong> que usaremos para resolver el ejercicio.'],
        ['¡Correcto! Es una descomposición válida.'],
        ['Ahora introduce unos valores de ejemplo en los recuadros de entrada, el exponente a de ser par. Puedes utilizar el siguiente ejemplo: a = Rat4toill3'],
        ['El <strong>subproblema</strong> se resuelve automáticamente al hacer la llamada recursiva. Queda componer el resultado del mismo con el valor de la descomposición.'],
        ['Muy cerca, el problema es que estarías poniendo el principio al principio y el final al final.', '¡Correcto! Tienes que invertir el orden de los string y estaría resuelto.',
            'El operador ++ es autoincrementar en 1, cuidado no confundirse con append.'],
        ['¡Enhorabuena! Con esto habriamos terminado el ejercicio de potencias.']
    ]

    options = [
        ['<div class="option-content next3">len(palabra)</div> <div class="option-content next1">palabra</div> <div class="option-content next2">log(palabra)</div>'],
        ['<div class="next back">Volver a intentar</div>',
            '<div class="next back">Volver a intentar</div>', '<div class="next next1">Seguir</div>'],
        ['<div class="option-content next1">len(a)<=1</div> <div class="option-content next2">len(a)==0</div> <div class="option-content next3">len(a)==1</div>'],
        ['<div class="next next1">Seguir</div>', '<div class="next next1">Seguir</div>',
            '<div class="next back">Volver a intentar</div>'],
        ['<div class="option-content next1">""</div> <div class="option-content next2">a</div> <div class="option-content next3">a[0]</div>'],
        ['<div class="next back">Volver a intentar</div>', '<div class="next next1">Seguir</div>',
            '<div class="next back">Volver a intentar</div>'],
        ['<div class="option-content next2">Sí</div> <div class="option-content next1">No</div>'],
        ['<div class="next back">Volver a intentar</div>',
            '<div class="next next1">Seguir</div>'],
        ['<div class="option-content hardnext1">Quitar el primer caracter</div> <div class="option-content hardnext2">Quitar el último caracter</div> <div class="option-content next1">Dividir a la mitad</div>'],
        ['<div class="next next1">Seguir</div>'],
        ['<div class="next evaluate">Calcular</div>'],
        ['<div class="option-content next1">particion1 + particion2</div> <div class="option-content next2">particion2 + particion1</div> <div class="option-content next3">particion1 ++ particion2</div>'],
        ['<div class="next back">Volver a intentar</div>', '<div class="next next1">Seguir</div>',
            '<div class="next back">Volver a intentar</div>'],
        ['<div class="next end_exercise">Finalizar ejercicio</div>']
    ]

    code = [
        [''],
        ['', '', 'def invertir_string(a):<br>'],
        [''],
        ['&nbsp&nbsp&nbspif len(a)<=1:<br>',
         '&nbsp&nbsp&nbspif len(a)<=1:<br>'],
        [''],
        ['', '&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn a<br>'],
        [''],
        ['', '&nbsp&nbsp&nbspelse:<br>'],
        [''],
        ['<span class="delete">&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn <span class="step_simpler">invertir_string(<span class="step_subproblem">a[:len(a)]//2]</span>)</span> <span class="step_simpler">invertir_string(<span class="step_subproblem">a[len(a)]//2:]</span>)</span></span>'],
        [''],
        [''],
        ['',
            '&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn <span class="step_solution"><span class="step_simpler">invertir_string(<span class="step_subproblem">a[len(a)]//2:]</span>)</span> + <span class="step_simpler">invertir_string(<span class="step_subproblem">a[:len(a)]//2]</span>)</span></span><br>'],
        ['']
    ]

    '''false no tiene varias opciones (solo continuar o retroceder)
    true tiene varias opciones (a elegir)'''
    optionsChange = [
        True,
        False,
        True,
        False,
        True,
        False,
        True,
        False,
        True,
        False,
        False,
        True,
        False,
        False
    ]

    paragraph1 = [
        ['¡Muy bien! Al quitar el último elemento reducimos el tamaño de la lista.'],
        ['Ahora introduce unos valores de ejemplo en el recuadro de arriba. Puedes utilizar el siguiente ejemplo: a = Rat4toill3'],
        ['El <strong>subproblema</strong> se resuelve automáticamente al hacer la llamada recursiva. Queda componer el resultado del mismo con el valor de la descomposición para el caso par.'],
        ['Casi es correcto. El problema estarías añadiendo el último caracter al principio en vez de al final.', '¡Por supuesto! Solo tenemos que añadirlo al final.',
            '¡Por supuesto! Solo tenemos que añadirlo al final.'],
        ['¡Enhorabuena! Con esto habriamos terminado el ejercicio de potencias.']
    ]

    options1 = [
        ['<div class="next next1">Seguir</div>'],
        ['<div class="next evaluate">Calcular</div>'],
        ['<div class="option-content next2">+ a[0]</div> <div class="option-content next1">a[0] +</div> <div class="option-content next3">.append(a[0])</div>'],
        ['<div class="next back">Volver a intentar</div>', '<div class="next next1">Seguir</div>',
            '<div class="next next1">Seguir</div>'],
        ['<div class="next end_exercise">Finalizar ejercicio</div>']
    ]

    code1 = [
        ['<span class="delete">&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn <span class="step_simpler">invertir_string(<span class="step_subproblem">a[1:]</span>)</span></span>'],
        [''],
        [''],
        ['', '&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn <span class="step_solution"><span class="step_simpler">invertir_string(<span class="step_subproblem">a[1:]</span>)</span> + a[0]</span><br>',
         '&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn <span class="step_solution"><span class="step_simpler">invertir_string(<span class="step_subproblem">a[1:]</span>)</span>.append(a[0])</span><br>'],
        ['']
    ]

    '''false no tiene varias opciones (solo continuar o retroceder)
    true tiene varias opciones (a elegir)'''
    optionsChange1 = [
        False,
        False,
        True,
        False,
        False
    ]

    paragraph2 = [
        ['¡Muy bien! Al quitar el último elemento reducimos el tamaño de la lista.'],
        ['Ahora introduce unos valores de ejemplo en el recuadro de arriba. Puedes utilizar el siguiente ejemplo: a = Rat4toill3'],
        ['El <strong>subproblema</strong> se resuelve automáticamente al hacer la llamada recursiva. Queda componer el resultado del mismo con el valor de la descomposición para el caso par.'],
        ['¡Por supuesto! Solo tenemos que añadirlo al principio.', 'Casi es correcto. El problema estarías añadiendo el primer caracter al final en vez de al principio.',
            'Casi es correcto. El problema estarías añadiendo el primer caracter al final en vez de al principio.'],
        ['¡Enhorabuena! Con esto habriamos terminado el ejercicio de potencias.']
    ]

    options2 = [
        ['<div class="next next1">Seguir</div>'],
        ['<div class="next evaluate">Calcular</div>'],
        ['<div class="option-content next2">+ a[-1]</div> <div class="option-content next1">a[-1] +</div> <div class="option-content next3">.append(a[-1])</div>'],
        ['<div class="next next1">Seguir</div>', '<div class="next back">Volver a intentar</div>',
            '<div class="next back">Volver a intentar</div>'],
        ['<div class="next end_exercise">Finalizar ejercicio</div>']

    ]

    code2 = [
        ['<span class="delete">&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn <span class="step_simpler">invertir_string(<span class="step_subproblem">a[:-1]</span>)</span></span>'],
        [''],
        [''],
        ['&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn <span class="step_solution">a[-1] + <span class="step_simpler">invertir_string(<span class="step_subproblem">a[:-1]</span>)</span></span><br>'],
        ['']
    ]

    '''false no tiene varias opciones (solo continuar o retroceder)
    true tiene varias opciones (a elegir)'''
    optionsChange2 = [
        False,
        False,
        True,
        False,
        False
    ]

    data = {
        'exercise': exercise,
        'description': description,
        'form': form,
        'paragraph': paragraph,
        'paragraph1': paragraph1,
        'paragraph2': paragraph2,
        'options': options,
        'options1': options1,
        'options2': options2,
        'code': code,
        'code1': code1,
        'code2': code2,
        'optionsChange': optionsChange,
        'optionsChange1': optionsChange1,
        'optionsChange2': optionsChange2,
    }

    return {'data': data, 'request': request}


def merge_sort(request, exercise):
    description = 'Dada una lista de enteros no vacia <strong>a</strong>. Se desea ordenar <strong>a</strong>. Por ejemplo para <span class="focus-wraper"><span class="outline o1"><strong>a</strong> = [4, -5, 7]</span><span class="ring r1"></span><span class="stick s1"></span></span> el resultado sería [-5, 4, 7] ya que -5 < 4 < 7.'
    form = forms.listForm()

    paragraph = [
        ['Un último dato antes de empezar. Hay varios algoritmos de ordenación. El algoritmo merge consiste en dividir una lista en partes y combinar el resultado de las divisiones para obtener la lista final.'],
        ['Siguiendo el ejemplo marcado seleccionaremos el <strong>tamaño del problema</strong>:'],
        ['¡Correcto! Lo más habitual al trabajar con listas es usar la longitud para determinar el tamaño del problema.',
            'La a podría ser una solución posible; en muchos lenguajes las listas no son tipos primitivos y es más difícil usarlas en condicionales. Habitualmente se utiliza el tamaño de la lista dado que es más sencillo. ¡Os animo a intentarlo!'],
        ['A continuación tendremos que elegir el <strong>caso base</strong> que se ajuste al problema.'],
        ['Podriamos empezar con este <strong>caso base</strong>, sería correcto, pero vamos a mejorarlo un poco utilizando también el tamaño 1 dado que el valor a devolver es el mismo.', 'Es parcialmente correcto, pero también tenemos que contemplar la lista vacia.',
            '¡Correcto! Este <strong>caso base</strong> contempla ambos valores.'],
        ['Ahora elegiremos el valor de retorno una vez lleguemos al <strong>caso base</strong>.'],
        ['No es del todo correcto. Sería válido si no fuese porque también contemplamos el <strong>caso base</strong> de len(a)==1.', '¡Correcto! Para la lista vacia devuelves una lista vacia y para una lista con un elemento devuelves la lista con el elemento, están ordenadas en ambos casos.',
            'No funcionaria dado que con el <strong>caso base</strong> de la lista vacia daría error en ejecución.'],
        ['¿Con un <strong>caso base</strong> es suficiente?'],
        ['No nos hacen falta más casos base. Con uno ya es suficiente.',
            '¡Efectivamente! Ya tenemos todos los casos posibles contemplados.'],
        ['Ahora tendremos que elegir la <strong>descomposición</strong> que usaremos para resolver el ejercicio.'],
        ['Es una opción correcta, pero no para este algoritmo.', 'Es una opción correcta, pero no para este algoritmo.',
            '¡Correcto! Para el merge sort está es la descomposición, tenemos que dividir la lista en dos partes para ordenar cada una individualmente.'],
        ['Ahora introduce unos valores de ejemplo en los recuadros de entrada, el exponente a de ser par. Puedes utilizar el siguiente ejemplo: a = [-3, 4, 2, -1, 7, 6]'],
        ['El <strong>subproblema</strong> se resuelve automáticamente al hacer la llamada recursiva. Queda componer el resultado del mismo con el valor de la descomposición.'],
        ['No podemos simplemente concatenar, no quedaría ordenado.', '¡Eso es! Lo que tenemos que hacer es mezclar los elementos aunque como están ordenados es relativamente fácil. Se puede hacer tanto iterativa como recursivamente.',
            'Si los invertimos y concatenamos no ganamos tampoco nada porque no estarían tampoco ordenados de mayor a menor.'],
        ['¡Enhorabuena! Con esto habriamos terminado el ejercicio de potencias.']
    ]

    options = [
        ['<div class="next next1">Seguir</div>'],
        ['<div class="option-content next1">len(a)</div> <div class="option-content next2">a</div>'],
        ['<div class="next next1">Seguir</div>',
            '<div class="next back">Volver a intentar</div>'],
        ['<div class="option-content next1">len(a)==0</div> <div class="option-content next2">len(a)==1</div> <div class="option-content next3">len(a)<=1</div>'],
        ['<div class="next next1">Seguir</div>', '<div class="next back">Volver a intentar</div>',
            '<div class="next next1">Seguir</div>'],
        ['<div class="option-content next1">[]</div> <div class="option-content next2">a</div> <div class="option-content next3">a[0]</div>'],
        ['<div class="next back">Volver a intentar</div>', '<div class="next next1">Seguir</div>',
            '<div class="next back">Volver a intentar</div>'],
        ['<div class="option-content next2">Sí</div> <div class="option-content next1">No</div>'],
        ['<div class="next back">Volver a intentar</div>',
            '<div class="next next1">Seguir</div>'],
        ['<div class="option-content next1">Quitar el primer elemento</div> <div class="option-content next2">Quitar el último elemento</div> <div class="option-content next3">Dividir a la mitad</div>'],
        ['<div class="next back">Volver a intentar</div>',
            '<div class="next back">Volver a intentar</div>', '<div class="next next1">Seguir</div>'],
        ['<div class="next evaluate">Calcular</div>'],
        ['<div class="option-content next1">concatenar</div> <div class="option-content next2">mezclar</div> <div class="option-content next3">invertir y concatenar</div>'],
        ['<div class="next back">Volver a intentar</div>', '<div class="next next1">Seguir</div>',
            '<div class="next back">Volver a intentar</div>'],
        ['<div class="next end_exercise">Finalizar ejercicio</div>']
    ]

    code = [
        [''],
        [''],
        ['def merge_sort(a):<br>'],
        [''],
        ['&nbsp&nbsp&nbspif len(a)<=1:<br>', '',
         '&nbsp&nbsp&nbspif len(a)<=1:<br>'],
        [''],
        ['', '&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn a<br>', ''],
        [''],
        ['', '&nbsp&nbsp&nbspelse:<br>'],
        [''],
        ['', '',
            '<span class="delete">&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn <span class="step_simpler">merge_sort(<span class="step_subproblem">a[:len(a)]//2]</span>)</span> <span class="step_simpler">merge_sort(<span class="step_subproblem">a[len(a)]//2:]</span>)</span></span>'],
        [''],
        [''],
        ['',
            '&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn <span class="step_solution">mezclar(<span class="step_simpler">merge_sort(<span class="step_subproblem">a[:len(a)]//2]</span>)</span>, <span class="step_simpler">merge_sort(<span class="step_subproblem">a[len(a)]//2:]</span>)</span>)</span><br>'],
        ['']
    ]

    '''false no tiene varias opciones (solo continuar o retroceder)
    true tiene varias opciones (a elegir)'''
    optionsChange = [
        False,
        True,
        False,
        True,
        False,
        True,
        False,
        True,
        False,
        True,
        False,
        False,
        True,
        False,
        False
    ]

    data = {
        'exercise': exercise,
        'description': description,
        'form': form,
        'paragraph': paragraph,
        'options': options,
        'code': code,
        'optionsChange': optionsChange,
    }

    return {'data': data, 'request': request}


def insert_sort(request, exercise):
    description = 'Dada una lista de enteros no vacia <strong>a</strong>. Se desea ordenar <strong>a</strong>. Por ejemplo para <span class="focus-wraper"><span class="outline o1"><strong>a</strong> = [4, -5, 7]</span><span class="ring r1"></span><span class="stick s1"></span></span> el resultado sería [-5, 4, 7] ya que -5 < 4 < 7.'
    form = forms.listForm()

    paragraph = [
        ['Un último dato antes de empezar. Hay varios algoritmos de ordenación. El algoritmo insert consiste en ir intercambiando la posición del elemento x con los anteriores hasta encontrar uno que sea menor o llegar al principio de la lista.'],
        ['Siguiendo el ejemplo marcado seleccionaremos el <strong>tamaño del problema</strong>:'],
        ['¡Correcto! Lo más habitual al trabajar con listas es usar la longitud para determinar el tamaño del problema.',
            'La a podría ser una solución posible; en muchos lenguajes las listas no son tipos primitivos y es más difícil usarlas en condicionales. Habitualmente se utiliza el tamaño de la lista dado que es más sencillo. ¡Os animo a intentarlo!'],
        ['A continuación tendremos que elegir el <strong>caso base</strong> que se ajuste al problema.'],
        ['Podriamos empezar con este <strong>caso base</strong>, sería correcto, pero vamos a mejorarlo un poco utilizando también el tamaño 1 dado que el valor a devolver es el mismo.', 'Es parcialmente correcto, pero también tenemos que contemplar la lista vacia.',
            '¡Correcto! Este <strong>caso base</strong> contempla ambos valores.'],
        ['Ahora elegiremos el valor de retorno una vez lleguemos al <strong>caso base</strong>.'],
        ['No es del todo correcto. Sería válido si no fuese porque también contemplamos el <strong>caso base</strong> de len(a)==1.', '¡Correcto! Para la lista vacia devuelves una lista vacia y para una lista con un elemento devuelves la lista con el elemento, están ordenadas en ambos casos.',
            'No funcionaria dado que con el <strong>caso base</strong> de la lista vacia daría error en ejecución.'],
        ['¿Con un <strong>caso base</strong> es suficiente?'],
        ['No nos hacen falta más casos base. Con uno ya es suficiente.',
            '¡Efectivamente! Ya tenemos todos los casos posibles contemplados.'],
        ['Ahora tendremos que elegir la <strong>descomposición</strong> que usaremos para resolver el ejercicio.'],
        ['Es una opción correcta, pero no para este algoritmo.', '¡Correcto! Para el insert sort está es la descomposición. Aunque parecería que lo estamos haciendo al contrario tenemos que recordar que estamos haciendo el último paso, no el primero.',
            'Es una opción correcta, pero no para este algoritmo.'],
        ['Ahora introduce unos valores de ejemplo en los recuadros de entrada, el exponente a de ser par. Puedes utilizar el siguiente ejemplo: a = [-3, 4, 2, -1, 7, 6]'],
        ['El <strong>subproblema</strong> se resuelve automáticamente al hacer la llamada recursiva. Queda componer el resultado del mismo con el valor de la descomposición.'],
        ['¡Eso es! Ir comparando con el anterior e intercambiar si es más grande hasta llegar a uno más pequeño o hasta el principio de la lista. Esto se puede hacer porque ya está ordenado la lista.', 'La lista ya está ordenada, no necesitamos invertirla.',
            'No hay que invertir la lista, ya está ordenada. Además simplemente hacer un append no indica que el elemento vaya a ser el más pequeño, podría ser uno intermedio.'],
        ['¡Enhorabuena! Con esto habriamos terminado el ejercicio de potencias.']
    ]

    options = [
        ['<div class="next next1">Seguir</div>'],
        ['<div class="option-content next1">len(a)</div> <div class="option-content next2">a</div>'],
        ['<div class="next next1">Seguir</div>',
            '<div class="next back">Volver a intentar</div>'],
        ['<div class="option-content next1">len(a)==0</div> <div class="option-content next2">len(a)==1</div> <div class="option-content next3">len(a)<=1</div>'],
        ['<div class="next next1">Seguir</div>', '<div class="next back">Volver a intentar</div>',
            '<div class="next next1">Seguir</div>'],
        ['<div class="option-content next1">[]</div> <div class="option-content next2">a</div> <div class="option-content next3">a[0]</div>'],
        ['<div class="next back">Volver a intentar</div>', '<div class="next next1">Seguir</div>',
            '<div class="next back">Volver a intentar</div>'],
        ['<div class="option-content next2">Sí</div> <div class="option-content next1">No</div>'],
        ['<div class="next back">Volver a intentar</div>',
            '<div class="next next1">Seguir</div>'],
        ['<div class="option-content next1">Quitar el primer elemento</div> <div class="option-content next2">Quitar el último elemento</div> <div class="option-content next3">Dividir a la mitad</div>'],
        ['<div class="next back">Volver a intentar</div>', '<div class="next next1">Seguir</div>',
            '<div class="next back">Volver a intentar</div>'],
        ['<div class="next evaluate">Calcular</div>'],
        ['<div class="option-content next1">comparar y colocar</div> <div class="option-content next2">invertir y colocar</div> <div class="option-content next3">invertir y concatenar</div>'],
        ['<div class="next next1">Seguir</div>', '<div class="next back">Volver a intentar</div>',
            '<div class="next back">Volver a intentar</div>'],
        ['<div class="next end_exercise">Finalizar ejercicio</div>']
    ]

    code = [
        [''],
        [''],
        ['def insert_sort(a):<br>'],
        [''],
        ['&nbsp&nbsp&nbspif len(a)<=1:<br>', '',
         '&nbsp&nbsp&nbspif len(a)<=1:<br>'],
        [''],
        ['', '&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn a<br>', ''],
        [''],
        ['', '&nbsp&nbsp&nbspelse:<br>'],
        [''],
        ['',
            '<span class="delete">&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn <span class="step_simpler">insert_sort(<span class="step_subproblem">a[:-1]</span>)</span></span>'],
        [''],
        [''],
        ['&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn <span class="step_solution">colocar(a[-1], <span class="step_simpler">insert_sort(<span class="step_subproblem">a[:-1]</span>)</span>)</span><br>'],
        ['']
    ]

    '''false no tiene varias opciones (solo continuar o retroceder)
    true tiene varias opciones (a elegir)'''
    optionsChange = [
        False,
        True,
        False,
        True,
        False,
        True,
        False,
        True,
        False,
        True,
        False,
        False,
        True,
        False,
        False
    ]

    data = {
        'exercise': exercise,
        'description': description,
        'form': form,
        'paragraph': paragraph,
        'options': options,
        'code': code,
        'optionsChange': optionsChange,
    }

    return {'data': data, 'request': request}


def quick_sort(request, exercise):
    description = 'Dada una lista de enteros no vacia <strong>a</strong>. Se desea ordenar <strong>a</strong>. Por ejemplo para <span class="focus-wraper"><span class="outline o1"><strong>a</strong> = [4, -5, 7]</span><span class="ring r1"></span><span class="stick s1"></span></span> el resultado sería [-5, 4, 7] ya que -5 < 4 < 7.'
    form = forms.listForm()

    paragraph = [
        ['Un último dato antes de empezar. Hay varios algoritmos de ordenación. El algoritmo quick consiste en elegir un pivote y colocar los elementos menores a la izquierda y los mayores a la derecha.'],
        ['Siguiendo el ejemplo marcado seleccionaremos el <strong>tamaño del problema</strong>:'],
        ['¡Correcto! Lo más habitual al trabajar con listas es usar la longitud para determinar el tamaño del problema. Además dado que vamos a usar la partición de Hoare necesitamos unos índices, pero como no debe pasarlos la persona lo haremos internamente.',
            'La a podría ser una solución posible; en muchos lenguajes las listas no son tipos primitivos y es más difícil usarlas en condicionales. Habitualmente se utiliza el tamaño de la lista dado que es más sencillo. ¡Os animo a intentarlo!'],
        ['A continuación tendremos que elegir el <strong>caso base</strong> que se ajuste al problema.'],
        ['Podriamos empezar con este <strong>caso base</strong>, sería correcto, aunque sería más interesante mejorarlo un poco utilizando también el tamaño 1 dado que el valor a devolver es el mismo.', 'Es una opción correcta, pero no para la partición Hoare.',
            '¡Correcto! Para la partición hoare vamos a utilizar un inicio y un final, solo vamos a trabajar mientras sea no se crucen los indices, tampoco vamos a devolver nada como tal porque vamos a trabajar sobre la propia lista.'],
        ['Para la <strong>descomposición</strong> vamos a usar la partición Hoare. Con los índices inicio y fin iremos buscando un par de elementos mayor y menor que el pivote en los lados incorrectos y los cambiaremos, haremos esto hasta que se crucen. Te animo a hacer el algoritmo por tu cuenta'],
        ['Ahora introduce unos valores de ejemplo en los recuadros de entrada, el exponente a de ser par. Puedes utilizar el siguiente ejemplo: a = [-3, 4, 2, -1, 7, 6]'],
        ['El <strong>subproblema</strong> se resuelve automáticamente al hacer la llamada recursiva. Queda componer el resultado del mismo con el valor de la descomposición.'],
        ['¡Eso es! La partición Hoare actua directamente sobre la propia lista por lo que no tenemos que hacer nada y la lista ya estará ordenada.', 'Es una buena idea, pero dado que trabajamos sobre la lista porque solo devolvemos el pivote no funcionaría. Pero se puede hacer ¡Te animo a intentarlo!.',
            'Es una buena idea, pero dado que trabajamos sobre la lista porque solo devolvemos el pivote no funcionaría. Pero se puede hacer ¡Te animo a intentarlo!.'],
        ['¡Enhorabuena! Con esto habriamos terminado el ejercicio de potencias.']
    ]

    options = [
        ['<div class="next next1">Seguir</div>'],
        ['<div class="option-content next1">len(a)</div> <div class="option-content next2">a</div>'],
        ['<div class="next next1">Seguir</div>',
            '<div class="next back">Volver a intentar</div>'],
        ['<div class="option-content next1">len(a)==0</div> <div class="option-content next2">len(a)<=1</div> <div class="option-content next3">ini < fin</div>'],
        ['<div class="next next1">Seguir</div>', '<div class="next back">Volver a intentar</div>',
            '<div class="next next1">Seguir</div>'],
        ['<div class="next next1">Seguir</div>'],
        ['<div class="next evaluate">Calcular</div>'],
        ['<div class="option-content next1">No hacer nada</div> <div class="option-content next2">concatenar</div> <div class="option-content next3">concatenar con el pivote en medio</div>'],
        ['<div class="next next1">Seguir</div>', '<div class="next back">Volver a intentar</div>',
            '<div class="next back">Volver a intentar</div>'],
        ['<div class="next end_exercise">Finalizar ejercicio</div>']
    ]

    code = [
        [''],
        [''],
        ['def quick_sort(a):<br>&nbsp&nbsp&nbspquick_sort_index(a, 0, len(a) - 1)<br><br>def quick_sort_index(a, ini, fin):<br>'],
        [''],
        ['', '', '&nbsp&nbsp&nbspif ini < fin:<br>'],
        ['&nbsp&nbsp&nbsp&nbsp&nbsp&nbspindice_pivote = particion_hoare(a, ini, fin)'],
        [''],
        [''],
        ['<span class="step_solution">&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<span class="step_simpler">quick_sort_index(<span class="step_subproblem">a, ini, indice_pivote - 1</span>)</span><br>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<span class="step_simpler">quick_sort_index(<span class="step_subproblem">a, indice_pivote + 1, fin</span>)</span></span>'],
        ['']
    ]

    '''false no tiene varias opciones (solo continuar o retroceder)
    true tiene varias opciones (a elegir)'''
    optionsChange = [
        False,
        True,
        False,
        True,
        False,
        False,
        False,
        True,
        False,
        False
    ]

    data = {
        'exercise': exercise,
        'description': description,
        'form': form,
        'paragraph': paragraph,
        'options': options,
        'code': code,
        'optionsChange': optionsChange,
    }

    return {'data': data, 'request': request}


def select_sort(request, exercise):
    description = 'Dada una lista de enteros no vacia <strong>a</strong>. Se desea ordenar <strong>a</strong>. Por ejemplo para <span class="focus-wraper"><span class="outline o1"><strong>a</strong> = [4, -5, 7]</span><span class="ring r1"></span><span class="stick s1"></span></span> el resultado sería [-5, 4, 7] ya que -5 < 4 < 7.'
    form = forms.listForm()

    paragraph = [
        ['Un último dato antes de empezar. Hay varios algoritmos de ordenación. El algoritmo select consiste en ir intercambiar la posición del primero con el menor de la lista e ir haciendolo consecutivamente con el segundo, tercero,... hasta llegar al final.'],
        ['Siguiendo el ejemplo marcado seleccionaremos el <strong>tamaño del problema</strong>:'],
        ['¡Correcto! Lo más habitual al trabajar con listas es usar la longitud para determinar el tamaño del problema.',
            'La a podría ser una solución posible; en muchos lenguajes las listas no son tipos primitivos y es más difícil usarlas en condicionales. Habitualmente se utiliza el tamaño de la lista dado que es más sencillo. ¡Os animo a intentarlo!'],
        ['A continuación tendremos que elegir el <strong>caso base</strong> que se ajuste al problema.'],
        ['Podriamos empezar con este <strong>caso base</strong>, sería correcto, pero vamos a mejorarlo un poco utilizando también el tamaño 1 dado que el valor a devolver es el mismo.', 'Es parcialmente correcto, pero también tenemos que contemplar la lista vacia.',
            '¡Correcto! Este <strong>caso base</strong> contempla ambos valores.'],
        ['Ahora elegiremos el valor de retorno una vez lleguemos al <strong>caso base</strong>.'],
        ['No es del todo correcto. Sería válido si no fuese porque también contemplamos el <strong>caso base</strong> de len(a)==1.', '¡Correcto! Para la lista vacia devuelves una lista vacia y para una lista con un elemento devuelves la lista con el elemento, están ordenadas en ambos casos.',
            'No funcionaria dado que con el <strong>caso base</strong> de la lista vacia daría error en ejecución.'],
        ['¿Con un <strong>caso base</strong> es suficiente?'],
        ['No nos hacen falta más casos base. Con uno ya es suficiente.',
            '¡Efectivamente! Ya tenemos todos los casos posibles contemplados.'],
        ['Ahora tendremos que elegir la <strong>descomposición</strong> que usaremos para resolver el ejercicio.'],
        ['Es una opción correcta, pero no para este algoritmo.', 'Es una opción correcta, pero no para este algoritmo.',
            '¡Correcto! Lo que tenemos que hacer es encontrar el mínimo de la lista y sacarlo de la misma, también se puede hacer sin modificar si lo intercambiamos.'],
        ['Ahora introduce unos valores de ejemplo en los recuadros de entrada, el exponente a de ser par. Puedes utilizar el siguiente ejemplo: a = [-3, 4, 2, -1, 7, 6]'],
        ['El <strong>subproblema</strong> se resuelve automáticamente al hacer la llamada recursiva. Queda componer el resultado del mismo con el valor de la descomposición.'],
        ['Parte es correcta, pero no nos hace falta comparar porque sabemos que es el mínimo.', 'No hace falta recorrer la lista, sabemos que el que tenemos es el más pequeño y está ordenada la lista.',
            '¡Correcto! Dado que es el mínimo y la lista está ya ordenada solo nos hace falta colocarlo al principio.'],
        ['¡Enhorabuena! Con esto habriamos terminado el ejercicio de potencias.']
    ]

    options = [
        ['<div class="next next1">Seguir</div>'],
        ['<div class="option-content next1">len(a)</div> <div class="option-content next2">a</div>'],
        ['<div class="next next1">Seguir</div>',
            '<div class="next back">Volver a intentar</div>'],
        ['<div class="option-content next1">len(a)==0</div> <div class="option-content next2">len(a)==1</div> <div class="option-content next3">len(a)<=1</div>'],
        ['<div class="next next1">Seguir</div>', '<div class="next back">Volver a intentar</div>',
            '<div class="next next1">Seguir</div>'],
        ['<div class="option-content next1">[]</div> <div class="option-content next2">a</div> <div class="option-content next3">a[0]</div>'],
        ['<div class="next back">Volver a intentar</div>', '<div class="next next1">Seguir</div>',
            '<div class="next back">Volver a intentar</div>'],
        ['<div class="option-content next2">Sí</div> <div class="option-content next1">No</div>'],
        ['<div class="next back">Volver a intentar</div>',
            '<div class="next next1">Seguir</div>'],
        ['<div class="option-content next1">Quitar el primer elemento</div> <div class="option-content next2">Quitar el último elemento</div> <div class="option-content next3">Quitar el mínimo</div>'],
        ['<div class="next back">Volver a intentar</div>',
            '<div class="next back">Volver a intentar</div>', '<div class="next next1">Seguir</div>'],
        ['<div class="next evaluate">Calcular</div>'],
        ['<div class="option-content next1">comparar y colocar</div> <div class="option-content next2">recorrer y colocar</div> <div class="option-content next3">añadir al principio</div>'],
        ['<div class="next back">Volver a intentar</div>', '<div class="next back">Volver a intentar</div>',
            '<div class="next next1">Seguir</div>'],
        ['<div class="next end_exercise">Finalizar ejercicio</div>']
    ]

    code = [
        [''],
        [''],
        ['def select_sort(a):<br>'],
        [''],
        ['&nbsp&nbsp&nbspif len(a)<=1:<br>', '',
         '&nbsp&nbsp&nbspif len(a)<=1:<br>'],
        [''],
        ['', '&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn a<br>', ''],
        [''],
        ['', '&nbsp&nbsp&nbspelse:<br>'],
        [''],
        ['', '',
            '&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<span class="step_subproblem">a.remove(min(a))</span><br><span class="delete">&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn <span class="step_simpler">select_sort(<span class="step_subproblem">a</span>)</span></span>'],
        [''],
        [''],
        ['', '',
            '&nbsp&nbsp&nbsp&nbsp&nbsp&nbspreturn <span class="step_solution">[min(a)] + <span class="step_simpler">select_sort(<span class="step_subproblem">a</span>)</span>'],
        ['']
    ]

    '''false no tiene varias opciones (solo continuar o retroceder)
    true tiene varias opciones (a elegir)'''
    optionsChange = [
        False,
        True,
        False,
        True,
        False,
        True,
        False,
        True,
        False,
        True,
        False,
        False,
        True,
        False,
        False
    ]

    data = {
        'exercise': exercise,
        'description': description,
        'form': form,
        'paragraph': paragraph,
        'options': options,
        'code': code,
        'optionsChange': optionsChange,
    }

    return {'data': data, 'request': request}
