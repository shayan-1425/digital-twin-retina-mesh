# Run this once if dependencies are missing:
# !pip install trimesh matplotlib numpy

import os
import trimesh
import matplotlib.pyplot as plt

results_dir = "data/results_surface_mesh/"
gravity_scenarios = ["0.0g", "1.0g", "3.0g"]

fig = plt.figure(figsize=(18, 6))

print("--- Rendering Multi-Environment Gravity Comparison ---")

for i, target_gravity in enumerate(gravity_scenarios):
    ax = fig.add_subplot(1, 3, i + 1, projection='3d')
    
    output_files = [f for f in os.listdir(results_dir) if f.endswith(".stl") and target_gravity in f] if os.path.exists(results_dir) else []
    
    if not output_files:
        print(f"Warning: No surface mesh files found for {target_gravity} in {results_dir}.")
        continue
        
    for filename in sorted(output_files):
        path = os.path.join(results_dir, filename)
        mesh = trimesh.load(path, process=True)
            
        vertices = mesh.vertices
        faces = mesh.faces
        layer_label = filename.split('_')[0]
        
        ax.plot_trisurf(
            vertices[:, 0], vertices[:, 1], vertices[:, 2], 
            triangles=faces, 
            alpha=0.5, 
            linewidth=0.1,
            edgecolor='k'
        )

    ax.set_title(f"Simulation ({target_gravity}) - 15x")
    ax.set_xlabel("X (microns)")
    ax.set_ylabel("Y (microns)")
    ax.set_zlabel("Z (microns)")

plt.tight_layout()
plt.show()
print("Visualization successfully rendered.")
