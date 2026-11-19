# Proyecto final · Triaje de una alerta SOC

Actúas como analista junior de un centro de operaciones de seguridad (SOC). Recibes una alerta a las 14:05 UTC por al menos tres fallos del mismo actor y servicio en cinco minutos. El equipo entrante necesita saber qué ocurrió, qué sigue pendiente y quién debe revisarlo.

**Antes de empezar:** completa la [práctica de triaje](../../practicas/triaje.md). Abre los [eventos sintéticos](eventos.csv) con un editor o una hoja de cálculo. Todos corresponden al mismo día y los identificadores de equipo no indican si eran dispositivos autorizados.

## Trabajo

1. Verifica la alerta. Documenta actor, servicio, identificadores de los fallos y minutos entre el primero y el último. Mantén la hora en UTC.
2. Reconstruye la secuencia posterior. Distingue los eventos directamente relacionados con la regla de los que aportan contexto. Explica por qué el éxito en el servicio de archivos merece revisión aunque no pertenezca al recuento de fallos de correo.
3. Formula una hipótesis legítima y otra de acceso indebido. Para cada una, señala qué evidencia la apoyaría o debilitaría.
4. Decide si cierras o escalas para revisión. Indica prioridad, justificación, responsable de la próxima acción y qué confirmación cambiaría la decisión. Describe el estado provisional del caso.
5. Completa la [plantilla de informe](informe.md) y revisa tu entrega con la rúbrica. Para el portafolio, incorpora el CSV y los pasos necesarios para reproducir tu análisis.

## Rúbrica

Asigna **0** si falta la evidencia, **1** si es parcial y **2** si otra persona puede verificarla siguiendo el informe.

| Aspecto | Para obtener 2 puntos |
| --- | --- |
| Reproducción de la alerta | Identifica el actor y el servicio correctos, cita los tres eventos y calcula el intervalo. |
| Línea de tiempo | Ordena los eventos en UTC y explica cuáles activan la regla y cuáles aportan contexto. |
| Hipótesis | Plantea dos explicaciones y solicita evidencia concreta para distinguirlas. |
| Decisión | Justifica prioridad y estado, asigna la siguiente acción y especifica qué cambiaría la decisión. |
| Portafolio | Incluye el CSV, pasos reproducibles, limitaciones y una síntesis que otra persona pueda explicar. |

**Criterio de salida:** alcanza al menos 8 de 10 puntos, con 2 en reproducción de la alerta y en decisión.

<details>
<summary>Comprobar la alerta después de entregar</summary>

E01, E02 y E04 son fallos de actor-1 en correo. Ocurren entre las 14:02 y las 14:04 UTC, un intervalo de dos minutos. E05 y E06 muestran accesos exitosos desde equipo-C, pero no establecen quién estaba usando la cuenta ni si el equipo estaba autorizado. Una acción defendible es escalar para revisión y pedir al equipo de identidad que confirme el uso del segundo factor y la relación del equipo con la cuenta.

</details>

[Preparar el portafolio](../../06-empleo.md) · [Volver al mapa](../../README.md)
