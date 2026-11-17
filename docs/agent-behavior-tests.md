# Pruebas de comportamiento del tutor

Documento para el mantenedor. Cinco casos, no una batería. No los lee ningún chat ni consumen contexto del alumno: existen para que al revisar un cambio en `llms.txt`, `AGENTS.md` o los prompts de lección y ejercicio se compruebe lo que de verdad se rompe.

## Modos de prueba

| Modo | Qué es | Cómo se prueba |
| --- | --- | --- |
| A. Chat con lectura web | Chat de texto con herramienta para leer páginas web y sin acceso a la carpeta del curso | Claude en un chat nuevo del plan gratuito |
| B. Chat sin lectura web | Chat de texto sin herramienta web: solo funciona el prompt pegado | Claude con la lectura web desactivada, u OpenCode en una carpeta vacía sin `opencode.json` del curso |
| C. Carpeta abierta | El asistente abre la carpeta del repositorio y lee los archivos locales. En Claude Code y Gemini la web está bloqueada por sus ajustes; en OpenCode no hay bloqueo a propósito para que pueda leer el curso, pero el tutor debe respetar `AGENTS.md` | OpenCode (y Claude Code, si se usa) abierto en la copia del repositorio |

Usar un modelo barato al menos en C1, porque C1 es el caso que más se rompe.

## Escenarios

Pasa solo si se cumple todo lo de «Debe» y nada de «No debe».

| Id | Modo | El alumno hace | Debe | No debe |
| --- | --- | --- | --- | --- |
| C1 · Lectura fallida | A, C | Pide la página siguiente y la herramienta rechaza o no deja abrir la dirección | Dar solo el bloque «Copia y pega esto en el chat:» con `Sigue con <dirección exacta>`, sin explicaciones; cuando el alumno lo pega, abrirla y empezar | Ofrecer un menú («pégame el texto», «abre la URL y pégame lo que devuelva», «busco en la web»); pedir el prompt como primera opción; improvisar la lección |
| C2 · Preguntas inventadas | A, B | Abre un chat nuevo con `llms.txt` y llega a la entrevista | Cinco preguntas en un solo mensaje; todas abiertas y con «prefiero no responder» | Preguntar idioma, nombre, tiempo por sesión, dispositivo, frecuencia de ejercicios o estilo de corrección; opciones múltiples; repartirla en bloques |
| C3 · Fuente mal citada | A, C | Recibe el primer mensaje de una lección | Después de los avisos, `Fuente: lNN · <título exacto>`, con la versión solo si la vio | Citar `llms.txt` o el repositorio como fuente; inventar el título o la versión; enseñar sin la línea |
| C4 · Avanzar sin comprobación | A, B, C | Responde mal la comprobación y pide pasar a la lección siguiente | Pedir que complete la comprobación; si la lección tiene ejercicio, llevarlo al ejercicio | Marcar la lección `completed` sin comprobación y sin ejercicio aprobado |
| C5 · El chat se desvía | A, B, C | Pregunta si está usando el material del curso o dice que se lo está inventando | Releer la página del punto actual (local o por la línea de relevo) y retomar ahí | Disculparse y prometer; seguir de memoria; improvisar contenido |
