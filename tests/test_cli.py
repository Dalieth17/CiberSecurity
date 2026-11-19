import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


class AuthenticationCliTest(unittest.TestCase):
    def run_cli(self, *args):
        return subprocess.run(
            [sys.executable, str(ROOT / "cibersecurity.py"), *map(str, args)],
            capture_output=True,
            text=True,
        )

    def run_records(self, records):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "events.jsonl"
            source.write_bytes(records)
            return self.run_cli(source)

    def test_example(self):
        result = self.run_cli(ROOT / "examples/autenticacion.jsonl")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(
            json.loads(result.stdout),
            {"failed_attempts": {"actor-1": 2, "actor-2": 1}, "invalid_lines": 1},
        )

    def test_empty_file(self):
        result = self.run_records(b"")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout), {"failed_attempts": {}, "invalid_lines": 0})

    def test_invalid_records_do_not_stop_analysis_or_leak_values(self):
        result = self.run_records(
            b'\xff\n\n{\n[]\n{"actor_id":"sensitive@example.invalid","outcome":"failure"}\n'
            b'{"actor_id":"actor-3","outcome":[]}\n{"actor_id":"actor-3","outcome":"failure"}'
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(
            json.loads(result.stdout), {"failed_attempts": {"actor-3": 1}, "invalid_lines": 6}
        )
        self.assertEqual(result.stderr, "")

    def test_missing_file(self):
        with tempfile.TemporaryDirectory() as directory:
            result = self.run_cli(Path(directory) / "missing.jsonl")
        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stdout, "")
        self.assertEqual(result.stderr.strip(), "No se pudo leer el archivo de entrada.")

    def test_requires_input_path(self):
        self.assertEqual(self.run_cli().returncode, 2)
