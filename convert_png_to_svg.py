import base64
from pathlib import Path

png_path = Path("icons/vana_scanmaster.jpg")
svg_path = Path("icons/vana_scanmaster.svg")

data = base64.b64encode(png_path.read_bytes()).decode("utf-8")

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="500" height="500">
  <image href="data:image/jpeg;base64,{data}" width="500" height="500"/>
</svg>'''

svg_path.write_text(svg, encoding="utf-8")