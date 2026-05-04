import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import numpy as np

P = lambda w: w**2 - 6 * w + 13

w = np.linspace(0, 6, 101)
plt.plot(w, P(w), linewidth=2)
plt.plot(3, P(3), 'ro')
plt.xlabel('w')
plt.ylabel('P(w)')
plt.title('Plot of $P(w) = w^2 - 6w + 13$')
plt.ylim(0, 15)
plt.grid()
plt.savefig('second_order_polynomial_plot.pdf')
plt.show()