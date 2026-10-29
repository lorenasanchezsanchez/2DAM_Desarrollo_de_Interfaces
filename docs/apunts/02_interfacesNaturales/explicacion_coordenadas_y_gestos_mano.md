# ¿Qué gesto hace la mano? — Explicación del código y de las coordenadas

## 1. ¿Qué intenta hacer este programa?

El objetivo del ejercicio es analizar las coordenadas de una mano y decidir qué gesto está haciendo. Por ejemplo:

- **PUÑO**: ningún dedo está extendido.
- **MANO ABIERTA**: los cinco dedos están extendidos.
- **VICTORIA**: están extendidos el índice y el corazón.
- **SEÑALAR**: solo está extendido el índice.
- **PULGAR**: solo está extendido el pulgar.
- **PINZA**: la punta del pulgar está muy cerca de la punta del índice.
- **DESCONOCIDO**: no coincide con ninguno de los casos anteriores.

El ejercicio utiliza coordenadas de ejemplo escritas en la entrada del programa. No está detectando una mano real con la cámara. En una aplicación real, una herramienta de visión artificial —por ejemplo, MediaPipe Hands o ML Kit— podría detectar puntos de la mano y proporcionar sus coordenadas.

## 2. ¿Qué son los puntos de referencia o *landmarks*?

Un detector de manos puede identificar varios puntos importantes de la mano, llamados *landmarks*. En el enunciado se indica que algunos sistemas detectan 21 puntos. Para simplificar el ejercicio, se trabaja con 11 puntos por mano:

- La muñeca.
- La punta de cada uno de los cinco dedos.
- Una articulación intermedia de cada dedo.

Cada punto tiene dos coordenadas: `x` e `y`.

Por ejemplo:

```text
muneca 0.50 0.80
indice_punta 0.48 0.20
indice_medio 0.49 0.45
```

Cada línea contiene tres elementos:

1. El nombre del punto: `muneca`, `indice_punta`, etc.
2. Su coordenada `x`.
3. Su coordenada `y`.

Los valores están normalizados entre `0` y `1`, en lugar de expresarse en píxeles.

## 3. ¿Cómo funcionan las coordenadas `x` e `y`?

Imagina una imagen de la cámara dividida en una cuadrícula. Las coordenadas indican dónde se encuentra cada punto.

- `x` indica la posición horizontal.
- `y` indica la posición vertical.

En este sistema:

- La esquina superior izquierda de la imagen es aproximadamente `(0, 0)`.
- La esquina superior derecha es aproximadamente `(1, 0)`.
- La esquina inferior izquierda es aproximadamente `(0, 1)`.
- La esquina inferior derecha es aproximadamente `(1, 1)`.

**Importante:** en las coordenadas habituales de una pantalla, el valor de `y` aumenta hacia abajo, no hacia arriba.

Ejemplo:

```text
(0,0) -------------------- (1,0)
  |                           |
  |        imagen             |
  |                           |
(0,1) -------------------- (1,1)
```

Si un punto tiene estas coordenadas:

```text
indice_punta 0.48 0.20
```

significa que está aproximadamente al 48 % del ancho de la imagen y al 20 % de su altura, medido desde la esquina superior izquierda.

### ¿Por qué se utilizan valores entre 0 y 1?

Porque así las coordenadas no dependen del tamaño de la imagen. Por ejemplo, una coordenada horizontal `x = 0.5` indica la mitad del ancho tanto si la imagen mide 640 píxeles como si mide 1920 píxeles.

## 4. ¿Cómo sabe el programa si un dedo está extendido?

El programa compara las posiciones de varios puntos del dedo. En este ejercicio se utiliza una regla geométrica simplificada:

> Un dedo se considera extendido si la distancia entre su punta y la muñeca es mayor que la distancia entre su articulación intermedia y la muñeca, multiplicada por un factor.

Para los dedos que no son el pulgar, el factor indicado es `1.15`. Para el pulgar se utiliza `1.1`.

De forma simplificada:

```text
distancia(muneca, punta) > distancia(muneca, articulacion) * factor
```

Si se cumple la condición, el programa considera que el dedo está extendido.

### Ejemplo numérico

Imagina estas distancias:

- Distancia desde la muñeca hasta la articulación intermedia: `0.30`.
- Distancia desde la muñeca hasta la punta del dedo: `0.50`.

