!pip install fast-simplification

import trimesh

# Load original mesh
loaded = trimesh.load('Retina.stl')
if isinstance(loaded, trimesh.Scene):
    mesh = trimesh.util.concatenate(list(loaded.geometry.values()))
else:
    mesh = loaded

print(f"Original Face Count: {len(mesh.faces)}")

# Decimate mesh to ~50,000 faces (approx 1% of original size)
decimated_mesh = mesh.simplify_quadric_decimation(face_count=50000)

print(f"Decimated Face Count: {len(decimated_mesh.faces)}")
print(f"Is Decimated Watertight?: {decimated_mesh.is_watertight}")

# Export simplified version
decimated_mesh.export('retina_simplified_50k.stl')
print("Successfully saved 'retina_simplified_50k.stl'!")
