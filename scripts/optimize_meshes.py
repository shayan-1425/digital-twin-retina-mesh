# Run this once if dependencies are missing:
# !pip install trimesh numpy

import os
import trimesh
import numpy as np

# Define input/output directories matching your data structure
input_dir = "data/raw/"
output_dir = "data/optimized_meshes/"
os.makedirs(output_dir, exist_ok=True)

# Target anatomical components
layers = ["retina", "cornea", "lens", "sclera_simplified_50k", "OpticNerve"]

print("--- Starting Mesh Optimization & Standardization Pipeline ---")

for layer in layers:
    # Look for either .stl or .step extensions in raw data
    file_path = os.path.join(input_dir, f"{layer}.stl")
    if not os.path.exists(file_path):
        file_path = os.path.join(input_dir, f"{layer}.step")
    if not os.path.exists(file_path):
        # Fallback check for alternate casing
        file_path = os.path.join(input_dir, f"{layer.capitalize()}.stl")
        
    if not os.path.exists(file_path):
        print(f"Warning: Could not find raw file for {layer}. Skipping.")
        continue
        
    print(f"Processing and optimizing: {layer}...")
    mesh = trimesh.load(file_path, process=True)
    
    # Clean up mesh: fill holes, fix normals, remove degenerate elements
    if not mesh.is_watertight:
        trimesh.repair.fill_holes(mesh)
    trimesh.repair.fix_normals(mesh)
    mesh.remove_degenerate_faces()
    mesh.remove_unreferenced_vertices()
    
    out_path = os.path.join(output_dir, f"{layer}_optimized.stl")
    mesh.export(out_path)
    print(f"Successfully optimized and saved -> {out_path} ({len(mesh.vertices)} vertices)")

print("\nAll mesh optimizations complete! Saved in data/optimized_meshes/")
