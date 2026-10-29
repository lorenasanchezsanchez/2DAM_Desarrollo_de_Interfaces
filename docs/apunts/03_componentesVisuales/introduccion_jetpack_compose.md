# Introducción a Jetpack Compose

## 1. ¿Qué es Jetpack Compose?

**Jetpack Compose** es el conjunto de herramientas moderno de Android para construir interfaces gráficas utilizando Kotlin. En lugar de describir la interfaz mediante archivos XML y modificar sus componentes de forma imperativa, se describe en código qué debe mostrarse según los datos actuales de la aplicación.

Es un enfoque **declarativo**: se escribe una función que describe la interfaz y Compose se encarga de actualizarla cuando cambia el estado que utiliza.

### 1.1. Interfaz imperativa y declarativa

En un enfoque imperativo, normalmente se obtiene una referencia a un componente y se modifica directamente:

```kotlin
texto.text = "Hola"
```

En Compose se describe el resultado que debe verse:

```kotlin
@Composable
fun Saludo() {
    Text(text = "Hola")
}
```

Si el texto depende de un dato, se pasa ese dato como parámetro o se obtiene de un estado observable.

### 1.2. ¿Para qué sirve?

Compose permite crear pantallas, formularios, listas, botones, menús y otros elementos de interfaz. Se integra con el ecosistema Android y puede convivir con interfaces XML en proyectos existentes.

---

## 2. Preparación de un proyecto

Para trabajar con Jetpack Compose se utiliza normalmente **Android Studio**, Kotlin y un proyecto Android configurado para Compose.

Al crear un proyecto nuevo, selecciona una plantilla que incluya Compose, si está disponible en tu versión de Android Studio. La plantilla configura las dependencias y el plugin de Kotlin necesarios.

Un proyecto típico contiene:
- `MainActivity.kt`: punto de entrada de la actividad.
- Funciones `@Composable`: describen las partes de la interfaz.
- `AndroidManifest.xml`: declara componentes y características de la aplicación.
- Archivos Gradle: configuran plugins, dependencias y opciones de compilación.

No es necesario memorizar toda la configuración Gradle para empezar a diseñar pantallas, pero sí entender que las dependencias y los plugins se gestionan desde el sistema de construcción del proyecto.

### 2.1. Ejemplo de entrada en una actividad

Una plantilla de Compose suele llamar a una función composable desde `setContent`:

```kotlin
class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        setContent {
            Saludo()
        }
    }
}
```

`setContent` establece la interfaz de Compose que se mostrará en la actividad.

---

## 3. La anotación `@Composable`

Una función que participa en la construcción de la interfaz de Compose se marca habitualmente con `@Composable`.

```kotlin
@Composable
fun Saludo() {
    Text(text = "Hola, DAM")
}
```

Aspectos importantes:
- Una función composable puede llamar a otras funciones composables.
- Puede recibir parámetros para personalizar lo que muestra.
- Puede incluir componentes de interfaz como `Text`, `Button`, `Row` o `Column`.
- Compose puede volver a ejecutar funciones composables cuando cambia el estado del que dependen. Este proceso se denomina **recomposición**.

### 3.1. Composable con parámetros

```kotlin
@Composable
fun SaludoPersonalizado(nombre: String) {
    Text(text = "Hola, $nombre")
}
```

Uso:

```kotlin
SaludoPersonalizado(nombre = "Alex")
SaludoPersonalizado(nombre = "Noa")
```

La función se reutiliza para mostrar distintos nombres.

---

## 4. Componentes básicos

### 4.1. `Text`

Muestra texto.

```kotlin
Text(text = "Bienvenidos a Desarrollo de Interfaces")
```

Se pueden ajustar algunas propiedades:

```kotlin
Text(
    text = "Título de la pantalla",
    fontSize = 24.sp,
    fontWeight = FontWeight.Bold
)
```

Para utilizar `sp`, `dp` y otros tipos habituales se importan las unidades correspondientes de Compose.

### 4.2. `Button`

Representa un botón que ejecuta una acción al pulsarlo.

```kotlin
Button(
    onClick = {
        println("Se ha pulsado el botón")
    }
) {
    Text("Pulsar")
}
```

- `onClick` recibe una función que se ejecuta al pulsar.
- El bloque interior describe el contenido del botón.

