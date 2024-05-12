# EdgeScramble
Left:  Image with original edges
Right: Image with scrambled edges
![alt Result](https://github.com/pkorrapati/EdgeScramble/blob/main/Result_15px.png)

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
Each pixel that is on the detected edge gets a randomized new position that lies in a rectangular neighborhood of +/- pix

![alt Result](https://github.com/pkorrapati/EdgeScramble/blob/main/scramble_distribution.png)

## Euler Uniform Distribution. (Method: scramble2)
Each pixel that is on the detected edge gets a randomized new position that lies in a circular neighborhood of radius pix

![alt Result](https://github.com/pkorrapati/EdgeScramble/blob/main/scramble2_distribution.png)
