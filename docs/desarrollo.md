# Guía de desarrollo

## De la tarea a la revisión

Define cada tarea con su objetivo defensivo, el resultado esperado, los datos de entrada y un criterio de aceptación observable. Identifica qué permisos, archivos o servicios necesita. Para un cambio que maneje datos, documenta qué lee, qué guarda y qué muestra.

Implementa cambios pequeños y revisables. Conserva la compatibilidad con los formatos existentes salvo que la tarea requiera modificarlos. Al presentar un cambio, incluye su propósito, cómo comprobarlo y cualquier impacto en datos o configuración.

## Validación

- Prueba el caso normal y las entradas vacías, incompletas o malformadas que correspondan al cambio.
- Comprueba que los errores sean comprensibles y que los informes omitan secretos y datos personales. Usa archivos sintéticos y mantén las pruebas reproducibles sin depender de servicios externos.
- Cuando exista código, ejecuta las pruebas y las comprobaciones disponibles en el repositorio. Documenta los comandos de instalación y verificación cuando se incorporen por primera vez.
- Ante un hallazgo, registra el componente afectado, el impacto, la mitigación y cómo verificarla. Usa canales privados si el hallazgo contiene información sensible.

## Primera funcionalidad propuesta

Crear un analizador local de registros sintéticos de autenticación. Una primera versión leería un archivo JSON Lines y resumiría los intentos fallidos por identificador ficticio. El informe mostraría los recuentos y señalaría las filas inválidas sin copiar su contenido.

La tarea se puede dar por terminada cuando un archivo de ejemplo produce los recuentos esperados, un archivo vacío produce un resumen vacío y una fila inválida queda contabilizada sin impedir el procesamiento de las filas válidas. La herramienta debe funcionar sin red y con permisos de lectura sobre el archivo de entrada.
