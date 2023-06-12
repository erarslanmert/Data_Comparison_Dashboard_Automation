import numpy as np
import matplotlib.pyplot as plt

P0 = 101325.0  # Pressure [Pa]
d = 0.155  # Diameter [m]
CPA = 0.05  # Closest point of approach [m]
vs = 340.0  # Speed of sound [m/s]
l = 0.8787  # Length scale [m]
amplitudes = []
periods = []
peak_times = [28.093,   32.391,   27.135,   31.960,   27.875,   33.398,   25.751,   21.964,   22.976,   23.599,   31.344]
times = []
Mach = []
def period(M):
    return (1.82 * M * d * CPA**(1/4)) / (vs * (M**2 - 1)**(3/8) * l**(1/4))

def amplitude(M):
    return (0.53 * P0 * (M**2 - 1)**(1/8) * d) / (CPA**(3/4) * l**(1/4))

for i in range(len(peak_times)):
    T_value = period()
    times.append()
    amplitudes.append()


# Create x-axis with time values from 4 to 12 seconds, with 0.01 second increment
# Initialize y-axis values to zero for all time points
# Create scatter plot of peak amplitudes at their corresponding peak times
plt.scatter(peak_times, amplitudes, color='red')
plt.xlabel('Time [s]')
plt.ylabel('Peak Amplitude [Pa]')
plt.title('Peak Amplitudes at Peak Times')
plt.show()





