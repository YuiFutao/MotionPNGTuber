import urllib.request
import os
import subprocess
import shutil

url = "https://astral.sh/uv/install.ps1"
install_script = "install_uv.ps1"

try:
    print(f"Downloading {url}...")
    urllib.request.urlretrieve(url, install_script)
    
    print(f"Running {install_script}...")
    # Run powershell script
    result = subprocess.run(["powershell", "-ExecutionPolicy", "ByPass", "-File", install_script], capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print("Error/Warning output:")
        print(result.stderr)
        
    print("Done.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    if os.path.exists(install_script):
        print("Cleaning up script file...")
        os.remove(install_script)
