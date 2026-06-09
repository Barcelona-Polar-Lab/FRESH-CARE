"""
Configuration file for LUQ calculation.
arosquete - 2026/02/13
"""

# Imports
import numpy as np

# Physical constants
R_EARTH = 6371000.0  # Earth's radius in meters
LAT_MAX = np.float32(1.569051)  # ~89.9° in radians
EPOCH = np.datetime64("1950-01-01T00:00:00", "s")

# Evaluation parameters
EVAL_PARAMS = {
    "tau_days": [5, 10, 15],
    "r_kms": [10, 20, 40],
    "dt_sec": 3600,
    "nx": 100,
    "ny": 100,
    "min_valid_frac": 0.75,
}

# Dataset paths and configurations
# Dataset paths and configurations
DATASETS = {
    "AVISO": {
        "path": "/data/FRESH-CARE/Data_satellite/AVISO/regridded/0.25",
        "u_name": "ugos",
        "v_name": "vgos",
        "time_name": "time",
        "lat_name": "lat",
        "lon_name": "lon",
    },
    "OSCAR": {
        "path": "/data/FRESH-CARE/ext_currents_datasets/OSCAR/data",
        "u_name": "u",
        "v_name": "v",
        "time_name": "time",
        "lat_name": "lat",
        "lon_name": "lon",
    },
    "GLORYS": {
        "path": "/data/FRESH-CARE/GLORYS/glorys_daily_2011_2021",
        "u_name": "uo",
        "v_name": "vo",
        "time_name": "time",
        "lat_name": "latitude",
        "lon_name": "longitude",
    },
    "GLOBCURRENT": {
        "path": "/data/FRESH-CARE/GLOBCURRENT/daily",
        "u_name": "uo",
        "v_name": "vo",
        "time_name": "time",
        "lat_name": "latitude",
        "lon_name": "longitude",
    },
    "TOPAZ": {
        "path": "/data/FRESH-CARE/TOPAZ4b/daily",
        "u_name": "vxo",
        "v_name": "vyo",
        "time_name": "time",
        "lat_name": "latitude",
        "lon_name": "longitude",
    },
    "NEUROST": {
        "path": "/data/FRESH-CARE/NEUROST_processed/",
        "u_name": "u",
        "v_name": "v",
        "time_name": "time",
        "lat_name": "latitude",
        "lon_name": "longitude",
    },
}


# Paths
DRIFTERS_PATH = "/home/rosquete/Documents/FRESH-CARE/data/fusion_evaluation/classic_evaluation/in_situ_data/selected_drifters/"
OUTPUT_PATH = "../results/"


# Drifter column names
DRIFTER_COLUMNS = {"time_col": "time", "lon_col": "longitude", "lat_col": "latitude"}
