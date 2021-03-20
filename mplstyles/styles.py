import os
import matplotlib.pyplot as plt
import matplotlib as mpl
import contextlib

_pth = os.path.dirname(os.path.realpath(__file__))
_style_names = ['paper','notebook','presentation','website']

_paths = {}
for name in _style_names:
    _paths[name] = os.path.join(_pth, f'{name}.mplstyle')

def use(style):
    """set matplotlib style to custom settings

    Parameters
    ----------
    style : str
        style name from ['paper','notebook','presentation','website']
    """
    plt.style.use(_paths[style])

@contextlib.contextmanager
def style_context(style,after_reset=False):
    """context manager to set matplotlib style

    Parameters
    ----------
    style : str
        style name from ['paper','notebook','presentation','website']
    after_reset : bool, optional
        If True, apply style after resetting settings to their defaults;
        otherwise, apply style on top of the current settings.
    """
    with mpl.rc_context():
        if after_reset:
            mpl.rcdefaults()
        use(style)
        yield