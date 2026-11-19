# Terminal, archivos y permisos

**Necesitas** una terminal Bash en Linux, macOS o WSL. Ejecuta cada bloque en la misma sesión. La práctica crea una carpeta temporal y solo modifica un archivo ficticio dentro de ella.

## Ubicarte y crear un archivo

Una ruta absoluta empieza en la raíz del sistema. Una ruta relativa se interpreta desde tu directorio actual. Los nombres que se pasan entre comillas se interpretan como un solo argumento, aunque incluyan espacios.

```bash
directorio_practica=$(mktemp -d)
cd "$directorio_practica"
pwd
printf '%s\n' 'actor-1 failure' 'actor-1 success' 'actor-2 failure' > eventos.txt
ls -l eventos.txt
```

`pwd` muestra una ruta absoluta. `eventos.txt` es relativa a esa ruta. El operador `>` escribe la salida en el archivo indicado y reemplaza su contenido si ya existe.

## Filtrar y contar

```bash
grep -n 'failure$' eventos.txt
grep -c 'failure$' eventos.txt
```

La primera orden muestra las líneas 1 y 3. La segunda imprime `2`. El signo `$` en el patrón exige que `failure` aparezca al final de la línea.

## Revisar permisos

```bash
chmod 600 eventos.txt
ls -l eventos.txt
```

Al inicio de la salida verás `-rw-------`. El primer carácter indica un archivo regular. Los tres grupos siguientes representan permisos de propietario, grupo y otros. Aquí el propietario puede leer y escribir. Los otros dos grupos no reciben permisos ordinarios sobre el archivo.

**Entrega:** guarda el recuento y el modo observado. Explica quién puede leer el archivo con esos permisos y por qué conviene crear una carpeta temporal para practicar.

[Volver a sistemas y redes](../02-sistemas-redes.md)
