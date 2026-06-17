# WP1: Data Fusion & Ocean Surface Currents Validation 🌊🛠️

**Work Package 1 (WP1) of the FRESH-CARE Project (ERC Starting Grant)**

This directory serves as the central hub for the computational frameworks, pipelines, and mathematical toolkits developed under WP1 of the **FRESH-CARE** project. The main goal is to process, fuse, and validate diverse Arctic ocean surface geophysical fields and current products against state-of-the-art observational networks.

---

## 📂 Work Package Architecture

The source code is divided into two specialized toolkit subdirectories:

### 1. [📁 Ocean_currents/](./Ocean_currents/)
* **Focus:** Comprehensive diagnostic benchmarking of satellite-derived Arctic surface current fields.
* **Core Modules:** 
  * **Eulerian Validation:** Sequential pipeline (Jupyter + Python) executing point-to-point statistical analysis (RMSE, Bias, Taylor Diagrams, KDEs) against the *Global Drifter Program (GDP)*.
  * **Lagrangian Evaluation:** Trajectory prediction assessment driven by the **Lagrangian Uncertainty Quantification (LUQ)** methodology (García-Sánchez et al., 2021, 2022, 2023, 2025), utilizing `Numba` high-performance execution.

### 2. [📁 Fusion_toolkit/](./Fusion_toolkit/)
* **Focus:** Sharpening gridded geophysical fields via advanced data-fusion algorithms.
* **Core Modules:** Implements a NaN-aware 2D/3D **spatially weighted local linear regression** to blend coarse Level-3 (L3) satellite observations with high-resolution templates, ensuring physical consistency and quantitative traceability (L4 outputs). Includes an `xarray` wrapper and a robust Command Line Interface (CLI).

---

## ⚙️ Technical Environment
* **Environment:** Python 3.9+ recommended.
* **Core Matrix:** `numpy`, `scipy`, `xarray`, `pandas`, `geopandas`, `shapely`, `cartopy`, `numba`, `netCDF4`, `matplotlib`, `skill_metrics`.
* *Note: Remember that geospatial libraries like `cartopy` and `geopandas` require system-level C bindings (`libgeos-dev`, `libproj-dev`).*

---

## 🇪🇺 Funding & Acknowledgements
This software framework is part of the **FRESH-CARE** project (*Unraveling FRESHwater and ocean Currents changes in the Arctic using REmote sensing*), which has received funding from the **European Research Council (ERC)** under the European Union’s Horizon Europe research and innovation programme (Grant Agreement No. 10116451). 
