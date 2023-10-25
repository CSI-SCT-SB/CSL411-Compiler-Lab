import matplotlib.pyplot as plt
import numpy as np

data = []
while True:
    try:
        value = float(input("Enter a numeric value (or 'q' to quit): "))
        data.append(value)
    except ValueError:
        break

if data:
    plt.boxplot(data, vert=False)
    plt.xlabel('Data')
    plt.title('Box Plot with Outliers')
    plt.show()
else:
    print("No data to plot.")
