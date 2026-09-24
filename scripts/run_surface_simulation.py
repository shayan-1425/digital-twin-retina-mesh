# Run this once if dependencies are missing:
# !pip install trimesh numpy

import os
import trimesh
import numpy as np

# Physiological material definitions for eye layers
EYE_MATERIALS = {
    "retina": {"youngs_modulus": 0.18, "poissons_ratio": 0.45},
    "cornea": {"youngs_modulus": 1.20, "poissons_ratio": 0.47},
    "lens": {"youngs_modulus": 0.50, "poissons_ratio": 0.49},
    "sclera": {"youngs_modulus": 3.00, "poissons_ratio": 0.45},
    "opticnerve": {"youngs_modulus": 2.00, "poissons_ratio": 0.40}
}

input_dir = "data/optimized_meshes/"
output_dir = "data/results_surface_mesh/"
os.makedirs(output_dir, exist_ok=True)

layers = ["retina_optimized", "cornea_optimized", "lens_optimized", "sclera_simplified_50k_optimized", "OpticNerve_optimized"]

# Establish a unified global center derived from the optimized sclera for stable alignment
sclera_path = os.path.join(input_dir, "sclera_simplified_50k_optimized.stl")
global_center = trimesh.load(sclera_path).vertices.mean(axis=0) if os.path.exists(sclera_path) else np.array([0.0, 0.0, 0.0])

gravity_scenarios = [0.0, 1.0, 3.0]
exaggeration_factor = 15.0

print("--- Starting Multi-Environment Surface Simulation Pipeline ---")

for gravity_g in gravity_scenarios:
    for layer_name in layers:
        key = layer_name.split("_")[0].lower()
        mat = EYE_MATERIALS.get(key, {"youngs_modulus": 1.0, "poissons_ratio": 0.45})
        
        file_path = os.path.join(input_dir, f"{layer_name}.stl")
        if not os.path.exists(file_path):
            print(f"Warning: {file_path} not found.")
            continue
            
        mesh = trimesh.load(file_path, process=True)
        vertices = mesh.vertices.copy()
        
        # Calculate internal pressure load and directional gravitational body forces
        pressure_load = 0.001
        pressure_displacement = (vertices - global_center) * (pressure_load / mat["youngs_modulus"])
        gravity_vector = np.array([0.0, 0.0, -200.0 * gravity_g / mat["youngs_modulus"]])
        gravity_displacement = np.tile(gravity_vector, (len(vertices), 1))
        
        total_displacement = (pressure_displacement + gravity_displacement) * exaggeration_factor
        mesh.vertices = vertices + total_displacement
        
        clean_label = layer_name.replace("_optimized", "")
        out_file_path = os.path.join(output_dir, f"{clean_label}_surface_{gravity_g}g.stl")
        mesh.export(out_file_path)
        print(f"Exported: {clean_label} for {gravity_g}g environment")

print("\nSurface mesh simulations successfully completed and saved to data/results_surface_mesh/.")
