# Triaje con una línea de tiempo

**Necesitas** haber completado el [laboratorio de autenticación](../04-deteccion.md). Esta práctica se resuelve leyendo la tabla.

## Caso

A las 09:05 UTC recibes una alerta por tres fallos de autenticación del mismo actor en cinco minutos. Los equipos y actores de la tabla son ficticios.

| Hora UTC | Actor | Equipo | Evento |
| --- | --- | --- | --- |
| 09:00 | actor-1 | equipo-A | Fallo |
| 09:01 | actor-1 | equipo-A | Fallo |
| 09:03 | actor-1 | equipo-A | Fallo |
| 09:04 | actor-1 | equipo-B | Éxito |
| 09:06 | actor-2 | equipo-C | Éxito |

1. Escribe la secuencia relevante y calcula el intervalo entre primer fallo y éxito.
2. Formula dos hipótesis. Considera tanto un cambio legítimo de equipo como un posible uso indebido de la cuenta.
3. Indica qué evidencia distinguiría las hipótesis. Incluye a quién solicitarías confirmación y qué registros consultarías.
4. Redacta una nota de triaje con hechos, hipótesis, decisión y próxima acción.

## Comprueba tu respuesta

Los tres fallos se concentran en tres minutos y el inicio exitoso ocurre cuatro minutos después del primer fallo, desde otro equipo. El éxito posterior merece revisión, pero la tabla por sí sola no demuestra un compromiso. Una próxima acción razonable es validar con el responsable de la cuenta y revisar el inventario de equipos y los registros del segundo factor. El evento de `actor-2` por sí solo no aporta evidencia sobre la alerta.

**Entrega:** conserva tu nota de triaje como evidencia de portafolio. Incluye qué hallazgo elevaría la prioridad y qué confirmación permitiría cerrar el caso.

[Volver a detección y respuesta](../04-deteccion.md)
