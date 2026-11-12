# Compatibilidad con planes gratuitos

Regla fundamental: todo el curso se completa con el plan gratuito de los asistentes de IA más comunes, sin tarjeta ni funciones de pago. Los límites cambian a menudo y no siempre se publican, así que el curso se diseña contra el caso más restrictivo observado y no contra un producto concreto.

## Presupuesto de diseño

Todo archivo nuevo o modificado debe cumplirlo.

| Recurso | Límite |
| --- | --- |
| «Prompt para tu asistente» y prompt de revisión | 1.200 palabras como máximo, rúbrica incluida |
| Entregable de un ejercicio | 600 palabras como máximo, pegado como texto |
| Documento de trabajo (E5, E6) | 2 páginas como máximo, pegado como texto |
| Archivos adjuntos obligatorios | Ninguno |
| Funciones obligatorias | Solo chat de texto: sin búsqueda web, imágenes, voz, memoria, proyectos ni ejecución de código |
| Pago, tarjeta o prueba temporal | Nunca |

## Aviso al alumno

Al empezar la Lección 1, el tutor avisa de que los planes gratuitos limitan los mensajes, que la cuota cambia y puede agotarse a mitad de lección, y de que la tarjeta permite seguir en otro chat. No se promete un número fijo de mensajes.

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

No hay un número fijo de mensajes por sesión ni por lección: reparte la lección en las sesiones que necesites. Una revisión completa de un ejercicio cabe en un intercambio; el protocolo de dos intentos consume cuatro mensajes.

## Qué evitar al escribir contenido

- Pedir que el asistente «busque en internet» o «abra» un documento: se pide al alumno que lo haga y pegue el resultado.
- Pedir imágenes, voz o archivos adjuntos.
- Depender de que el asistente recuerde conversaciones anteriores: la tarjeta lo sustituye.
- Fijar un número de mensajes por sesión: las cuotas cambian y no son iguales en todos los asistentes.
- Exigir una tabla Markdown como único formato: acepta una lista con los mismos campos y no penalices el formato.
- Prompts largos con ejemplos innecesarios: cada palabra cuenta contra el contexto disponible.
- Nombres de herramientas en el temario: esta matriz es el único sitio donde aparecen.

## Matriz de compatibilidad

Última comprobación: **12 de noviembre de 2026**, con las páginas de ayuda oficiales de cada proveedor. Ningún proveedor publica un número fijo de mensajes del plan gratuito y todos avisan de que los límites cambian: por eso el curso no promete cifras. Revisar cada trimestre. Usa solo fuentes oficiales en esta tabla.

| Asistente (plan gratuito) | Límite observado | Efecto en el curso |
| --- | --- | --- |
| Claude | Límite por sesión que se renueva cada cinco horas; el límite y la ventana de contexto varían según la demanda ([fuente](https://support.claude.com/en/articles/8602283-about-free-claude-usage)) | Sesiones cortas; prompts cortos |
| ChatGPT | El modelo y los límites del plan gratuito cambian con el tiempo; subir archivos, imágenes y análisis de datos tienen límites propios ([fuente](https://help.openai.com/en/articles/9275245-chatgpt-free-tier-faq)) | Cero adjuntos obligatorios |
| Gemini | Límites por plan que pueden cambiar; la capacidad se renueva periódicamente ([fuente](https://support.google.com/gemini/answer/16275805)) | Poder parar y retomar; tarjeta de continuidad |
| OpenCode | Modelos gratuitos sin cuenta y con lista cambiante; los datos se guardan cuando se usan esos modelos gratuitos ([fuente](https://opencode.ai/), [modelos](https://opencode.ai/docs/zen)) | Ninguna lección depende de un modelo concreto; con estos modelos, el aviso de privacidad pesa todavía más |

## Cuando cambie un límite

1. Actualizar la fila de la matriz con fecha y fuente.
2. Si el límite empeora respecto al presupuesto, revisar primero los prompts más largos y las sesiones que más mensajes consumen.
3. Subir la `version` de los archivos modificados (ver [`translation.md`](translation.md)).
4. Registrar el cambio en [`translation-status.md`](translation-status.md) cuando afecte a ambos idiomas.
