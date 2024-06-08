import numpy as np
import time

# KODE SUMBER
def simpson_13(f, a, b, N):
    if N % 2 == 1:
        raise ValueError("N harus genap untuk metode Simpson 1/3")
    
    h = (b - a) / N
    x = np.linspace(a, b, N + 1)
    y = f(x)
    
    S = y[0] + y[-1]
    S += 4 * sum(y[1:-1:2])
    S += 2 * sum(y[2:-2:2])
    
    return (h / 3) * S

def f(x):
    return 4 / (1 + x**2)

# KODE TESTING
# Untuk variasi nilai dari N
N_values = [10, 100, 1000, 10000]

# Untuk nilai referensi pi
pi_ref = 3.14159265358979323846

# Galat RMS dan waktu eksekusi
rms_errors = []
execution_times = []

for N in N_values:
    start_time = time.time()
    integral_value = simpson_13(f, 0, 1, N)
    end_time = time.time()
    
    rms_error = np.sqrt((integral_value - pi_ref)**2)
    execution_time = end_time - start_time
    
    rms_errors.append(rms_error)
    execution_times.append(execution_time)
    
    print(f"N = {N}, Integral = {integral_value}, RMS Error = {rms_error}, Execution Time = {execution_time} seconds")
