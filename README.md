# Enigma Machine Emulator

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
