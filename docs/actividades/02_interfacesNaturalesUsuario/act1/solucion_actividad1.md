

# PrimeraAppReconocimientoVoz

## Análisis del proyecto Android y configuración del entorno

**Tecnologías:** Android · Kotlin · XML · Gradle

**Objetivos:**
- Comprender la estructura de un proyecto Android.
- Identificar la función de cada archivo.
- Entender cómo funciona el reconocimiento de voz.
- Configurar Android Studio.
- Ejecutar la aplicación en un emulador o dispositivo físico.

---

## 1. ¿Qué vamos a desarrollar?

Vamos a trabajar con una aplicación Android que permite realizar determinadas acciones mediante comandos de voz.

La aplicación incorpora:

- Una pantalla de inicio.
- Una pantalla de ajustes.
- Un botón de micrófono.
- Reconocimiento de voz en español.
- Visualización del texto reconocido.
- Ejecución de comandos de voz.
- Cambio entre tema claro y oscuro.
- Animación mientras se escucha.
- Mensajes y cuadros de diálogo.

La aplicación está desarrollada principalmente con **Kotlin**, mientras que las interfaces se definen mediante archivos XML.

---

## 2. ¿Cómo funciona la aplicación?

El funcionamiento general se puede representar así:

```text
          USUARIO
             |
             | Habla
             v
       MICRÓFONO
             |
             v
  RECONOCIMIENTO DE VOZ
             |
             | Texto reconocido
             v
  INTERPRETACIÓN DEL COMANDO
             |
             | Acción identificada
             v
      MAIN ACTIVITY
             |
             v
   ACCIÓN EN LA INTERFAZ
```

**Ejemplo:**

1. El usuario mantiene pulsado el micrófono.
2. Dice: «Ir a ajustes».
3. Android reconoce el texto.
4. La aplicación interpreta el comando.
5. Se muestra la pantalla de ajustes.

El reconocimiento depende del servicio de voz disponible en el dispositivo.



## 3. Tecnologías utilizadas

| Tecnología          | Función                                                              |
| ------------------- | -------------------------------------------------------------------- |
| Android             | Sistema operativo donde se ejecuta la aplicación.                    |
| Kotlin              | Lenguaje utilizado para implementar la lógica.                       |
| XML                 | Definición de las interfaces gráficas.                               |
| Android Studio      | Entorno de desarrollo.                                               |
| Gradle              | Herramienta de construcción del proyecto.                            |
| Android SDK         | Herramientas y API necesarias para desarrollar aplicaciones Android. |
| SpeechRecognizer    | API de Android para reconocimiento de voz.                           |
| AndroidX            | Bibliotecas de compatibilidad y componentes Android.                 |
| Material Components | Componentes visuales de Material Design.                             |

Cada tecnología tiene una responsabilidad diferente.

Kotlin no sustituye al XML: ambos se complementan para construir la aplicación.

---

## 4. Estructura general del proyecto

La estructura del proyecto es similar a la siguiente:

```text
PrimeraAppReconocimientoVoz/
│
├── settings.gradle.kts
├── build.gradle.kts
├── gradle.properties
├── README.md
│
└── app/
    ├── build.gradle.kts
    │
    └── src/
        └── main/
            ├── AndroidManifest.xml
            │
            ├── java/
            │   └── com/example/reconocimientovoz/
            │       ├── MainActivity.kt
            │       ├── HomeFragment.kt
            │       ├── SettingsFragment.kt
            │       ├── SpeechRecognitionManager.kt
            │       └── VoiceCommandProcessor.kt
            │
            └── res/
                ├── layout/
                ├── drawable/
                ├── values/
                └── values-night/
```

Podemos dividir el proyecto en tres partes:

1. **Configuración:** archivos de Gradle.
2. **Lógica:** archivos Kotlin.
3. **Interfaz y recursos:** archivos XML, textos, colores y temas.

---

## 5. Los archivos de configuración

![Image](res/arch_configuracion.png)

Antes de ejecutar la aplicación, Android Studio necesita conocer:

* Qué módulos tiene el proyecto.
* Qué complementos debe utilizar.
* Qué bibliotecas necesita.
* Qué versión del SDK utiliza.
* Qué versión de Java necesita Gradle.

Esta información se encuentra principalmente en los archivos de Gradle.

Los tres archivos principales son:

| Archivo               | Responsabilidad                                      |
| --------------------- | ---------------------------------------------------- |
| `settings.gradle.kts` | Configura el proyecto y sus módulos.                 |
| `build.gradle.kts`    | Declara complementos y sus versiones.                |
| `gradle.properties`   | Configura propiedades generales de Gradle y Android. |

Además, el módulo `app` tiene su propio archivo `build.gradle.kts`.

---

## 6. `settings.gradle.kts`

Este archivo configura el proyecto y determina qué módulos lo componen.

Ejemplo de contenido:

```kotlin
pluginManagement {
    repositories {
        google()
        mavenCentral()
        gradlePluginPortal()
    }
}

dependencyResolutionManagement {
    repositoriesMode.set(
        RepositoriesMode.FAIL_ON_PROJECT_REPOS
    )

    repositories {
        google()
        mavenCentral()
    }
}

rootProject.name = "PrimeraAppReconocimientoVoz"

include(":app")
```

### ¿Qué significa?

| Elemento           | Función                                                               |
| ------------------ | --------------------------------------------------------------------- |
| `pluginManagement` | Define dónde buscar los complementos de Gradle.                       |
| `google()`         | Permite descargar componentes publicados en el repositorio de Google. |
| `mavenCentral()`   | Permite descargar bibliotecas de Maven Central.                       |
| `rootProject.name` | Establece el nombre del proyecto.                                     |
| `include(":app")`  | Indica que el proyecto contiene un módulo llamado `app`.              |

**Importante:** este archivo organiza el proyecto, pero no implementa el reconocimiento de voz.

---

## 7. `build.gradle.kts` de la raíz

El proyecto tiene un archivo `build.gradle.kts` en su carpeta principal.

Su configuración incluye:

```kotlin
plugins {
    id("com.android.application") version "8.7.3" apply false
    id("org.jetbrains.kotlin.android") version "2.0.21" apply false
}
```

Se declaran dos complementos:

* `com.android.application`: permite construir aplicaciones Android.
* `org.jetbrains.kotlin.android`: permite compilar código Kotlin para Android.

#### ¿Qué significa `apply false`?

Significa que se declara el complemento y su versión, pero no se aplica directamente en el proyecto raíz.

Se aplicará en el módulo que lo necesite.

#### Versiones del proyecto

| Componente            | Versión declarada |
| --------------------- | ----------------- |
| Android Gradle Plugin | 8.7.3             |
| Kotlin                | 2.0.21            |

Estas versiones deben ser compatibles con la versión de Gradle utilizada.

---

## 8. `gradle.properties`

Este archivo contiene propiedades generales del proyecto.

Ejemplo:

```properties
org.gradle.jvmargs=-Xmx2048m -Dfile.encoding=UTF-8
android.useAndroidX=true
kotlin.code.style=official
android.nonTransitiveRClass=true
```

### Función de cada propiedad

