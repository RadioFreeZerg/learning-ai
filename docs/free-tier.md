# Compatibilidad con planes gratuitos

Regla fundamental: todo el curso se completa con el plan gratuito de los asistentes de IA más comunes, sin tarjeta ni funciones de pago. Los límites cambian a menudo y no siempre se publican, así que el curso se diseña contra el caso más restrictivo observado y no contra un producto concreto.

## Presupuesto de diseño

Todo archivo nuevo o modificado debe cumplirlo.

| Recurso | Límite |
| --- | --- |
| Mensajes del alumno por sesión | 12 como máximo |
| Sesiones por lección | 2 a 4 sesiones cortas, cada una en un chat nuevo |
| «Prompt para tu asistente» y prompt de revisión | 1.200 palabras como máximo, rúbrica incluida |
| Conversación completa de una sesión | 8.000 palabras como máximo |
| Entregable de un ejercicio | 600 palabras como máximo, pegado como texto |
| Documento de trabajo (E5, E6) | 2 páginas como máximo, pegado como texto |
| Archivos adjuntos obligatorios | Ninguno |
| Funciones obligatorias | Solo chat de texto: sin búsqueda web, imágenes, voz, memoria, proyectos ni ejecución de código |
| Pago, tarjeta o prueba temporal | Nunca |

## Tarjeta de continuidad

Cada sesión termina con una tarjeta de 150 palabras como máximo. El alumno la guarda y la pega al abrir el chat siguiente, en el mismo asistente o en otro. Es texto pegado, no un archivo ni una función del asistente: funciona en cualquier chat, también en los planes gratuitos. Algunos asistentes tienen memoria, pero no está garantizada ni conserva el estado exacto de intentos y avisos; la tarjeta es el respaldo que controla el alumno. Con acceso a archivos, `progress.json` cumple esa función; la tarjeta es la versión portátil para chats sin archivos. Formato:

```text
TARJETA DE CONTINUIDAD
Perfil: idioma=es; rol=...; profundidad=...; accesibilidad=...
Progreso: Lección 1=ok Lección 2=ok Lección 3=doing | E1=ok
Punto actual: Lección 3, parte 2 de 3; falta: la actividad guiada
Siguiente paso: abrir un chat nuevo, pegar esta tarjeta en el prompt de la lección y enviarlo
```

### Línea de progreso

| Código | Lección | Ejercicio |
| --- | --- | --- |
| `ok` | `completed` | `passed` |
| `warn` | `completed_with_warning` | `passed_with_warning` |
| `doing` | `in_progress` | `in_progress` |
| `skip` | `skipped` | `skipped` |
| (omitida) | `not_started` | `not_started` |

Un ejercicio con aviso se escribe con su identificador: `E3=warn(w001)`.

## Estructura de una sesión corta

1. El alumno pega la tarjeta en el prompt de la lección (en la primera sesión, el prompt de la Lección 1 se pega sin tarjeta).
2. El tutor resume el punto actual en dos frases y propone el objetivo de la sesión.
3. Trabajo en bloques pequeños: concepto, ejemplo, actividad.
4. Cierre: comprobación (si la lección la tiene), revisión del ejercicio, bloque de progreso y tarjeta nueva.

Con 12 mensajes del alumno como máximo, una lección se reparte en 2 a 4 sesiones. Una revisión completa de un ejercicio cabe en un intercambio; el protocolo de dos intentos consume cuatro mensajes.

## Qué evitar al escribir contenido

- Pedir que el asistente «busque en internet» o «abra» un documento: se pide al alumno que lo haga y pegue el resultado.
- Pedir imágenes, voz o archivos adjuntos.
- Depender de que el asistente recuerde conversaciones anteriores: la tarjeta lo sustituye.
- Prompts largos con ejemplos innecesarios: cada palabra cuenta contra el contexto disponible.
- Nombres de herramientas en el temario: esta matriz es el único sitio donde aparecen.

## Matriz de compatibilidad

Última comprobación: **11 de noviembre de 2026**. Las cifras son orientativas: proceden de fuentes secundarias, no de las páginas oficiales de cada proveedor, y deben verificarse con ellas antes de cambiar el presupuesto. Revisar cada trimestre.

| Asistente (plan gratuito) | Límite observado | Efecto en el curso |
| --- | --- | --- |
| Claude | Unos 15–40 mensajes por ventana de 5 horas, variable según la demanda y la longitud de los mensajes ([fuente](https://www.heyuan110.com/posts/ai/2026-07-08-claude-free-tier-limits/)); el tope depende de los tokens, no de un número fijo ([fuente](https://daehnhardt.com/blog/2026/05/21/claude-pro-vs-free/)) | Sesiones de 12 mensajes o menos; prompts cortos |
| ChatGPT | Chats de texto sin tope desde agosto de 2026; archivos e imágenes con límite ([fuente](https://engadget.com/2234173/chatgpt-free-features-2026)); unos 3 archivos al día ([fuente](https://blog.laozhang.ai/en/posts/chatgpt-file-upload-limits-free-plus-pro)) | Cero adjuntos obligatorios |
| Gemini | Ventana de contexto de 32.000 tokens ([fuente](https://dupple.com/learn/is-gemini-free)); límites por cómputo que se renuevan cada 5 horas dentro de un tope semanal ([fuente](https://aiplanfinder.com/gemini-usage-limits)) | Conversación completa de una sesión por debajo de 8.000 palabras; poder parar y retomar |
| OpenCode | Modelos gratuitos sin registro, con límites por IP y lista cambiante ([fuente](https://learnopencode.com/en/1-start/04a-free-models)) | Ninguna lección depende de un modelo concreto |

## Cuando cambie un límite

1. Actualizar la fila de la matriz con fecha y fuente.
2. Si el límite empeora respecto al presupuesto, revisar primero los prompts más largos y las sesiones que más mensajes consumen.
3. Subir la `version` de los archivos modificados (ver [`translation.md`](translation.md)).
4. Registrar el cambio en [`translation-status.md`](translation-status.md) cuando afecte a ambos idiomas.