En una aplicación real, la acción suele modificar el estado, navegar a otra pantalla o llamar a una operación de la aplicación.

### 4.3. `TextField`

Permite introducir texto. Para que sea interactivo, normalmente se conecta a un estado.

```kotlin
@Composable
fun CampoNombre() {
    var nombre by remember { mutableStateOf("") }

    TextField(
        value = nombre,
        onValueChange = { nuevoValor ->
            nombre = nuevoValor
        },
        label = { Text("Nombre") }
    )
}
```

`value` contiene el texto actual y `onValueChange` comunica el nuevo texto cuando la persona escribe.

### 4.4. `Image`

Muestra una imagen. Por ejemplo, para una imagen incluida en los recursos `drawable`:

```kotlin
Image(
    painter = painterResource(id = R.drawable.logo),
    contentDescription = "Logotipo de la aplicación"
)
```

`contentDescription` ayuda a que las tecnologías de asistencia puedan interpretar el contenido de la imagen. Si la imagen es puramente decorativa, se puede valorar si corresponde utilizar una descripción vacía.

---

## 5. Organización de los elementos

Compose ofrece componentes de distribución que permiten organizar otros componentes.

### 5.1. `Column`

Coloca sus elementos verticalmente.

```kotlin
Column {
    Text("Nombre")
    Text("Apellidos")
    Button(onClick = { /* acción */ }) {
        Text("Guardar")
    }
}
```

### 5.2. `Row`

Coloca sus elementos horizontalmente.

```kotlin
Row {
    Button(onClick = { /* acción */ }) {
        Text("Aceptar")
    }
    Button(onClick = { /* acción */ }) {
        Text("Cancelar")
    }
}
```

### 5.3. `Box`

Permite colocar elementos en una misma zona, por ejemplo, superponer un texto sobre una imagen.

```kotlin
Box {
    Image(
        painter = painterResource(R.drawable.logo),
        contentDescription = "Logotipo"
    )
    Text("Mi aplicación")
}
```

### 5.4. Espaciado y alineación

Se pueden utilizar parámetros de alineación y separación:

```kotlin
Column(
    verticalArrangement = Arrangement.spacedBy(12.dp),
    horizontalAlignment = Alignment.CenterHorizontally
) {
    Text("Primer elemento")
    Text("Segundo elemento")
}
```

`Arrangement.spacedBy(12.dp)` establece separación entre elementos. `Alignment.CenterHorizontally` centra los elementos horizontalmente dentro de la columna.

---

## 6. `Modifier`: tamaño, margen, fondo y otras propiedades

`Modifier` permite configurar cómo se mide, coloca o dibuja un componente, así como añadir comportamiento.

```kotlin
Text(
    text = "Hola",
    modifier = Modifier.padding(16.dp)
)
```

Ejemplos frecuentes:

```kotlin
Modifier
    .fillMaxWidth()
    .padding(16.dp)
```

```kotlin
Modifier
    .size(120.dp)
```

```kotlin
Modifier
    .background(Color.LightGray)
    .padding(12.dp)
```

Modificadores comunes:
- `padding(...)`: añade espacio interior o exterior según dónde se aplique en la cadena.
- `fillMaxWidth()`: solicita ocupar el ancho máximo disponible.
- `fillMaxSize()`: solicita ocupar el espacio máximo disponible.
- `size(...)`: establece un tamaño solicitado.
- `background(...)`: dibuja un fondo.
- `clickable { ... }`: hace que el elemento responda a pulsaciones.
- `weight(...)`: distribuye espacio dentro de un `Row` o `Column`, según el contexto.

**El orden de los modificadores importa.** Por ejemplo, aplicar `background` antes o después de `padding` puede cambiar la zona que queda coloreada.

---

## 7. Eventos y lambdas

Una **lambda** es una función que se puede pasar como valor a otra función. En Compose se utilizan frecuentemente para responder a eventos.

```kotlin
Button(
    onClick = {
        println("Acción ejecutada")
    }
) {
    Text("Ejecutar")
}
```

También se puede definir una función aparte:

```kotlin
fun guardarDatos() {
    println("Datos guardados")
}

@Composable
fun BotonGuardar() {
    Button(onClick = { guardarDatos() }) {
        Text("Guardar")
    }
}
```

