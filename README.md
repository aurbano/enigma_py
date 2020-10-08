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
