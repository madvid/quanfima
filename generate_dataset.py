from quanfima import simulation

# =========================================================================== #
#                      definition of variables for dataset generation
# =========================================================================== #

# number of fibers cells desired.
number_box = 10 

# config control the profil of generated fibers cells. It is related to the
# angle distribution of the fibers.
# 3 values are possible: "default", "unique", "uniform"
#       "default" = dataset will be constituted of the default profils defined
# 					in function generate_params_datasets (aligned, medium ...)
#					each profil will appears rd times based on the result of
#					rng.integers.
#       "unique"  = dataset will be constituted of only one kind of default
#					profil (aligned, alignedish, medium, ...) specified via
# 					the parameter 'profil'.
#       "uniform" = dataset will be constituted of profil draw uniformally
#					azimuth and lattituce means are draw in a uniform
#					distribution as its respective standard deviation.
#					It is possible to specify means and std via the parameters
#					'mean_lat', 'mean_azth', 'std_lat' and 'std_azth'.

# ================== #
config = "default"
# ================== #
#config = "unique"
#profil = "aligned" # | "alignedish" | "medium" | "mediumish" | "disordered" |
# ================== #
#config = "uniform"
#mean_lat = __ # float between 0 and 90 degree 
#mean_azth = __ # float between -179 and 180
#std_lat = __ # positive float between 0 and 90
#std_azth = __ # positive float between 0 and 90
# ================== #

volume_size=(64, 64, 64)
n_fibers=10
radius_lim=(4, 10)
length_lim=(0.7, 0.9)
gap_lim=(3, 10)
max_fails=100
median_rad=3
intersect=False
exclusion_zone = False
output_dir="test_generation"
distribution="uniform" # "normal"
verbose=True


# =========================================================================== #
#                      Generation of params dict for the profils of cells
# =========================================================================== #


# ======= For default config ========== #
params = simulation.generate_params_datasets(config = "default",
								  box_population = number_box)
# ================== #

# ======= For unique config =========== #
#params = generate_params_datasets(config = "unique",
# 								   box_population = number_box,
# 								   profil = profil)
# ================== #

# ======== For uniform config ========== #
#params = generate_params_datasets(config = "uniform",
# 								   box_population = number_box)
###
#params = generate_params_datasets(config = "uniform",
# 								   box_population = number_box,
# 								   mean_lat = mean_lat,
# 								   mean_azth = mean_azth,
# 								   std_lat = std_lat,
# 								   std_azth = std_azth)
# ================== #


# =========================================================================== #
#                      Generation of the dataset
# =========================================================================== #

simulation.generate_datasets(volume_size=volume_size,
				  n_fibers=n_fibers,
				  radius_lim=radius_lim,
				  length_lim=length_lim,
				  gap_lim=gap_lim,
				  max_fails=max_fails,
				  median_rad=median_rad,
				  intersect=intersect,
				  exclusion_zone=exclusion_zone,
				  output_dir=output_dir,
				  distribution=distribution,
				  params=params,
				  verbose=verbose)