No es lo mismo ejecutar una función inmediatamente que pasar una acción para ejecutarla más tarde:

```kotlin
onClick = { guardarDatos() } // La acción se ejecuta al pulsar.
```

En cambio, una expresión que llama a la función directamente durante la composición puede ejecutarla antes de que se pulse el botón. Para los eventos de Compose, se suele pasar una lambda.

### 7.1. Eventos de campos de texto

```kotlin
TextField(
    value = nombre,
    onValueChange = { textoNuevo ->
        nombre = textoNuevo
    }
)
```

`onValueChange` es una función que Compose llama cuando cambia el contenido del campo. La lambda recibe el valor nuevo y actualiza el estado.

---

## 8. Estado y recomposición

El **estado** es información que puede cambiar y que influye en lo que muestra la interfaz: un contador, el nombre escrito en un formulario, una opción seleccionada o si un diálogo está abierto.

Una variable local normal no basta para provocar actualizaciones de interfaz cuando cambia. Para los ejemplos iniciales se puede utilizar `remember` junto con `mutableStateOf`.

```kotlin
@Composable
fun Contador() {
    var contador by remember { mutableIntStateOf(0) }

    Column {
        Text(text = "Valor: $contador")

        Button(onClick = { contador++ }) {
            Text("Incrementar")
        }
    }
}
```

En este ejemplo:
1. El estado comienza en `0`.
2. `Text` muestra el valor actual.
3. Al pulsar el botón, se incrementa `contador`.
4. Compose detecta el cambio del estado leído por la interfaz y actualiza el contenido necesario mediante recomposición.

Para utilizar `by` con estados, normalmente se necesitan los imports de delegación correspondientes (`getValue` y `setValue`) cuando el IDE no los añade automáticamente.

### 8.1. `remember` y `mutableStateOf`

- `mutableStateOf(valor)` crea un estado observable.
- `remember { ... }` conserva ese objeto durante las recomposiciones mientras se mantenga la misma posición en la composición.
- `mutableIntStateOf(0)` es una alternativa específica para estados enteros.
- `remember` por sí solo no garantiza que un dato sobreviva a la recreación de la actividad o al cierre del proceso.

### 8.2. `rememberSaveable`

Cuando sea apropiado conservar un valor sencillo ante cambios de configuración, se puede utilizar `rememberSaveable`:

```kotlin
var nombre by rememberSaveable { mutableStateOf("") }
```

La conservación depende del tipo de dato y de los mecanismos de guardado disponibles. Para estados de pantalla más complejos o lógica que deba sobrevivir a cambios de configuración, se puede utilizar un `ViewModel`.

### 8.3. Estado frente a variable normal

Una variable local ordinaria puede cambiar durante una ejecución, pero Compose no la observa automáticamente:

```kotlin
var contador = 0
contador++
```

Para una interfaz reactiva, utiliza un estado observable:

```kotlin
var contador by remember { mutableIntStateOf(0) }
contador++
```

Este segundo fragmento debe aparecer dentro de una función composable y el cambio debe producirse como parte de una acción o lógica adecuada.

---

## 9. Formularios y mensajes dinámicos

El siguiente ejemplo combina un campo de texto, un botón y un mensaje que depende del valor introducido.

```kotlin
@Composable
fun FormularioSaludo() {
    var nombre by rememberSaveable { mutableStateOf("") }
    var mensaje by remember { mutableStateOf("Escribe tu nombre") }

    Column(
        modifier = Modifier
            .fillMaxWidth()
            .padding(16.dp),
        verticalArrangement = Arrangement.spacedBy(12.dp)
    ) {
        TextField(
            value = nombre,
            onValueChange = { nombre = it },
            label = { Text("Nombre") },
            modifier = Modifier.fillMaxWidth()
        )

        Button(
            onClick = {
                mensaje = if (nombre.isBlank()) {
                    "Debes escribir un nombre"
                } else {
                    "Hola, $nombre"
                }
            }
        ) {
            Text("Saludar")
        }

        Text(text = mensaje)
    }
}
```

Observa:
- El campo está vinculado al estado `nombre`.
- La lambda de `onValueChange` guarda lo que se escribe.
- El botón actualiza `mensaje`.
- Cuando cambia un estado leído por la interfaz, el mensaje visible se actualiza.

