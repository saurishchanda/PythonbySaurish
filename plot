import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-10,10,50)
y=x**3

fig = plt.figure(figsize=(10, 8))

plt.plot(x, y)


plt.show()
