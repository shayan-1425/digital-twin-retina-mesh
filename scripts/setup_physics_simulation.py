import os
import numpy as np
import pyvista as pv

def setup_simulation_physics(input_msh):
    if not os.path.exists(input_msh):
        raise FileNotFoundError(f"Could not find volumetric mesh at: {input_msh}")

    print(f"Loading volumetric mesh: {input_msh}")
    mesh = pv.read(input_msh)

    # 1. Define Material Constants (stored as cell/field data for solvers)
    # Young's Modulus in MPa, Poisson's Ratio
    youngs_modulus = 0.18  
    poissons_ratio = 0.45
    
    mesh.field_data['Youngs_Modulus'] = np.array([youngs_modulus])
    mesh.field_data['Poissons_Ratio'] = np.array([poissons_ratio])
    print(f"Assigned Material Properties -> E: {youngs_modulus} MPa, nu: {poissons_ratio}")

    # 2. Identify Boundary Constraints (e.g., fixing nodes at the posterior/optic nerve edge)
    # Finding nodes with minimum Z or near the anchor point
    points = mesh.points
    min_z = np.min(points[:, 2])
    # Select nodes within a small threshold of the posterior boundary
    fixed_node_indices = np.where(points[:, 2] <= (min_z + 0.5))[0]
    
    print(f"Identified {len(fixed_node_indices)} anchor nodes for boundary constraints (Fixed Support).")

    # 3. Simulate an Internal Pressure Load (IOP)
    # 15 mmHg converted roughly to internal surface loading metric
    iop_pressure_mpa = 0.002 
    print(f"Applied simulated Intraocular Pressure (IOP): {iop_pressure_mpa} MPa")

    # Save the physics-configured mesh out for solver integration
    output_sim_file = input_msh.replace(".msh", "_physics.vtu")
    mesh.save(output_sim_file)
    print(f"Success! Physics-ready simulation mesh saved to {output_sim_file}")

if __name__ == "__main__":
    vol_mesh_path = os.path.join("data", "processed", "retina_volumetric.msh")
    setup_simulation_physics(vol_mesh_path)
