import re
import os
from util import resource_path  # Added for PyInstaller bundled paths

# Compile regex pattern
TAG_PATTERN = re.compile(r'^\s*\[(.*?)\]\s*$')

def ptxt_to_html(ptxt_text: str) -> str:
    """
    Convert .ptxt text into HTML paragraphs with animation + font metadata.
    Supports effects like fade-in, slide-up, zoom, wave, bounce and font changes.
    """
    html_paragraphs = []
    lines = ptxt_text.splitlines()
    current_effect = None
    effect_params = {}
    current_font = None

    for line in lines:
        line = line.strip()

        if not line:
            current_effect = None
            effect_params = {}
            current_font = None
            continue

        tag_match = TAG_PATTERN.match(line)
        if tag_match:
            content = tag_match.group(1).strip()

            if '=' in content:
                parts = content.split()
                tag_type = parts[0].split('=')[0].lower()
                params = {}
                for part in parts:
                    if "=" in part:
                        k, v = part.split("=", 1)
                        params[k.lower().strip()] = v.strip().strip('"\'')
                if tag_type == "font":
                    current_font = params.get("name") or params.get("font")
                elif tag_type == "effect":
                    current_effect = params.get("effect")
                    effect_params = params.copy()
                elif tag_type in ["fade-in", "slide-up", "zoom", "wave", "bounce"]:
                    current_effect = tag_type
                    effect_params = params.copy()
            else:
                tag_name = content.lower()
                if tag_name in ["fade-in", "slide-up", "zoom", "wave", "bounce"]:
                    current_effect = tag_name
                    effect_params = {}
            continue

        # Build paragraph HTML
        attrs = []
        css_styles = []

        if current_effect:
            attrs.append(f'data-effect="{current_effect}"')
            duration = effect_params.get("duration")
            if duration:
                attrs.append(f'data-duration="{duration}"')
            for k, v in effect_params.items():
                if k not in ["effect", "duration"]:
                    attrs.append(f'data-{k}="{v}"')

        if current_font:
            css_styles.append(f"font-family: '{current_font}', sans-serif")

        if css_styles:
            attrs.append(f'style="{"; ".join(css_styles)};"')

        attrs_str = " " + " ".join(attrs) if attrs else ""
        html_paragraphs.append(f'<div class="paragraph"{attrs_str}>{line}</div>')

    return "\n".join(html_paragraphs)


def parse_ptxt(ptxt_text: str, template_path: str = None) -> str:
    """
    Parse .ptxt content and return complete HTML.
    Bundles template.html automatically if template_path is None.
    """
    try:
        body_html = ptxt_to_html(ptxt_text)

        if not template_path:
            template_path = resource_path("src/template.html")

        if os.path.exists(template_path):
            with open(template_path, "r", encoding="utf-8") as f:
                template = f.read()
            return template.replace("<!--CONTENT-->", body_html)
        else:
            return f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>PTEXTOR Preview</title>
<style>
body {{ font-family: Arial, sans-serif; padding: 20px; }}
.paragraph {{ margin-bottom: 15px; font-size: 18px; line-height: 1.6; }}
</style>
</head>
<body>
{body_html}
</body>
</html>
"""
    except Exception as e:
        print(f"Error in parse_ptxt: {e}")
        return f"<div>Error parsing content: {str(e)}</div>"
