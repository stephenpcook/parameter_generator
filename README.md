# Parameter randomiser

Python functions for creating the product of iterables.  The intended use is
when the output product is expected to be very large, and we want to take random
samples without generating the whole thing.

The main functionality is delivered through the `Product` class, accessible from
`rand_param`:

```python
>>> from rand_param import Product
>>> p = Product([range(1000)]*5)
>>> p[-1]
(999, 999, 999, 999, 999)
```

A demonstration script is included as `parameter_generation.py`, which produces
a random distribution of parameters for an experiment in a CSV file, and
histograms of each parameter.

Stephen P. Cook 2022-11
