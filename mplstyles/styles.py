import os
import matplotlib.pyplot as plt

_pth = os.path.dirname(os.path.realpath(__file__))
_style_names = ['paper','notebook','presentation','website']

_paths = {}
for name in _style_names:
    _paths[name] = os.path.join(_pth, f'{name}.mplstyle')

def _set_style(style):
    """set matplotlib style to custom settings

    Parameters
    ----------
    style : str
        style name from ['paper','notebook','presentation','website']
    """
    plt.style.use(_paths[style])


class StyleContext(object): 
    def __init__(self, style): 
        self.style = style
      
    def __enter__(self): 
        _set_style(self.style)
  
    def __exit__(self,type, value, traceback): 
        plt.style.use('default')