---

## 10. Mostrar y ocultar elementos

Es posible utilizar condiciones de Kotlin para decidir qué elementos se muestran.

```kotlin
@Composable
fun MensajeCondicional() {
    var mostrar by remember { mutableStateOf(false) }

    Column {
        Button(onClick = { mostrar = !mostrar }) {
            Text(if (mostrar) "Ocultar mensaje" else "Mostrar mensaje")
        }

        if (mostrar) {
            Text("¡Este mensaje está visible!")
        }
    }
}
```

El botón alterna el valor booleano `mostrar`. Si es `true`, se incluye el texto en la interfaz; si es `false`, no se muestra.

---

## 11. Listas con `LazyColumn`

Para mostrar listas que pueden contener muchos elementos se utiliza habitualmente `LazyColumn`, que compone los elementos que necesita mostrar en cada momento.

```kotlin
@Composable
fun ListaAlumnos() {
    val alumnos = listOf("Alex", "Noa", "Mar", "Pau")

    LazyColumn {
        items(alumnos) { alumno ->
            Text(
                text = alumno,
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(12.dp)
            )
        }
    }
}
```

Para este ejemplo se necesita importar `androidx.compose.foundation.lazy.LazyColumn` y `androidx.compose.foundation.lazy.items`.

Si cada elemento tiene un identificador estable, es recomendable proporcionar una clave cuando corresponda:

```kotlin
LazyColumn {
    items(
        items = alumnos,
        key = { alumno -> alumno }
    ) { alumno ->
        Text(alumno)
    }
}
```

La clave debe ser única dentro de la lista.

---

## 12. Tarjetas y componentes reutilizables

Los componentes se pueden dividir en funciones pequeñas para reutilizarlos y facilitar la lectura.

```kotlin
@Composable
fun TarjetaAlumno(nombre: String, curso: String) {
    Card(
        modifier = Modifier
            .fillMaxWidth()
            .padding(vertical = 6.dp)
    ) {
        Column(modifier = Modifier.padding(16.dp)) {
            Text(text = nombre, fontWeight = FontWeight.Bold)
            Text(text = curso)
        }
    }
}
```

Uso:

```kotlin
@Composable
fun PantallaAlumnos() {
    Column(modifier = Modifier.padding(16.dp)) {
        TarjetaAlumno("Alex", "2º DAM")
        TarjetaAlumno("Noa", "2º DAW")
    }
}
```

La función `TarjetaAlumno` recibe los datos mediante parámetros. Así puede utilizarse con alumnos distintos sin duplicar la estructura visual.

---

## 13. Ejemplo completo: ficha de alumno

Este ejemplo reúne varios conceptos: `Column`, `Row`, `Card`, `Text`, `Button`, `Modifier`, separación y estado.

```kotlin
@Composable
fun PantallaAlumno() {
    var favorito by rememberSaveable { mutableStateOf(false) }
    var visitas by rememberSaveable { mutableIntStateOf(0) }

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(16.dp),
        verticalArrangement = Arrangement.spacedBy(16.dp)
    ) {
        Text(
            text = "Ficha de alumno",
            fontSize = 24.sp,
            fontWeight = FontWeight.Bold
        )

        Card(modifier = Modifier.fillMaxWidth()) {
            Column(
                modifier = Modifier.padding(16.dp),
                verticalArrangement = Arrangement.spacedBy(8.dp)
            ) {
                Text("Nombre: Alex")
                Text("Ciclo: Desarrollo de Aplicaciones Multiplataforma")

                Row(
                    horizontalArrangement = Arrangement.spacedBy(8.dp)
                ) {
                    Button(onClick = { favorito = !favorito }) {
                        Text(if (favorito) "Quitar favorito" else "Marcar favorito")
                    }

                    Button(onClick = { visitas++ }) {
                        Text("Registrar visita")
                    }
                }

                Text(
                    text = if (favorito) "Alumno favorito" else "Sin marcar como favorito"
                )
                Text("Visitas registradas: $visitas")
            }
        }
    }
}
```

### 13.1. Qué debes identificar

