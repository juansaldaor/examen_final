# examen_final
# Explicación del Código de Traducción a Binario

## Estructura del Programa

El código proporciona una interfaz de línea de comandos para traducir caracteres o palabras a su representación binaria. Está compuesto por varias funciones y un menú de selección.

## Funciones

### 1. `char_to_binary(char)`

Esta función toma un carácter como entrada, calcula su valor ASCII y devuelve tanto el valor ASCII como la representación binaria de 8 bits de ese carácter.

### 2. `word_to_binary(word)`

Esta función toma una palabra como entrada, itera sobre cada carácter de la palabra y utiliza la función `char_to_binary` para obtener la representación binaria de cada carácter. Muestra en la consola el valor ASCII y la representación binaria de cada carácter. Luego, devuelve la representación binaria de toda la palabra.

### 3. `get_results(word)`

Esta función simplemente llama a `word_to_binary` con la palabra proporcionada y devuelve el resultado.

## Flujo Principal del Programa

1. El programa solicita al usuario que elija entre traducir un carácter o una palabra mediante un menú.

2. Si elige traducir un carácter (`menu == 1`), el programa solicita al usuario que ingrese un solo carácter y asigna esa letra a la variable `char`. Luego, la variable `word` se establece igual a `char`.

3. Si elige traducir una palabra (`menu == 2`), el programa solicita al usuario que ingrese una palabra y asigna esa palabra a la variable `word`.

4. Si elige una opción no válida, el programa se cierra.

5. Luego, el programa muestra los resultados llamando a `get_results` con la palabra proporcionada.

6. Finalmente, muestra en la consola el resultado, que es la representación binaria de la letra o palabra ingresada.

## Uso del Código

El usuario interactúa con el programa ingresando su elección y los datos correspondientes, y el programa devuelve la traducción a binario junto con el valor ASCII de cada carácter.

