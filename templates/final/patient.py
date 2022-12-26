import tkinter as tk
from tkinter import ttk


def main_window():
    root = tk.Tk()

    root.mainloop()

if __name__ == '__main__':
    main_window()

# creat a sine wave
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10, 0.1)
y = np.sin(x)
plt.plot(x, y)
plt.show()
