import argparse
import sys
import pyvista as pv


def visualize_mesh(file_path, show_edges=True, opacity=1.0, color="lightcoords"):
    """Loads an STL mesh and opens an interactive PyVista viewer

    to inspect surface geometry, element edges, and cross-sections.
    """
    print(f"\n==========================================")
    print(f"   Interactive Mesh Visualizer")
    print(f"==========================================\n")
    print(f"Loading mesh: {file_path}")

    try:
        mesh = pv.read(file_path)
    except Exception as e:
        print(f"❌ Error loading file with PyVista: {e}")
        sys.exit(1)

    # Setup plotter
    plotter = pv.Plotter(title=f"Digital Twin Retina - {file_path}")
    plotter.add_text(
        f"Mesh: {file_path}\nFaces: {mesh.n_cells:,}", position="upper_left"
    )

    # Render main surface
    plotter.add_mesh(
        mesh,
        color="lightblue",
        show_edges=show_edges,
        edge_color="darkblue",
        opacity=opacity,
        smooth_shading=True,
    )

    # Add reference axes and bounds
    plotter.add_axes()
    plotter.show_bounds(grid="front", location="all", ticks="both")

    print(
        "Displaying mesh window. Close the viewer window to finish execution."
    )
    plotter.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Visualize 3D Ocular Meshes using PyVista."
    )
    parser.add_argument(
        "--file",
        type=str,
        default="../data/processed/retina_simplified_50k.stl",
        help="Path to STL file to visualize",
    )
    parser.add_argument(
        "--no-edges",
        action="store_true",
        help="Disable wireframe triangle edges display",
    )
    parser.add_argument(
        "--opacity",
        type=float,
        default=1.0,
        help="Set mesh opacity (0.0 to 1.0)",
    )

    args = parser.parse_args()
    visualize_mesh(
        args.file, show_edges=not args.no-edges, opacity=args.opacity
    )