Para un dedo distinto del pulgar, el cálculo sería:

```text
0.30 * 1.15 = 0.345
```

Después se compara:

```text
0.50 > 0.345
```

Como la condición es verdadera, el dedo se considera extendido.

En cambio, si la distancia hasta la punta fuera `0.32`:

```text
0.32 > 0.345
```

La condición sería falsa y el dedo no se consideraría extendido.

**Ten en cuenta:** esta es una heurística, es decir, una regla aproximada. No es una detección perfecta de la anatomía de la mano.

## 5. ¿Cómo se calcula la distancia entre dos puntos?

Cada punto tiene coordenadas `(x, y)`. Para calcular la distancia entre dos puntos se utiliza la fórmula de distancia en el plano:

```text
distancia = √((x2 - x1)² + (y2 - y1)²)
```

Por ejemplo, si un punto está en `(0.2, 0.3)` y otro en `(0.5, 0.7)`:

```text
distancia = √((0.5 - 0.2)² + (0.7 - 0.3)²)
          = √(0.3² + 0.4²)
          = √(0.09 + 0.16)
          = √0.25
          = 0.5
```

En Java, se puede calcular así:

```java
static double distancia(double[] a, double[] b) {
    double dx = b[0] - a[0];
    double dy = b[1] - a[1];

    return Math.sqrt(dx * dx + dy * dy);
}
```

Aquí:

- `a[0]` es la coordenada `x` del primer punto.
- `a[1]` es la coordenada `y` del primer punto.
- `b[0]` y `b[1]` son las coordenadas del segundo punto.
- `Math.sqrt(...)` calcula la raíz cuadrada.

## 6. ¿Cómo sabe si la mano mira hacia arriba o hacia abajo?

**El código de este ejercicio no determina directamente si la palma de la mano mira hacia arriba o hacia abajo.**

Lo que hace es comparar distancias entre puntos de la mano para estimar qué dedos están extendidos. El enunciado propone este método porque puede funcionar aunque la mano esté girada dentro del plano de la imagen.

Hay que distinguir dos situaciones:

1. **Girar la mano dentro de la imagen:** por ejemplo, inclinar la mano hacia un lado. Las distancias entre los puntos se mantienen aproximadamente iguales, por lo que una comparación de distancias puede seguir funcionando.
2. **Girar la mano hacia la cámara o alejándola de ella:** por ejemplo, mostrar la palma o el dorso. Con solo coordenadas `x` e `y`, el programa no puede distinguir de forma fiable todas estas situaciones.

Por tanto, el algoritmo no “sabe” realmente hacia dónde mira la palma. Solo aplica una regla geométrica a las coordenadas recibidas. La regla puede fallar si la perspectiva hace que un dedo parezca más corto o si los puntos detectados no son precisos.

Para estimar la orientación de la palma con mayor fiabilidad, normalmente se necesitaría información adicional, como coordenadas tridimensionales (`x`, `y`, `z`) y un algoritmo específico para interpretar la orientación.

## 7. ¿Cómo detecta el gesto de PINZA?

La pinza se detecta comprobando si la punta del pulgar y la punta del índice están suficientemente cerca.

El ejercicio indica esta condición:

```text
distancia(pulgar_punta, indice_punta)
    < 0.25 * distancia(muneca, indice_medio)
```

Es decir, la distancia entre las puntas debe ser menor que una cuarta parte de la distancia de referencia entre la muñeca y la articulación intermedia del índice.

Se utiliza una distancia de referencia para adaptar la comparación al tamaño de la mano en la imagen.

Ejemplo:

```text
Distancia entre la punta del pulgar y la del índice: 0.04
Distancia entre la muñeca y la articulación del índice: 0.30

0.25 * 0.30 = 0.075
```

Como `0.04 < 0.075`, el programa consideraría que hay una pinza.

El umbral `0.25` es una regla elegida para este ejercicio. En una aplicación real podría necesitar ajustes.

## 8. ¿Cómo se decide el nombre del gesto?

Una vez que el programa ha calculado qué dedos están extendidos, comprueba varias condiciones. Según el enunciado, el orden es:

