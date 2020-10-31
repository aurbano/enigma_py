# Enigma Machine Emulator

This is a simulator for general Enigma Machines, it includes rotor definitions for most versions of the machine (see list below), and is flexible enough that it can be used to simulate any other ones.

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

## Enigma Versions

This simulator includes a comprehensive list of rotors that were used in the different enigma versions that existed over time.

These rotors are available in `enigma/builtin_rotors.py`, and tests are available in `enigma/tests/custom_extensions_test.py` for most of them.

The following variants have rotors available:

* Enigma M3 & M4
* German Railway (Rocket)
* M3 & M4 Naval
* Swiss K (custom entry wheel)
* M4 R1
* Enigma D
* Enigma KD
* Enigma T - Tirpitz (custom entry wheel)
* Norway (Norenigma)
* Railway Enigma

## Machine Settings

### Arbitrary Number of Rotors
This simulator supports both arbitrary rotos and setting which is the last rotor that can turn. This is because in most versions of the machine, only the first 3 rotors would turn with each keystroke.

### Multiple Notches
Rotors can have from 0 to any number of notches.

### Entry Wheel (i.e. Enigma T - Tirpitz)
Enigma machines could have an entry wheel that determined the wiring from the keys to the plugboard, and from the plugboard to the lamps.

### Extended Alphabet
The rotors allow defining an input alphabet. This can be used to extend from the standard uppercase ASCII used in most machines, to use any unicode character.

Examples of characters that can be encoded with `enigma_py`:

* Alphanumeric
* Mixed-case messages
* Non-roman alphabets (Russian, Japanese... )
* Special characters

`enigma_py/enigma/tests/custom_extensions_test.py` features a test (`test_machine_encodes_custom_alphabets`) with mixed-case inputs and numbers.

It is trivial to use any unicode character - even _emoji_ (as they are just a unicode extension)!

Just for fun I made a few custom "emoji-rotors", so that we can encode:

* Input: `THIS ENIGMA MACHINE SUPPORTS EMOJIS! 😜😍🥰`
* Encoded: `😆QK😗 😋🤣FUR😉 SX😚😇😜T😜 😃😂😃😄U😌A😚 😝😛😘😇W🙃! TO😍`

To see the Machine and rotors used for the strings above look for the `test_emoji_machine`.

## Documentation

Autogenerated documentation for all modules is available in `docs/index.html` and live in https://aurbano.github.io/enigma.py/

To update the docs:

```
pip install sphinx
cd docs-config
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