| Propiedad                     | Función                                                             |
| ----------------------------- | ------------------------------------------------------------------- |
| `org.gradle.jvmargs`          | Configura parámetros de la máquina virtual Java que ejecuta Gradle. |
| `android.useAndroidX`         | Activa las bibliotecas AndroidX.                                    |
| `kotlin.code.style`           | Define el estilo de código Kotlin.                                  |
| `android.nonTransitiveRClass` | Limita la clase `R` del módulo a sus propios recursos.              |

Este archivo también puede utilizarse para ajustar propiedades relacionadas con Android.

---

## 9. Un problema del ZIP original: Gradle Wrapper

El ZIP original no incluye los archivos del Gradle Wrapper.

Normalmente, un proyecto que lo utiliza contiene:

```text
gradlew
gradlew.bat

gradle/
└── wrapper/
    ├── gradle-wrapper.jar
    └── gradle-wrapper.properties
```

### ¿Para qué sirve?

El Gradle Wrapper permite utilizar una versión concreta de Gradle sin depender de que esté instalada globalmente en cada ordenador.

Por ejemplo, en Windows se puede ejecutar:

```powershell
.\gradlew.bat --version
```

Este comando muestra la versión de Gradle utilizada por el proyecto.

**En nuestro caso, no funcionará si el archivo `gradlew.bat` no existe.**

La ausencia del Wrapper en el ZIP original es una carencia que debemos corregir para disponer de una configuración reproducible.

---

## 10. `app/build.gradle.kts`

Este archivo configura específicamente la aplicación Android.

Ejemplo de configuración:

```kotlin
android {
    namespace = "com.example.reconocimientovoz"

    compileSdk = 35

    defaultConfig {
        applicationId = "com.example.reconocimientovoz"
        minSdk = 23
        targetSdk = 35
        versionCode = 1
        versionName = "1.0"
    }
}
```

Es uno de los archivos más importantes para compilar la aplicación.

Contiene información sobre:

* El espacio de nombres.
* El SDK de compilación.
* El identificador de la aplicación.
* La versión mínima de Android.
* La versión objetivo.
* La versión de la aplicación.

---

## 11. Diferencias entre los SDK de Android

No debemos confundir `compileSdk`, `minSdk` y `targetSdk`.

| Parámetro    | Valor | Significado                                       |
| ------------ | ----: | ------------------------------------------------- |
| `compileSdk` |    35 | API de Android utilizada para compilar.           |
| `minSdk`     |    23 | Nivel mínimo de API declarado para la aplicación. |
| `targetSdk`  |    35 | Nivel de API al que se dirige la aplicación.      |

### `compileSdk = 35`

Necesitamos instalar el SDK correspondiente a Android 15, API 35.

### `minSdk = 23`

La configuración declara compatibilidad desde Android 6.0, aunque cada función también puede tener sus propios requisitos.

### `targetSdk = 35`

No significa que la aplicación solo funcione en Android 15.

Indica el nivel de API al que se dirige la aplicación.

---

## 12. Java 17 y Kotlin

El proyecto utiliza Java 17 como nivel de compatibilidad.

Configuración:

```kotlin
compileOptions {
    sourceCompatibility = JavaVersion.VERSION_17
    targetCompatibility = JavaVersion.VERSION_17
}

kotlinOptions {
    jvmTarget = "17"
}
```

### ¿Qué significa?

* `sourceCompatibility`: nivel de lenguaje Java aceptado.
* `targetCompatibility`: nivel de bytecode Java generado.
* `jvmTarget`: nivel de bytecode que debe generar Kotlin.

Además, necesitamos que Gradle se ejecute con un JDK compatible.

Para este proyecto, debemos seleccionar **JDK 17**.

No es necesario instalar Java por separado si Android Studio ya proporciona un JDK 17 adecuado.

---

## 13. Dependencias del proyecto

Las dependencias son bibliotecas que el proyecto utiliza para implementar funcionalidades.

Ejemplo:

```kotlin
dependencies {
    implementation("androidx.core:core-ktx:1.15.0")
    implementation("androidx.appcompat:appcompat:1.7.0")
    implementation("androidx.activity:activity-ktx:1.9.3")
    implementation("androidx.fragment:fragment-ktx:1.8.5")
    implementation("androidx.lifecycle:lifecycle-runtime-ktx:2.8.7")
    implementation("androidx.lifecycle:lifecycle-viewmodel-ktx:2.8.7")
    implementation("com.google.android.material:material:1.12.0")
}
```

### ¿Para qué sirve cada biblioteca?

| Biblioteca              | Función                                                    |
| ----------------------- | ---------------------------------------------------------- |
| Core KTX                | Facilita determinadas operaciones de Android desde Kotlin. |
| AppCompat               | Proporciona compatibilidad y componentes de interfaz.      |
| Activity KTX            | Facilita el trabajo con actividades.                       |
| Fragment KTX            | Facilita el trabajo con fragmentos.                        |
| Lifecycle Runtime KTX   | Proporciona utilidades relacionadas con el ciclo de vida.  |
| Lifecycle ViewModel KTX | Facilita el uso de ViewModel desde Kotlin.                 |
| Material Components     | Proporciona componentes visuales de Material Design.       |

Cuando sincronizamos el proyecto, Gradle descarga las dependencias necesarias.

**No tenemos que descargarlas manualmente.**

---

## 14. Los archivos Kotlin

El código Kotlin se encuentra en:

```text
app/src/main/java/com/example/reconocimientovoz/
```

Los archivos principales son:

| Archivo                       | Responsabilidad                    |
| ----------------------------- | ---------------------------------- |
| `MainActivity.kt`             | Coordina la aplicación.            |
| `SpeechRecognitionManager.kt` | Gestiona el reconocimiento de voz. |
| `VoiceCommandProcessor.kt`    | Interpreta los comandos.           |
| `HomeFragment.kt`             | Gestiona la pantalla de inicio.    |
| `SettingsFragment.kt`         | Gestiona la pantalla de ajustes.   |

![archivos](res/archivos.png)

Cada archivo tiene una responsabilidad concreta.

Esta separación facilita el mantenimiento y permite modificar una funcionalidad sin tener que reescribir toda la aplicación.

---

## 15. `MainActivity.kt`

Una `Activity` representa un punto de entrada y un contenedor principal de la interfaz de una aplicación Android.

En nuestro proyecto, `MainActivity.kt` coordina las principales funciones.

Se encarga de:

* Inicializar la interfaz.
* Mostrar el fragmento inicial.
* Controlar el botón del micrófono.
* Solicitar el permiso de grabación de audio.
* Iniciar y detener el reconocimiento.
* Recibir los resultados reconocidos.
* Ejecutar los comandos.
* Cambiar el tema.
* Actualizar la animación del círculo.
* Mostrar mensajes y diálogos.
* Liberar recursos cuando se destruye la actividad.

### Ejemplo: comprobar el permiso del micrófono

```kotlin
private fun checkPermissionAndStart() {
    if (
        ContextCompat.checkSelfPermission(
            this,
            Manifest.permission.RECORD_AUDIO
        ) == PackageManager.PERMISSION_GRANTED
    ) {
        startListening()
    } else {
        requestAudioPermission.launch(
            Manifest.permission.RECORD_AUDIO
        )
    }
}
```

![Image](res/permisos_micro.png)

### ¿Qué hace este código?

