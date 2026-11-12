# Plan del curso: Fundamentos de IA para todos

Versión resumida del plan de construcción. Los detalles ya implementados viven en su propio archivo y aquí solo se enlazan:

- Esquema de progreso: [`progress-schema.md`](progress-schema.md)
- Entrevista y perfil: [`interview.md`](interview.md)
- Protocolo de revisión: [`review-protocol.md`](review-protocol.md)
- Traducción y sincronización: [`translation.md`](translation.md), [`translation-status.md`](translation-status.md)
- Planes gratuitos: [`free-tier.md`](free-tier.md)
- Uso sin acceso a archivos: [`no-file-access.md`](no-file-access.md)
- Accesibilidad y glosario: [`accessibility.md`](accessibility.md), [`glossary.md`](glossary.md)
- Rúbrica: [`../rubrics/es/general.md`](../rubrics/es/general.md)

## 1. Resumen ejecutivo

«Fundamentos de IA para todos» / «AI Fundamentals for Everyone» es un curso para aprender a usar la IA con criterio en tareas cotidianas. Está pensado para estudiantes y profesionales no técnicos: no pide terminal, código ni cuentas de pago.

El curso es un repositorio Git de archivos de texto. El alumno abre la carpeta con el asistente de IA que prefiera, o copia un prompt en un chat. El asistente lee `AGENTS.md`, hace una entrevista inicial, guía 12 lecciones (L0–L11) y revisa 10 ejercicios (E1–E10) con una rúbrica común. El avance queda en `progress.json`.

Lo distinto: es bilingüe (ES/EN con archivos paralelos), funciona con el plan gratuito de cualquier asistente común, incluso sin acceso a archivos, y la evaluación orienta pero no bloquea: tras dos intentos fallidos el alumno decide si repite o avanza con un aviso registrado.

## 2. Decisiones y supuestos

| Tema | Decisión |
| --- | --- |
| Nombre | «Fundamentos de IA para todos» / «AI Fundamentals for Everyone» |
| Estructura | 12 lecciones (L0–L11) y 10 ejercicios (E1–E10); L0 y L11 sin ejercicio |
| Independencia | Cualquier asistente; `AGENTS.md` para quien lee archivos y prompt autocontenido por lección para el resto |
| Idiomas | ES y EN en archivos paralelos con el mismo slug; ES es el original |
| Progreso | `progress.json` en la raíz, legible por máquina |
| Perfil | Entrevista en L0 que genera `PROFILE.md` con 9 campos más nombre opcional |
| Evaluación | Rúbrica 5 dimensiones × 4 niveles; aprobado = todos los imprescindibles + mínimo 2 por dimensión |
| Segundo fallo | El alumno elige revisar de nuevo o avanzar con aviso (`warnings[]` con `revisit: true`) |
| Límites de contenido | Sin certificaciones, sin marcas en el temario, sin código; agentes de programación solo como concepto en L9 |

Supuestos:

1. El repositorio es `RadioFreeZerg/learning-ai`; la rama de trabajo inicial es `feature/course-scaffold`.
2. Los slugs son ASCII en inglés y minúsculas, iguales en ambos idiomas.
3. `PROFILE.md`, `progress.json` y las entregas se generan en la copia del alumno y git los ignora.
4. El repositorio no incluye scripts; las comprobaciones las hace el asistente leyendo archivos.
5. `AGENTS.md` está en inglés porque lo lee el agente; `README.md` y `COURSE.md` son bilingües en un mismo archivo.

## 3. Regla fundamental: planes gratuitos

Todo el curso debe poder completarse con el plan gratuito de los asistentes más comunes, sin tarjeta ni funciones de pago. La ruta principal es copiar y pegar en un chat de texto; el acceso a archivos es una comodidad opcional.

| Recurso | Límite que cumple cada lección y ejercicio |
| --- | --- |
| Mensajes del alumno por sesión | 12 como máximo |
| Sesiones por lección | 2 a 4 sesiones cortas, cada una en un chat nuevo |
| «Prompt para tu asistente» y prompt de revisión | 1.200 palabras como máximo, rúbrica incluida |
| Conversación completa de una sesión | 8.000 palabras como máximo |
| Entregable de un ejercicio | 600 palabras como máximo, pegado como texto |
| Documento de trabajo (E5, E6) | 2 páginas como máximo, pegado como texto |
| Archivos adjuntos obligatorios | Ninguno |
| Funciones obligatorias | Solo chat de texto |
| Pago, tarjeta o prueba temporal | Nunca |

Las cifras de los proveedores cambian a menudo; la matriz con fecha vive en [`free-tier.md`](free-tier.md).

## 4. Mapa del curso

