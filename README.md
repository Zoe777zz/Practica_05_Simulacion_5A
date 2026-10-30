# Practica 05 - Generador Congruencial Lineal (LCG)

Dos implementaciones simples del mismo generador: Python y Java.

## Parametros

- Multiplicador `a = 1664525`
- Incremento `c = 1013904223`
- Modulo `m = 2^32 = 4294967296`
- Semillas `12345` y `54321` (esta ultima se usa para comparar)
- Cantidad `10000` por semilla

Formula: `X(n+1) = (a * X(n) + c) % m`, `Un = Xn / m`.
El primer valor guardado es **X1**, calculado desde la semilla X0.

## Ejecucion en Ubuntu

Desde la carpeta del proyecto:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 generador_python.py
javac GeneradorJava.java
java GeneradorJava
python3 comparar.py
```

**Resultados:** se guardan en `salidas/`. Incluyen los CSV de ambas semillas, la comparacion de 20 filas y dos graficas en PNG. La comparacion comprueba las 10000 observaciones (no solo las 20 de la tabla).

**Nota:** Los codigos son independientes. Java no necesita librerias externas; Matplotlib solo se utiliza en Python para dibujar las graficas.

## Periodo

El periodo teorico maximo es `2^32 = 4294967296` valores. La condicion se verifica por el criterio de Hull-Dobell: `c` es impar y coprimo con `m`; `a-1 = 1664524` es multiplo de `2` y de `4`. No es necesario generar los 4294967296 valores para fundamentar ese resultado. Los 10000 valores son una muestra, no una comprobacion experimental del ciclo completo.

## Estructura

- `generador_python.py`: genera CSV y graficas.
- `GeneradorJava.java`: genera CSV en Java.
- `comparar.py`: compara ambos lenguajes y las dos semillas.
- `salidas/`: resultados obtenidos en una ejecucion de prueba.