1. Comprueba si se ha concedido el permiso.
2. Si existe el permiso, inicia la escucha.
3. Si no existe, solicita autorización al usuario.
4. La aplicación podrá continuar cuando se conceda el permiso.

El permiso debe estar declarado también en el manifiesto.

---

## 16. `SpeechRecognitionManager.kt`

Este archivo se encarga de gestionar el reconocimiento de voz.

Utiliza clases proporcionadas por Android:

```kotlin
SpeechRecognizer
RecognizerIntent
RecognitionListener
```

Su responsabilidad principal es transformar la voz en texto.

### Flujo de reconocimiento

```text
Usuario habla
      |
      v
SpeechRecognizer
      |
      v
Servicio de reconocimiento
      |
      v
Texto reconocido
      |
      v
MainActivity
```

El reconocimiento puede proporcionar resultados parciales mientras el usuario habla y un resultado final cuando termina de procesar la frase.

El archivo diferencia varios estados.

```kotlin
sealed class VoiceState {
    data object Idle : VoiceState()
    data object Listening : VoiceState()
    data class Partial(val text: String) : VoiceState()
    data class Result(val text: String) : VoiceState()
    data class Error(val message: String) : VoiceState()
}
```

---

## 17. Estados del reconocimiento de voz

| Estado      | Significado                            |
| ----------- | -------------------------------------- |
| `Idle`      | El sistema no está escuchando.         |
| `Listening` | El sistema está escuchando al usuario. |
| `Partial`   | Existe una transcripción provisional.  |
| `Result`    | Se ha obtenido un resultado final.     |
| `Error`     | Ha ocurrido un problema.               |

Por ejemplo, el resultado final podría ser:

```kotlin
VoiceState.Result("ir a ajustes")
```

El gestor comunica el texto reconocido a `MainActivity`.

Después, otro componente interpretará el texto para decidir qué acción ejecutar.

![Image](res/escuchando.png)

### Idioma de reconocimiento

El proyecto solicita el español de España:

```kotlin
putExtra(
    RecognizerIntent.EXTRA_LANGUAGE,
    "es-ES"
)
```

Esto indica el idioma deseado, pero la precisión depende del servicio de reconocimiento y de las condiciones de uso.

---

## 18. `VoiceCommandProcessor.kt`

Este archivo interpreta el texto reconocido.

No se encarga de escuchar al usuario, sino de determinar qué significa el texto recibido.

Por ejemplo:

```text
Texto reconocido:
"ir a ajustes"
        |
        v
VoiceCommandProcessor
        |
        v
VoiceCommand.GoSettings
```

El procesador identifica diferentes comandos:

```kotlin
sealed class VoiceCommand {
    data object GoHome : VoiceCommand()
    data object GoSettings : VoiceCommand()
    data object DarkTheme : VoiceCommand()
    data object LightTheme : VoiceCommand()
    data object ShowMessage : VoiceCommand()
    data object OpenDialog : VoiceCommand()
    data object CloseDialog : VoiceCommand()
    data object Help : VoiceCommand()
    data object Unknown : VoiceCommand()
}
```

Cada objeto representa una acción lógica.

---

## 19. Comandos disponibles

| Frase reconocida  | Acción lógica |
| ----------------- | ------------- |
| «Inicio»          | `GoHome`      |
| «Ir a ajustes»    | `GoSettings`  |
| «Modo oscuro»     | `DarkTheme`   |
| «Modo claro»      | `LightTheme`  |
| «Mostrar mensaje» | `ShowMessage` |
| «Abrir diálogo»   | `OpenDialog`  |
| «Cerrar diálogo»  | `CloseDialog` |
| «Ayuda»           | `Help`        |

El procesador normaliza el texto para facilitar la interpretación.

Por ejemplo, puede convertir el texto a minúsculas y tratar las tildes de forma uniforme.

La frase reconocida se compara con los comandos admitidos.

Si no se reconoce ningún comando, se devuelve `Unknown`.

### Ventaja de separar responsabilidades

* El gestor de voz obtiene el texto.
* El procesador interpreta el texto.
* La actividad ejecuta la acción.

Así resulta más sencillo añadir nuevos comandos.

---

## 20. `HomeFragment.kt`

Un `Fragment` representa una parte reutilizable de la interfaz.

`HomeFragment.kt` gestiona la pantalla de inicio.

En este proyecto permite trabajar con elementos como:

* Un botón para mostrar un mensaje.
* Un botón para abrir un diálogo.

![Image](res/dialogo.png)

Ejemplo de un mensaje temporal:

```kotlin
binding.btnShowMessage.setOnClickListener {
    Snackbar.make(
        view,
        "¡Hola! Este es el mensaje de ejemplo.",
        Snackbar.LENGTH_LONG
    ).show()
}
```

![Image](res/mensaje.png)

### ¿Qué hace?

1. Espera a que el usuario pulse el botón.
2. Crea un `Snackbar`.
3. Muestra el mensaje durante un tiempo limitado.

La misma acción puede ejecutarse mediante un comando de voz si la lógica de la aplicación la conecta correctamente.

---

## 21. `SettingsFragment.kt`

Este archivo gestiona la pantalla de ajustes.

Entre sus funciones está permitir volver a la pantalla de inicio.

Ejemplo:

```kotlin
binding.btnBackHome.setOnClickListener {
    parentFragmentManager.beginTransaction()
        .replace(
            R.id.fragmentContainer,
            HomeFragment()
        )
        .commit()
}
```

### ¿Qué hace el código?

1. Espera a que se pulse el botón.
2. Inicia una transacción de fragmentos.
3. Sustituye el fragmento actual por `HomeFragment`.
4. Confirma la transacción.

De esta manera, se cambia la pantalla sin crear una nueva actividad.

---

## 22. Los archivos XML

Los archivos XML definen la estructura visual de las pantallas.

Se encuentran en:

```text
app/src/main/res/layout/
```

Los principales son:

| Archivo                 | Función                             |
| ----------------------- | ----------------------------------- |
| `activity_main.xml`     | Interfaz principal de la actividad. |
| `fragment_home.xml`     | Interfaz de la pantalla de inicio.  |
| `fragment_settings.xml` | Interfaz de la pantalla de ajustes. |

### ¿Qué diferencia hay entre Kotlin y XML?

**XML define qué elementos aparecen y cómo se organizan.**

**Kotlin define qué ocurre cuando interactuamos con ellos.**

Por ejemplo:

* XML crea un botón.
* Kotlin define qué sucede al pulsarlo.
* XML establece el tamaño y el aspecto del botón.
* Kotlin puede cambiar su comportamiento durante la ejecución.

Los identificadores de los elementos deben coincidir con los utilizados en el código Kotlin.

---

## 23. Recursos visuales y temas

Además de los diseños de las pantallas, el proyecto contiene otros recursos.

```text
res/
├── drawable/
│   ├── circle_idle.xml
│   └── circle_listening.xml
│
├── values/
│   ├── strings.xml
│   └── themes.xml
│
└── values-night/
    └── themes.xml
```

### `circle_idle.xml`

Define la apariencia del círculo cuando no está escuchando.

### `circle_listening.xml`

Define la apariencia del círculo durante la escucha.

### `strings.xml`

