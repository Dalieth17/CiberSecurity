# Especificación de requisitos de software

## 1. Propósito y alcance

CiberSecurity ayudará a estudiantes y mantenedores a revisar eventos de autenticación en un entorno local. La versión 0.1 será una interfaz de línea de comandos que resume intentos fallidos a partir de un archivo sintético, sin modificarlo. La versión inicial se limita a procesamiento por lotes local.

## 2. Usuarios

- Analista o estudiante. Proporciona el archivo sintético y consulta el resumen.
- Mantenedor. Desarrolla en `DEV`, verifica en `QA` y publica en `MAIN`.

## 3. Requisitos funcionales

| ID | Requisito | Criterio de aceptación |
| --- | --- | --- |
| RF-01 | Leer un archivo JSON Lines con un objeto por línea. Cada objeto incluye `actor_id` y `outcome`. | El ejemplo incluido produce un resumen JSON en stdout. |
| RF-02 | Contar solo eventos con `outcome` igual a `failure`, agrupados por identificador. `success` es el otro valor válido. | Dos fallos y un éxito del mismo actor producen un recuento de dos. |
| RF-03 | Contar líneas inválidas y continuar. Se consideran inválidas las líneas vacías, el JSON malformado, el UTF-8 inválido y los registros que incumplen el contrato. | Los registros válidos posteriores a una línea inválida aparecen en el resumen. |
| RF-04 | Admitir archivos vacíos y comunicar errores de lectura. | Un archivo vacío devuelve recuentos vacíos y cero líneas inválidas. Un error de lectura devuelve código 1 y un diagnóstico genérico por stderr. |

## 4. Datos, interfaces y calidad

- Entrada. Ruta local y contenido JSON Lines codificado en UTF-8. Para datos sintéticos, `actor_id` tiene el formato `actor-N`, con entre uno y nueve dígitos ASCII. Se ignoran los campos adicionales.
- Salida. Objeto JSON con `failed_attempts` e `invalid_lines`. El orden de las claves es estable. El código de salida es 0 al completar el análisis, incluso si hay líneas inválidas. Un uso incorrecto de la CLI devuelve 2.
- Privacidad. El informe incluye solo identificadores con el formato sintético y recuentos. Los diagnósticos omiten rutas y contenido de registros. Para las pruebas se usan exclusivamente datos ficticios.
- Portabilidad. Python 3.10 o posterior, sin dependencias externas ni acceso a la red en ejecución.
- Recursos. Lectura secuencial. La memoria depende de la línea más larga y del número de actores distintos con fallos.

## 5. Diseño y entrega

`cibersecurity.py` contiene la validación, la agregación y la CLI. `examples/` contiene la entrada sintética y `tests/` verifica la interfaz y sus casos límite.

1. En `DEV`, actualiza los requisitos, implementa y añade las pruebas que correspondan.
2. En `QA`, prueba el commit candidato con `python3 -m unittest discover -s tests -v` y ejecuta el ejemplo del README. Si hay un fallo, corrígelo en `DEV` y repite ambas verificaciones.
3. Promueve a `MAIN` el commit verificado. Deja constancia de los resultados de QA junto a la entrega.

## 6. Evolución

Después de la versión 0.1 se podrán evaluar alertas por umbral y filtros temporales. Antes de incorporarlos, amplía esta especificación con sus formatos, comportamiento y pruebas de aceptación.
