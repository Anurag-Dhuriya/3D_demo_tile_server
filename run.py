import sys
import subprocess
from convert import convert_obj_to_glb

if len(sys.argv) < 2:
    print("Usage: python run.py path_to_obj_file")
    exit()

obj_path = sys.argv[1]

# Convert file
convert_obj_to_glb(obj_path)

# Start server
subprocess.run(["uvicorn", "main:app", "--reload"])