Contiene textos de la aplicación.

Centralizar los textos facilita su modificación y traducción.

### `themes.xml`

Define los estilos y el tema visual general.

### `values-night/themes.xml`

Permite definir recursos específicos para el modo nocturno.

`MainActivity.kt` controla cuándo se cambia entre los temas claro y oscuro.


![Image](res/tema.png)
---

## 24. `AndroidManifest.xml`

El manifiesto contiene información que Android necesita conocer sobre la aplicación.

Se encuentra en:

```text
app/src/main/AndroidManifest.xml
```

Entre otras cosas, declara:

* Los permisos.
* Las actividades.
* La actividad de inicio.
* Determinadas características y configuraciones de la aplicación.

### Permisos del proyecto

```xml
<uses-permission
    android:name="android.permission.RECORD_AUDIO" />

<uses-permission
    android:name="android.permission.INTERNET" />
```

`RECORD_AUDIO` permite solicitar acceso al micrófono.

`INTERNET` declara que la aplicación puede necesitar conectividad de red.

**Declarar un permiso no equivale a obtenerlo.**

El permiso del micrófono también debe solicitarse durante la ejecución cuando sea necesario.

---

## 25. La actividad de inicio

En el manifiesto aparece una declaración similar a esta:

```xml
<activity
    android:name=".MainActivity"
    android:exported="true">

    <intent-filter>
        <action android:name="android.intent.action.MAIN" />

        <category
            android:name="android.intent.category.LAUNCHER" />
    </intent-filter>

</activity>
```

### ¿Qué significa?

* `android:name`: identifica la actividad.
* `MAIN`: indica que es un punto de entrada principal.
* `LAUNCHER`: permite que la actividad se inicie desde el lanzador.
* `exported="true"`: permite que el sistema u otros componentes autorizados puedan iniciarla según las reglas de Android.

Esta configuración hace que `MainActivity` sea la actividad que se abre al iniciar la aplicación desde su icono.

---

## 26. Preparar Android Studio

Vamos a configurar el entorno antes de ejecutar el proyecto.

Necesitamos:

* Android Studio.
* Android SDK.
* SDK Platform API 35.
* Android SDK Build-Tools.
* Android SDK Platform-Tools.
* JDK 17.
* Una configuración de Gradle compatible.
* Un emulador o un móvil Android.

El primer objetivo es conseguir que Android Studio sincronice el proyecto correctamente.

---

## 27. Paso 1: utilizar una ruta sencilla

El error que apareció en nuestro proyecto indica que la ruta contiene caracteres no ASCII.

La ruta original incluía una carpeta con el nombre:

```text
Conselleria d'Educació
```

Android Gradle Plugin puede rechazar rutas que contienen caracteres no ASCII en determinadas configuraciones de Windows.

### Solución recomendada

Cierra Android Studio y copia el proyecto a:

```text
C:\Android\PrimeraAppReconocimientoVoz
```

Si no existe la carpeta `C:\Android`, créala.

La estructura debe quedar así:

```text
C:\Android\PrimeraAppReconocimientoVoz\
│
├── settings.gradle.kts
├── build.gradle.kts
├── gradle.properties
└── app\
    └── build.gradle.kts
```

No debe haber una carpeta duplicada con el mismo nombre entre la ruta y los archivos principales.

---

## 28. Paso 2: abrir el proyecto

Una vez copiado el proyecto:

1. Abre Android Studio.
2. Selecciona **File → Open**.
3. Busca `C:\Android\PrimeraAppReconocimientoVoz`.
4. Selecciona la carpeta que contiene `settings.gradle.kts`.
5. Pulsa **OK**.
6. Espera a que Android Studio cargue el proyecto.

Si aparece una solicitud de confianza, acepta únicamente si se trata del proyecto que has copiado y reconoces.

**No abras solamente la carpeta `app`.**

Debemos abrir la raíz del proyecto, donde están los archivos generales de Gradle.

---

## 29. Paso 3: instalar Android SDK API 35

En Android Studio, abre:

**Tools → SDK Manager**

En la pestaña **SDK Platforms**:

1. Busca Android 15.0.
2. Comprueba que corresponde a API Level 35.
3. Marca la plataforma si no está instalada.
4. Pulsa **Apply**.
5. Espera a que termine la instalación.

Puedes conservar otras versiones de Android que ya tengas instaladas.

El proyecto necesita API 35 porque contiene:

```kotlin
compileSdk = 35
```

---

## 30. Paso 4: instalar las herramientas del SDK

En la misma ventana del SDK Manager, entra en **SDK Tools**.

Comprueba que estén instalados:

* Android SDK Build-Tools.
* Android SDK Platform-Tools.
* Android SDK Command-line Tools, si están disponibles.
* Android Emulator, si vas a utilizar un emulador.

Si falta algún componente, selecciónalo y pulsa **Apply**.

### ¿Para qué sirve cada herramienta?

| Herramienta        | Función                                                          |
| ------------------ | ---------------------------------------------------------------- |
| Build-Tools        | Proporciona herramientas para construir aplicaciones Android.    |
| Platform-Tools     | Incluye herramientas como ADB para comunicarse con dispositivos. |
| Command-line Tools | Proporciona utilidades de gestión del SDK.                       |
| Android Emulator   | Permite simular un dispositivo Android en el ordenador.          |

---

## 31. Paso 5: configurar JDK 17

Android Studio necesita un JDK para ejecutar Gradle.

En Windows, abre:

**File → Settings → Build, Execution, Deployment → Build Tools → Gradle**

Busca el campo:

**Gradle JDK**

Selecciona un JDK 17 disponible.

En muchas instalaciones puedes utilizar el JDK incluido con Android Studio, siempre que sea la versión adecuada.

Pulsa **Apply** y después **OK**.

### Recuerda

JDK y Android SDK no son lo mismo.

* JDK 17: entorno Java utilizado por Gradle.
* Android SDK API 35: API de Android utilizada para compilar.

Necesitamos configurar ambos correctamente.

---

## 32. Paso 6: revisar la versión de Gradle

Este paso es importante porque en el error anterior aparecía:

```text
Gradle 9.6.0
```

Sin embargo, nuestro proyecto declara:

```kotlin
id("com.android.application") version "8.7.3" apply false
```

Android Gradle Plugin 8.7 utiliza Gradle 8.9 como versión correspondiente.

Por tanto, debemos comprobar qué versión de Gradle utiliza realmente Android Studio.

### ¿Qué debemos revisar?

* Si el proyecto tiene Gradle Wrapper.
* Si Android Studio ha vinculado correctamente el proyecto.
* Si se está utilizando una instalación global de Gradle.
* Si la versión de Gradle es compatible con el complemento de Android.

**No cambies las versiones al azar.**

Primero hay que comprobar cómo se está ejecutando Gradle.

---

## 34. Paso 8: sincronizar Gradle

Cuando los archivos y las versiones sean correctos, Android Studio debe sincronizar el proyecto.

Busca:

**File → Sync Project with Gradle Files**

Pulsa esa opción si está disponible.

Durante la sincronización, Android Studio puede descargar las bibliotecas que necesita el proyecto.

Es normal que la primera sincronización tarde más tiempo.

### ¿Qué ocurre si falla?

No modifiques varios archivos simultáneamente.