1. **PINZA**: la punta del pulgar y la del índice están muy cerca.
2. **PUÑO**: no hay ningún dedo extendido.
3. **MANO ABIERTA**: están extendidos los cinco dedos.
4. **PULGAR**: solo está extendido el pulgar.
5. **VICTORIA**: solo están extendidos el índice y el corazón.
6. **SEÑALAR**: solo está extendido el índice.
7. **DESCONOCIDO**: no se cumple ninguna de las condiciones anteriores.

El orden importa. Por ejemplo, si se cumple la condición de pinza, el programa debe clasificarla como `PINZA` antes de evaluar otros gestos.

## 9. Explicación del código Java inicial

Este es el código que proporciona el ejercicio:

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Map<String, double[]>> manos = new ArrayList<>();
        Map<String, double[]> actual = new LinkedHashMap<>();

        while (sc.hasNextLine()) {
            String l = sc.nextLine().trim();

            if (l.equals("---")) {
                manos.add(actual);
                actual = new LinkedHashMap<>();
                continue;
            }

            if (l.isEmpty()) continue;

            String[] p = l.split(" ");
            actual.put(p[0], new double[]{
                Double.parseDouble(p[1]),
                Double.parseDouble(p[2])
            });
        }

        if (!actual.isEmpty()) manos.add(actual);

        String[] DEDOS = {
            "pulgar", "indice", "corazon", "anular", "menique"
        };

        // TODO: decidir qué dedos están extendidos y qué gesto hace cada mano
    }
}
```

### 9.1. `import java.util.*;`

```java
import java.util.*;
```

Importa clases útiles de Java, como `Scanner`, `List`, `Map`, `ArrayList` y `LinkedHashMap`.

### 9.2. El método `main`

```java
public static void main(String[] args) {
```

Es el punto de entrada del programa. Java empieza a ejecutar el programa desde este método.

### 9.3. Leer los datos

```java
Scanner sc = new Scanner(System.in);
```

Crea un objeto `Scanner` para leer el texto que se introduce por la entrada estándar, por ejemplo, los datos pegados en la consola.

### 9.4. ¿Qué significa `List<Map<String, double[]>>`?

Esta declaración puede parecer complicada:

```java
List<Map<String, double[]>> manos = new ArrayList<>();
```

Se puede leer desde dentro hacia fuera:

- `double[]`: un array de números decimales. En este programa contiene dos valores: `x` e `y`.
- `Map<String, double[]>`: una estructura que relaciona un nombre con un array de coordenadas. Por ejemplo, `muneca` se relaciona con `[0.50, 0.80]`.
- `List<Map<String, double[]>>`: una lista de mapas, de modo que se puede guardar un mapa por cada mano.
- `new ArrayList<>()`: crea la lista vacía.

Una representación simplificada sería:

```text
manos
 ├── Mano 1
 │    ├── "muneca"       → [0.50, 0.80]
 │    ├── "indice_punta" → [0.48, 0.20]
 │    └── ...
 ├── Mano 2
 │    ├── "muneca"       → [0.40, 0.75]
 │    └── ...
 └── ...
```

### 9.5. Guardar los puntos de la mano actual

```java
Map<String, double[]> actual = new LinkedHashMap<>();
```

Crea un mapa para almacenar los puntos de la mano que se está leyendo.

`LinkedHashMap` guarda las asociaciones entre nombres y coordenadas y conserva el orden de inserción.

### 9.6. Leer una línea cada vez

```java
while (sc.hasNextLine()) {
    String l = sc.nextLine().trim();
```

- `sc.hasNextLine()` comprueba si queda otra línea por leer.
- `sc.nextLine()` lee la siguiente línea.
- `trim()` elimina espacios al principio y al final.

La variable `l` contiene la línea actual.

### 9.7. Separar las manos con `---`

```java
if (l.equals("---")) {
    manos.add(actual);
    actual = new LinkedHashMap<>();
    continue;
}
```

El texto `---` indica que termina una mano y empieza otra.

Cuando se encuentra:

1. Se añade el mapa de la mano actual a la lista `manos`.
2. Se crea un mapa vacío para la siguiente mano.
3. `continue` hace que el bucle pase directamente a la siguiente línea.

### 9.8. Ignorar las líneas vacías

```java
if (l.isEmpty()) continue;
```

Si la línea no contiene texto, el programa no intenta procesarla y pasa a la siguiente.

### 9.9. Separar el nombre y las coordenadas

```java
String[] p = l.split(" ");
```

Divide la línea usando los espacios como separadores.

Por ejemplo, esta línea:

```text
muneca 0.50 0.80
```

se convierte en un array parecido a este:

```text
p[0] = "muneca"
p[1] = "0.50"
p[2] = "0.80"
```

Después se guarda el punto:

```java
actual.put(p[0], new double[]{
    Double.parseDouble(p[1]),
    Double.parseDouble(p[2])
});
```

- `p[0]` es la clave, es decir, el nombre del punto.
- `Double.parseDouble(p[1])` convierte el texto de la coordenada `x` en un número decimal.
- `Double.parseDouble(p[2])` hace lo mismo con la coordenada `y`.
- `new double[]{...}` crea el array con las dos coordenadas.
- `actual.put(...)` guarda la asociación en el mapa.

**Nota:** `split(" ")` es suficiente para las líneas del ejemplo si tienen un único espacio entre valores. Para tolerar varios espacios o tabuladores, suele ser más robusto utilizar `split("\\s+")`.

### 9.10. Guardar la última mano

```java
if (!actual.isEmpty()) manos.add(actual);
```

Cuando termina la lectura, puede quedar una última mano que no acaba con `---`. Esta condición comprueba que el mapa no esté vacío y, si contiene datos, lo añade a la lista.

### 9.11. El array `DEDOS`

```java
String[] DEDOS = {
    "pulgar", "indice", "corazon", "anular", "menique"
};
```

Crea un array con los nombres de los cinco dedos.

El programa podrá recorrerlo para comprobar cada dedo. Los nombres deben coincidir con los que se utilicen después al buscar los puntos correspondientes en el mapa.

### 9.12. ¿Qué significa `TODO`?

```java
// TODO: decidir qué dedos están extendidos y qué gesto hace cada mano
```

`TODO` es un comentario que indica una parte pendiente de implementar. El código inicial todavía **no calcula los dedos extendidos ni clasifica los gestos**. Esa es precisamente la tarea que hay que completar en el ejercicio.

## 10. ¿Qué hace el programa con varias manos?

Los datos de cada mano se separan con una línea que contiene:

```text
---
```

Por ejemplo:

```text
muneca 0.50 0.80
indice_punta 0.48 0.20
indice_medio 0.49 0.45
---
muneca 0.40 0.75
indice_punta 0.42 0.70
indice_medio 0.41 0.60
```

El programa guarda los puntos anteriores al separador en un mapa y los siguientes en otro mapa. Ambos mapas quedan almacenados en la lista `manos`.

De este modo, puede analizar cada mano por separado y producir una salida como:

```text
Mano 1: PUÑO (extendidos: ninguno)
Mano 2: MANO ABIERTA (extendidos: pulgar, indice, corazon, anular, menique)
```

La salida exacta depende de las coordenadas y de las reglas de clasificación implementadas.

## 11. Resumen

- Las coordenadas `x` e `y` indican la posición de un punto dentro de la imagen.
- Los valores normalizados entre `0` y `1` permiten trabajar sin depender del tamaño de la imagen.
- `y` aumenta hacia abajo.
- El ejercicio usa puntos de la muñeca, las puntas de los dedos y las articulaciones intermedias.
- Se comparan distancias para estimar si los dedos están extendidos.
- La pinza se reconoce comparando la distancia entre las puntas del pulgar y del índice con una distancia de referencia.
- El gesto se clasifica según qué dedos están extendidos y según el orden de las condiciones.
- El código inicial solo lee y organiza las coordenadas; la parte marcada con `TODO` queda pendiente.
- El algoritmo no determina directamente si la palma mira hacia arriba o hacia abajo. Con solo coordenadas 2D no se puede resolver de forma fiable la orientación completa de la mano.

## 12. Una forma sencilla de recordar el proceso

```text
Leer las líneas de entrada
        ↓
Separar los datos de cada mano
        ↓
Guardar cada punto con sus coordenadas x e y
        ↓
Calcular distancias entre la muñeca y los puntos de los dedos
        ↓
Estimar qué dedos están extendidos
        ↓
Comprobar si hay una pinza
        ↓
Aplicar las reglas de clasificación
        ↓
Mostrar el gesto de cada mano
```
