# Esquema de `progress.json`

`progress.json` es la única fuente de verdad del avance. Se crea copiando [`templates/progress.template.json`](../templates/progress.template.json) y está en `.gitignore`: vive solo en la copia del alumno. Las claves y los estados van en inglés para que no dependan del idioma del alumno.

## Campos

| Campo | Tipo | Descripción |
| --- | --- | --- |
| `schemaVersion` | texto | Versión del esquema. Hoy `"1.0"` |
| `course.id` | texto | `ai-fundamentals-for-everyone` |
| `course.title` | objeto | Título en `es` y `en` |
| `course.contentVersion` | texto | Versión del contenido con la que se creó el archivo |
| `course.totalWeeks`, `course.estimatedHours` | número | 12 y 70 |
| `student.displayName` | texto o `null` | Nombre opcional |
| `student.lang` | `es`, `en` o `null` | Idioma elegido en la entrevista |
| `student.profileFile` | texto | Siempre `PROFILE.md` |
| `student.profileCompleted` | booleano | `true` cuando la entrevista terminó |
| `student.hoursPerWeek` | número o `null` | Copiado del perfil |
| `student.startedAt` | fecha o `null` | `AAAA-MM-DD` |
| `current.lesson` | `l00`–`l11` | Lección en curso |
| `current.exercise` | `e01`–`e10` o `null` | Ejercicio en curso |
| `lessons[]` | lista de 12 | `id`, `slug`, `status`, `startedAt`, `completedAt`, `warningId` |
| `exercises[]` | lista de 10 | `id`, `slug`, `lesson`, `status`, `warningId`, `attempts[]` |
| `exercises[].attempts[]` | lista | `n`, `date`, `result`, `requiredItemsMet`, `scores`, `submission`, `review` |
| `warnings[]` | lista | `id`, `type`, `exercise`, `lesson`, `failedDimensions`, `missingRequiredItems`, `note`, `createdAt`, `revisit`, `resolvedAt` |
| `updatedAt` | fecha-hora o `null` | ISO 8601 en UTC |
| `updatedBy` | `agent`, `student` o `null` | Quién escribió por última vez |

## Estados de lección

| Estado | Significado | ¿Desbloquea la siguiente? |
| --- | --- | --- |
| `not_started` | Aún no se ha abierto | No |
| `in_progress` | Abierta; falta la lección o su ejercicio | No |
| `completed` | Lección hecha y ejercicio en `passed` (o sin ejercicio) | Sí |
| `completed_with_warning` | Lección hecha; su ejercicio quedó en `passed_with_warning` o `skipped` | Sí |
| `skipped` | El alumno decidió no estudiarla | Sí, con aviso |

## Estados de ejercicio

| Estado | Significado | ¿Desbloquea la siguiente? |
| --- | --- | --- |
| `not_started` | Sin entregas | No |
| `in_progress` | En elaboración o con un intento fallido y otro pendiente | No |
| `passed` | Cumple la regla de aprobación | Sí |
| `passed_with_warning` | Dos o más intentos fallidos y el alumno eligió avanzar | Sí, con aviso |
| `skipped` | El alumno avanzó sin entregar | Sí, con aviso |

## Reglas de escritura

- `attempts[].result` solo admite `pass` o `fail`.
- `attempts[].scores` usa enteros de 0 a 3 en `concept`, `clarity`, `verification`, `ethics` y `applicability`.
- `warnings[].type` admite `advanced_without_pass`, `exercise_skipped` y `lesson_skipped`.
- Todo aviso nace con `revisit: true` y `resolvedAt: null`.
- Un aviso se cierra cuando el alumno retoma el ejercicio y aprueba: se añade el intento, el ejercicio pasa a `passed`, la lección a `completed` y `resolvedAt` recibe la fecha. El aviso no se borra.
- Nunca se eliminan intentos ni avisos anteriores.
- El asistente actualiza `updatedAt` y `updatedBy` en cada escritura.
- `student.displayName` es opcional y puede quedar en `null`.

## Validación al inicio de cada sesión

El tutor comprueba, sin corregir nada en silencio:

