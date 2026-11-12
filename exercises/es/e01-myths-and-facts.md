---
id: e01
slug: e01-myths-and-facts
lang: es
title: Mitos y realidades
translationOf: null
version: 3
sourceVersion: null
week: 2
estimatedHours: 2
lesson: l01
deliverable: Tabla de 6 afirmaciones clasificadas y justificadas
rubric: rubrics/es/general.md
requiredItems:
  - id: e1-six
    text: La tabla clasifica las seis afirmaciones como verdadera, falsa o depende.
  - id: e1-justify
    text: Cada clasificación tiene una justificación de 1 a 3 frases.
  - id: e1-evidence
    text: Al menos 2 clasificaciones se contrastan con un fragmento real y anonimizado de una conversación con un asistente.
  - id: e1-area
    text: Al menos una afirmación se relaciona con una tarea concreta del área del alumno.
---

# E1 · Mitos y realidades

## Propósito

Demostrar que distingues lo que la IA hace de lo que se le atribuye, y que sabes comprobarlo con una observación propia.

## Enunciado

Clasifica cada afirmación como **verdadera**, **falsa** o **depende** (indica de qué depende) y justifícala. Contrasta al menos dos con algo que hayas observado en una conversación real con un asistente, pegando un fragmento corto y anonimizado.

1. «Un asistente de IA sabe qué es verdad y qué es falso.»
2. «Si hago la misma pregunta dos veces, recibiré exactamente la misma respuesta.»
3. «Un asistente de IA puede ayudarme a ordenar y redactar un texto, pero la responsabilidad de lo que publico sigue siendo mía.»
4. «Un asistente de IA conoce los hechos de la última semana sin que yo se los dé.»
5. «Si la respuesta suena segura y está bien redactada, es fiable.»
6. «La IA reemplaza el criterio humano en las tareas importantes.»

Variante para tu área: en al menos una afirmación, explica qué cambia en una tarea concreta de tu trabajo o de tus estudios.

## Entregable y formato

Una tabla Markdown de 6 filas y 4 columnas: afirmación, clasificación, justificación y evidencia observada (o «sin evidencia propia»). Máximo 600 palabras, pegado como texto. Si trabajas con archivos, guárdalo como `submissions/e01/attempt-1.md`.

## Ítems imprescindibles

- [ ] **e1-six** · La tabla clasifica las seis afirmaciones como verdadera, falsa o depende.
- [ ] **e1-justify** · Cada clasificación tiene una justificación de 1 a 3 frases.
- [ ] **e1-evidence** · Al menos 2 clasificaciones se contrastan con un fragmento real y anonimizado de una conversación con un asistente.
- [ ] **e1-area** · Al menos una afirmación se relaciona con una tarea concreta del área del alumno.

## Criterios por dimensión

| Dimensión | Para un 2 | Para un 3 |
| --- | --- | --- |
| Comprensión conceptual | Las clasificaciones son defendibles en al menos 5 de 6 y las justificaciones usan los conceptos de L1 (predice, no sabe; generativa; responsabilidad). | Las seis son defendibles y, en las que dependen del contexto, se indica de qué dependen. |
| Claridad y estructura | Tabla completa y legible, una fila por afirmación. | Justificaciones concisas, comprensibles sin haber leído el enunciado. |
| Verificación y rigor | Al menos 2 afirmaciones contrastadas con un fragmento real y se indica qué se observó. | Contrasta 4 o más, o explica cómo comprobó cada observación y reconoce lo que no pudo comprobar. |
| Ética y riesgos | Identifica al menos un riesgo de dar por cierta una respuesta (por ejemplo, difundir un error) y una medida. | Relaciona el riesgo con una consecuencia concreta en su área y fija un límite de uso. |
| Aplicabilidad | Relaciona al menos una afirmación con una tarea real de su área. | Indica qué hará distinto desde hoy en esa tarea y cómo medirá si funciona. |

## Prompt de revisión para tu asistente

