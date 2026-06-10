# FRESH-CARE 🌊❄️
**Unraveling FRESHwater and ocean Currents changes in the Arctic using REmote sensing**

Welcome to the official repository of the **FRESH-CARE** project, an **ERC Starting Grant** hosted by the **Barcelona Polar Lab**.

* **Principal Investigator:** Marta Umbert Ceresuela 📧 [mumbert@icm.csic.es](mailto:mumbert@icm.csic.es)
* **Host Institution:** Barcelona-Polar-Lab, Institut de Ciències del Mar (ICM-CSIC), Barcelona
* **Funding:** European Research Council (ERC) Starting Grant

---

## 📢 Code Availability & Release Policy

In compliance with ERC Open Science guidelines, the source code, processing pipelines, and model configurations developed within this project are being released progressively. Code modules are transitioned from internal development branches to this public repository **upon the acceptance/publication of their corresponding peer-reviewed scientific papers**.

---

## 📂 Repository Structure & Status

This repository acts as a centralized "monorepo" organized strictly by Work Packages (WPs) and field activities. 

| Directory | Description | Status |
| :--- | :--- | :--- |
| 📂 `WP1/` | Ocean surface currents evaluation | 🟢 **Available** (Eulerian and lagrangian (LUQ) validation pipelines) |
| 📂 `campaigns/` | In-situ data processing and analysis (CTD, ADCP...) | 🟢 **Available** (SIMSVAL & FANS oceanographic campaigns) |
| 📁 `WP2/` | LSTM to reconstruct 4D oceanographic data | 🟡 *In progress* (Released post-publication) |
| 📁 `WP3/` | Arctic freshwater content (FWC) analysis | 🟡 *In progress* (Released post-publication) |
| 📁 `WP4/` | Freshwater transport (FWT) across Arctic gateways | 🟡 *In progress* (Released post-publication) |
| 📁 `WP5/` | Arctic Ocean Numerical Model (ROMS-Sea ice) | 🟡 *In progress* (Released post-publication) |

```text
fresh-care/
├── WP1/          # Ocean surface currents evaluation [AVAILABLE]
├── campaigns/    # In-situ data processing and analysis [AVAILABLE]
├── WP2/          # LSTM to reconstruct 4D oceanographic data [UPCOMING]
├── WP3/          # Arctic freshwater content (FWC) analysis
├── WP4/          # Freshwater transport (FWT) across Arctic gateways
└── WP5/          # Arctic Ocean Numerical Model (ROMS-Sea ice)
