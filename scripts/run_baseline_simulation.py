import os
import numpy as np
import pyvista as pv

def run_simulation():
    input_file = os.path.join("data", "processed", "retina_volumetric_physics.vtu")
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Run the physics setup script first! Missing: {input_file}")

    print("Loading physics-configured mesh...")
    mesh = pv.read(input_file)

    # Simple estimation for baseline demonstration:
    # Calculate outward displacement vectors based on surface normals and internal pressure load
    print("Computing baseline mechanical deformation under simulated IOP...")
    
    # Compute point normals to direct the pressure force outward
    mesh.compute_normals(cell_normals=False, point_normals=True, inplace=True)
    
    # Simulate a minor displacement field (scaling factor for visualization)
    pressure_load = 0.002 # MPa
    stiffness = mesh.field_data['Youngs_Modulus'][0]
    
    # Displacement magnitude estimation proportional to pressure/stiffness
- displacement_magnitude = (pressure_load / stiffness) * 50.0 
    vectors = mesh.point_data['Normals'] * displacement_magnitude
    mesh.point_data['Displacement'] = vectors
    
    # Warp the geometry to visualize the physical deformation
    warped_mesh = mesh.warp_by_vector('Displacement', factor=1.0)

    # Save output results
    output_result_path = os.path.join("results", "retina_deformation_result.vtu")
    os.makedirs("results", exist_ok=True)
    warped_mesh.save(output_result_path)
    
    print(f"Simulation test completed successfully! Results saved to {output_result_path}")

if __name__ == "__main__":
    run_simulation()