1. El archivo es JSON válido.
2. Hay 12 lecciones (`l00`–`l11`) y 10 ejercicios (`e01`–`e10`) con los `slug` de la plantilla.
3. Cada estado es uno de los cinco permitidos para su tipo.
4. `current.lesson` apunta a una lección que no está `completed` ni `completed_with_warning`, salvo que todo esté terminado.
5. Todo `warningId` existe en `warnings[]` y viceversa.
6. Un ejercicio `passed_with_warning` tiene al menos 2 intentos con `result: fail`, o un aviso `exercise_skipped` si está `skipped`.

Si algo falla, lo explica en lenguaje llano y propone la corrección.

## Ejemplo realista

Una alumna en la semana 5: L0–L2 completadas, L3 completada con aviso, L4 en progreso, E2 aprobado al segundo intento y E3 avanzado sin aprobar.

```json
{
  "schemaVersion": "1.0",
  "course": {
    "id": "ai-fundamentals-for-everyone",
    "title": {
      "es": "Fundamentos de IA para todos",
      "en": "AI Fundamentals for Everyone"
    },
    "contentVersion": "1.0.0",
    "totalWeeks": 12,
    "estimatedHours": 70
  },
  "student": {
    "displayName": null,
    "lang": "es",
    "profileFile": "PROFILE.md",
    "profileCompleted": true,
    "hoursPerWeek": 6,
    "startedAt": "2026-11-16"
  },
  "current": { "lesson": "l04", "exercise": "e04" },
  "lessons": [
    { "id": "l00", "slug": "l00-welcome", "status": "completed", "startedAt": "2026-11-16", "completedAt": "2026-11-18", "warningId": null },
    { "id": "l01", "slug": "l01-what-is-ai", "status": "completed", "startedAt": "2026-11-23", "completedAt": "2026-11-27", "warningId": null },
    { "id": "l02", "slug": "l02-how-language-models-work", "status": "completed", "startedAt": "2026-11-30", "completedAt": "2026-12-06", "warningId": null },
    { "id": "l03", "slug": "l03-clear-instructions", "status": "completed_with_warning", "startedAt": "2026-12-07", "completedAt": "2026-12-13", "warningId": "w001" },
    { "id": "l04", "slug": "l04-context-and-iteration", "status": "in_progress", "startedAt": "2026-12-14", "completedAt": null, "warningId": null },
    { "id": "l05", "slug": "l05-verifying-results", "status": "not_started", "startedAt": null, "completedAt": null, "warningId": null },
    { "id": "l06", "slug": "l06-documents-and-data", "status": "not_started", "startedAt": null, "completedAt": null, "warningId": null },
    { "id": "l07", "slug": "l07-ethics-and-bias", "status": "not_started", "startedAt": null, "completedAt": null, "warningId": null },
    { "id": "l08", "slug": "l08-privacy-and-law", "status": "not_started", "startedAt": null, "completedAt": null, "warningId": null },
    { "id": "l09", "slug": "l09-automation-and-agents", "status": "not_started", "startedAt": null, "completedAt": null, "warningId": null },
    { "id": "l10", "slug": "l10-workflow-design", "status": "not_started", "startedAt": null, "completedAt": null, "warningId": null },
    { "id": "l11", "slug": "l11-wrap-up", "status": "not_started", "startedAt": null, "completedAt": null, "warningId": null }
  ],
  "exercises": [
    {
      "id": "e01", "slug": "e01-myths-and-facts", "lesson": "l01", "status": "passed", "warningId": null,
      "attempts": [
        {
          "n": 1, "date": "2026-11-27", "result": "pass", "requiredItemsMet": true,
          "scores": { "concept": 3, "clarity": 2, "verification": 2, "ethics": 2, "applicability": 3 },
          "submission": "submissions/e01/attempt-1.md", "review": "submissions/e01/review-1.md"
        }
      ]
    },
    {
      "id": "e02", "slug": "e02-explain-to-a-colleague", "lesson": "l02", "status": "passed", "warningId": null,
      "attempts": [
        {
          "n": 1, "date": "2026-12-03", "result": "fail", "requiredItemsMet": true,
          "scores": { "concept": 1, "clarity": 2, "verification": 2, "ethics": 2, "applicability": 2 },
          "submission": "submissions/e02/attempt-1.md", "review": "submissions/e02/review-1.md"
        },
        {
          "n": 2, "date": "2026-12-06", "result": "pass", "requiredItemsMet": true,
          "scores": { "concept": 2, "clarity": 3, "verification": 2, "ethics": 2, "applicability": 2 },
          "submission": "submissions/e02/attempt-2.md", "review": "submissions/e02/review-2.md"
        }
      ]
    },
    {
      "id": "e03", "slug": "e03-rewrite-three-instructions", "lesson": "l03", "status": "passed_with_warning", "warningId": "w001",
      "attempts": [
        {
          "n": 1, "date": "2026-12-10", "result": "fail", "requiredItemsMet": false,
          "scores": { "concept": 2, "clarity": 2, "verification": 1, "ethics": 2, "applicability": 2 },
          "submission": "submissions/e03/attempt-1.md", "review": "submissions/e03/review-1.md"
        },
        {
          "n": 2, "date": "2026-12-13", "result": "fail", "requiredItemsMet": true,
          "scores": { "concept": 2, "clarity": 2, "verification": 1, "ethics": 2, "applicability": 2 },
          "submission": "submissions/e03/attempt-2.md", "review": "submissions/e03/review-2.md"
        }
      ]
    },
    { "id": "e04", "slug": "e04-iteration-log", "lesson": "l04", "status": "in_progress", "warningId": null, "attempts": [] },
    { "id": "e05", "slug": "e05-verification-report", "lesson": "l05", "status": "not_started", "warningId": null, "attempts": [] },
    { "id": "e06", "slug": "e06-verified-summary", "lesson": "l06", "status": "not_started", "warningId": null, "attempts": [] },
    { "id": "e07", "slug": "e07-ethics-case", "lesson": "l07", "status": "not_started", "warningId": null, "attempts": [] },
    { "id": "e08", "slug": "e08-data-traffic-light", "lesson": "l08", "status": "not_started", "warningId": null, "attempts": [] },
    { "id": "e09", "slug": "e09-automation-map", "lesson": "l09", "status": "not_started", "warningId": null, "attempts": [] },
    { "id": "e10", "slug": "e10-final-workflow", "lesson": "l10", "status": "not_started", "warningId": null, "attempts": [] }
  ],
  "warnings": [
    {
      "id": "w001",
      "type": "advanced_without_pass",
      "exercise": "e03",
      "lesson": "l03",
      "failedDimensions": ["verification"],
      "missingRequiredItems": [],
      "note": "Las instrucciones reescritas no indican cómo comprobar el resultado.",
      "createdAt": "2026-12-13",
      "revisit": true,
      "resolvedAt": null
    }
  ],
  "updatedAt": "2026-12-14T19:30:00Z",
  "updatedBy": "agent"
}
```

