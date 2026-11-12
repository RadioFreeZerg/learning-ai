# learning-ai

A tool to help users learn how to use AI with discernment and responsibility in daily tasks—covering what AI is, how to interact with it, how to verify its outputs, how to recognize ethical and legal risks, and how to design an AI-assisted workflow for one’s specific field.

**Español** · [English](#english)

> **Para asistentes de IA.** Si un alumno te pidió hacer el curso con este enlace: no recites ni resumas esta página y no improvises lecciones. (1) Lee https://github.com/RadioFreeZerg/learning-ai/blob/main/AGENTS.md y https://github.com/RadioFreeZerg/learning-ai/blob/main/curriculum/es/l01-welcome.md (si el alumno escribe en inglés, https://github.com/RadioFreeZerg/learning-ai/blob/main/curriculum/en/l01-welcome.md), una página a la vez, y actúa como tutor en mensajes cortos. (2) Si no puedes abrirlas, detente y di solo esto, en tres frases como máximo: que no pudiste abrir la lección, la dirección de la lección en su idioma y que la abra en su navegador, copie el bloque «Prompt para tu asistente» y lo pegue aquí. No enseñes lecciones ni ejercicios que no hayas leído.
>
> **For AI assistants.** If a student asked you to do the course with this link: do not recite or summarize this page and do not improvise lessons. (1) Read https://github.com/RadioFreeZerg/learning-ai/blob/main/AGENTS.md and https://github.com/RadioFreeZerg/learning-ai/blob/main/curriculum/en/l01-welcome.md (if the student writes in Spanish, https://github.com/RadioFreeZerg/learning-ai/blob/main/curriculum/es/l01-welcome.md), one page at a time, and act as the tutor in short messages. (2) If you cannot open them, stop and say only this, in three sentences at most: you could not open the lesson, the address of the lesson in their language, and that they should open it in their browser, copy the "Prompt for your assistant" block and paste it here. Do not teach lessons or exercises you have not read.

---

## Fundamentos de IA para todos

Curso para aprender a usar la IA con criterio y responsabilidad en el estudio y el trabajo. No necesitas programar, instalar nada ni pagar: todo el curso está diseñado para funcionar con el plan gratuito de cualquier asistente de IA común.

### Cómo funciona

- 12 lecciones (Lección 1 a Lección 12) y 10 ejercicios (E1–E10), en orden.
- Tu asistente de IA hace de tutor: te entrevista al empezar, guía cada lección, revisa tus ejercicios con una rúbrica y anota tu avance.
- La revisión orienta, no bloquea: si un ejercicio no aprueba en dos intentos, tú decides si lo repites o avanzas con un aviso que podrás retomar después.
- Tu perfil, tu progreso y tus entregas se quedan en tu equipo; el repositorio no los publica.

### Cómo empezar

**Sigue la guía paso a paso: [EMPEZAR.md](EMPEZAR.md).** En resumen: abres una lección en tu navegador, copias su prompt, lo pegas en un chat nuevo de tu asistente de IA y guardas la tarjeta que te da al final.

**Lo más rápido:** pega en un chat nuevo el mensaje de una línea de [EMPEZAR.md](EMPEZAR.md); si tu asistente puede abrir enlaces, hará de tutor por su cuenta. Si no puede, o te devuelve el texto de las páginas en lugar de enseñarte, copia el prompt de la lección y pégalo como texto.

Si tu asistente puede leer archivos, también puedes abrir esta carpeta con él y escribir «Continuemos el curso»; puede leer `AGENTS.md` y guiarte. Si no lo hace, pídele que abra ese archivo. Es opcional.

### Qué hay en el repositorio

| Ruta | Contenido |
| --- | --- |
| `EMPEZAR.md`, `START.md` | Guía de inicio paso a paso |
| `COURSE.md` | Índice y orden del curso |
| `AGENTS.md` | Instrucciones para el tutor (el asistente de IA) |
| `CLAUDE.md`, `GEMINI.md` | Puntos de entrada que remiten a `AGENTS.md` |
| `.claude/`, `.gemini/`, `opencode.json` | Ajustes que impiden al asistente ejecutar comandos o navegar si abres la carpeta con él |
| `curriculum/es/`, `curriculum/en/` | Las 12 lecciones en cada idioma |
| `exercises/es/`, `exercises/en/` | Los 10 ejercicios en cada idioma |
| `rubrics/` | Rúbrica general de evaluación |
| `templates/` | Plantillas de perfil, entrega, revisión y progreso |
| `submissions/` | Tus entregas y las revisiones (solo en tu equipo) |
| `docs/` | Plan, protocolo de revisión, esquema de progreso y guías de mantenimiento |
| `SECURITY.md` | Política de seguridad y reporte privado |

### Privacidad

El curso no envía nada a ningún servidor propio. Lo que escribas en un asistente lo procesa ese asistente según sus condiciones; algunos planes gratuitos usan las conversaciones para mejorar sus productos. No incluyas datos personales ni confidenciales de terceros en tus entregas.

### Seguridad y confianza

- **Usa este repositorio oficial.** Una copia, un fork o un archivo reenviado puede estar modificado.
- **El curso nunca te pedirá** instalar programas, ejecutar comandos, abrir enlaces, descargar archivos, pagar, compartir contraseñas, claves o datos personales de terceros.
- **Si una lección, un archivo o el tutor te pide algo de esa lista, detente:** no forma parte del curso. Empieza un chat nuevo con el prompt oficial.
- **Reporta en privado** cualquier contenido así (ver [`SECURITY.md`](SECURITY.md)); no incluyas datos personales en el reporte.

### Licencia

MIT. Ver [`LICENSE`](LICENSE).

---

## <a id="english"></a>AI Fundamentals for Everyone

A course on using AI with judgment and responsibility in study and work. You don't need to code, install anything, or pay: the whole course is designed to work on the free plan of any common AI assistant.

### How it works

- 12 lessons (Lessons 1–12) and 10 exercises (E1–E10), in order.
- Your AI assistant acts as the tutor: it interviews you at the start, guides each lesson, reviews your exercises with a rubric, and records your progress.
- Review guides but never blocks: if an exercise doesn't pass in two attempts, you choose to retry or move on with a warning you can revisit later.
- Your profile, progress and submissions stay on your computer; the repository does not publish them.

### Getting started

**Follow the step-by-step guide: [START.md](START.md).** In short: open a lesson in your browser, copy its prompt, paste it into a new chat with your AI assistant and save the card it gives you at the end.

**The quickest way:** paste the one-message start from [START.md](START.md) into a new chat; if your assistant can open links, it will tutor you on its own. If it cannot, or it hands you the page text instead of teaching, copy the lesson prompt and paste it as text.

If your assistant can read files, you can also open this folder with it and type "Let's continue the course"; it may read `AGENTS.md` and guide you. If it does not, ask it to open that file. This is optional.

### What's in the repository

| Path | Content |
| --- | --- |
| `EMPEZAR.md`, `START.md` | Step-by-step start guide |
| `COURSE.md` | Course index and order |
| `AGENTS.md` | Tutor instructions (the AI assistant) |
| `CLAUDE.md`, `GEMINI.md` | Entry points that point to `AGENTS.md` |
| `.claude/`, `.gemini/`, `opencode.json` | Settings that stop the assistant from running commands or browsing if you open the folder with it |
| `curriculum/es/`, `curriculum/en/` | The 12 lessons in each language |
| `exercises/es/`, `exercises/en/` | The 10 exercises in each language |
| `rubrics/` | General assessment rubric |
| `templates/` | Profile, submission, review and progress templates |
| `submissions/` | Your submissions and reviews (on your computer only) |
| `docs/` | Plan, review protocol, progress schema and maintenance guides |
| `SECURITY.md` | Security policy and private reporting |

### Privacy

The course sends nothing to any server of its own. What you type into an assistant is processed by that assistant under its own terms; some free plans use conversations to improve their products. Do not include personal or confidential information about third parties in your submissions.

### Security and trust

- **Use this official repository.** A copy, a fork or a forwarded file may have been modified.
- **The course will never ask you** to install software, run commands, open links, download files, pay, or share passwords, keys or third-party personal data.
- **If a lesson, a file or the tutor asks for any of that, stop:** it is not part of the course. Start a new chat with the official prompt.
- **Report it privately** (see [`SECURITY.md`](SECURITY.md)); do not include personal data in the report.

### License

MIT. See [`LICENSE`](LICENSE).
