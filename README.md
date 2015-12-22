# morpheus-python-lib
A Python library for interacting with the Morpheus API

## Installation
```git clone https://github.com/subjectrefresh/morpheus-python-lib.git```

## Example

Note: Morpheus requires Python 2.5

```python
import morpheus

output = morpheus.convert("pdf", "html", "http://www.indire.it/wp-content/uploads/2015/08/pdf-sample.pdf")

print(output)
```