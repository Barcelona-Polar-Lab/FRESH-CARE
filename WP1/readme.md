# WP1: Ocean Surface Currents Methodology 🌊

**Eulerian and Lagrangian Assessment of Arctic Surface Current Products Using Drifter Observations**

This work package contains the complete computational framework and benchmarking pipelines developed under the **FRESH-CARE** project to evaluate satellite-derived ocean surface current products (including regular and curvilinear gridded models) against *in-situ* observations from the Global Drifter Program (GDP) across the Arctic Ocean.

## 👥 Authors & Contributors
* **Aleida Rosquete-Estévez**
* **Júlia Crespin**
* **Luis Yubero**
* **Ana M. Mancho**
* **Marta Umbert**

---

## 📂 Repository Structure

The source code and pipelines are organized into two independent yet complementary evaluation frameworks:

### 1. [📁 Eulerian_validation/](./Eulerian_validation/)
* **Focus:** Classical point-to-point validation of surface current fields.
* **Methodology:** Ingests raw GDP NetCDF streams, applies low-pass Butterworth filters to remove tidal/inertial variability, and executes spatial joins with Arctic sector shapefiles. 
* **Diagnostics:** Computes pan-Arctic and regional metrics (RMSE, Bias, Pearson Correlation, Taylor diagrams, KDE plots, and polar-rose directional error distributions).
* **Development:** Main architecture by A. Rosquete-Estévez, with expansions by J. Crespin.

### 2. [📁 Lagrangian_LUQ_evaluation/](./Lagrangian_LUQ_evaluation/)
* **Focus:** Lagrangian Uncertainty Quantification (LUQ) benchmarking.
* **Methodology:** Evaluates dataset accuracy by comparing predicted virtual particle trajectories against true observed drifter pathways, utilizing high-performance `Numba` JIT compilation.
* **Scientific Basis:** Builds upon the foundational LUQ methodology and baseline software developments described in García-Sánchez et al. (2021), García-Sánchez, Mancho, and Wiggins (2022), García-Sánchez et al. (2023), and García-Sánchez et al. (2025).
* **Development:** Adapted for this framework by A. Rosquete-Estévez, with plotting suites expanded by J. Crespin.

---

## ⚙️ Technical Requirements
* **Environment:** Python 3.8+ (Python 3.11 recommended)
* **Core Dependencies:** `xarray`, `pandas`, `numpy`, `scipy`, `geopandas`, `shapely`, `cartopy`, `numba`, `matplotlib`, `skill_metrics`.
* *Note: `cartopy` and `geopandas` require underlying system libraries (`libgeos-dev`, `libproj-dev`).*

---

## 🇪🇺 Funding & Acknowledgements
This software framework is part of the **FRESH-CARE** project, which has received funding from the **European Research Council (ERC)** under the European Union’s Horizon Europe research and innovation programme (Grant Agreement No. 10116451). 

This research framework was developed through a collaborative scientific fellowship between the **Institut de Ciències del Mar (ICM-CSIC)** and the **Instituto de Ciencias Matemáticas (ICMAT)**. 

We acknowledge funding from:
* The Spanish government through the 'Severo Ochoa Centre of Excellence' accreditation (Grant CEX2024-001494-S funded by AEI 10.13039/501100011033).
* Grant PID2021-123348OB-I00 funded by MCIN/AEI/10.13039/501100011033/ and by FEDER "A way to make Europe" (A. M. Mancho).
* The CSIC JAE Intro ICU 2025 call, funded by the Spanish Ministry of Science, Innovation and Universities (Grant Ref: PolarCSIC-01; A. Rosquete-Estévez).

This work is a contribution to **CSIC Conexión Polar** and **CSIC Thematic Interdisciplinary Platform PTI Teledetect**.
