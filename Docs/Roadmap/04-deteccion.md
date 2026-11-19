# 4. Detección y respuesta

Completa primero [Seguridad aplicada](03-seguridad-aplicada.md).

Un evento es un hecho observado, una alerta señala que una regla o un analista considera que merece revisión y el triaje determina qué atención necesita. Un informe debe distinguir lo observado, las hipótesis y la decisión.

## Laboratorio de autenticación

Abre el [archivo sintético](../../examples/autenticacion.jsonl). Cada línea representa un registro. Cuenta los eventos con `outcome` igual a `failure` por identificador. Marca como inválido el evento al que le falta `outcome`.

Puedes verificar el resultado con Python 3.10 o posterior, desde la raíz del repositorio:

```bash
python3 cibersecurity.py examples/autenticacion.jsonl
```

Resultado esperado:

```json
{"failed_attempts": {"actor-1": 2, "actor-2": 1}, "invalid_lines": 1}
```

El recuento permite priorizar qué registros revisar. Los datos carecen de hora y contexto, por lo que no permiten determinar si hubo un incidente. Redacta un informe que incluya fuente, observaciones, hipótesis, datos faltantes y una acción siguiente. Una acción válida es solicitar marcas de tiempo y el contexto de autenticación al responsable.

**Criterio de salida:** reproduce los recuentos y explica por qué reportarías un evento para revisión o lo cerrarías. Indica qué dato adicional cambiaría tu decisión.

[Continuar a perfiles profesionales](05-perfiles.md) · [Volver al mapa](README.md)
