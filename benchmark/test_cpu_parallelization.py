import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import ndimage as ndi
from skimage import morphology
from quanfima import simulation
from quanfima import morphology as mrph
from quanfima import utils
from quanfima import visualization as vis
import time
from multiprocessing import cpu_count

n_cpu = cpu_count()
cpu_use = int(n_cpu / 2)
print("nb cpu used = ", cpu_use)

lst_fibers = [1, 2, 3, 4, 5, 10, 15, 20]
nb_run = 10

result = pd.DataFrame(columns=["n fibers", "volume", "radius_lim", "elapsed time", "parallelization"])
for iteration in range(1, nb_run + 1):
	for n_fib in lst_fibers:
		start = time.perf_counter()
		volume, lat_ref, azth_ref, diameter, _, _ = \
		  simulation.simulate_fibers((128,128,128), n_fibers=n_fib, max_fails=100,
									 radius_lim=(2, 8), gap_lim=(3,5), parallelization="CPU")
		end = time.perf_counter()
		result=result.append({"n fibers":n_fib, "volume":(128,128,128), "radius_lim":(2,8), "elapsed time":end - start, "parallelization": f"yes ({cpu_use})"}, ignore_index=True)

print ("\n\n", result)
print("batch 1 fin")

for iteration in range(1, nb_run + 1):
	for n_fib in lst_fibers:
		start = time.perf_counter()
		volume, lat_ref, azth_ref, diameter, _, _ = \
		  simulation.simulate_fibers((256,256,256), n_fibers=n_fib, max_fails=100,
									 radius_lim=(2, 8), gap_lim=(3,5), parallelization="CPU")
		end = time.perf_counter()
		result=result.append({"n fibers":n_fib, "volume":(256,256,256), "radius_lim":(2,8), "elapsed time":end - start, "parallelization": f"yes ({cpu_use})"}, ignore_index=True)

print ("\n\n", result)
print("batch 2 fin")

for iteration in range(1, nb_run + 1):
	for n_fib in lst_fibers:
		start = time.perf_counter()
		volume, lat_ref, azth_ref, diameter, _, _ = \
		  simulation.simulate_fibers((128,128,128), n_fibers=n_fib, max_fails=100,
									 radius_lim=(2, 8), gap_lim=(3,5))
		end = time.perf_counter()
		result=result.append({"n fibers":n_fib, "volume":(128,128,128), "radius_lim":(2,8), "elapsed time":end - start, "parallelization": "no"}, ignore_index=True)

print("batch 3 fin")
for iteration in range(1, nb_run + 1):
	for n_fib in lst_fibers:
		start = time.perf_counter()
		volume, lat_ref, azth_ref, diameter, _, _ = \
		  simulation.simulate_fibers((256,256,256), n_fibers=n_fib, max_fails=100,
									 radius_lim=(2, 8), gap_lim=(3,5))
		end = time.perf_counter()
		result=result.append({"n fibers":n_fib, "volume":(256,256,256), "radius_lim":(2,8), "elapsed time":end - start, "parallelization": "no"}, ignore_index=True)

#print("batch 4 fin")
#for iteration in range(1, nb_run + 1):
#	for n_fib in [1, 2, 3, 4, 5, ]:
#		start = time.perf_counter()
#		volume, lat_ref, azth_ref, diameter, _, _ = \
#		  simulation.simulate_fibers((128,128,128), n_fibers=n_fib, max_fails=100,
#									 radius_lim=(8, 16), gap_lim=(3,5))
#		end = time.perf_counter()
#		result=result.append({"n fibers":n_fib, "volume":(128,128,128), "radius_lim":(16,24), "elapsed time":end - start, "parallelization": "no"}, ignore_index=True)

#print("batch 5 fin")
#for iteration in range(1, nb_run + 1):
#	for n_fib in lst_fibers:
#		start = time.perf_counter()
#		volume, lat_ref, azth_ref, diameter, _, _ = \
#		  simulation.simulate_fibers((128,128,128), n_fibers=n_fib, max_fails=100,
#									 radius_lim=(8, 16), gap_lim=(3,5), parallelization="CPU")
#		end = time.perf_counter()
#		result=result.append({"n fibers":n_fib, "volume":(128,128,128), "radius_lim":(16,24), "elapsed time":end - start, "parallelization": f"yes ({cpu_use})"}, ignore_index=True)

print("batch 6 fin")
result.to_csv("benchmark_parallelization.csv")
exit()