Comprueba primero:

1. La ruta del proyecto.
2. El JDK seleccionado.
3. La versión de Gradle.
4. La configuración de los complementos.
5. La conexión a Internet, si necesita descargar dependencias.

Si vuelve a aparecer un error, copia el mensaje completo para identificar su causa.

---

## 35. Paso 9: crear un dispositivo virtual

Podemos ejecutar la aplicación en un emulador.

En Android Studio, abre:

**Tools → Device Manager**

Después:

1. Pulsa `+` o **Create Virtual Device**.
2. Selecciona un modelo de teléfono, por ejemplo, un Pixel.
3. Pulsa **Next**.
4. Selecciona una imagen del sistema Android compatible.
5. Descarga la imagen si es necesario.
6. Finaliza la creación del dispositivo.

El emulador simula un teléfono Android dentro del ordenador.

Para probar el reconocimiento de voz, debe disponer de un servicio de reconocimiento compatible.

---

## 36. Paso 10: ejecutar la aplicación

Cuando la sincronización haya terminado correctamente:

1. Selecciona la configuración de ejecución `app`.
2. Selecciona el emulador o el móvil conectado.
3. Pulsa el botón verde **Run**.
4. Espera a que se instale la aplicación.
Por eso, este comando puede fallar:

```powershell
.\gradlew.bat --version
```

No se puede ejecutar un archivo que no existe.

### ¿Qué debemos conseguir?

Incorporar un Gradle Wrapper compatible con el proyecto y configurado para utilizar una versión adecuada.

La combinación original prevista es:

| Componente            | Versión |
| --------------------- | ------- |
| Android Gradle Plugin | 8.7.3   |
| Gradle                | 8.9     |
| JDK                   | 17      |
| Android SDK           | API 35  |

Una vez configurado correctamente el Wrapper, podremos comprobar la versión de Gradle desde la terminal.

---

# 34. Paso 8: sincronizar Gradle

Cuando los archivos y las versiones sean correctos, Android Studio debe sincronizar el proyecto.

Busca:

**File → Sync Project with Gradle Files**

Pulsa esa opción si está disponible.

Durante la sincronización, Android Studio puede descargar las bibliotecas que necesita el proyecto.

Es normal que la primera sincronización tarde más tiempo.

### ¿Qué ocurre si falla?

No modifiques varios archivos simultáneamente.

Comprueba primero:

1. La ruta del proyecto.
2. El JDK seleccionado.
3. La versión de Gradle.
4. La configuración de los complementos.
5. La conexión a Internet, si necesita descargar dependencias.

Si vuelve a aparecer un error, copia el mensaje completo para identificar su causa.

---

# 35. Paso 9: crear un dispositivo virtual

Podemos ejecutar la aplicación en un emulador.

En Android Studio, abre:

**Tools → Device Manager**

Después:

1. Pulsa `+` o **Create Virtual Device**.
2. Selecciona un modelo de teléfono, por ejemplo, un Pixel.
3. Pulsa **Next**.
4. Selecciona una imagen del sistema Android compatible.
5. Descarga la imagen si es necesario.
6. Finaliza la creación del dispositivo.

El emulador simula un teléfono Android dentro del ordenador.

Para probar el reconocimiento de voz, debe disponer de un servicio de reconocimiento compatible.

---

# 36. Paso 10: ejecutar la aplicación

Cuando la sincronización haya terminado correctamente:

1. Selecciona la configuración de ejecución `app`.
2. Selecciona el emulador o el móvil conectado.
3. Pulsa el botón verde **Run**.
4. Espera a que se instale la aplicación.
5. Comprueba que se abre la pantalla principal.

Si utilizas un móvil físico, activa las opciones de desarrollador y la depuración USB.

Conecta el dispositivo y acepta la autorización que aparezca en su pantalla.

---

## 37. Paso 11: conceder permiso al micrófono

La primera vez que se utilice el reconocimiento de voz, Android puede solicitar permiso para acceder al micrófono.

Concede el permiso si quieres utilizar esta función.

Si lo deniegas, la aplicación no podrá utilizar el micrófono hasta que se conceda el permiso.

También debes comprobar que el servicio de reconocimiento de voz esté disponible en el dispositivo.

Algunos servicios necesitan conexión a Internet.

---

## 38. Paso 12: probar los comandos

Una vez abierta la aplicación:

1. Mantén pulsado el botón del micrófono.
2. Pronuncia una de las frases admitidas.
3. Comprueba el texto reconocido.
4. Observa si se ejecuta la acción correspondiente.

Prueba estos comandos:

| Comando           | Resultado esperado             |
| ----------------- | ------------------------------ |
| «Inicio»          | Mostrar la pantalla de inicio. |
| «Ir a ajustes»    | Abrir la pantalla de ajustes.  |
| «Modo oscuro»     | Activar el tema oscuro.        |
| «Modo claro»      | Activar el tema claro.         |
| «Mostrar mensaje» | Mostrar un mensaje.            |
| «Abrir diálogo»   | Abrir un cuadro de diálogo.    |
| «Cerrar diálogo»  | Cerrar el cuadro de diálogo.   |
| «Ayuda»           | Mostrar la ayuda implementada. |

Si un comando no funciona, debemos comprobar tanto el texto reconocido como la lógica que interpreta los comandos.

---

## 39. Problemas frecuentes

| Problema                                   | Posible causa                                             | Qué comprobar                                                 |
| ------------------------------------------ | --------------------------------------------------------- | ------------------------------------------------------------- |
| Error por caracteres no ASCII              | Ruta del proyecto con caracteres especiales               | Mover el proyecto a `C:\Android\PrimeraAppReconocimientoVoz`. |
| `Unresolved reference: android`            | Proyecto sin sincronizar o módulo mal configurado         | Revisar Gradle y sincronizar.                                 |
| No aparece la opción de sincronizar        | Proyecto no vinculado correctamente como proyecto Gradle  | Abrir la raíz del proyecto y comprobar la vinculación.        |
| No se encuentra `gradlew.bat`              | Falta el Gradle Wrapper                                   | Incorporar el Wrapper correctamente.                          |
| Error al aplicar `com.android.application` | Incompatibilidad de versiones o problema de configuración | Revisar Android Gradle Plugin, Gradle y JDK.                  |
| No aparece el emulador                     | No se ha creado un dispositivo virtual                    | Abrir Device Manager.                                         |
| La aplicación no reconoce la voz           | Permiso denegado o servicio de voz no disponible          | Revisar permisos y servicio de reconocimiento.                |
| Gradle no descarga dependencias            | Problema de conexión o repositorios                       | Comprobar la conexión y la configuración de repositorios.     |

---
## 40. Resumen de la configuración

Antes de ejecutar el proyecto, comprueba esta tabla.

| Elemento                   | Configuración                                               |
| -------------------------- | ----------------------------------------------------------- |
| Android Studio             | Instalado y preparado para el proyecto.                     |
| Ruta                       | `C:\Android\PrimeraAppReconocimientoVoz`                    |
| Android SDK                | API 35 instalada.                                           |
| SDK Build-Tools            | Instaladas.                                                 |
| Platform-Tools             | Instaladas.                                                 |
| Gradle JDK                 | JDK 17.                                                     |
| Android Gradle Plugin      | 8.7.3.                                                      |
| Gradle                     | 8.9, como versión correspondiente al complemento declarado. |
| Gradle Wrapper             | Debe incorporarse al proyecto.                              |
| Dispositivo                | Emulador o móvil Android.                                   |
| Permiso de micrófono       | Concedido.                                                  |
| Servicio de reconocimiento | Disponible y configurado.                                   |

