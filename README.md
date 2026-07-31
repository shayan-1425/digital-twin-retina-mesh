# Digital Twin Retina: 3D Surface Mesh Assets

This repository provides simulation-ready 3D surface mesh assets of the human retina, extracted from CAD ocular geometries (`feelpp/mesh.eye`) and optimized for physics/FEM simulations and synthetic data generation within the NASA GeneLab AWG AI/ML subgroup.

## 📦 Available Assets

| Asset Name | Triangle Count | Watertight? | Description |
| :--- | :--- | :--- | :--- |
| **`retina_simplified_50k.stl`** | 50,000 | `True` | Quadric-decimated manifold surface mesh (~1% size of raw CAD export). Optimized for OpenFOAM, MOOSE, or Blender. |

---

## 📐 Geometry Characteristics
* **Source Geometry:** `Eye.step` from [`feelpp/mesh.eye`](https://github.com/feelpp/mesh.eye)
* **Isolated Region:** Posterior ocular shell (retinal boundary layer)
* **Bounding Dimensions (X, Y, Z):** ~17.36 mm × 22.00 mm × 22.00 mm
* **Topology:** 100% Watertight Manifold (`is_watertight = True`)

---

## 🛠 Workflow Summary
1. **CAD Extraction:** Isolated the posterior retinal surface boundary using Onshape from multi-component CAD STEP files.
2. **Topology Verification:** Analyzed initial raw surface mesh geometry (~4.97M faces) for manifold integrity in Python.
3. **Decimation:** Applied quadric surface simplification via `trimesh` + `fast-simplification` to reduce polygon overhead by 99% while preserving structural volume and surface continuity.

---

## 🚀 Quickstart (Python)

### Installation
```bash
pip install trimesh fast-simplification
import trimesh

# Load the decimated mesh
mesh = trimesh.load('meshes/retina_simplified_50k.stl')

# Print health metrics
print("--- 3D Mesh Health Report ---")
print(f"Number of Vertices: {len(mesh.vertices)}")
print(f"Number of Triangles/Faces: {len(mesh.faces)}")
print(f"Is Watertight / Manifold?: {mesh.is_watertight}")
print(f"Bounding Box Dimensions (mm): {mesh.extents}")
