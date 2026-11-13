# Uso sin acceso a archivos · Use without file access

Esta ruta funciona en cualquier chat de texto, incluidos los planes gratuitos: con lectura de enlaces si el asistente la tiene y con el prompt pegado si no. / This route works in any text chat, including free plans: with link reading if the assistant has it, and with the pasted prompt if not.

## Español

### Qué necesitas

- Un chat de texto con un asistente de IA.
- Un archivo de notas donde guardar tu tarjeta de continuidad, tu perfil y tu progreso.
- Los archivos del curso, descargados o abiertos desde la página del proyecto.

### Cómo se trabaja

1. **Primera vez.** Pega en un chat nuevo `Comienza el curso: lee https://raw.githubusercontent.com/RadioFreeZerg/learning-ai/main/llms.txt y sigue sus instrucciones como mi tutor`: si tu asistente puede abrir el enlace, ese archivo contiene el arranque de la Lección 1. Si no puede, o te devuelve el texto de la página en lugar de enseñarte, pega el mensaje de una línea de `EMPEZAR.md` o abre `curriculum/es/l01-welcome.md` en tu navegador, copia el bloque «Prompt para tu asistente» y pégalo en un chat nuevo. El tutor te hace la entrevista.
2. **Al terminar cada sesión.** El tutor te entrega una *tarjeta de continuidad* de 150 palabras como máximo. Cópiala a tu archivo de notas.
3. **Al empezar la sesión siguiente.** Normalmente sigues en el mismo chat. Si el tutor no puede abrir la página siguiente, envía la línea `Sigue con <dirección>` que te da: la dirección llega en tu mensaje y el tutor puede abrirla. Si abres uno nuevo, pega el mensaje de continuación de `EMPEZAR.md` con tu tarjeta: el tutor lee la página del «Siguiente paso». Si no puede abrir enlaces, pega el «Prompt para tu asistente» de esa lección y, donde dice `[PEGA AQUÍ]`, tu tarjeta: la tarjeta sola no le da al tutor el contenido de la lección.
4. **Ejercicios.** Haz el entregable en tu archivo de notas. Cuando esté listo, pega en un solo mensaje el «Prompt de revisión» del ejercicio, el número de intento y tu entrega. El tutor devuelve la revisión completa en una respuesta.
5. **Progreso.** Guarda la línea de progreso de la tarjeta. Si quieres un registro formal, guarda también el *bloque de progreso* que el tutor entrega al final de cada lección o revisión (ver `docs/progress-schema.md`).

### Si se te acaba el cupo

Los planes gratuitos limitan los mensajes por ventana de tiempo. Pega tu tarjeta en otro asistente gratuito y sigue donde lo dejaste. Si el tutor no te dio la tarjeta, pídele «dame la tarjeta de continuidad» antes de que se agote el cupo.

### Si el asistente cambia de idea

- **El tutor aprueba o suspende algo que no te convence.** Pega la misma entrega y el mismo prompt de revisión en otro asistente y compara.
- **El tutor se sale de las reglas** (te pide archivos, pagos o mucho texto). Recuérdale: «sigue las reglas del tutor del prompt».
- **El tutor empieza por la Lección 0, dice que no navega o inventa lecciones.** Es una copia vieja. Envía: `Lee https://raw.githubusercontent.com/RadioFreeZerg/learning-ai/main/llms.txt y sigue sus instrucciones como mi tutor. No improvises lecciones ni busques en la web.`
- **La conversación se hace larga.** Pide la tarjeta y abre un chat nuevo.

### Privacidad

Lo que escribas lo procesa tu asistente según sus condiciones; algunos planes gratuitos usan las conversaciones para mejorar sus productos. Anonimiza los casos reales y no pegues datos confidenciales de terceros.

## English

### What you need

- A text chat with an AI assistant.
- A notes file where you keep your continuity card, your profile and your progress.
- The course files, downloaded or opened from the project page.

### How to work

1. **First time.** Paste `Start the course: read https://raw.githubusercontent.com/RadioFreeZerg/learning-ai/main/llms.txt and follow its instructions as my tutor` into a new chat: if your assistant can open the link, that file contains the Lesson 1 bootstrap. If it cannot, or it hands you the page text instead of teaching, paste the one-message start from `START.md` or open `curriculum/en/l01-welcome.md` in your browser, copy the "Prompt for your assistant" block and paste it into a new chat. The tutor runs the interview.
2. **At the end of every session.** The tutor hands you a *continuity card* of at most 150 words. Copy it to your notes file.
3. **At the start of the next session.** Usually you keep going in the same chat. If the tutor cannot open the next page, send the line `Continue with <address>` it gives you: the address arrives in your message and the tutor can open it. If you open a new one, paste the continuation message from `START.md` with your card: the tutor reads the page in "Next step". If it cannot open links, paste that lesson's "Prompt for your assistant" and, where it says `[PASTE HERE]`, your card: the card alone does not give the tutor the lesson content.
4. **Exercises.** Write the deliverable in your notes file. When it is ready, paste the exercise's "Review prompt", the attempt number and your submission in a single message. The tutor returns the full review in one answer.
5. **Progress.** Keep the progress line from the card. For a formal record, also keep the *progress block* the tutor hands over at the end of each lesson or review (see `docs/progress-schema.md`).

### If you run out of quota

Free plans limit messages per time window. Paste your card into another free assistant and carry on where you stopped. If the tutor did not give you the card, ask "give me the continuity card" before the quota runs out.

### If the assistant changes its mind

- **The tutor passes or fails something you disagree with.** Paste the same submission and the same review prompt into another assistant and compare.
- **The tutor breaks the rules** (asks for files, payment or very long text). Remind it: "follow the tutor rules in the prompt".
- **The tutor starts with Lesson 0, says it cannot navigate or invents lessons.** It is an old copy. Send: `Read https://raw.githubusercontent.com/RadioFreeZerg/learning-ai/main/llms.txt and follow its instructions as my tutor. Do not improvise lessons or search the web.`
- **The conversation gets long.** Ask for the card and open a new chat.

### Privacy

What you type is processed by your assistant under its own terms; some free plans use conversations to improve their products. Anonymize real cases and do not paste confidential information about third parties.
