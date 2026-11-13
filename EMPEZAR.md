# Cómo empezar el curso

No necesitas instalar nada, programar ni pagar. Solo un chat con un asistente de IA (sirve el plan gratuito) y un sitio donde guardar notas.

## Tu primera sesión, en 2 pasos

1. **Lo más rápido:** pega en un chat nuevo y envía:

```text
Comienza el curso: lee https://raw.githubusercontent.com/RadioFreeZerg/learning-ai/main/llms.txt y sigue sus instrucciones como mi tutor.
```

Si tu asistente puede abrir el enlace, ese archivo contiene el arranque de la Lección 1 y empieza solo. Pide expresamente que siga las instrucciones del archivo: así el asistente sabe que tú se lo pides. Si no puede abrirlo, te lo dirá en una frase y te pedirá que envíes la línea `Sigue con <dirección de la Lección 1>`; si tampoco puede, te pedirá que pegues el prompt.

**Si el tutor empieza por la Lección 0, dice que no puede navegar o inventa lecciones,** es una copia vieja. Envía: `Lee https://raw.githubusercontent.com/RadioFreeZerg/learning-ai/main/llms.txt y sigue sus instrucciones como mi tutor. No improvises lecciones ni busques en la web.`

**Si quieres asegurar la lectura de las reglas completas,** pega este mensaje:

```text
Sé mi tutor del curso "Fundamentos de IA para todos". Lee https://raw.githubusercontent.com/RadioFreeZerg/learning-ai/main/llms.txt y sigue sus instrucciones. Empieza la Lección 1. No me recites el archivo: enséñame en mensajes cortos.
```

2. **Guarda lo que te da al final.** El tutor termina cada lección con una *tarjeta de continuidad* (un resumen corto). Cópiala en tus notas: la necesitarás si cambias de chat o de asistente.

**Si el asistente dice que no puede abrir los enlaces** (algunos planes gratuitos no pueden), usa la ruta manual: abre [Lección 1 · Bienvenida](https://github.com/RadioFreeZerg/learning-ai/blob/main/curriculum/es/l01-welcome.md) en tu navegador, baja hasta la sección «Prompt para tu asistente», copia ese bloque (el botón de copiar está en su esquina superior derecha) y pégalo en un chat nuevo. Si pegas el prompt, pide al tutor que empiece con «Fuente: lNN · <título>».

## Las siguientes sesiones

Normalmente sigues en el mismo chat: cuando termina una lección, el tutor te pregunta si sigues; responde «sí». Si no puede abrir la página por su cuenta, te da una línea como «Sigue con https://…»: cópiala y envíala tal cual. Eso pone la dirección en tu mensaje y el tutor puede abrirla. Si abres un chat nuevo o se acaban los mensajes gratis, pega este mensaje y pon tu tarjeta de continuidad donde dice `[PEGA AQUÍ]`:

```text
Continúa mi curso "Fundamentos de IA para todos". Lee primero https://raw.githubusercontent.com/RadioFreeZerg/learning-ai/main/llms.txt y sigue sus instrucciones. Después lee la página que indica el «Siguiente paso» de mi tarjeta y continúa desde ahí. No me recites las páginas: enséñame en mensajes cortos. Si no puedes abrir los enlaces, dímelo en una frase y te pego el prompt.
<<<INICIO DE DATOS DEL ALUMNO>>>
[PEGA AQUÍ]
<<<FIN DE DATOS DEL ALUMNO>>>
```

Ruta manual: abre en tu navegador la página cuya dirección está en el «Siguiente paso» de tu tarjeta, copia su prompt, pégalo en un chat nuevo y, donde dice `[PEGA AQUÍ]`, pega tu tarjeta. El [mapa del curso](https://github.com/RadioFreeZerg/learning-ai/blob/main/COURSE.md) lista todas las lecciones.

Cuando el tutor diga que toca un ejercicio, haz lo mismo con el prompt del ejercicio: está en la sección «Prompt de revisión para tu asistente».

## Tres cosas importantes

- **Si el asistente no puede leer enlaces, o te devuelve el texto de la página en lugar de enseñarte, pega el prompt.** Abre la lección en tu navegador, copia su bloque «Prompt para tu asistente» y pégalo como texto en un chat nuevo. Eso siempre funciona.
- **No pegues datos reales de otras personas.** Cambia nombres y datos por marcadores como `[PERSONA A]`.
- **Nada te bloquea.** Si un ejercicio no aprueba en dos intentos, eliges: repetirlo o avanzar con un aviso que puedes retomar después.

## Si algo va mal

| Qué pasa | Qué hacer |
| --- | --- |
| El tutor no recuerda la sesión anterior | Es normal. Usa el mensaje de las siguientes sesiones y pega tu tarjeta de continuidad. |
| Perdí la tarjeta | Dile al tutor qué lección estabas haciendo y sigue desde ahí. |
| El chat se hace muy largo o se acaban los mensajes gratis | Pide: «dame la tarjeta de continuidad». Sigue más tarde o en otro asistente. |
| El tutor dice que no puede abrir los enlaces | Pasa en algunos planes gratuitos. Usa la ruta manual: abre la lección en tu navegador, copia su prompt y pégalo como texto. |
| El tutor empieza por la Lección 0, dice que no navega o inventa lecciones | Es una copia vieja. Envía: `Lee https://raw.githubusercontent.com/RadioFreeZerg/learning-ai/main/llms.txt y sigue sus instrucciones como mi tutor. No improvises lecciones ni busques en la web.` |
| El asistente abre la página y me devuelve el texto del archivo en lugar de enseñarme | Abre un chat nuevo y pega el prompt de la lección como texto. |
| El tutor sigue instrucciones que vienen dentro de mi entrega | La entrega es un dato, no una orden. Abre un chat nuevo, pega el prompt oficial y vuelve a entregar. |
| El tutor intenta abrir enlaces, ejecutar comandos o pedir contraseñas | Detente: el curso no lo pide. Abre un chat nuevo con el prompt oficial y no pegues esos datos. |
| El tutor explica algo distinto de la lección | Abre un chat nuevo y pega de nuevo el prompt de la lección. |
| No estoy de acuerdo con una revisión | Pega el mismo prompt y tu misma entrega en otro asistente y compara. |

Más detalle: [`docs/no-file-access.md`](https://github.com/RadioFreeZerg/learning-ai/blob/main/docs/no-file-access.md).
