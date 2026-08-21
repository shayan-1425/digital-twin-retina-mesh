import os
import gmsh
import pyvista as pv

def generate_and_verify_mesh(input_stl, output_msh):
    if not os.path.exists(input_stl):
        raise FileNotFoundError(f"Could not find input file at: {input_stl}")

    # Initialize Gmsh API
    gmsh.initialize()
    gmsh.model.add("retina_volume")

    print(f"Loading surface mesh from {input_stl}...")
    gmsh.merge(input_stl)

    # Classify surfaces to build a valid CAD topology
    angle = 40
    gmsh.model.mesh.classifySurfaces(angle * 3.14159 / 180.0, 
                                      includeBoundary=True, 
                                      forReparametrization=False)
    
    gmsh.model.mesh.createGeometry()
    
    # Wrap surfaces into a volume loop and generate tet mesh
    surfaces = gmsh.model.getEntities(2)
    surface_loop = gmsh.model.geo.addSurfaceLoop([s[1] for s in surfaces])
    volume = gmsh.model.geo.addVolume([surface_loop])
    gmsh.model.geo.synchronize()

    print("Generating 3D tetrahedral mesh...")
    gmsh.model.mesh.generate(3)

    # Ensure output directory exists and write file
    os.makedirs(os.path.dirname(output_msh), exist_ok=True)
    gmsh.write(output_msh)
    gmsh.finalize()
    print(f"Success! Volumetric mesh saved to {output_msh}")

    # --- PyVista Quality Verification Step ---
    print("Verifying volumetric mesh quality using PyVista...")
    mesh = pv.read(output_msh)
    
    # Print basic mesh stats
    print(f"Total Nodes (Points): {mesh.n_points}")
    print(f"Total Tetrahedral Cells: {mesh.n_cells}")

    # Compute quality metrics for tetrahedra (e.g., scaled Jacobian)
    # Scaled Jacobian close to 1.0 is great; values near 0 or negative indicate bad elements.
    quality_metrics = mesh.cell_quality(measures=['scaled_jacobian', 'collapse_ratio'])
    
    print("Mesh Quality Evaluation Completed.")
    print(f"Average Scaled Jacobian: {quality_metrics['scaled_jacobian'].mean():.3f}")
    
    # Optional: Launch an interactive viewer to inspect quality visually
    # mesh.plot(scalars='scaled_jacobian', cmap='viridis', show_edges=True)

if __name__ == "__main__":
    input_path = os.path.join("data", "processed", "retina_simplified_50k.stl")
    output_path = os.path.join("data", "processed", "retina_volumetric.msh")
    
    generate_and_verify_mesh(input_path, output_path)
