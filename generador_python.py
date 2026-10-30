"""Practica 05: generador congruencial lineal en Python."""

import csv
from pathlib import Path

import matplotlib.pyplot as plt

# Parametros de la guia
MULTIPLICADOR = 1664525
INCREMENTO = 1013904223
MODULO = 2**32
CANTIDAD = 10000
SEMILLA = 12345
OTRA_SEMILLA = 54321

CARPETA = Path(__file__).parent / "salidas"


def generar(semilla, cantidad):
    """Devuelve pares (Xn, Un) con el metodo LCG."""
    numero = semilla
    datos = []
    for _ in range(cantidad):
        numero = (MULTIPLICADOR * numero + INCREMENTO) % MODULO
        datos.append((numero, numero / MODULO))
    return datos


def guardar_csv(ruta, datos):
    with open(ruta, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["n", "Xn", "Un"])
        for indice, (numero, valor) in enumerate(datos, start=1):
            escritor.writerow([indice, numero, f"{valor:.10f}"])


def graficar(datos, otros):
    # Se muestran 200 valores para que la secuencia se lea claramente.
    cantidad_grafica = 200
    posiciones = list(range(1, cantidad_grafica + 1))
    plt.figure(figsize=(9, 4))
    plt.plot(posiciones, [u for _, u in datos[:cantidad_grafica]], ".", markersize=4, label="Semilla 12345")
    plt.plot(posiciones, [u for _, u in otros[:cantidad_grafica]], ".", markersize=4, alpha=0.55, label="Semilla 54321")
    plt.title("Secuencia LCG: primeras 200 observaciones")
    plt.xlabel("Observacion")
    plt.ylabel("Un")
    plt.ylim(0, 1)
    plt.legend()
    plt.grid(alpha=0.2)
    plt.tight_layout()
    plt.savefig(CARPETA / "grafica_secuencias.png", dpi=170)
    plt.close()

    plt.figure(figsize=(9, 4))
    plt.hist([u for _, u in datos], bins=20, edgecolor="white")
    plt.title("Distribucion de 10 000 valores normalizados")
    plt.xlabel("Intervalos de Un")
    plt.ylabel("Frecuencia")
    plt.tight_layout()
    plt.savefig(CARPETA / "histograma.png", dpi=170)
    plt.close()


def main():
    CARPETA.mkdir(exist_ok=True)
    datos = generar(SEMILLA, CANTIDAD)
    otros = generar(OTRA_SEMILLA, CANTIDAD)
    guardar_csv(CARPETA / "secuencia_python.csv", datos)
    guardar_csv(CARPETA / "secuencia_python_otra_semilla.csv", otros)
    graficar(datos, otros)

    print("PYTHON - Primeros 20 valores (semilla 12345)")
    print("n       Xn            Un")
    for indice, (numero, valor) in enumerate(datos[:20], start=1):
        print(f"{indice:<3} {numero:>12}   {valor:.10f}")
    print("\nSe generaron 10 000 valores por semilla.")
    print("CSV y graficas guardadas en la carpeta salidas/.")


if __name__ == "__main__":
    main()
