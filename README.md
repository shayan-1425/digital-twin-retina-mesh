# Digital Twin Retina & 3D Mesh Pipeline: Project Overview

## What This Project Is
This repository is a computational biomedical engineering pipeline. It takes raw 3D anatomical eye scans (like the retina, cornea, lens, sclera, and optic nerve) and transforms them from hollow, digital shapes into solid, physics-ready models. 

## The Purpose
While standard medical tools provide visual 3D models to look at anatomy, they cannot calculate how living tissue reacts to physical forces. The purpose of this repository is to bridge that gap by providing automated code that:
1. **Cleans and shrinks massive 3D files** so computers can process them without crashing.
2. **Fills the hollow shapes** into solid 3D blocks (tetrahedral meshes) required for physics math.
3. **Applies biological rules** (such as soft-tissue rubber-like elasticity and internal eye pressure) so researchers can simulate real-world biomechanics.

---

## Detailed Directory & File Breakdown

### 1. `data/raw/`
* **Purpose:** Acts as the secure storage folder for original, untouched source files downloaded from anatomical databases.
* **Files:** 
  * `Eye.step`, `cornea.step`, `lens.step`, `Optic Nerve.step`, `retina.step`, `sclera.step`: The raw CAD files representing each distinct layer of the eye.

### 2. `data/processed/`
* **Purpose:** Stores cleaned-up, lightweight geometry assets that have been filtered and optimized for computational work.
* **Files:**
  * `retina_simplified.stl`, `cornea_simplified.stl`, `lens_simplified.stl`, `OpticNerve_simplified.stl`, `sclera_simplified_50k.stl`: Surface shell files with reduced triangle counts so simulation software can run smoothly.

### 3. `scripts/`
* **Purpose:** Houses all the Python automation code that performs calculations, file conversions, and data processing.
* **Files:**
  * `inspect_mesh.py`: Scans raw files to verify they are structurally sound and watertight.
  * `inspect_and_decimate.py`: Cuts down massive high-resolution polygon counts into smooth, manageable files.
  * `generate_tet_mesh.py`: Converts hollow surface shells into solid 3D tetrahedral volumes (`.msh`).
  * `setup_physics_simulation.py`: Stamping mechanical properties (like stiffness and stretching limits) and anchoring the back edge of the eye in place.
  * `run_baseline_simulation.py`: Simulates internal eye pressure and calculates how much the tissue deforms.
  * `visualize.py`: Opens an interactive 3D window to display the anatomical mesh shapes.
  * `visualize_results.py`: Opens an interactive 3D window to display mechanical stress and deformation heatmaps.