---
## 41. Orden recomendado de trabajo

Para evitar mezclar problemas, sigue este orden:

1. Mover el proyecto a una ruta sencilla.
2. Abrir la raíz del proyecto en Android Studio.
3. Configurar JDK 17.
4. Instalar Android SDK API 35.
5. Revisar las versiones de Gradle.
6. Incorporar el Gradle Wrapper.
7. Sincronizar el proyecto.
8. Crear un emulador o conectar un móvil.
9. Ejecutar la aplicación.
10. Probar el reconocimiento de voz.

**No es necesario modificar el código Kotlin para resolver un problema de configuración de Gradle.**

Primero debemos conseguir que el proyecto compile.

---

## 42. Conclusiones

La aplicación está organizada siguiendo una separación de responsabilidades.

* `MainActivity.kt` coordina el funcionamiento general.
* `SpeechRecognitionManager.kt` gestiona el reconocimiento de voz.
* `VoiceCommandProcessor.kt` interpreta las frases reconocidas.
* `HomeFragment.kt` gestiona la pantalla de inicio.
* `SettingsFragment.kt` gestiona la pantalla de ajustes.
* Los XML definen la interfaz gráfica.
* `AndroidManifest.xml` declara permisos y componentes.
* Gradle configura y construye la aplicación.

Para ejecutar el proyecto correctamente, necesitamos un entorno compatible y una sincronización satisfactoria.

**El primer objetivo es que Android Studio pueda compilar el proyecto; después comprobaremos que todos los comandos de voz funcionan como esperamos.**

---

<!-- _class: lead -->

# Ficheros

# com.example.reconocimientovoz

## MainActivity.kt

```kotlin
package com.example.reconocimientovoz

import android.Manifest
import android.content.pm.PackageManager
import android.os.Bundle
import android.view.MotionEvent
import android.view.View
import android.view.animation.AccelerateDecelerateInterpolator
import android.animation.ObjectAnimator
import android.animation.PropertyValuesHolder
import android.widget.Toast
import androidx.activity.result.contract.ActivityResultContracts
import androidx.appcompat.app.AlertDialog
import androidx.appcompat.app.AppCompatActivity
import androidx.appcompat.app.AppCompatDelegate
import androidx.core.content.ContextCompat
import androidx.lifecycle.lifecycleScope
import com.example.reconocimientovoz.databinding.ActivityMainBinding
import com.google.android.material.snackbar.Snackbar
import kotlinx.coroutines.launch

class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding
    private lateinit var speechManager: SpeechRecognitionManager
    private val commandProcessor = VoiceCommandProcessor()
    private var listeningAnimator: ObjectAnimator? = null
    private var helpDialog: AlertDialog? = null
    private var isListening = false

    private val requestAudioPermission =
        registerForActivityResult(ActivityResultContracts.RequestPermission()) { granted ->
            if (granted) startListening()
            else showAction("Permiso de micrófono denegado")
        }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        speechManager = SpeechRecognitionManager(this)
        if (savedInstanceState == null) {
            supportFragmentManager.beginTransaction()
                .replace(binding.fragmentContainer.id, HomeFragment())
                .commit()
        }

        binding.btnTheme.setOnClickListener { toggleTheme() }
        binding.fabMicrofono.setOnTouchListener { _, event ->
            when (event.action) {
                MotionEvent.ACTION_DOWN -> {
                    checkPermissionAndStart()
                    true
                }
                MotionEvent.ACTION_UP, MotionEvent.ACTION_CANCEL -> {
                    stopListening()
                    true
                }
                else -> true
            }
        }

        lifecycleScope.launch {
            speechManager.state.collect { state ->
                when (state) {
                    is VoiceState.Idle -> setListeningUi(false, "Micrófono inactivo")
                    is VoiceState.Listening -> setListeningUi(true, "Escuchando…")
                    is VoiceState.Partial -> {
                        setListeningUi(true, "Escuchando…")
                        binding.txtRecognized.text = "Parcial: ${state.text}"
                    }
                    is VoiceState.Result -> {
                        setListeningUi(false, "Reconocimiento completado")
                        binding.txtRecognized.text = "Resultado final: ${state.text}"
                        handleCommand(state.text)
                    }
                    is VoiceState.Error -> {
                        setListeningUi(false, state.message)
                        binding.txtRecognized.text = state.message
                    }
                }
            }
        }
    }

    private fun checkPermissionAndStart() {
        if (ContextCompat.checkSelfPermission(this, Manifest.permission.RECORD_AUDIO) ==
            PackageManager.PERMISSION_GRANTED) {
            startListening()
        } else {
            requestAudioPermission.launch(Manifest.permission.RECORD_AUDIO)
        }
    }

    private fun startListening() {
        isListening = true
        speechManager.startListening()
    }

    private fun stopListening() {
        if (isListening) {
            isListening = false
            speechManager.stopListening()
        }
    }

    private fun setListeningUi(listening: Boolean, status: String) {
        binding.txtListeningStatus.text = status
        if (listening) {
            binding.listeningCircle.setBackgroundResource(R.drawable.circle_listening)
            if (listeningAnimator == null) {
                val sx = PropertyValuesHolder.ofFloat(View.SCALE_X, 1f, 1.45f, 1f)
                val sy = PropertyValuesHolder.ofFloat(View.SCALE_Y, 1f, 1.45f, 1f)
                listeningAnimator = ObjectAnimator.ofPropertyValuesHolder(binding.listeningCircle, sx, sy).apply {
                    duration = 850
                    repeatCount = ObjectAnimator.INFINITE
                    interpolator = AccelerateDecelerateInterpolator()
                }
            }
            if (listeningAnimator?.isStarted != true) listeningAnimator?.start()
        } else {
            listeningAnimator?.cancel()
            binding.listeningCircle.scaleX = 1f
            binding.listeningCircle.scaleY = 1f
            binding.listeningCircle.setBackgroundResource(R.drawable.circle_idle)
        }
    }

    private fun handleCommand(text: String) {
        when (commandProcessor.process(text)) {
            VoiceCommand.GoHome -> {
                navigate(HomeFragment())
                showAction("Navegación: inicio")
            }
            VoiceCommand.GoSettings -> {
                navigate(SettingsFragment())
                showAction("Navegación: ajustes")
            }
            VoiceCommand.DarkTheme -> {
                AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_YES)
                showAction("Tema oscuro activado")
            }
            VoiceCommand.LightTheme -> {
                AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_NO)
                showAction("Tema claro activado")
            }
            VoiceCommand.ShowMessage -> {
                Snackbar.make(binding.root, "¡Comando de voz ejecutado correctamente!", Snackbar.LENGTH_LONG).show()
                showAction("Se ha mostrado un mensaje")
            }
            VoiceCommand.OpenDialog -> {
                showCommandDialog()
                showAction("Diálogo abierto")
            }
            VoiceCommand.CloseDialog -> {
                if (helpDialog?.isShowing == true) {
                    helpDialog?.dismiss()
                    showAction("Diálogo cerrado")
                } else {
                    showAction("No hay ningún diálogo abierto")
                }
            }
            VoiceCommand.Help -> {
                showHelpDialog()
                showAction("Ayuda mostrada")
            }
            VoiceCommand.Unknown -> {
                showAction("Comando no reconocido: \"$text\". Di «ayuda» para ver los comandos.")
            }
        }
    }

    private fun navigate(fragment: androidx.fragment.app.Fragment) {
        supportFragmentManager.beginTransaction()
            .replace(binding.fragmentContainer.id, fragment)
            .commit()
    }

    private fun toggleTheme() {
        val current = AppCompatDelegate.getDefaultNightMode()
        val dark = current == AppCompatDelegate.MODE_NIGHT_YES ||
            (current == AppCompatDelegate.MODE_NIGHT_FOLLOW_SYSTEM &&
                (resources.configuration.uiMode and android.content.res.Configuration.UI_MODE_NIGHT_MASK) ==
                android.content.res.Configuration.UI_MODE_NIGHT_YES)
        AppCompatDelegate.setDefaultNightMode(
            if (dark) AppCompatDelegate.MODE_NIGHT_NO else AppCompatDelegate.MODE_NIGHT_YES
        )
    }

    private fun showCommandDialog() {
        helpDialog?.dismiss()
        helpDialog = AlertDialog.Builder(this)
            .setTitle("Diálogo de ejemplo")
            .setMessage("Este diálogo se ha abierto mediante un comando de voz. Di «cerrar diálogo» para cerrarlo.")
            .setPositiveButton("Cerrar") { dialog, _ -> dialog.dismiss() }
            .create()
        helpDialog?.show()
    }

    private fun showHelpDialog() {
        helpDialog?.dismiss()
        helpDialog = AlertDialog.Builder(this)
            .setTitle("Comandos disponibles")
            .setMessage(
                "• Inicio / ir a inicio\\n" +
                "• Ajustes / ir a ajustes\\n" +
                "• Tema oscuro / tema claro\\n" +
                "• Mostrar mensaje\\n" +
                "• Abrir diálogo / cerrar diálogo\\n" +
                "• Ayuda"
            )
            .setPositiveButton("Entendido", null)
            .create()
        helpDialog?.show()
    }

    private fun showAction(message: String) {
        binding.txtLastAction.text = "Acción: $message"
    }

    override fun onDestroy() {
        listeningAnimator?.cancel()
        helpDialog?.dismiss()
        speechManager.destroy()
        super.onDestroy()
    }
}

```

