# Digital Twin Retina & 3D Mesh Pipeline: Project Overview

## What This Project Is

This repository is a computational biomedical engineering pipeline. It takes raw 3D anatomical eye scans (like the retina, cornea, lens, sclera, and optic nerve) and transforms them from hollow, digital shapes into optimized, physics-ready models.

## The Purpose

While standard medical tools provide visual 3D models to look at anatomy, they cannot calculate how living tissue reacts to physical forces. The purpose of this repository is to bridge that gap by providing automated code that:
* Cleans and shrinks massive 3D files so computers can process them without crashing.
* Standardizes clean triangular surface meshes for reliable structural simulations.
* Applies biological rules (such as soft-tissue rubber-like elasticity, internal eye pressure, and gravitational body forces) so researchers can simulate real-world biomechanics and spaceflight conditions ($0.0g$, $1.0g$, and $3.0g$).

## Detailed Directory & File Breakdown

### 1. data/raw/
* **Purpose:** Acts as the secure storage folder for original, untouched source files downloaded from anatomical databases.
* **Files:** `Eye.step`, `cornea.step`, `lens.step`, `Optic Nerve.step`, `retina.step`, `sclera.step` (The raw CAD files representing each distinct layer of the eye).

### 2. data/processed/
* **Purpose:** Stores cleaned-up, lightweight geometry assets that have been filtered and optimized for computational work.
* **Files:** `retina_simplified.stl`, `cornea_simplified.stl`, `lens_simplified.stl`, `OpticNerve_simplified.stl`, `sclera_simplified_50k.stl`.

### 3. data/optimized_meshes/ *(New Baseline)*
* **Purpose:** Stores sanitized, high-integrity surface meshes processed via `trimesh` to serve as the permanent structural baseline for all simulations.
* **Files:** `retina_simplified_optimized.stl`, `cornea_simplified_optimized.stl`, `lens_simplified_optimized.stl`, `sclera_simplified_50k_optimized.stl`, `OpticNerve_simplified_optimized.stl`.

### 4. data/results_surface_mesh/ *(Simulation Outputs)*
* **Purpose:** Stores multi-environment deformation outputs comparing tissue behavior under varying gravitational loads ($0.0g$ weightlessness, $1.0g$ terrestrial baseline, and $3.0g$ hypergravity) with a $15\times$ visual exaggeration factor.
* **Files:** Layer-specific deformed `.stl` exports across all three gravity scenarios.

### 5. scripts/
* **Purpose:** Houses all the Python automation code that performs calculations, file conversions, and data processing.
* **Files:**
  * `inspect_mesh.py`: Scans raw files to verify they are structurally sound and watertight.
  * `inspect_and_decimate.py`: Cuts down massive high-resolution polygon counts into smooth, manageable files.
  * `optimize_meshes.py`: Automatically sanitizes and standardizes surface meshes into the permanent baseline folder.
  * `generate_tet_mesh.py`: Converts hollow surface shells into solid 3D tetrahedral volumes (`.msh`).
  * `setup_physics_simulation.py`: Stamping mechanical properties and anchoring the back edge of the eye in place.
  * `run_baseline_simulation.py`: Simulates internal eye pressure and calculates tissue deformation.
  * `run_surface_simulation.py`: Executes multi-layer surface simulations across varying gravity environments.
  * `visualize.py`: Opens an interactive 3D window to display anatomical mesh shapes.
  * `visualize_results.py`: Opens an interactive 3D window to display mechanical stress and deformation heatmaps.
  * `visualize_surface_gravity.py`: Renders side-by-side multi-panel 3D surface triangulations comparing $0.0g$, $1.0g$, and $3.0g$ environments.

## Material Parameters
* **Retina:** $E = 0.18$ MPa, $\nu = 0.45$
* **Cornea:** $E = 1.20$ MPa, $\nu = 0.47$
* **Lens:** $E = 0.50$ MPa, $\nu = 0.49$
* **Sclera:** $E = 3.00$ MPa, $\nu = 0.45$
* **Optic Nerve:** $E = 2.00$ MPa, $\nu = 0.40$