1. `PantallaAlumno` describe una pantalla.
2. `Column` organiza verticalmente los elementos.
3. `Card` agrupa visualmente la información.
4. `Row` coloca los botones en horizontal.
5. `Modifier.padding` añade separación.
6. `favorito` y `visitas` son estados observables.
7. Los botones cambian los estados.
8. Los textos que dependen de esos estados se actualizan tras la recomposición.

Los imports concretos de los componentes deben añadirse desde Android Studio; el IDE puede importarlos automáticamente.

---

## 14. Elevar el estado (*state hoisting*)

Cuando una interfaz crece, conviene separar el componente que **guarda y modifica el estado** del componente que únicamente lo **muestra**.

Este patrón se conoce como *state hoisting* o elevación del estado. El componente padre mantiene el estado y lo pasa al hijo mediante parámetros. El hijo comunica las acciones mediante funciones de retorno (*callbacks*).

```kotlin
@Composable
fun ContadorPresentacion(
    contador: Int,
    alIncrementar: () -> Unit
) {
    Row(
        verticalAlignment = Alignment.CenterVertically,
        horizontalArrangement = Arrangement.spacedBy(12.dp)
    ) {
        Text("Contador: $contador")
        Button(onClick = alIncrementar) {
            Text("Incrementar")
        }
    }
}

@Composable
fun PantallaContador() {
    var contador by rememberSaveable { mutableIntStateOf(0) }

    ContadorPresentacion(
        contador = contador,
        alIncrementar = { contador++ }
    )
}
```

En este diseño:
- `PantallaContador` es el componente padre y posee el estado.
- `ContadorPresentacion` recibe el valor `contador`.
- El hijo no modifica directamente el estado del padre: llama a `alIncrementar`.
- El padre procesa la acción y pasa el valor actualizado al hijo.

Esto favorece componentes reutilizables y facilita las pruebas.

### 14.1. Flujo unidireccional de datos

El patrón suele explicarse así:

1. El estado baja desde el padre hacia los componentes hijos.
2. Los eventos suben desde los hijos hacia el padre mediante callbacks.
3. El padre actualiza el estado.
4. Compose actualiza las partes de la interfaz que dependen del nuevo valor.

Este enfoque se conoce como **flujo unidireccional de datos** (UDF, *Unidirectional Data Flow*).

---

## 15. Navegación y estructura de una aplicación

En una aplicación con varias pantallas se necesita decidir cómo se pasa de una a otra. Jetpack Compose puede utilizarse con Navigation Compose, una biblioteca de navegación del ecosistema Android.

La navegación es un tema posterior a los componentes básicos. Para empezar, es suficiente con distinguir:
- **Componente composable:** representa una parte de la interfaz.
- **Actividad:** componente Android que sirve como punto de entrada de una ventana.
- **Navegación:** mecanismo para cambiar entre destinos o pantallas.
- **Estado:** datos que determinan qué muestra la interfaz.

No conviene mezclar toda la lógica de negocio, navegación y estado complejo en una única función composable.

---

## 16. Compose y XML: diferencias principales

| Aspecto | Interfaces XML tradicionales | Jetpack Compose |
|---|---|---|
| Definición de la interfaz | Principalmente archivos XML | Funciones Kotlin |
| Enfoque | Habitualmente imperativo para actualizar vistas | Declarativo |
| Componentes | `TextView`, `Button`, `LinearLayout`, etc. | `Text`, `Button`, `Column`, `Row`, etc. |
| Actualización de datos | Se modifican vistas y propiedades | El estado determina lo que se representa |
| Reutilización | Layouts, vistas personalizadas y otros recursos | Funciones composables reutilizables |
| Integración | Enfoque tradicional ampliamente utilizado | Puede convivir con vistas XML en una misma aplicación |

Compose no significa que XML desaparezca de Android: existen proyectos que siguen usando vistas tradicionales y proyectos que combinan ambas tecnologías.

---

## 17. Jetpack Compose y Compose Multiplatform

**No son exactamente lo mismo.** Comparten conceptos y parte de la tecnología, pero tienen objetivos y ámbitos de uso distintos.

### 17.1. Jetpack Compose

Jetpack Compose es el toolkit declarativo de interfaz de usuario de Android. Se utiliza para crear interfaces Android con Kotlin y se integra con las bibliotecas de Android Jetpack.

