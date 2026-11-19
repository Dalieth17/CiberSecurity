# 1. Fundamentos

**Requisitos previos:** ninguno. **Material:** una hoja de papel o un editor de texto.

## Qué se protege

Un **activo** es algo que importa, como una cuenta, un archivo o un servicio. Una **amenaza** es una causa potencial de daño. Una **vulnerabilidad** es una debilidad que puede facilitarlo. El **riesgo** combina la probabilidad y el impacto del daño. Un **control** reduce ese riesgo. Una pérdida de acceso a una cuenta es un impacto posible de depender de un solo método de recuperación.

La confidencialidad protege frente a divulgaciones indebidas. La integridad protege frente a cambios indebidos. La disponibilidad permite usar el recurso cuando hace falta. El mismo archivo puede requerir las tres propiedades.

## Identidad, acceso y evidencia

La autenticación comprueba quién solicita acceso. La autorización comprueba qué puede hacer esa identidad. Una persona puede iniciar sesión correctamente y carecer de permisos para aprobar un pago.

Un evento es algo que sucede y un registro es la evidencia que produce el sistema. Un fallo de autenticación puede deberse a un error al escribir. Para justificar una escalada, explica qué observaste, qué hipótesis tienes y qué evidencia falta.

## Práctica

Imagina una cafetería con una cuenta de correo, el archivo de ventas y el servicio de pedidos. Para cada activo, anota su responsable, qué puede salir mal, qué propiedad se vería afectada y un control verificable.

| Activo | Riesgo | Control | Verificación |
| --- | --- | --- | --- |
| Archivo de ventas | Pérdida del archivo por un fallo del equipo | Copia de seguridad periódica | Restaurar una copia ficticia y comprobar sus datos |

**Criterio de salida:** documenta tres activos con un riesgo y un control por activo, cubre confidencialidad, integridad y disponibilidad al menos una vez, y explica con un ejemplo la diferencia entre autenticación y autorización.

[Continuar a sistemas y redes](02-sistemas-redes.md) · [Volver al mapa](README.md)
