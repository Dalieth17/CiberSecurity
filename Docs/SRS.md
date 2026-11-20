# Especificación de requisitos del roadmap

## Propósito

CiberSecurity es una ruta autodidacta en español para personas sin experiencia previa. El objetivo es que el estudiante adquiera fundamentos y pueda demostrar competencias relevantes para postular a un primer puesto. El catálogo se amplía por etapas conforme se validan las lecciones y laboratorios.

## Requisitos

| ID | Requisito | Criterio de aceptación |
| --- | --- | --- |
| RF-01 | Ofrecer un punto de entrada y una progresión por etapas | Desde el README se llega a un mapa con acceso a todas las etapas y a sus evidencias esperadas. |
| RF-02 | Proporcionar contenidos de lectura y aplicación | Cada etapa contiene conceptos o instrucciones de trabajo, una actividad y un criterio de salida. |
| RF-03 | Incluir laboratorios defensivos reproducibles | El primer laboratorio usa registros sintéticos e incluye un resultado esperado y una alternativa manual. |
| RF-04 | Vincular el estudio con perfiles junior | La ruta presenta proyectos por perfil y un proceso para contrastar evidencias con vacantes, redactar el CV y preparar entrevistas. |
| RF-05 | Permitir seguimiento individual | El estudiante puede copiar la lista de etapas y marcar su progreso en sus propias notas. |

## Calidad y mantenimiento

Los documentos se leen en GitHub como Markdown. La lectura requiere un navegador y el laboratorio opcional requiere Python 3.10 o posterior. Las prácticas usan datos sintéticos, explican los términos al introducirlos y enlazan al mapa. Las evidencias se guardan localmente o en un portafolio a elección del estudiante.

Las contribuciones se preparan en DEV, se verifican en QA y se publican en MAIN. En QA se comprueban rutas internas, criterios de salida y la reproducción de los laboratorios incluidos.

## Evolución

La primera entrega establece seis etapas y un laboratorio reproducible. Las próximas ampliaciones pueden dividir las etapas en lecciones, añadir cuestionarios y laboratorios, e incorporar referencias por tema. Cada ampliación incluirá un resultado verificable antes de publicarse.

## Roadmap interactivo

El HTML autónomo presenta siete niveles por itinerario. Los cuatro niveles comunes iniciales desembocan en una especialización elegida por el estudiante. Las cuatro ramas convergen en validación defensiva avanzada y preparación laboral.

Cada módulo contiene tres conceptos, un ejercicio con datos ficticios y pasos explícitos, un resultado de referencia, una lista de evidencias y dos preguntas. Verificar un módulo requiere confirmar todas las evidencias y acertar ambas respuestas. El HTML guía hacia el primer nivel pendiente del itinerario y conserva el progreso por rama cuando el navegador ofrece almacenamiento local. Las guías del repositorio se abren por internet.

Cada módulo ofrece un cuaderno local con método, resultado y decisión. El estudiante puede editar borradores sin alterar sus verificaciones. El portafolio Markdown incluye los módulos con notas y su estado de autoevaluación. La copia JSON guarda la ruta, resultados y borradores. La restauración valida el formato, muestra un resumen y requiere aceptar el reemplazo del avance actual.

El recorrido incluye tres laboratorios interactivos con escenarios ficticios. La consola de triaje filtra registros y verifica la ventana de correlación, el banco de autorización comprueba decisiones por rol y recurso, y el evaluador de detección revisa las matrices y los límites del contexto operativo. Los laboratorios generan retroalimentación local y pueden añadir el resultado comprobado al cuaderno sin reemplazar las anotaciones existentes.
