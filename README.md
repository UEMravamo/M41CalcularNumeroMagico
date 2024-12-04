# Calcular Numero Mágico
 
Un número tuentístico es cualquier número que, al escribirse en inglés, contenga la palabra "twenty" (por ejemplo, 20, 21 o 120000). Como en Tuenti amamos los números tuentísticos, nos gusta representar cualquier número no tuentístico como una suma de números tuentísticos positivos para aumentar su tuentísticidad (a esto lo llamamos una suma tuentística). Por ejemplo, el número no tuentístico 50 puede representarse como la suma tuentística 25 + 25. Los propios números tuentísticos también cuentan como sumas tuentísticas. 

Dado un número positivo, queremos saber el número máximo de elementos que puede tener una de sus sumas tuentísticas.

## Entrada
La primera línea contiene el número de casos, **C**. Luego, siguen **C** líneas, cada una con un número **N**. 


## Salida 

Para cada caso, imprime Case #X: M, donde **X** es el número del caso (el primer caso tiene el número 1) y **M** es el número máximo de elementos en una suma tuentística de **N**. Si no es posible representar N como una suma tuentística, imprime Case #X: IMPOSSIBLE. 


## Límites 

* 1≤C≤500
* 1≤N≤262

## Ejemplo de Entrada: 

3   
20   
80   
35   
 
## Ejemplo de Salida: 

Case #1: 1   
Case #2: 4   
Case #3: IMPOSSIBLE   


---

## Requisitos

- Usa Python 3.7.
- Escribe código conforme a PEP8.
- Escribe algunas pruebas (considera usar pytest o uniitest).
- Documenta tu solución en un archivo
