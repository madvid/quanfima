from numpy import rad2deg

# ============================================================================ #
#                         Verbose global variables                             #
# ============================================================================ #
verb_line = "=" * 62

# ============================================================================ #
#                             Verbose functions                                #
# ============================================================================ #
def header(txt, t):
    l = len(txt)
    head = txt.center(l + 4, ' ')
    head = head.center(62, '=') + '\n'
    if t is None:
       elapsed_time = ""
    else:
        elapsed_time = f" Elapsed time = {t:.3f}"

    print(verb_line + "\n" + head + verb_line + elapsed_time + "\n")


def simulate_fibers_verbose(volume,
                            n_fibers,
                            intersect,
                            exclusion_zone,
                            radius_lim,
                            length_lim,
                            lat_lim,
                            azth_lim,
							distribution,
							parallelization):
    """Verbose of simulate_fibers_verbose.

	Parameters
	----------
	volume_shape : tuple
		Indicates the size of the volume.

	n_fibers : integer
		Indicates the number of fibers to be generated.

	radius_lim : tuple
		Indicates the range of radii for fibers to be generated.

	length_lim : tuple
		Indicates the range of lengths for fibers to be generated.

	lat_lim : tuple
		Indicates the range of latitude / elevation component of the orientation angles of
		the fibers to be generated.

	azth_lim : tuple
		Indicates the range of azimuth component of the orientation angles of the fibers to
		be generated.

	intersect : boolean
		Specifies if generated fibers can intersect.
	
	exclusion_zone: boolean
		Specifies if generated fibers can be very closed to each others and sometimes touching
		each others

	distribution: str
		Nature of the distribution for the generation of fibers azimuth and lattitude.

	parallelization: str
		Nature of the parallelization, can be either CPU parallelized, GPU parallelized or mono core.

	Remarks:
	-------
	intersect and exclusion: If exclusion_zone is True, intersect must be False.
	Returns
	-------
	(volume, lat_ref, azth_ref, diameter, n_generated, elapsed_time) : tuple of arrays and numbers
		The binary volume of generated fibers, the volumes of latitude / elevation and
		azimuth angles at every fiber point, the volume of diameters at every fibers point,
		the number of generated fibers and the simulation time.
    """
    header("Start of the fibers simulation generation", None)
    if intersect and exclusion_zone:
        e_str = "Parameter Errors: intersect cannot be True if exclusion_zone is True."
        raise Exception(e_str)

    str_verbose = f"Parallelization".ljust(35, ' ') + f":[{parallelization}]\n" \
	            + "Volume of cell (in (pxl,pxl,pxl)):".ljust(35, ' ') + f":{volume.shape}\n" \
	            + f"Attempting number of fibers:".ljust(35, ' ') + f":{n_fibers}\n" \
	            + f"Intersection allowed:".ljust(35, ' ') + f":{str(intersect)}\n" \
	            + f"Exclusion volume around fibers:".ljust(35, ' ') + f":{str(exclusion_zone)}\n" \
				+ f"Nature of the random generator: {distribution}\n" \
	            + "\n________  PARAMETERS ________ :\n" \
	            + f"Radius (in pixels)                      : min = {radius_lim[0]}    max = {radius_lim[1]}\n" \
	            + f"Length range of fibers (% of min V size): min = {length_lim[0]}    max = {length_lim[1]}\n" \
	            + f"Latitude range (rad|degree)             : min = {lat_lim[0]:6.2f}||{rad2deg(lat_lim[0]):6.2f}    max = {lat_lim[1]:.2f}||{rad2deg(lat_lim[1]):.2f}\n" \
	            + f"Azimuth (rad|degree)                    : min = {azth_lim[0]:6.2f}||{rad2deg(azth_lim[0]):6.2f}    max = {azth_lim[1]:.2f}||{rad2deg(azth_lim[1]):.2f}\n" \
	            + verb_line + "\n"
    print(str_verbose)


def generate_datasets_verbose(params, default_params):
    header("Start of dataset generation", None)
    str_verbose = "________  PARAMETERS ________ :\n" \
                + "Default params:" + str(default_params) + "\n" \
                + "Number of generation: " + str(len(params)) + "\n"
    print(str_verbose)