## HomeFragment.kt

```kotlin
package com.example.reconocimientovoz

import android.os.Bundle
import android.view.View
import androidx.fragment.app.Fragment
import com.example.reconocimientovoz.databinding.FragmentHomeBinding
import com.google.android.material.snackbar.Snackbar

class HomeFragment : Fragment(R.layout.fragment_home) {
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        val binding = FragmentHomeBinding.bind(view)
        binding.btnShowMessage.setOnClickListener {
            Snackbar.make(view, "¡Hola! Este es el mensaje de ejemplo.", Snackbar.LENGTH_LONG).show()
        }
        binding.btnOpenDialog.setOnClickListener {
            androidx.appcompat.app.AlertDialog.Builder(requireContext())
                .setTitle("Diálogo de ejemplo")
                .setMessage("Este diálogo se ha abierto desde el fragmento Inicio.")
                .setPositiveButton("Cerrar", null)
                .show()
        }
    }
}

```

## SettingsFragment.kt

```kotlin
package com.example.reconocimientovoz

import android.os.Bundle
import android.view.View
import androidx.fragment.app.Fragment
import com.example.reconocimientovoz.databinding.FragmentSettingsBinding

class SettingsFragment : Fragment(R.layout.fragment_settings) {
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        val binding = FragmentSettingsBinding.bind(view)
        binding.btnBackHome.setOnClickListener {
            parentFragmentManager.beginTransaction()
                .replace(R.id.fragmentContainer, HomeFragment())
                .commit()
        }
    }
}

```

## SpeechRecognitionManager.kt

```Kotlin
package com.example.reconocimientovoz

import android.content.Context
import android.content.Intent
import android.os.Bundle
import android.speech.RecognitionListener
import android.speech.RecognizerIntent
import android.speech.SpeechRecognizer
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import java.util.Locale

sealed class VoiceState {
    data object Idle : VoiceState()
    data object Listening : VoiceState()
    data class Partial(val text: String) : VoiceState()
    data class Result(val text: String) : VoiceState()
    data class Error(val message: String) : VoiceState()
}

class SpeechRecognitionManager(context: Context) {
    private val appContext = context.applicationContext
    private var recognizer: SpeechRecognizer? = null

    private val _state = MutableStateFlow<VoiceState>(VoiceState.Idle)
    val state: StateFlow<VoiceState> = _state.asStateFlow()

    fun isAvailable(): Boolean = SpeechRecognizer.isRecognitionAvailable(appContext)

    fun startListening() {
        if (!isAvailable()) {
            _state.value = VoiceState.Error("No hay un servicio de reconocimiento de voz instalado.")
            return
        }

        try {
            if (recognizer == null) {
                recognizer = SpeechRecognizer.createSpeechRecognizer(appContext).also { sr ->
                    sr.setRecognitionListener(object : RecognitionListener {
                        override fun onReadyForSpeech(params: Bundle?) {
                            _state.value = VoiceState.Listening
                        }
                        override fun onBeginningOfSpeech() {
                            _state.value = VoiceState.Listening
                        }
                        override fun onRmsChanged(rmsdB: Float) {}
                        override fun onBufferReceived(buffer: ByteArray?) {}
                        override fun onEndOfSpeech() {
                            // Se mantiene el estado hasta recibir resultado/error.
                        }
                        override fun onError(error: Int) {
                            val message = when (error) {
                                SpeechRecognizer.ERROR_AUDIO -> "Error de audio."
                                SpeechRecognizer.ERROR_CLIENT -> "Reconocimiento interrumpido."
                                SpeechRecognizer.ERROR_INSUFFICIENT_PERMISSIONS -> "Falta permiso para usar el micrófono."
                                SpeechRecognizer.ERROR_NETWORK -> "Error de red."
                                SpeechRecognizer.ERROR_NETWORK_TIMEOUT -> "Tiempo de espera de red agotado."
                                SpeechRecognizer.ERROR_NO_MATCH -> "No se ha entendido el comando. Inténtalo otra vez."
                                SpeechRecognizer.ERROR_RECOGNIZER_BUSY -> "El reconocedor está ocupado."
                                SpeechRecognizer.ERROR_SPEECH_TIMEOUT -> "No se ha detectado voz."
                                else -> "Error de reconocimiento ($error)."
                            }
                            _state.value = VoiceState.Error(message)
                        }
                        override fun onResults(results: Bundle?) {
                            val matches = results?.getStringArrayList(SpeechRecognizer.RESULTS_RECOGNITION)
                            val text = matches?.firstOrNull()
                            _state.value = if (text.isNullOrBlank()) {
                                VoiceState.Error("No se ha obtenido ningún resultado.")
                            } else {
                                VoiceState.Result(text)
                            }
                        }
                        override fun onPartialResults(partialResults: Bundle?) {
                            val matches = partialResults?.getStringArrayList(SpeechRecognizer.RESULTS_RECOGNITION)
                            matches?.firstOrNull()?.let { _state.value = VoiceState.Partial(it) }
                        }
                        override fun onEvent(eventType: Int, params: Bundle?) {}
                    })
                }
            }

            val intent = Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH).apply {
                putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, RecognizerIntent.LANGUAGE_MODEL_FREE_FORM)
                putExtra(RecognizerIntent.EXTRA_LANGUAGE, "es-ES")
                putExtra(RecognizerIntent.EXTRA_LANGUAGE_PREFERENCE, "es-ES")
                putExtra(RecognizerIntent.EXTRA_PARTIAL_RESULTS, true)
                putExtra(RecognizerIntent.EXTRA_MAX_RESULTS, 3)
                putExtra(RecognizerIntent.EXTRA_PROMPT, "Di un comando, por ejemplo: ir a ajustes")
            }
            _state.value = VoiceState.Listening
            recognizer?.startListening(intent)
        } catch (e: SecurityException) {
            _state.value = VoiceState.Error("No hay permiso para usar el micrófono.")
        } catch (e: Exception) {
            _state.value = VoiceState.Error("No se pudo iniciar el reconocimiento: ${e.localizedMessage ?: "error"}")
        }
    }

    fun stopListening() {
        try {
            recognizer?.stopListening()
        } catch (_: Exception) {
            _state.value = VoiceState.Idle
        }
    }

    fun destroy() {
        recognizer?.destroy()
        recognizer = null
        _state.value = VoiceState.Idle
    }
}

```

