# 2. Sistemas y redes

Completa primero [Fundamentos](01-fundamentos.md).

## Conceptos

Un proceso es un programa en ejecución. El sistema operativo administra procesos, archivos y permisos. Los permisos de lectura, escritura y ejecución indican qué operaciones puede realizar una identidad sobre un recurso. Aplicar mínimo privilegio significa otorgar solo los permisos necesarios para cumplir la tarea.

Una dirección IP permite direccionar el tráfico. Un puerto identifica un servicio de transporte en un equipo. DNS ayuda a resolver nombres de dominio. HTTP define el intercambio de mensajes entre cliente y servidor. HTTPS utiliza TLS para proteger HTTP en tránsito y verificar la identidad del servidor mediante su certificado. Una conexión TLS válida no establece si el contenido del sitio es confiable.

## Práctica

Dibuja cómo un navegador obtiene una página ficticia. Marca la resolución de nombre, la conexión, TLS y el intercambio HTTP. Después asigna permisos de lectura y escritura a dos perfiles ficticios, lector y editor, sobre una carpeta de informes. Explica cómo verificarías cada permiso desde una cuenta de prueba local.

**Criterio de salida:** explica el papel de DNS, IP, puerto, HTTP y TLS, y muestra una tabla de permisos con una acción permitida y una denegada para el lector.

[Continuar a seguridad aplicada](03-seguridad-aplicada.md) · [Volver al mapa](README.md)
