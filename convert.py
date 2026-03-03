import trimesh
import sys
import os

def convert_obj_to_glb(obj_path):
    if not os.path.exists(obj_path):
        print("File not found!")
        return None

    # Load object (allow scene or mesh)
    mesh = trimesh.load(obj_path)

    output_path = "static/model.glb"

    mesh.export(output_path)

    print("Converted to GLB successfully!")
    return output_path