## VoiceCommandProcessor.kt

```kotlin
package com.example.reconocimientovoz

import java.text.Normalizer
import java.util.Locale

sealed class VoiceCommand {
    data object GoHome : VoiceCommand()
    data object GoSettings : VoiceCommand()
    data object DarkTheme : VoiceCommand()
    data object LightTheme : VoiceCommand()
    data object ShowMessage : VoiceCommand()
    data object OpenDialog : VoiceCommand()
    data object CloseDialog : VoiceCommand()
    data object Help : VoiceCommand()
    data object Unknown : VoiceCommand()
}

class VoiceCommandProcessor {
    fun process(text: String): VoiceCommand {
        val normalized = Normalizer.normalize(text.lowercase(Locale("es", "ES")), Normalizer.Form.NFD)
            .replace("\\p{Mn}+".toRegex(), "")
            .trim()

        return when {
            normalized.contains("inicio") || normalized.contains("pantalla principal") ||
                normalized == "home" -> VoiceCommand.GoHome
            normalized.contains("ajustes") || normalized.contains("configuracion") ||
                normalized.contains("configuración") -> VoiceCommand.GoSettings
            normalized.contains("tema oscuro") || normalized.contains("modo oscuro") ||
                normalized == "oscuro" -> VoiceCommand.DarkTheme
            normalized.contains("tema claro") || normalized.contains("modo claro") ||
                normalized == "claro" -> VoiceCommand.LightTheme
            normalized.contains("mostrar mensaje") || normalized == "mensaje" ||
                normalized.contains("ensename un mensaje") -> VoiceCommand.ShowMessage
            normalized.contains("abrir dialogo") || normalized.contains("abre dialogo") ||
                normalized.contains("abrir cuadro") -> VoiceCommand.OpenDialog
            normalized.contains("cerrar dialogo") || normalized.contains("cierra dialogo") ||
                normalized.contains("cerrar cuadro") -> VoiceCommand.CloseDialog
            normalized.contains("ayuda") || normalized.contains("comandos") -> VoiceCommand.Help
            else -> VoiceCommand.Unknown
        }
    }
}

```


# res > layout

## activity_main.xml

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="16dp">

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:gravity="center_vertical"
        android:orientation="horizontal">

        <View
            android:id="@+id/listeningCircle"
            android:layout_width="20dp"
            android:layout_height="20dp"
            android:background="@drawable/circle_idle" />

        <TextView
            android:id="@+id/txtListeningStatus"
            android:layout_width="0dp"
            android:layout_height="wrap_content"
            android:layout_marginStart="10dp"
            android:layout_weight="1"
            android:text="Micrófono inactivo"
            android:textSize="16sp" />

        <com.google.android.material.button.MaterialButton
            android:id="@+id/btnTheme"
            style="@style/Widget.Material3.Button.OutlinedButton"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Tema" />
    </LinearLayout>

    <TextView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginTop="12dp"
        android:text="Texto reconocido (parcial y final)"
        android:textStyle="bold"
        android:textSize="16sp" />

    <TextView
        android:id="@+id/txtRecognized"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:minHeight="54dp"
        android:layout_marginTop="6dp"
        android:background="?attr/colorSurfaceVariant"
        android:padding="12dp"
        android:text="Aquí aparecerá lo que digas…"
        android:textSize="16sp" />

    <TextView
        android:id="@+id/txtLastAction"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginTop="8dp"
        android:text="Acción: ninguna"
        android:textSize="14sp" />

    <FrameLayout
        android:id="@+id/fragmentContainer"
        android:layout_width="match_parent"
        android:layout_height="0dp"
        android:layout_marginTop="10dp"
        android:layout_weight="1" />

    <com.google.android.material.button.MaterialButton
        android:id="@+id/fabMicrofono"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Mantener para hablar"
        android:textSize="16sp"
        app:icon="@android:drawable/ic_btn_speak_now"
        app:iconGravity="textStart" />

    <TextView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginTop="4dp"
        android:gravity="center"
        android:text="Mantén pulsado el botón mientras das el comando"
        android:textSize="12sp" />
</LinearLayout>

```

## fragment_home.xml

```xml

<?xml version="1.0" encoding="utf-8"?>
<ScrollView xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent">
    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="vertical"
        android:padding="16dp">
        <TextView
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:text="Pantalla de inicio"
            android:textSize="26sp"
            android:textStyle="bold" />
        <TextView
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:layout_marginTop="12dp"
            android:text="Prueba a decir: «ir a ajustes», «tema oscuro», «mostrar mensaje» o «abrir diálogo»."
            android:textSize="17sp" />
        <com.google.android.material.button.MaterialButton
            android:id="@+id/btnShowMessage"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:layout_marginTop="18dp"
            android:text="Mostrar mensaje" />
        <com.google.android.material.button.MaterialButton
            android:id="@+id/btnOpenDialog"
            style="@style/Widget.Material3.Button.OutlinedButton"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:text="Abrir diálogo" />
    </LinearLayout>
</ScrollView>

```

## fragment_settings.xml

```xml

<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="16dp">
    <TextView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Ajustes"
        android:textSize="26sp"
        android:textStyle="bold" />
    <TextView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginTop="12dp"
        android:text="Esta es la segunda pantalla. Puedes volver diciendo «inicio»."
        android:textSize="17sp" />
    <com.google.android.material.button.MaterialButton
        android:id="@+id/btnBackHome"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginTop="18dp"
        android:text="Volver a inicio" />
</LinearLayout>

```