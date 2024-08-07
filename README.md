# EdgeScramble
**Image Left**:  Original edges\
**Image Right**: Scrambled edges\

![Result](https://github.com/pkorrapati/EdgeScramble/raw/main/results/Result_15px.png)

# Example

See simpleExample.py and imageExample.py for a detailed examples

# Usage
```python
rows, cols = scramble(GRAYSCALE_EDGES_IMAGE, pix=NO_OF_PIXELS_TO_RANDOMIZE_BY)
```

or

```python
rows, cols = scramble2(GRAYSCALE_EDGES_IMAGE, pix=NO_OF_PIXELS_TO_RANDOMIZE_BY)
```

# Appendix
## Cartesian Uniform Distribution. (Method: scramble)
Each pixel that is on the detected edge gets a randomized new position that lies in a rectangular neighborhood spanning &pm;*pix*

<img src="https://github.com/pkorrapati/EdgeScramble/raw/main/distributions/scramble_distribution.png" alt="Cartesian Uniform Distribution" width="300px" style="max-width: 300px !important;">

## Euler Uniform Distribution. (Method: scramble2)
Each pixel that is on the detected edge gets a randomized new position that lies in a circular neighborhood with radius *pix*

<img src="https://github.com/pkorrapati/EdgeScramble/raw/main/distributions/scramble2_distribution.png" alt="Euler Uniform Distribution" width="300px" style="max-width: 300px !important;">

