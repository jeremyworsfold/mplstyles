from mplstyles import StyleContext, _set_style, _style_names
import matplotlib.pyplot as plt
import numpy as np


def test_plot():
    x = np.arange(10)
    y1 = np.random.uniform(0,1,10)
    y2 = np.random.uniform(0,1,10)

    for style in _style_names:
        _set_style(style)
        plt.figure()
        plt.plot(x,y1,label='line1')
        plt.plot(x,y2,label='line2')
        plt.legend()
        plt.xlabel(r'Time ($t$)')
        plt.ylabel(r'$y(t)$')
        plt.savefig(f'figs/line_{style}')

def test_colormap():
    X = np.arange(20)
    Y = np.arange(20) 
    XX,YY = np.meshgrid(X,Y)
    vals = XX+YY

    for style in _style_names:
        _set_style(style)
        fig,ax = plt.subplots()
        cax = ax.imshow(vals)
        ax.grid(False)
        fig.colorbar(cax)
        fig.savefig(f'figs/colormap_{style}')

def test_context():
    x = np.arange(10)
    y1 = np.random.uniform(0,1,10)
    y2 = np.random.uniform(0,1,10)

    for style in _style_names:
        with StyleContext(style):
            plt.figure()
            plt.plot(x,y1,label='line1')
            plt.plot(x,y2,label='line2')
            plt.legend()
            plt.xlabel(r'Time ($t$)')
            plt.ylabel(r'$y(t)$')
            plt.savefig(f'figs/line_{style}')

if __name__ == "__main__":
    test_plot()
    test_colormap()
    test_context()