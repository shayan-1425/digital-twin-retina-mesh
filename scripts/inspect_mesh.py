import argparse
import sys
import trimesh


def inspect_stl(file_path):
    """Inspects an STL file and prints essential geometric quality metrics

    for digital twin simulations.
    """
    print(f"\n==========================================")
    print(f"   Mesh Inspection: {file_path}")
    print(f"==========================================\n")

    try:
        mesh = trimesh.load(file_path)
    except Exception as e:
        print(f"Error loading mesh file: {e}")
        sys.exit(1)

    # Basic stats
    print(f"Vertices Count : {len(mesh.vertices):,}")
    print(f"Faces Count    : {len(mesh.faces):,}")

    # Topological Integrity
    print(f"Is Watertight? : {mesh.is_watertight}")
    print(f"Is Manifold?   : {mesh.is_winding_consistent}")

    # Physical Dimensions
    bounds = mesh.extents
    print(
        f"Bounding Box   : {bounds[0]:.2f} x {bounds[1]:.2f} x {bounds[2]:.2f} mm"
    )

    if mesh.is_watertight:
        print(f"Volume         : {mesh.volume:.2f} mm³")
        print(f"Surface Area   : {mesh.area:.2f} mm²")
    else:
        print("⚠️ Warning: Mesh is non-watertight. Volume calculation skipped.")

    print(f"\n==========================================\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Inspect mesh quality for Digital Twin Retina models."
    )
    parser.add_argument(
        "--file",
        type=str,
        default="../data/processed/retina_simplified_50k.stl",
        help="Path to STL mesh file",
    )
    args = parser.parse_args()

    inspect_stl(args.file)
