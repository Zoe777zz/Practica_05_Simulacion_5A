"""Compara las secuencias CSV creadas por Python y Java."""

import csv
from pathlib import Path

CARPETA = Path(__file__).parent / "salidas"


def leer(nombre):
    with open(CARPETA / nombre, newline="", encoding="utf-8") as archivo:
        return list(csv.DictReader(archivo))


def main():
    python = leer("secuencia_python.csv")
    java = leer("secuencia_java.csv")
    iguales = len(python) == len(java) == 10000 and all(
        a["Xn"] == b["Xn"] and a["Un"] == b["Un"]
        for a, b in zip(python, java)
    )

    with open(CARPETA / "comparacion_20.csv", "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["n", "Xn Python", "Xn Java", "Un Python", "Un Java", "Iguales"])
        for a, b in zip(python[:20], java[:20]):
            escritor.writerow([
                a["n"], a["Xn"], b["Xn"], a["Un"], b["Un"],
                "Si" if a["Xn"] == b["Xn"] and a["Un"] == b["Un"] else "No"
            ])

    print("COMPARACION DE LOS PRIMEROS 20 VALORES")
    print("n   Xn Python      Xn Java       Coinciden")
    for a, b in zip(python[:20], java[:20]):
        print(f"{a['n']:>2}  {a['Xn']:>12}   {b['Xn']:>12}     {'Si' if a == b else 'No'}")
    print(f"\nTotal comparado: {len(python)} valores")
    print("Resultado:", "COINCIDEN LOS 10 000" if iguales else "HAY DIFERENCIAS")

    python_otro = leer("secuencia_python_otra_semilla.csv")
    java_otro = leer("secuencia_java_otra_semilla.csv")
    otra_igual = len(python_otro) == len(java_otro) == 10000 and python_otro == java_otro
    semillas_diferentes = python != python_otro
    print("Otra semilla: Python y Java coinciden:", "Si" if otra_igual else "No")
    print("La nueva semilla cambia la secuencia:", "Si" if semillas_diferentes else "No")
    if not (iguales and otra_igual and semillas_diferentes):
        raise SystemExit("La verificacion no se completo correctamente.")


if __name__ == "__main__":
    main()
