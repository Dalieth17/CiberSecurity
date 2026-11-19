# Leer una conexión HTTPS

**Necesitas** papel o un editor. Los datos son ficticios y puedes resolver la práctica sin conexión.

## Del nombre a la respuesta

Lee este registro simplificado. Las direcciones pertenecen a rangos reservados para documentación.

| Paso | Observación |
| --- | --- |
| 1 | DNS resuelve `portal.example` como `192.0.2.20`. |
| 2 | El cliente `198.51.100.7` abre una conexión TCP desde el puerto `51000` hacia el puerto `443` del servidor. |
| 3 | El cliente negocia TLS y valida el certificado para `portal.example`. |
| 4 | El servidor recibe la solicitud `GET /informe` y responde `403 Forbidden`. |

Dibuja cliente y servidor. Añade el nombre, las IP, los puertos y el orden de los pasos. Identifica en qué capa se observó la negativa y qué evidencia pedirías al propietario del servicio.

## Comprueba tu respuesta

DNS resolvió el nombre, TCP estableció el transporte y TLS protegió la conexión. El `403` es una decisión de la capa HTTP. Para entender el motivo, revisa los permisos esperados para la cuenta ficticia y solicita al propietario los registros de la aplicación vinculados a la solicitud.

Si DNS no puede resolver el nombre y el cliente carece de una dirección alternativa, la secuencia se interrumpe antes de TCP. Si falla la validación del certificado, no se debe continuar con la solicitud HTTPS.

**Entrega:** incluye el diagrama, una explicación del `403` y un dato que permitiría confirmar su causa.

[Volver a sistemas y redes](../02-sistemas-redes.md)
