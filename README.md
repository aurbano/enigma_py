# Enigma Machine Emulator

This is a simulator for the Enigma Machine M3 and M4, but extensible so that it can be used to simulate any variant of the Enigma Machine.

### Example

```python
from enigma import Machine
from enigma.builtin_rotors import Rotors

machine = Machine(
    [Rotors["I"](), Rotors["II"](), Rotors["III"]()],
    Rotors["A"]()
)

assert(machine.encode("ENIGMA MACHINE") == "BYEJNJ RSRWHTF")
```

## Documentation

Autogenerated documentation for all modules is available in `docs/index.html` and live in https://aurbano.github.io/enigma.py/

To update the docs:

```
pip install sphinx
cd docs
make github
```

## Test

```
python -m unittest discover -s ./enigma/tests -p '\*\_test.py'
```

## Coverate report

```
coverage run -m unittest discover -s ./enigma/tests -p '*_test.py'
coverage html --omit="*/test*" && open ./htmlcov/index.html
```

## Lint

```
flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
```
