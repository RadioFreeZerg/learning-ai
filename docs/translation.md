# Regla de traducción

El español es el original; el inglés es una traducción con el mismo slug. Cada archivo de `curriculum/`, `exercises/` y `rubrics/` lleva en su frontmatter los campos que permiten comparar las dos versiones.

## Campos

| Campo | En ES (original) | En EN (traducción) |
| --- | --- | --- |
| `lang` | `es` | `en` |
| `slug` | Igual al nombre del archivo sin `.md` | Idéntico al de ES |
| `version` | Entero; sube en 1 con cada cambio de contenido | Entero propio de la traducción |
| `translationOf` | `null` | Ruta del original, por ejemplo `curriculum/es/l05-verifying-results.md` |
| `sourceVersion` | `null` | `version` del original que se tradujo |

Las plantillas del repositorio (`templates/`) y los documentos de `docs/` no llevan estos campos; se sincronizan a mano.

## Cuándo un par está desincronizado

Un par ES/EN está desincronizado si se cumple cualquiera de estas condiciones:

1. Falta el archivo en uno de los dos idiomas.
2. El `slug` no coincide con el nombre del archivo o entre ambos idiomas.
3. `translationOf` apunta a una ruta que no existe.
4. `sourceVersion` del archivo EN es menor que `version` del archivo ES.
5. El EN tiene `lang` distinto de `en` o el ES distinto de `es`.

## Flujo de cambio

1. Todo cambio de contenido se hace primero en ES y sube su `version` en 1.
2. Se actualiza el archivo EN con el mismo cambio y se fija `sourceVersion` igual a la nueva `version` del ES.
3. Se anota el par en [`translation-status.md`](translation-status.md).
4. Un cambio que no altera el contenido (ortografía, formato) no sube `version`.

Para trabajo por lotes: traducir al cerrar una fase, no lección a lección.

## Comprobación

El asistente del mantenedor recorre los pares de `curriculum/`, `exercises/` y `rubrics/`, compara los campos y actualiza `translation-status.md` con una fila por par: slug, `version` ES, `sourceVersion` EN, estado (`sincronizado`, `atrasado` o `falta EN`). Un par `atrasado` o `falta EN` se corrige antes de etiquetar una versión.

## Qué se traduce y qué no

- Se traduce el texto de lecciones, ejercicios y rúbrica, incluidos los prompts de los bloques «Prompt para tu asistente» y «Prompt de revisión».
- Los identificadores no se traducen: claves de `progress.json`, estados, códigos del perfil (`none`, `occasional`…), identificadores de ítems imprescindibles y nombres de archivo.
- Los títulos y términos clave siguen el [glosario](glossary.md).

## Cuando el alumno estudia en inglés

Si su lección está atrasada, el tutor se lo avisa una vez y ofrece trabajar desde el original en español. Ver `AGENTS.md`, regla 2.3.
