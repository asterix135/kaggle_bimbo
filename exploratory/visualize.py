import matplotlib.pyplot as plt

import time
from load_data import load_train

start_time = time.time()
subset = False

all_data = load_train(subset)

# Histogram for weeks
plt.hist(all_data['Semana'], bins=7)
plt.xlabel('Week')
plt.ylabel('Count')
plt.title('Week histogram')
plt.grid(True)
plt.savefig('histograms/week.png', format='png')
plt.clf()

# Histogram for weekly sales units
plt.hist(all_data['Venta_uni_hoy'], log=True, bins=50)
plt.xlabel('Unit sales per week')
plt.ylabel('Count')
plt.title('Histogram of unit sales per week')
plt.grid(True)
plt.savefig('histograms/unit_sales.png', format='png')
plt.clf()

# Histogram for weekly sales in pesos
plt.hist(all_data['Venta_hoy'], log=True, bins=50)
plt.xlabel('Peso sales per week')
plt.ylabel('Count')
plt.title('Histogram of sales per week in pesos')
plt.grid(True)
plt.savefig('histograms/peso_sales.png', format='png')
plt.clf()

# Histogram for weekly return units
plt.hist(all_data['Dev_uni_proxima'], log=True, bins=50)
plt.xlabel('Unit returns per week')
plt.ylabel('Count')
plt.title("Histogram of unit returns per week")
plt.grid(True)
plt.savefig('histograms/unit_returns.png', format='png')
plt.clf()

# Histogram for weekly returns in pesos
plt.hist(all_data["Dev_proxima"], log=True, bins=50)
plt.xlabel('Returns per week in pesos')
plt.ylabel('Count')
plt.title('Histogram of returns per week in pesos')
plt.grid(True)
plt.savefig('histograms/peso_returns.png', format='png')

# Histogram for Demanda_uni_equil
plt.hist(all_data['Demanda_uni_equil'], log=True, )
