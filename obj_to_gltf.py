import trimesh
import sys

if len(sys.argv) < 2:
    print("Usage: python obj_to_gltf.py model.obj")
    exit()

mesh = trimesh.load(sys.argv[1])
mesh.export("model.glb")