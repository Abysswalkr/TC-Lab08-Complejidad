# Laboratorio 8 – Complejidad (Teoría de la Computación)

## Resumen del laboratorio

Implementamos y perfilamos tres fragmentos de código (P1–P3), y resolvimos por escrito los análisis de complejidad (P1.a, P2.a, P3.a), así como el **Problema 4** (mejor/promedio/peor caso para búsquedas y ordenamiento) y el **Problema 5** (V/F con justificación).

## Estructura del repositorio

```
TC-LAB08-Complejidad/
├─ Problem 1/
│  ├─ problem1.py        # Implementación del fragmento P1 (Parte b)
│  └─ profile_p1.py      # Perfilador: imprime tabla y guarda p1_demo.png
├─ Problem 2/
│  ├─ problem2.py
│  └─ profile_p2.py      # Guarda p2_demo.png en esta misma carpeta
├─ Problem 3/
│  ├─ problem3.py
│  └─ profile_p3.py      # Guarda p3_demo.png en esta misma carpeta
└─ Escritos/             
```

## Requisitos

* Python 3.9+ (probado con 3.12)
* `matplotlib`

  ```
  py -m pip install matplotlib
  ```

## Cómo ejecutar (Windows PowerShell)

> Nota: las carpetas tienen espacio en el nombre; usa comillas o escape con backtick.

```
# P1
python ".\Problem 1\profile_p1.py"

# P2
python ".\Problem 2\profile_p2.py"

# P3
python ".\Problem 3\profile_p3.py"
```

* Cada script imprime una **tabla** CSV-like en consola: `n,tiempo_seg,ops_estimado,estado`.
* Para guardar la tabla a CSV:

  ```
  python ".\Problem 2\profile_p2.py" > ".\Problem 2\p2_times.csv"
  ```
* Cada script guarda una **gráfica** en su propia carpeta:

  * `.\Problem 1\p1_demo.png`
  * `.\Problem 2\p2_demo.png`
  * `.\Problem 3\p3_demo.png`

## Notas de ejecución y rendimiento

* P1 y P3 pueden ser costosos. Dejamos un “**salto seguro**” que marca `SKIPPED` cuando la **estimación** de operaciones supera un umbral:

  * `profile_p1.py`: `safe_skip=True, max_ops=5e7`
  * `profile_p3.py`: `safe_skip=True, max_ops=2e7`
* Si se requiere **forzar todos los n** (incluidos 10^5 y 10^6), ajusta a `safe_skip=False` (puede tardar mucho).

---

## Resultados (resumen)

### Complejidades teóricas (Partes a)

* **P1.a:**
  Conteos exactos: (#i=n-\lfloor n/2\rfloor+1,\ #j=\lceil n/2\rceil,\ #k=\lfloor\log_2 n\rfloor+1).
  Total: (T(n)=\Theta(n^2\log n)).

* **P2.a:**
  Bucle interno rompe con `break` → 1 iteración por cada (i).
  Total: (T(n)=\Theta(n)).

* **P3.a:**
  (#i=\lfloor n/3\rfloor,\ #j=\lceil n/4\rceil).
  Total: (T(n)=\Theta(n^2)).

### Medidas empíricas (Partes b)

* **P1 (≈ (n^2\log n))**: tiempos crecen rápido; con el umbral activado se **omite** desde (n=10^4) en adelante (`SKIPPED`).
  Gráfica: `p1_demo.png` (crece casi lineal en eje y vs n en el rango medido, coherente con la forma superlineal).

* **P2 (≈ (n))**: corre para todos los n hasta (10^6); tiempos aumentan de forma proporcional; `p2_demo.png`.

* **P3 (≈ (n^2))**: se **omite** desde (n=10^5) por seguridad; `p3_demo.png` muestra crecimiento cuadrático en el rango medido.

### Problema 4 (mejor/promedio/peor)

* **Búsqueda Lineal**:
  Mejor (\Theta(1)), Promedio (\Theta(n)), Peor (\Theta(n)).
* **Búsqueda Binaria** (arreglo ordenado):
  Mejor (\Theta(1)), Promedio (\Theta(\log n)), Peor (\Theta(\log n)).
* **Quick Sort**:
  Mejor (\Theta(n\log n)), Promedio (\Theta(n\log n)), Peor (\Theta(n^2)).

### Problema 5 (V/F con justificación)

* **5.a** Verdadero: (\Theta) es transitiva y simétrica → (h(n)=\Theta(f(n))).
* **5.b** Verdadero: de (f=O(g)) y (g=O(h)) se deduce (f=O(h)), equivalente a (h=\Omega(f)).
* **5.c** Falso: el programa inserta sub-tuplas de longitud (k) con costo (O(k)) por par ((i,j)).
  (\sum (j-i) = \Theta(n^3)) ⇒ (f(n)=\Theta(n^3)).