Es la opción natural si el objetivo principal es aprender a desarrollar la interfaz de una aplicación Android.

### 17.2. Compose Multiplatform

**Compose Multiplatform** es una tecnología multiplataforma de JetBrains que permite reutilizar código Kotlin y construir interfaces para distintas plataformas, entre ellas Android, iOS y escritorio. El grado de soporte y las particularidades dependen de la plataforma y de la versión de las herramientas.

El objetivo es compartir tanto código de interfaz como parte de la lógica de la aplicación cuando el proyecto y sus dependencias lo permiten.

### 17.3. Comparación

| Aspecto | Jetpack Compose | Compose Multiplatform |
|---|---|---|
| Objetivo principal | Interfaces de Android | Interfaces y código compartido entre plataformas |
| Lenguaje | Kotlin | Kotlin |
| Android | Sí | Sí |
| iOS | No es su objetivo directo como toolkit Android | Puede compartir interfaz y lógica, con configuración específica |
| Escritorio | No es su objetivo principal | Permite aplicaciones de escritorio, por ejemplo para Windows, macOS y Linux |
| Bibliotecas Android específicas | Integración directa con el ecosistema Android | No todas las bibliotecas Android pueden usarse en otras plataformas |
| Código compartido | Dentro del proyecto Android y sus módulos | Puede organizarse en módulos comunes y módulos específicos de cada plataforma |
| Aprendizaje inicial | Adecuado para centrarse en Android | Requiere comprender también la estructura multiplataforma |

### 17.4. ¿Qué parte del código se puede compartir?

Que una aplicación utilice Compose Multiplatform no significa que absolutamente todo el código sea idéntico en todas las plataformas.

Se puede compartir, según la arquitectura:
- La mayor parte de la interfaz declarativa.
- Modelos y lógica de negocio escritos en Kotlin común.
- Validaciones y transformaciones de datos.
- Parte de la gestión del estado.

Puede necesitar código específico:
- Acceso a funciones propias del sistema operativo.
- Permisos y APIs de cada plataforma.
- Integraciones con bibliotecas que solo existen en Android o iOS.
- Configuración de ventanas, distribución y publicación.

### 17.5. ¿Cuál conviene estudiar primero en 2º DAM?

Una secuencia didáctica razonable es:

1. Aprender los fundamentos de Kotlin necesarios.
2. Crear pantallas con `Text`, `Button`, `Column`, `Row` y `Modifier`.
3. Trabajar con eventos, estado y recomposición.
4. Construir formularios, listas y componentes reutilizables.
5. Separar estado y presentación mediante *state hoisting*.
6. Introducir Compose Multiplatform y comparar qué cambia al compartir código.

Así se aprenden primero los conceptos visuales y reactivos sin añadir desde el principio la complejidad de configurar varias plataformas.

---

## 18. Errores frecuentes

- **Cambiar una variable normal y esperar que la pantalla se actualice:** utiliza un estado observable cuando el dato deba provocar recomposición.
- **Ejecutar la acción al construir el botón:** pasa una lambda a `onClick`.
- **Olvidar actualizar el estado de un `TextField`:** el valor de `onValueChange` debe guardarse en el estado que alimenta `value`.
- **Utilizar `remember` como almacenamiento permanente:** no está diseñado para guardar datos de forma permanente ni garantiza sobrevivir a todas las recreaciones.
- **Crear una función composable enorme:** divide la interfaz en componentes con responsabilidades claras.
- **Pensar que Compose Multiplatform convierte cualquier API Android en multiplataforma:** el código que usa APIs específicas debe adaptarse o implementarse por plataforma.
- **No añadir imports:** Android Studio puede sugerirlos automáticamente; comprueba que el import corresponde al componente correcto.
- **Ignorar la accesibilidad:** los controles deben ser comprensibles y utilizables con tecnologías de asistencia.

---

## 19. Resumen de conceptos

