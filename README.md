# CiberSecurity

Proyecto de ciberseguridad defensiva. El prototipo 0.1 analiza registros sintéticos de autenticación y resume los intentos fallidos.

## Ejecutar el prototipo

Con Python 3.10 o posterior, desde la raíz del repositorio:

```bash
python3 cibersecurity.py examples/autenticacion.jsonl
```

Resultado esperado:

```json
{"failed_attempts": {"actor-1": 2, "actor-2": 1}, "invalid_lines": 1}
```

Para ejecutar las pruebas:

```bash
python3 -m unittest discover -s tests -v
```

## Ramas y documentación

- `DEV` para desarrollo, `QA` para validación y `MAIN` para publicar versiones verificadas.
- [SRS](Docs/SRS.md) describe el alcance, las interfaces y los criterios de aceptación.
- [Guía de desarrollo](Docs/desarrollo.md) documenta las prácticas de trabajo.
- [AGENTS.md](AGENTS.md) orienta a los asistentes de IA.
