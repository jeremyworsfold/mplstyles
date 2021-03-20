# mplstyle

## installation

Download this repo and then run

```bash
python3 setup.py install
```

## Usage

```python
import mplstyles

# list possible styles
print(mplstyles._style_names)

# use the set style function to globally set the style
mpltstyles._set_style('paper')
fig, ax = plt.subplots()
ax.plot(range(5),range(5),label='line1')
fig.show()

# or set it for a block of code with a context manager
with mplstyles.StyleContext('presentation'):
    fig, ax = plt.subplots()
    ax.plot(range(5),range(5),label='line1')
    fig.show()

```

Look at the `test.py` script to see more examples of usage and the figures in `figs/` to see what the different types look like.