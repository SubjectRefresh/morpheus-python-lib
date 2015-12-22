# morpheus-python-lib
A Python library for interacting with the Morpheus API

## Installation
```git clone https://github.com/subjectrefresh/morpheus-python-lib.git```

## Example

>Note: Morpheus requires Python 3.5

```python
import morpheus

output = morpheus.convert("pdf", "html", "http://www.indire.it/wp-content/uploads/2015/08/pdf-sample.pdf")

# This may be slow with some files. Try writing to a file if it takes too long.
print(output)
```