# WP1: Ocean Surface Currents Methodology 🌊

**Eulerian and Lagrangian Assessment of Arctic Surface Current Products Using Drifter Observations**

This work package focuses on validating diverse Arctic surface ocean currents products.

## 👥 Authors & Contributors
* **Luis Yubero** (Researcher)
* **Aleida Rosquete** (Researcher)
* **Júlia Crespin** (Researcher)
* **Ana M. Mancho** (PI)
* **Marta Umbert** (PI)

---

## 📂 WP1 Structure

The source code and pipelines for WP1 are divided into two main evaluation frameworks:

### 1. `Eulerian_validation/`
* **Focus:** Classical validation of surface current fields.
* **Methodology:** Direct point-to-point statistical comparison (zonal/meridional velocities, correlation, and RMSE metrics) against the **Global Drifter Program (GDP)** dataset and other operational products (e.g., AVISO, OSCAR, TOPAZ).

### 2. `Lagrangian_LUQ_evaluation/`
* **Focus:** Lagrangian Uncertainty Quantification (LUQ) evaluation for surface current datasets.
* **Methodology:** Assessment of the trajectory prediction capabilities of each product.
