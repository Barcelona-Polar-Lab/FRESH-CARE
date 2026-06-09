# WP1: Ocean Surface Currents Methodology 🌊

**Eulerian and Lagrangian Assessment of Arctic Surface Current Products Using Drifter Observations**

This work package focuses on developing and validating an innovative methodology based on data fusion to estimate Arctic surface ocean currents, integrating sea level anomalies (SSH) with high-resolution remote sensing temperature (SST) and salinity (SSS) templates.

## 👥 Authors & Contributors
* **Aleida Rosquete** (Lead Developer / Researcher)
* **Júlia Crespin** (Lead Developer / Researcher)
* **Marta Umbert** (PI)

---

## 📂 WP1 Structure & Modules

The source code and pipelines for WP1 are divided into two main evaluation frameworks:

### 1. `Eulerian_validation/`
* **Focus:** Eulerian validation of derived surface current fields.
* **Methodology:** Direct point-to-point statistical comparison (zonal/meridional velocities, kinetic energy, correlation, and RMSE metrics) against the **Global Drifter Program (GDP)** dataset and other operational products (e.g., CMEMS, TOPAZ5).
* **Key Components:**
  * Satellite current product colocation with drifter trajectories.
  * Tidal and sub-mesoscale filtering algorithms for in-situ data.

### 2. `Lagrangian_LUQ_evaluation/`
* **Focus:** Lagrangian Uncertainty Quantification (LUQ) evaluation for FRESH-CARE surface current datasets.
* **Methodology:** Assessment of the trajectory prediction capabilities of the new fused datasets (`SSH_FC`, `SSH_T_FC`, `SSH_S_FC`).
* **Key Components:**
  * Synthetic particle deployment using numerical Lagrangian integrators.
  * Skill score computations based on absolute and relative dispersion metrics over various time horizons (e.g., 24h to 72h).
  * Quantification of spatial errors in freshwater-dominated regions.

## 📊 Research Outputs Reference
* **Research Output 1.1 (M12):** Regional surface ocean currents dataset for the Arctic Ocean (NetCDF format, 2010-2025).
* **Research Output 1.2 (M16):** Peer-reviewed journal submission containing the methodology and benchmarking results hosted in this directory.