| Lección | Ejercicio | Entregable |
| --- | --- | --- |
| L0 · Bienvenida, entrevista y forma de trabajo | — | `PROFILE.md` y `progress.json` iniciados |
| L1 · Qué es y qué no es la IA | E1 · Mitos y realidades | Tabla de 6 afirmaciones clasificadas y justificadas |
| L2 · Cómo funciona un modelo de lenguaje, sin matemáticas | E2 · Explícalo a un colega | Explicación de una página con analogía propia y tres límites |
| L3 · Comunicarse con la IA: instrucciones claras | E3 · Reescribe tres instrucciones | Tres pares antes/después con el porqué de cada cambio |
| L4 · Contexto, ejemplos e iteración | E4 · Bitácora de iteración | Registro de una conversación mejorada en 3 rondas |
| L5 · Verificar resultados: errores, invenciones y fuentes | E5 · Informe de verificación | Respuesta de IA auditada |
| L6 · Trabajar con documentos y datos propios | E6 · Resumen verificado | Resumen con cada afirmación trazada al original |
| L7 · Ética, sesgos y uso responsable | E7 · Caso ético de tu área | Análisis de un caso: afectados, riesgos y decisión |
| L8 · Privacidad, propiedad intelectual y marco legal | E8 · Semáforo de datos | Guía personal de qué compartir, anonimizar o no compartir |
| L9 · Automatización y agentes: conceptos | E9 · Mapa de automatización | Tareas clasificadas: delegar, asistir o no automatizar |
| L10 · Diseñar un flujo de trabajo asistido por IA | E10 · Flujo de trabajo final | Flujo documentado: pasos, verificación, riesgos y límites |
| L11 · Cierre: revisar avisos y plan de continuidad | — | Avisos revisados y plan personal de continuidad |

## 5. Fases de construcción

| Fase | Qué se construye | Entregable | Prueba de cierre |
| --- | --- | --- | --- |
| 1 · Cimientos | `README.md`, `COURSE.md`, `AGENTS.md`, `.gitignore`, `docs/PLAN.md`, carpetas | Repositorio navegable | Un asistente explica qué es el curso y cómo empezar |
| 2 · Perfil y progreso | Plantilla de progreso, plantillas de perfil, guion de entrevista, esquema, uso sin archivos, planes gratuitos, L0 en ES | Entrevista y motor de progreso | La entrevista genera `PROFILE.md` y un `progress.json` válido |
| 3 · Evaluación | Rúbrica, protocolo de revisión, plantillas de entrega y revisión, L1 y E1 en ES | Ciclo lección → ejercicio → revisión | Simulación con dos fallos: se ofrece A o B y el aviso queda registrado |
| 4 · Contenido ES | L2–L11, E2–E10 y glosario en español | Curso completo en español | Cada archivo cumple el formato; revisión de marcas, código y certificaciones |
| 5 · Traducción EN | Todo el contenido, rúbrica y plantillas en inglés; estado de sincronización | Curso bilingüe sincronizado | Ningún par desincronizado |
| 6 · Piloto y ajuste | Accesibilidad, pruebas con asistentes reales y personas no técnicas | Versión 1.0 | Criterios de aceptación cumplidos |

Las fases 1 a 3 fijan la mecánica con poco contenido; si algo del diseño falla, se descubre antes de escribir las 22 piezas.

## 6. Riesgos principales

| Riesgo | Mitigación |
| --- | --- |
| Mantener dos idiomas duplica el trabajo | ES como única fuente; `version`/`sourceVersion`; traducción por lotes; aviso al alumno si EN está atrasado |
| El alumno avanza con vacíos | Avisos con `revisit: true`; recordatorios; repaso en L11; E10 retoma verificación y ética |
| El agente no respeta `AGENTS.md` | Prompt autocontenido en cada lección y ejercicio; reglas numeradas; progreso verificable por el alumno |
| El tutor aprueba de más o de menos | Imprescindibles de sí o no; evidencia citada; regla de no aprobar por cortesía; segunda revisión con otro asistente |
| `progress.json` se corrompe | Esquema documentado; validación al inicio de cada sesión; nunca se borran intentos ni avisos |
| Accesibilidad | Markdown semántico; frases cortas; el perfil cambia el formato; [`accessibility.md`](accessibility.md) |
| Cupos del plan gratuito | Presupuesto de diseño; sesiones de 12 mensajes; tarjeta de continuidad; matriz con fecha revisada cada trimestre |
| Datos de terceros en las entregas | Advertencia en L0, L6 y L8; entregas ignoradas por git; los enunciados piden anonimizar |

## 7. Criterios de aceptación

- [x] El temario no menciona certificaciones, marcas ni productos.
- [x] No hay código en el curso; los agentes de programación solo aparecen como concepto en L9.
- [x] `curriculum/` y `exercises/` tienen carpetas `es/` y `en/` con los mismos nombres: 12 lecciones y 10 ejercicios.
- [x] La regla de traducción define `lang`, `translationOf`, `version` y `sourceVersion`.
- [x] El ejemplo de `progress.json` es JSON válido y cubre todos los estados.
- [x] El protocolo contempla el segundo fallo sin bloquear.
- [x] La rúbrica tiene 5 dimensiones y 4 niveles.
- [x] El mapa contiene las 12 lecciones y los 10 ejercicios en orden.
- [x] Ninguna lección ni ejercicio exige pago, adjuntos, búsqueda web del asistente ni funciones fuera del chat de texto.
- [x] Cada prompt y cada sesión cumplen el presupuesto de diseño.
- [ ] El ciclo entrevista → L1 → E1 se ha completado en el plan gratuito de al menos cuatro asistentes, tres de ellos solo con chat de texto.

## 8. Estado de la implementación

Fases 1 a 6 implementadas en la rama `feature/course-scaffold` (contenido ES y EN completo, plantillas, rúbrica, glosario, accesibilidad y estado de traducción). Pendiente, porque exige personas y asistentes reales: el piloto del último criterio de aceptación (entrevista → L1 → E1 en los planes gratuitos de al menos cuatro asistentes) y la matriz de planes gratuitos con fecha de revisión.
