"""Coding softmax function to work in numpy."""
import numpy as np
import matplotlib.pyplot as plt


def softmax(inp):
    """Softmax function in short."""
    return np.exp(inp) / np.sum(np.exp(inp))


def calc_softmax(inp):
    """Calculate softmax score for a numpy array."""
    if isinstance(inp, np.ndarray)==False:
        inp = np.array(inp)
    return softmax(inp)


def plt_softmax(inp):
    """Plot range of softmax values."""
    print(inp)
    print(calc_softmax(inp))
    plt.plot(inp, calc_softmax(inp), linewidth=2)
    plt.show()


def test():
    """The course op required."""
    scores = np.array([[1, 2, 3, 6], [2, 4, 5, 6], [3, 8, 7, 6]])
    plt_softmax(scores)
    x = np.arange(-2.0, 6.0, 0.1)
    scores = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])
    plt_softmax(scores)