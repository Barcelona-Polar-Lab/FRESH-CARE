# FRESH-CARE Fusion Toolkit 🛠️✨

**Advanced Spatiotemporal Geophysical Data Fusion via Local Linear Regression**

This directory contains the Python mathematical engine and utilities developed for Work Package 1 (WP1) of the **FRESH-CARE** project. It is specifically tailored to blend and fuse gridded geophysical fields using a robust, **spatially weighted local linear regression**. 

The toolkit optimizes data processing pipelines where a coarse Level-3 (L3) satellite product needs to be sharpened or downscaled using a high-resolution template while maintaining absolute quantitative traceability and preserving physical boundaries.

## 👥 Authors & Contributors
* **Aleida Rosquete-Estévez**
* **Marta Umbert**
  
---

## 🚀 Core Component Overview

The toolkit is structured into three highly optimized layers:

* **1. Mathematical Engine (`py_fusion.fusion`):** Houses the core numerical routines. It executes a NaN-aware 2D/3D local linear regression utilizing configurable spatial boundaries and inverse-distance weight kernels. 
  > 🛡️ **Stability Safe-Guard:** In areas where data is too sparse or unstable (insufficient valid spatial neighbors, e.g., complex coastlines), the algorithm automatically falls back to preserve the original L3 data values.
* **2. Multi-Dimensional Wrapper (`py_fusion.fusion_xr`):** An `xarray` abstraction layer that handles metadata, preserves native NetCDF coordinates/attributes, and streamlines batch execution on complex oceanographic datasets.
* **3. Production CLI Orchestrator (`py_fusion.cli_fusion`):** A robust Command Line Interface designed to handle multi-file batch inputs, dimension remapping, automated coordinate validation, and compressed NetCDF output generation.

---

## ⚙️ Requirements & Installation

### Requirements
* **OS / Environment:** Python 3.9 or newer (Tested thoroughly with CPython architectures).
* **Core Libraries:** `numpy`, `scipy`, `xarray`, `netCDF4` (or any backend engine supported by xarray for NetCDF IO).

### Installation Steps

1. Navigate to your local project directory:
```bash
git clone [https://github.com/Barcelona-Polar-Lab/FRESH-CARE.git](https://github.com/Barcelona-Polar-Lab/FRESH-CARE.git)
cd FRESH-CARE/WP1/Fusion_toolkit
```

2. Install the pinned data-science dependencies:
```bash
pip install numpy scipy xarray netCDF4
```

---

## ff Quickstart Guide

### Run Fusion via the Command Line Interface (CLI)
You can orchestrate the fusion execution loop directly from your terminal using the following template:

```bash
python -m py_fusion.cli_fusion \
    --l3 /path/to/L3.nc \
    --l3-var L3_variable_name \
    --template /path/to/template.nc \
    --template-var template_variable_name \
    --width 20 \
    --exponent 2 \
    --mask-mode L3 \
    --log-mode none \
    --boundary reflect \
    --output fused_output.nc \
    --verbose
```

### 🔑 Critical CLI Behaviors & Parameters

| Parameter Flag | Type | Functional Behavior |
| :--- | :--- | :--- |
| `--l3` / `--template` | `str` | Supports shell globs for multi-file batch execution (e.g., `"data/L3/*.nc"`). |
| `--width` / `--exponent` | `int` | Controls the regression window size ($W$) and the weight decay penalty exponent ($\alpha$). |
| `--boundary` | `str` | Manages spatial edge conditions (e.g., `reflect` grid pads at high latitudes). |
| `--verbose` | `flag`| Exposes deep debugging logging logs directly from the core mathematical engine. |

> 📌 **Technical Notes on Processing:**
> * **Grid Alignment:** The CLI verifies that the L3 layer and the high-resolution template share the exact same rectilinear grid alignment before processing. No implicit regridding is performed.
> * **Dimension Remapping:** If your source files use non-standard axes labels, use the explicit remapping flags (e.g., `--l3-x-dim`, `--t-y-dim`).
> * **Output Structure:** The resulting NetCDF (`L4` product) stores the optimized fused field alongside its diagnostic matrices: slope layer (`a`), intercept layer (`b`), correlation density (`rho`), and standard error residuals (`err`).

---

## 💻 Development & Contributions

* **Verbosity Toggle:** Always activate the `--verbose` flag during initial workflow testing to screen execution logs and regression stability indices.
* **Testing:** Custom automated testing suites are under continuous development. We highly recommend verifying downscaled variables using local case-specific Jupyter testing sandboxes.
* **Contributions:** Code improvements, bug fixes, or performance updates are highly welcome! Please submit a Pull Request (PR) or open an issue thread through the central repository framework.
