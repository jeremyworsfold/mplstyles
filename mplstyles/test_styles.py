import mplstyles
import matplotlib.pyplot as plt
import numpy as np


def test_use():
    x = np.arange(10)
    y1 = np.random.uniform(0,1,10)
    y2 = np.random.uniform(0,1,10)

    for style in mplstyles._style_names:
        mplstyles.use(style)
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

    for style in mplstyles._style_names:
        mplstyles.use(style)
        fig,ax = plt.subplots()
        cax = ax.imshow(vals)
        ax.grid(False)
        fig.colorbar(cax)
        fig.savefig(f'figs/colormap_{style}')

def test_style_context():
    x = np.arange(10)
    y1 = np.random.uniform(0,1,10)
    y2 = np.random.uniform(0,1,10)

    for style in mplstyles._style_names:
        with mplstyles.style_context(style):
            plt.figure()
            plt.plot(x,y1,label='line1')
            plt.plot(x,y2,label='line2')
            plt.legend()
            plt.xlabel(r'Time ($t$)')
            plt.ylabel(r'$y(t)$')
            plt.savefig(f'figs/line_{style}')

if __name__ == "__main__":
    test_use()
    test_colormap()
    test_style_context()