| Concepto | Para qué sirve |
|---|---|
| `@Composable` | Marca una función que describe una parte de la interfaz |
| `Text` | Muestra texto |
| `Button` | Ejecuta una acción al pulsarse |
| `TextField` | Permite introducir texto |
| `Column` | Organiza elementos verticalmente |
| `Row` | Organiza elementos horizontalmente |
| `Box` | Permite colocar elementos en una misma zona |
| `Modifier` | Configura tamaño, espacio, aspecto o comportamiento |
| `remember` | Conserva un valor entre recomposiciones mientras corresponda |
| `mutableStateOf` | Crea un estado observable |
| `rememberSaveable` | Conserva valores compatibles a través de recreaciones admitidas |
| Recomposición | Actualización de la interfaz cuando cambia un estado observado |
| Lambda | Función que se puede pasar como valor, por ejemplo para eventos |
| *State hoisting* | Mantiene el estado en un componente superior y lo pasa a los hijos |
| UDF | Flujo unidireccional de estado hacia abajo y eventos hacia arriba |
| Jetpack Compose | Toolkit declarativo de interfaz de Android |
| Compose Multiplatform | Tecnología para compartir interfaz y código Kotlin entre plataformas compatibles |

---

## 20. Actividades prácticas

### Actividad 1. Primera pantalla

Crea una función composable llamada `Presentacion` que muestre:
- Tu nombre.
- El ciclo que estudias.
- Un texto de bienvenida.

Utiliza `Text` y modifica el tamaño del título.

### Actividad 2. Distribución de componentes

Crea una pantalla que contenga:
- Un título.
- Dos botones en una misma fila.
- Un texto debajo de los botones.

Organiza la pantalla utilizando `Column` y `Row`.

### Actividad 3. Personalizar con `Modifier`

Modifica la actividad anterior para:
- Añadir espacio alrededor de la pantalla.
- Hacer que los botones ocupen el ancho disponible en una disposición adecuada.
- Añadir un fondo o una tarjeta.
- Probar a cambiar el orden de `background` y `padding` y describir la diferencia.

### Actividad 4. Contador

Crea un contador que comience en cero y tenga botones para incrementar y decrementar. El valor no debe bajar de cero.

**Requisitos:**
- Utilizar estado observable.
- Mostrar el valor actual.
- Actualizarlo desde las acciones de los botones.

### Actividad 5. Formulario de saludo

Crea un formulario con un campo de nombre y un botón «Saludar». Al pulsarlo:
- Si el campo está vacío, muestra un aviso.
- Si contiene un nombre, muestra un saludo personalizado.

### Actividad 6. Mostrar u ocultar un mensaje

Crea un botón que permita mostrar y ocultar un texto. El texto del botón debe cambiar según el estado.

### Actividad 7. Lista de asignaturas

Utiliza `LazyColumn` para mostrar una lista de al menos ocho asignaturas. Cada elemento debe tener separación y un aspecto uniforme.

### Actividad 8. Tarjetas reutilizables

Crea una función `TarjetaAsignatura(nombre: String, horas: Int)` que muestre una asignatura en una tarjeta. Invócala para representar al menos tres asignaturas distintas.

### Actividad 9. Ficha de alumno

Amplía el ejemplo de la ficha de alumno:
- Añade un campo para el curso.
- Incluye un botón para marcar o quitar el favorito.
- Añade un contador de visitas.
- Separa los datos visuales en componentes reutilizables.

### Actividad 10. Elevar el estado

Modifica el contador para que el componente que muestra el número no almacene el estado. El componente padre debe conservarlo y pasar al hijo el valor y la función para incrementarlo.

Explica qué responsabilidad tiene cada función.

### Actividad 11. Comparación entre tecnologías

Redacta una comparación breve entre Jetpack Compose y Compose Multiplatform. Incluye:
- Objetivo de cada tecnología.
- Plataformas principales.
- Qué código podría compartirse.
- Qué elementos podrían necesitar implementación específica.
- En qué orden estudiarías ambas tecnologías y por qué.

---

## 21. Referencias oficiales

- Documentación oficial de Jetpack Compose: https://developer.android.com/develop/ui/compose
- Guía de estado en Compose: https://developer.android.com/develop/ui/compose/state
- Documentación de listas en Compose: https://developer.android.com/develop/ui/compose/lists
- Documentación oficial de Compose Multiplatform: https://www.jetbrains.com/compose-multiplatform/
- Tutoriales de Compose Multiplatform: https://www.jetbrains.com/help/kotlin-multiplatform-dev/compose-multiplatform.html
