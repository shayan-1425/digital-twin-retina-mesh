import os
import pyvista as pv

def visualize_simulation_results():
    result_file = os.path.join("results", "retina_deformation_result.vtu")
    if not os.path.exists(result_file):
        raise FileNotFoundError(f"Result file not found at {result_file}. Run the simulation script first!")

    print("Opening interactive 3D viewer for simulation results...")
    mesh = pv.read(result_file)

    # Launch an interactive window showing the displacement/deformation
    plotter = pv.Plotter()
    plotter.add_mesh(mesh, scalars="Displacement", cmap="coolwarm", show_edges=True)
    plotter.add_scalar_bar(title="Displacement Magnitude")
    plotter.add_text("Retina Digital Twin - Baseline FEM Deformation", font_size=12)
    plotter.show()

if __name__ == "__main__":
    visualize_simulation_results()
