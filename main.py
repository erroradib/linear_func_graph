# Author: Adnan Adib
# 14th June, 2024
# 12:08 AM
import os
try:
    import matplotlib.pyplot as PLOT
    import numpy as np

except ImportError:
    
    os.system("pip install matplotlib")
    os.system("pip install numpy")
    import matplotlib.pyplot as PLOT
    import numpy as np





def plot_func(m, c, x_range=(-10, 10), num_point=400):
    x_val = np.linspace(x_range[0], x_range[1], num_point)
        
    y_val = m * x_val + c
        
    PLOT.figure(figsize=(8, 6))
    PLOT.plot(x_val, y_val, label=f'y = {m}x + {c}', color='red')
    PLOT.title(f'Plot of y = {m}x + {c}\nDev: Adnan Adib')
    PLOT.xlabel('x')
    PLOT.ylabel('y')
    PLOT.legend()
    PLOT.grid(True)
    PLOT.show()

if __name__ == "__main__":
        while True:
            try:
                m = input("slope, m: ")
                c = input("y-intercept, c: ")
                m = float(m)
                c = float(c)
                plot_func(m, c)
            except ValueError as e:
                print(e)
                
            command = input("do you want to plot another line (y/n): ").strip().lower()
            if command != 'y':
                print("Exiting...")
                break
