import numpy as np
from scipy import ndimage as ndi
from skimage import morphology
from quanfima import simulation
from quanfima import morphology as mrph
from quanfima import utils
from quanfima import visualization as vis

volume, lat_ref, azth_ref, diameter, _, _ = \
		  simulation.simulate_fibers((128,128,128), n_fibers=30, max_fails=200,
									 radius_lim=(2, 3), gap_lim=(3,5))
volume = volume.astype(np.uint8)
volume = ndi.binary_fill_holes(volume)
volume = ndi.median_filter(volume, footprint=morphology.ball(2))
lat_ref = ndi.median_filter(lat_ref, footprint=morphology.ball(2))
azth_ref = ndi.median_filter(azth_ref, footprint=morphology.ball(2))



# prepare data and analyze fibers
pdata, pskel, pskel_thick = utils.prepare_data(volume)
#oprops =  mrph.estimate_tensor_parallel('dataset_orientation_w36',
#										pskel, pskel_thick, 36,
#										'../../data/results')
oprops =  mrph.estimate_tensor_parallel('dataset_orientation_w36',
										pskel, pskel_thick, 36,
										'data/results')

odata = np.load(oprops['output_path'], allow_pickle=True).item()
lat, azth, skel = odata['lat'], odata['azth'], odata['skeleton']

dprops = mrph.estimate_diameter_single_run('dataset_diameter',
										   'data/results',
										   pdata, skel, lat, azth)
#dmtr = np.load(dprops['output_path']).item()['diameter']

# plot results
vis.plot_3d_orientation_map('dataset_w36', lat, azth,
							output_dir='data/results',
							camera_azth=40.47,
							camera_elev=32.5,
							camera_fov=35.0,
							camera_loc=(40.85, 46.32, 28.85),
							camera_zoom=0.005124)

#vis.plot_3d_diameter_map('dataset_w36', dmtr,
#						 output_dir='/data/results',
#						 measure_quantity='vox',
#						 camera_azth=40.47,
#						 camera_elev=32.5,
#						 camera_fov=35.0,
#						 camera_loc=(40.85, 46.32, 28.85),
#						 camera_zoom=0.005124,
#						 cb_x_offset=5,
#						 width=620)