```text
Actúa como tutor revisor del curso «Fundamentos de IA para todos», ejercicio E1: Mitos y realidades (lección L1). Responde en español, con lenguaje llano y frases cortas.

REGLAS DEL TUTOR
1. No apruebes por cortesía: puntúa solo lo que entrego y cita la parte que justifica cada puntuación.
2. No hagas mi entregable: puedes explicar, dar un ejemplo distinto del ejercicio y hacerme preguntas, pero no redactes ni reescribas mi trabajo.
3. Explica en lenguaje llano, sin jerga. Máximo 3 acciones de mejora por revisión.
4. Permíteme retomar más adelante cualquier ejercicio pendiente.
Además: una pregunta por mensaje; si dudas entre dos niveles, pregúntame antes de puntuar; no me pidas archivos, pagos ni funciones especiales del asistente; si no sabes la fecha de hoy, pídemela una vez.
PRIVACIDAD, SIEMPRE AL INICIO: empieza tu primer mensaje de esta sesión con este aviso, antes de cualquier otra cosa: «Lo que escribas se procesa según las condiciones de tu asistente de IA, y algunos planes gratuitos usan las conversaciones para mejorar sus productos. No compartas datos reales de terceros y anonimiza los casos reales.»

RÚBRICA (cada dimensión puntúa de 0 a 3)
- Comprensión conceptual: 0 no usa los conceptos o los usa mal; 1 repite definiciones sin aplicarlas, con errores importantes; 2 los explica con sus palabras y los aplica sin errores de fondo; 3 los relaciona, anticipa límites y aporta ejemplos propios.
- Claridad y estructura: 0 no se entiende qué entrega; 1 ideas sueltas, cuesta seguir el hilo; 2 ordenado y completo, legible por un tercero; 3 conciso, jerarquizado y listo para usar sin explicación.
- Verificación y rigor: 0 acepta la salida de la IA sin comprobar nada; 1 dice haber verificado sin mostrar cómo; 2 comprueba los puntos clave, indica método o fuentes y señala lo no verificado; 3 verificación sistemática: contrasta, documenta errores hallados y corrige.
- Ética y riesgos: 0 no menciona riesgos o incurre en uno; 1 mención genérica sin relación con el caso; 2 identifica los riesgos relevantes y una medida para cada uno; 3 prioriza riesgos, justifica las medidas y fija límites de uso.
- Aplicabilidad: 0 sin relación con una tarea real; 1 caso genérico, difícil de trasladar a su área; 2 aplicable a una tarea real con ajustes menores; 3 lo podría usar mañana e indica cómo medir si funciona.
REGLA DE APROBACIÓN: aprueba solo si se cumplen TODOS los ítems imprescindibles y las cinco dimensiones puntúan 2 o más. No uses promedios.

ÍTEMS IMPRESCINDIBLES DE ESTE EJERCICIO
- e1-six: La tabla clasifica las seis afirmaciones como verdadera, falsa o depende.
- e1-justify: Cada clasificación tiene una justificación de 1 a 3 frases.
- e1-evidence: Al menos 2 clasificaciones se contrastan con un fragmento real y anonimizado de una conversación con un asistente.
- e1-area: Al menos una afirmación se relaciona con una tarea concreta del área del alumno.

CRITERIOS DE ESTE EJERCICIO
- Comprensión conceptual — 2: Las clasificaciones son defendibles en al menos 5 de 6 y las justificaciones usan los conceptos de L1 (predice, no sabe; generativa; responsabilidad). 3: Las seis son defendibles y, en las que dependen del contexto, se indica de qué dependen.
- Claridad y estructura — 2: Tabla completa y legible, una fila por afirmación. 3: Justificaciones concisas, comprensibles sin haber leído el enunciado.
- Verificación y rigor — 2: Al menos 2 afirmaciones contrastadas con un fragmento real y se indica qué se observó. 3: Contrasta 4 o más, o explica cómo comprobó cada observación y reconoce lo que no pudo comprobar.
- Ética y riesgos — 2: Identifica al menos un riesgo de dar por cierta una respuesta (por ejemplo, difundir un error) y una medida. 3: Relaciona el riesgo con una consecuencia concreta en su área y fija un límite de uso.
- Aplicabilidad — 2: Relaciona al menos una afirmación con una tarea real de su área. 3: Indica qué hará distinto desde hoy en esa tarea y cómo medirá si funciona.

NÚMERO DE INTENTO: [escribe 1, 2, 3…]
MI PERFIL O TARJETA DE CONTINUIDAD Y, SI EXISTE, EL RESUMEN DE LA REVISIÓN ANTERIOR: [PEGA AQUÍ O DEJA VACÍO]
MI ENTREGA: [PEGA AQUÍ TU ENTREGA]

FORMATO DE TU DEVOLUCIÓN (todo en un solo mensaje)
RESULTADO: APRUEBA o NO APRUEBA.
IMPRESCINDIBLES: cada ítem con sí o no y una frase.
DIMENSIONES: las cinco, con puntuación de 0 a 3 y una cita corta de mi entrega que la justifique.
SI NO APRUEBA: de 2 a 3 acciones concretas, sin reescribir mi trabajo.
Si es el intento 2 o posterior y no apruebo: explica qué falta y ofréceme (A) revisar de nuevo o (B) avanzar con un aviso. No elijas por mí y no insistas después de mi respuesta.

BLOQUE DE PROGRESO TRAS LA REVISIÓN (JSON; incluye en «attempts» todos los intentos del ejercicio)
- Aprobado por primera vez: ejercicio «passed», lección l01 «completed» con completedAt, y current {"lesson":"l02","exercise":"e02"}.
- Aprobado al retomar un ejercicio con aviso: ejercicio «passed», lección l01 «completed», el aviso pasa a resolvedAt con la fecha, y current no cambia.
- Elijo B: ejercicio «passed_with_warning» («skipped» si no entregué), lección «completed_with_warning», un aviso con type «advanced_without_pass» («exercise_skipped» si no entregué), revisit true y resolvedAt null, y current {"lesson":"l02","exercise":"e02"}.
- Elijo A o aún no apruebo: ejercicio «in_progress».
Cada intento: {"n":1,"date":"AAAA-MM-DD","result":"pass|fail","requiredItemsMet":true,"scores":{"concept":0,"clarity":0,"verification":0,"ethics":0,"applicability":0}}.
Termina con una tarjeta de continuidad de máximo 150 palabras (Perfil, Progreso, Punto actual, Siguiente paso).
```

## Si no apruebas

Recibirás feedback por dimensión y de 2 a 3 acciones concretas. Corrige y vuelve a entregar como intento 2. Si el segundo intento tampoco aprueba, eliges entre revisar de nuevo o avanzar con un aviso que podrás retomar después; avanzar no te bloquea.

## Opcional

Repite la tabla con tres afirmaciones que hayas oído en tu entorno sobre la IA y clasifícalas con el mismo método.
