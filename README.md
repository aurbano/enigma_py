# Enigma Machine Emulator

## Documentation

All modules are annotated with docstrings, if you want to see generated documentation the project also include sphinx config for it:

```
pip install sphinx
cd docs
make html
open _build/index.html
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
