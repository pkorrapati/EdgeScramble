# EdgeScramble
**Image Left**:  Original edges\
**Image Right**: Scrambled edges\

![Result](https://github.com/pkorrapati/EdgeScramble/raw/main/Result_15px.png)

# Example

See imageTest.py for a detailed example

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

<img src="https://github.com/pkorrapati/EdgeScramble/raw/main/scramble_distribution.png" alt="Cartesian Uniform Distribution" style="max-width: 40%;">

## Euler Uniform Distribution. (Method: scramble2)
Each pixel that is on the detected edge gets a randomized new position that lies in a circular neighborhood with radius *pix*

<img src="https://github.com/pkorrapati/EdgeScramble/raw/main/scramble2_distribution.png" alt="Euler Uniform Distribution" style="max-width: 40%;">

