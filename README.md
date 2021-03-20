# mplstyle

Custom matplotlib styles to quickly make plots for me to add to papers, python notebooks, my website or presentations.

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

### Adding to default styles

You can take these `.mplstyle` files and put them with the default matplotlib styles if you can find their location. The location will be wherever your python version is stored and in something like 
```bash
Python39/Lib/site-packages/matplotlib/mpl-data/stylelib/
```
If you do this then you can use matplotlib's standard functionality for styles:
```python
import matplotlib.pyplot as plt

print(plt.style.available)

plt.style.use('presentation')

with plt.style.context('notebook'):
    plt.plot(range(5),range(5))
```