## Fragmentos de parche

Cuando el asistente no puede escribir archivos, entrega al final de la sesión un **fragmento de parche**: un objeto JSON con solo lo que cambió. El alumno lo guarda tal cual en un archivo de notas, o lo aplica a mano siguiendo estas reglas:

- `lessons[]` y `exercises[]`: la entrada con el mismo `id` sustituye a la anterior.
- `exercises[].attempts[]` en un parche contiene **todos** los intentos del ejercicio, no solo el nuevo.
- `warnings[]`: se añade la entrada si el `id` no existe; si existe, sustituye a la anterior.
- `student`, `current` y `updatedAt`: se copian.

Ejemplo: L3 completada y E3 avanzado con aviso.

```json
{
  "lessons": [{ "id": "l03", "slug": "l03-clear-instructions", "status": "completed_with_warning", "startedAt": "2026-12-07", "completedAt": "2026-12-13", "warningId": "w001" }],
  "exercises": [{ "id": "e03", "status": "passed_with_warning", "warningId": "w001" }],
  "warnings": [{ "id": "w001", "type": "advanced_without_pass", "exercise": "e03", "lesson": "l03", "failedDimensions": ["verification"], "missingRequiredItems": [], "note": "Las instrucciones reescritas no indican cómo comprobar el resultado.", "createdAt": "2026-12-13", "revisit": true, "resolvedAt": null }],
  "current": { "lesson": "l04", "exercise": "e04" },
  "updatedAt": "2026-12-13T20:00:00Z"
}
```

En el chat de texto basta con guardar la **línea de progreso** de la tarjeta de continuidad (ver [`free-tier.md`](free-tier.md)); el parche es opcional para quien quiera mantener un registro formal.
