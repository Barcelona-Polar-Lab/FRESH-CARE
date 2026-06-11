# FRESH-CARE LUQ Evaluation 🌀

**Lagrangian Uncertainty Quantification (LUQ) evaluation for surface current datasets.**

## 📘 Methodology & Scientific Citation

The core Lagrangian Uncertainty Quantification (LUQ) methodology and the baseline software components utilized in this repository were originally developed by the active research collaboration led by **García-Sánchez et al.** If you use this framework or parts of this software, please cite the foundational methodology papers:

1. García-Sánchez, L., Mancho, A. M., et al. (2021).
2. García-Sánchez, L., Mancho, A. M., Ramos, A. G., et al. (2023).
3. García-Sánchez, L., et al. (2025).

---

## 📝 Description

This directory contains high-performance tools to evaluate the accuracy of satellite-derived and fused surface current datasets (such as `ADT-SST`, `ADT-SSS`, etc.) by advecting virtual particles and comparing predicted trajectories against true observed drifter pathways using the LUQ metric.

## ✨ Features
* **Configurable Evaluation Parameters:** Flexible temporal filtering and dataset bounding.
* **Multi-Dataset Support:** Handles diverse current product formats simultaneously.
* **Performance-Optimized Execution:** Leverages `Numba` JIT compilation to handle heavy spatial array manipulations and Lagrangian integrations efficiently.
* **Command-Line Interface (CLI):** Easy-to-use terminal parameters with structured CSV/dataframe outputs.

---

## 🚀 Usage

### Basic Evaluation
Run the standard pipeline with default settings:

```bash
python run_evaluation.py
```

### Custom evaluation
Specify target datasets, advection time horizons (tau days), and custom temporal windows:

```bash
python run_evaluation.py --datasets ADT-SST --tau_days 5 10 --eval_start 2021-10-01 --eval_end 2021-12-31 
```

### Available options 
To view all available configuration flags:
```bash
python run_evaluation.py --help
```

## ⚙️ Configuration & Installation

### Configuration
Edit `config.py` directly to modify:
* Local dataset root paths and NetCDF internal variable names.
* Default evaluation parameters, advection tolerances, and output directories.

### Requirements
* Python 3.8+
* NumPy, Pandas, Xarray, Numba

### Installation
Ensure you are inside the repository environment and run:
```bash
pip install -r requirements.txt
```

---

## 👥 Authors & Code Credits
* **Methodology & Baseline Codebase:** García-Sánchez et al. (2021, 2023, 2025).
* **Pipeline Adaptation & Integration:** A. Rosquete-Estévez (2026/02/13).
* **Diagnostic Plotting & Notebooks:** J. Crespin (2026/06/09).
* **Supervision & Review:** Co-authored and reviewed by all team members.
