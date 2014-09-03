# Nocolon python encoding

**nocolon** is an utf-8 compatible encoding that removes the need of colons in
python files.

### Disclaimer

**NB: This is wrong, this is in so many ways very wrong.**

This has not been tested, some case like end line comments are not implemented.

This is a toy.

Don't use it, don't look at the source, forget this.

## Example:

```python
# -*- encoding: nocolon -*-

# Python without colons
if True
    for i in range(9)
        print('OMFG')

```


## Install
This has been tested on **python 3.4**, it could work in python 2 but as the
code is parsed in chunks it's a bit more complicated.

### The easy way
```bash
pip install nocolon
```

Now you can import the nocolon package in a regular python file and then import
nocolon files:

`main.py:`
```python
#!/bin/env python
# -*- encoding: utf-8 -*-
import nocolon # This patches the encodings module
import myfilewithoutcolons
```

`myfilewithoutcolons.py:`
```python
# -*- encoding: nocolon -*-

while True
    print('Freedom')
```

### The other way

If you don't want to import the nocolon from another regular python file,
you can put the `nocolon/__init__.py` file in your system directory:
`/usr/lib/python3.4/encodings/nocolon.py` and now you can directly use
`# -*- encoding: nocolon -*-`.

I'm not responsible for endless shit happening after that!
