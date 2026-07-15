import os
from html2image import Html2Image

script_dir = os.path.dirname(os.path.abspath(__file__))
workspace_dir = os.path.dirname(script_dir)
index_path = os.path.join(workspace_dir, "index.html")

print("Initializing Html2Image screen capturer...")
hti = Html2Image()
# Set aspect ratio size (1280x960 is great for displaying the core section metrics and charts in a high quality card view)
hti.size = (1280, 960)

output_file = "dashboard_preview.png"
print(f"Capturing dashboard page: {index_path}")
try:
    # Capture the html file
    hti.screenshot(html_file=index_path, save_as=output_file)
except Exception as e:
    print(f"Capture error encountered: {e}")

# Check if successfully generated, then relocate to Reference_Material
if os.path.exists(output_file):
    dest = os.path.join(script_dir, output_file)
    if os.path.exists(dest):
        os.remove(dest)
    os.rename(output_file, dest)
    print(f"Success! Real dashboard printscreen saved to: {dest}")
else:
    print("Error: Could not generate the screenshot file!")
