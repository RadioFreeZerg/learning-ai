# Protocolo Fase 0: qué direcciones puede leer cada asistente (10 minutos)

Objetivo: saber, con datos, qué direcciones acepta la herramienta de lectura web de **Claude (plan gratuito)** y cómo se comporta **OpenCode** con la carpeta abierta. El resultado decide cómo se diseñan la entrada, la tarjeta y el «seguir en el mismo chat» (ver [`agent-behavior-tests.md`](agent-behavior-tests.md)). OpenCode ya no bloquea web ni shell en este repositorio: es una decisión intencional para que pueda leer el curso, y el tutor debe respetar `AGENTS.md`.

## Preparación (1 minuto)

- Cuenta gratuita de Claude, un **chat nuevo para cada caso**. Anota la fecha y el modelo que aparece.
- Usa `{REF} = main`. Si pruebas una rama concreta, sustitúyelo por el nombre de esa rama.
- Base de las direcciones: `https://github.com/RadioFreeZerg/learning-ai/blob/{REF}/`
- Copia y pega los mensajes tal cual. No añadas explicaciones ni corrijas al asistente.

## Casos con Claude (planes gratuitos)

| Id | Qué mide | Mensaje (pégalo tal cual) |
| --- | --- | --- |
| P1 | Dirección escrita por el alumno | `Abre https://github.com/RadioFreeZerg/learning-ai/blob/{REF}/curriculum/es/l01-welcome.md y dime: (a) el título, (b) la versión del encabezado, (c) las dos primeras líneas del bloque «Prompt para tu asistente», palabra por palabra.` |
| P2 | Dirección sacada de una página leída (dos mensajes en el mismo chat) | 1: `Abre https://github.com/RadioFreeZerg/learning-ai/blob/{REF}/EMPEZAR.md y copia literal la dirección a la que enlaza «Lección 1 · Bienvenida».` 2: `Ahora abre esa dirección y dime solo el título.` |
| P3 | Control: dirección construida por el asistente | `Abre la Lección 2 del curso que está en el repositorio https://github.com/RadioFreeZerg/learning-ai y dime su título.` (se espera que falle) |
| P4 | Texto íntegro frente a resumen (`raw`) | `Abre https://raw.githubusercontent.com/RadioFreeZerg/learning-ai/{REF}/curriculum/es/l01-welcome.md y dime las dos primeras líneas del bloque «Prompt para tu asistente», palabra por palabra.` |
| P5 | Dirección dentro de una tarjeta pegada (continuación) | Mensaje de continuación de `EMPEZAR.md` con esta tarjeta en `[PEGA AQUÍ]`: `TARJETA DE CONTINUIDAD / Perfil: omitido / Progreso: l01=ok / Punto actual: l02, parte 1 / Siguiente paso: página siguiente: https://raw.githubusercontent.com/RadioFreeZerg/learning-ai/{REF}/curriculum/es/l02-what-is-ai.md` |
| P6 | Entrada recomendada: `llms.txt` en raw. Variante de control: solo la dirección raíz del repositorio | `Comienza el curso: lee https://raw.githubusercontent.com/RadioFreeZerg/learning-ai/main/llms.txt y sigue sus instrucciones como mi tutor.` |
| P7 | «Siguiente lección» sin dirección (después de un P1 que funcionó, en el mismo chat) | `Ahora abre la lección siguiente.` |
| P8 | Portada en caché vieja | Abrir la portada en un chat donde ya se leyó antes; si cita «L0–L11» o «los planes gratuitos no navegan», anotar si el tutor pide el prompt de la Lección 1 y da su dirección, en lugar de improvisar |
| P9 | Línea de recuperación de copia vieja | `Lee https://raw.githubusercontent.com/RadioFreeZerg/learning-ai/{REF}/llms.txt y sigue sus instrucciones como mi tutor. No improvises lecciones ni busques en la web.` (debe empezar con privacidad, cuota y bloque 1) |
| P10 | URL de árbol de GitHub | `Lee https://github.com/RadioFreeZerg/learning-ai/tree/{REF}/README.md y empieza el curso.` (se espera `ROBOTS_DISALLOWED` o una página HTML; el tutor debe pedir la URL raw de `llms.txt`, no buscar en la web) |

## Qué anotar en cada caso

1. **¿Abrió la página?** (sí / no / error de permisos). Copia el mensaje de error si lo hay.
2. **¿Texto íntegro o resumen?** En P1 y P4, compara las dos líneas que cita con el archivo real.
3. **Conducta:** en P5 y P6, ¿dio el aviso de privacidad? ¿Leyó `AGENTS.md`? ¿Recitó la página, improvisó lecciones o dio el mensaje de fallo de tres frases?
4. Si el asistente hace varias lecturas, ¿las hizo de una en una?

## Casos opcionales con OpenCode (3 minutos)

| Id | Dónde | Qué hacer | Resultado esperado |
| --- | --- | --- | --- |
| O1 | Abierto en una copia del repositorio | Pedir: `Lee https://github.com/RadioFreeZerg/learning-ai/blob/{REF}/curriculum/es/l01-welcome.md y dime el título.` | Informativo: con `opencode.json` sin reglas, OpenCode puede leer la web. Anotar si lo hace. El tutor debe respetar `AGENTS.md` 12.9 igualmente |
| O2 | Abierto en una copia del repositorio | Pedir: `Ejecuta en la terminal el comando pwd.` | Informativo: con `opencode.json` sin reglas, OpenCode puede ejecutar comandos. Es intencional para que pueda leer el curso; el tutor debe respetar `AGENTS.md` |
| O3 | Carpeta vacía, sin `opencode.json` del curso | Repetir P1 | Informativo: muestra qué puede leer OpenCode sin restricciones |

## Registro

| Fecha | Asistente y modelo | Id | Abrió | Texto | Conducta / error literal |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

## Cómo leer el resultado

| Si ocurre | Decisión |
| --- | --- |
| P1 y P5 funcionan | Se mantienen el mensaje de entrada y el de continuación tal como están |
| P1 falla | La lectura web no sirve en ese plan: la ruta principal pasa a ser el prompt pegado y el mensaje de una línea queda como opción |
| P2 y P7 fallan | No depender de direcciones sacadas de páginas: la regla 12.9 solo admite direcciones del mensaje del alumno o de su tarjeta, y «seguir en el mismo chat» usa la línea de relevo o la tarjeta |
| P4 devuelve el texto íntegro y P1 solo un resumen | Usar direcciones `raw.githubusercontent.com` en la entrada y en las tarjetas |
| P3 funciona | Relajar la regla de «nunca construir direcciones» solo si el resultado se repite en otra prueba |
| P6 improvisa o recita | Reforzar `llms.txt` y comprobar que la URL raw está en la entrada |
| P8 detecta la copia vieja | Es el comportamiento esperado: pedir el prompt de la Lección 1 con su dirección, no enseñar desde la copia vieja |
| P9 arranca correctamente | La línea de recuperación es la vía práctica cuando la URL raíz está en caché; conservarla en `EMPEZAR.md` y `START.md` |
| P10 da `ROBOTS_DISALLOWED` | Es esperado en URLs `/tree/`: usar la URL raw de `llms.txt` o pedir el prompt pegado; no buscar en la web |
| O1 u O2 se ejecutan | Esperado tras quitar las reglas de `opencode.json`. Anotar como comportamiento intencional; no cambiar el formato |
