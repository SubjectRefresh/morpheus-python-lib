# morpheus-python-lib
A Python library for interacting with the Morpheus API

## Installation
```git clone https://github.com/subjectrefresh/morpheus-python-lib.git```

## Example

>Note: Morpheus requires Python 3.5

```python
import morpheus

output = morpheus.convert("pdf", "html", "http://milesbudden.com/morpheus.pdf")

# This may be slow with some files. Try writing to a file if it takes too long.
print(output)
```