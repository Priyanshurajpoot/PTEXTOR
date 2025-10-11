<img width="111" height="111" alt="PTEXTOR" src="https://github.com/user-attachments/assets/527cd015-3f05-4db8-9100-50c2282f5e5c" />
         

# PTEXTOR

**PTEXTOR** is a lightweight desktop application for writers and storytellers, designed to create, edit, and share animated stories using custom file formats with beautiful visual effects.

![Version](https://img.shields.io/badge/version-1.0-blue)
![Python](https://img.shields.io/badge/python-3.7+-green)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey)
![License](https://img.shields.io/badge/license-MIT-orange)

---

## Table of Contents

- [Features](#features)
- [Screenshots](#screenshots)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage Guide](#usage-guide)
  - [Creating Stories](#creating-stories)
  - [Animation Effects](#animation-effects)
  - [Font Customization](#font-customization)
  - [File Operations](#file-operations)
- [File Formats](#file-formats)
- [Export Options](#export-options)
- [Tag Syntax Reference](#tag-syntax-reference)
- [Advanced Features](#advanced-features)
- [Development](#development)
- [Building from Source](#building-from-source)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## Features

### Core Features
- ✍️ **Simple Text Editor** - Clean, distraction-free writing environment
- 🎬 **Animated Effects** - Add cinematic animations to your paragraphs
- 👁️ **Live Preview** - See your story come alive with real-time animation preview
- 📦 **Custom File Formats** - Use `.ptxt` (plain text) and `.pdoc` (packaged document)
- 🌐 **HTML Export** - Share stories as standalone web pages
- 📄 **PDF Export** - Generate professional PDF documents
- 🎨 **Font Customization** - Apply custom fonts to any paragraph
- ⚡ **Lightweight** - Fast and responsive desktop application
- 🔗 **File Association** - Register file types with Windows for easy access

### Animation Effects
- **fade-in** - Smooth opacity transition
- **slide-up** - Graceful upward slide animation
- **bounce** - Playful elastic bounce effect
- **zoom** - Dramatic scale-in effect
- **wave** - Character-by-character wave animation

### Supported Fonts
Arial, Helvetica, Courier New, Times New Roman, Georgia, Verdana, Trebuchet MS, Impact, Comic Sans MS, and more!

---

## Screenshots

### Main Editor
```




```

### Preview Window
Beautiful gradient background with animated text appearing sequentially with chosen effects.

---

## Installation

### Method 1: Download Installer (Recommended)

1. Visit the **[Releases](https://github.com/Priyanshurajpoot/PTEXTOR/releases/tag/v1.0)** page
2. Download the latest `PTEXTOR-Setup.exe`
3. Run the installer
4. Follow the installation wizard
5. Launch PTEXTOR from Start Menu or Desktop shortcut

### Method 2: Portable Version

1. Download `PTEXTOR-Portable.zip` from Releases
2. Extract to desired location
3. Run `PTEXTOR.exe`

### Method 3: Install from Source

```bash
# Clone the repository
git clone https://github.com/priyanshurajpoot/PTEXTOR.git
cd PTEXTOR

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

### System Requirements
- **OS**: Windows 10/11 (64-bit)
- **Python**: 3.7+ (for source installation)
- **RAM**: 256 MB minimum
- **Disk Space**: 50 MB

---

## Quick Start

### Create Your First Animated Story

1. **Launch PTEXTOR** from Start Menu
2. **Type your story** in the editor
3. **Add animation tags** above paragraphs:
   ```
   [effect=fade-in duration=2000]
   Once upon a time, in a digital realm...
   ```
4. **Click Preview** (▶️) to see your story animated
5. **Save** your work as `.ptxt` file
6. **Export** as HTML to share with others

### Example Story

```ptxt
[effect=fade-in duration=2000]
Chapter One: The Beginning

[effect=slide-up duration=1500]
It was a dark and stormy night when the adventure began.

[font name=Georgia]
[effect=bounce duration=2000]
"We must hurry!" shouted the captain.

[effect=wave]
The crew sprang into action, each knowing their role.

[effect=zoom duration=1800]
And so, their journey into the unknown commenced...
```

---

## Usage Guide

### Creating Stories

#### Basic Writing
1. Open PTEXTOR
2. Type directly in the editor
3. Press Enter to create new paragraphs
4. Use toolbar buttons to add effects

#### Using the Toolbar

**File Operations:**
- **📂 Open** - Load existing `.ptxt` or `.pdoc` files
- **💾 Save** - Save current work as `.ptxt`
- **🌐 Export HTML** - Generate standalone HTML file
- **📄 Export PDF** - Create PDF document
- **📦 Export PDOC** - Package story with HTML

**Animation Controls:**
- **Effect Dropdown** - Choose animation type
- **Font Dropdown** - Select font family
- **Duration Input** - Set animation speed (milliseconds)
- **🏷️ Insert Tag** - Add selected effect/font tags
- **▶️ Preview** - Open animated preview window

**System Integration:**
- **🔗 Register File Types** - Associate `.ptxt` and `.pdoc` with PTEXTOR

### Animation Effects

#### Fade-in
Smoothly transitions from transparent to opaque.
```ptxt
[effect=fade-in duration=2000]
Your text appears gradually
```
**Best for:** Gentle introductions, atmospheric text

#### Slide-up
Text slides upward while fading in.
```ptxt
[effect=slide-up duration=1500]
Text rises from below
```
**Best for:** Dramatic reveals, chapter headings

#### Bounce
Elastic bounce effect with scaling.
```ptxt
[effect=bounce duration=2000]
Text bounces into view!
```
**Best for:** Playful content, emphasis, excitement

#### Zoom
Scales from small to full size.
```ptxt
[effect=zoom duration=1800]
Text zooms toward you
```
**Best for:** Important statements, dramatic emphasis

#### Wave
Character-by-character animation.
```ptxt
[effect=wave]
Each letter appears in sequence
```
**Best for:** Typewriter effect, dynamic text, emphasis

### Font Customization

Apply custom fonts to any paragraph:

```ptxt
[font name=Georgia]
This text uses Georgia font

[font name=Courier New]
This text looks like code

[font name=Impact]
Bold statement!
```

### Combining Effects and Fonts

```ptxt
[effect=fade-in duration=2000]
[font name=Times New Roman]
Classic fade-in with serif font
```

---

## File Formats

### .ptxt (PTEXTOR Text)
Plain text format with embedded animation tags.

**Structure:**
```
[effect=fade-in duration=2000]
Paragraph text here

[font name=Arial]
[effect=slide-up]
Another paragraph
```

**Advantages:**
- Human-readable
- Easy to edit in any text editor
- Version control friendly
- Small file size

### .pdoc (PTEXTOR Document)
Compressed package containing multiple files.

**Contents:**
- `story.ptxt` - Source text with tags
- `story.html` - Pre-rendered HTML
- `metadata.json` - Document information

**Advantages:**
- Self-contained package
- Includes pre-rendered HTML
- Preserves metadata
- Easy sharing

**Structure:**
```
story.pdoc (ZIP archive)
├── story.ptxt       # Original text
├── story.html       # Rendered HTML
└── metadata.json    # Title, date, version
```

---

## Export Options

### HTML Export
Creates a standalone HTML file with embedded animations.

**Features:**
- Self-contained (no external dependencies)
- Embedded Anime.js library
- Responsive design
- Works in any modern browser
- Beautiful gradient background
- Smooth animations

**Usage:**
1. Click **🌐 Export HTML**
2. Choose save location
3. Open in browser to view
4. Share via email or web hosting

**File size:** ~5-20 KB depending on content

### PDF Export
Generates a professional PDF document.

**Features:**
- A4 page size
- Automatic page breaks
- Text wrapping
- Clean formatting
- No animation tags in output
- Professional appearance

**Usage:**
1. Click **📄 Export PDF**
2. Choose save location
3. Open with any PDF reader
4. Print or share digitally

**Note:** Animations are not preserved in PDF format.

### PDOC Export
Creates a packaged document with source and rendered HTML.

**Usage:**
1. Click **📦 Export PDOC**
2. Choose save location
3. File can be opened in PTEXTOR
4. HTML version accessible inside package

---

## Tag Syntax Reference

### Effect Tags

**Basic syntax:**
```ptxt
[effect=EFFECT_NAME]
Your text here
```

**With duration:**
```ptxt
[effect=EFFECT_NAME duration=MILLISECONDS]
Your text here
```

**Available effects:**
- `fade-in` - Opacity transition
- `slide-up` - Upward slide
- `bounce` - Elastic bounce
- `zoom` - Scale effect
- `wave` - Character animation

**Duration values:**
- `500` - Very fast
- `1000` - Fast
- `1500` - Normal (default)
- `2000` - Slow
- `3000+` - Very slow

### Font Tags

**Syntax:**
```ptxt
[font name=FONT_NAME]
Your text here
```

**Examples:**
```ptxt
[font name=Arial]
Clean sans-serif text

[font name=Times New Roman]
Classic serif typography

[font name=Courier New]
Monospace code-like text
```

### Multiple Tags

Apply multiple effects to the same paragraph:
```ptxt
[effect=fade-in duration=2000]
[font name=Georgia]
This paragraph fades in using Georgia font
```

**Tag order doesn't matter:**
```ptxt
[font name=Arial]
[effect=bounce duration=1800]
Same result as above order
```

---

## Advanced Features

### File Association

Register `.ptxt` and `.pdoc` files with Windows:

1. Click **🔗 Register File Types** in toolbar
2. Confirm administrator permission dialog
3. Files now show custom icons in Explorer
4. Double-click `.ptxt` or `.pdoc` files to open in PTEXTOR

**Benefits:**
- Custom file icons in Windows Explorer
- Right-click → Open with PTEXTOR
- Double-click to launch PTEXTOR
- Integrated with Windows shell

**Unregister:**
```bash
python file_association.py unregister
```

### Custom Duration Control

Fine-tune animation timing:

```ptxt
[effect=fade-in duration=500]    # Quick fade
[effect=wave duration=3000]      # Slow wave
[effect=zoom duration=1200]      # Custom speed
```

**Timing guidelines:**
- **500-1000ms** - Fast, energetic
- **1500-2000ms** - Standard, comfortable
- **2500-3000ms** - Slow, dramatic
- **3000+ms** - Very slow, ceremonial

### Preview Window Features

- **Real-time rendering** with Anime.js
- **Sequential animations** - paragraphs animate in order
- **Gradient background** - Beautiful purple gradient
- **Responsive design** - Adapts to window size
- **Smooth transitions** - Professional-quality animations

---

## Development

### Project Structure

```
PTEXTOR/
├── assets/
│   ├── PTEXTOR.ico          # Application icon
│   ├── ptxt.ico             # .ptxt file icon
│   └── pdoc.ico             # .pdoc file icon
├── src/
│   └── template.html        # HTML template for preview/export
├── main.py                  # Application entry point
├── toolbar.py               # Toolbar and file operations
├── ptxt_parser.py           # Parser for .ptxt format
├── file_association.py      # Windows file association
├── util.py                  # Utility functions
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

### Dependencies

```python
PyQt5>=5.15.9              # GUI framework
PyQtWebEngine>=5.15.7      # Web rendering for preview
reportlab>=4.0             # PDF generation
```

### Architecture

**Main Components:**
1. **main.py** - Application window and preview management
2. **toolbar.py** - UI controls and file operations
3. **ptxt_parser.py** - Text parsing and HTML generation
4. **file_association.py** - Windows registry integration
5. **template.html** - HTML/CSS/JS for animations

**Key Classes:**
- `PTextor` - Main application window
- `PreviewWindow` - Animation preview window
- `ToolBarManager` - Toolbar controls and actions
- `FileAssociationManager` - File type registration

---

## Building from Source

### Prerequisites

```bash
# Python 3.7 or higher
python --version

# Install PyInstaller
pip install pyinstaller
```

### Build Executable

```bash
# Navigate to project directory
cd ptextor

# Build with PyInstaller
pyinstaller --name PTEXTOR \
    --windowed \
    --onefile \
    --icon=assets/PTEXTOR.ico \
    --add-data "assets;assets" \
    --add-data "src;src" \
    main.py

# Output: dist/PTEXTOR.exe
```

### Build Installer

```bash
# Use Inno Setup (Windows)
# Create installer script (setup.iss)
# Compile with Inno Setup Compiler
```

---

## Troubleshooting

### Preview Window Shows Empty Content
**Solution:** Ensure template.html is in the correct location. Try re-exporting as HTML first.

### Animations Not Working
**Solution:** Check internet connection (Anime.js loads from CDN). Preview in browser to verify.

### File Association Not Working
**Solution:** Run as administrator when registering file types. Restart Windows Explorer.

### PDF Export Fails
**Solution:** Ensure ReportLab is installed: `pip install reportlab>=4.0`

### Icons Not Showing
**Solution:** Verify assets folder is included in build. Check resource_path() function.

### App Won't Start
**Solution:** Install Microsoft Visual C++ Redistributable. Check Python version (3.7+).

---

## Contributing

We welcome contributions! Here's how you can help:

### Reporting Bugs
1. Check existing issues on GitHub
2. Create detailed bug report with steps to reproduce
3. Include system information and error messages

### Suggesting Features
1. Open an issue with "Feature Request" label
2. Describe the feature and use cases
3. Explain why it would benefit users

### Pull Requests
1. Fork the repository
2. Create a feature branch
3. Make your changes with clear commits
4. Test thoroughly
5. Submit pull request with description

### Development Guidelines
- Follow PEP 8 style guide
- Add comments for complex logic
- Update documentation for new features
- Test on Windows 10/11
- Ensure backward compatibility

---

## License

MIT License

Copyright (c) 2024 PTEXTOR 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

## Acknowledgments

- **PyQt5** - Cross-platform GUI framework
- **Anime.js** - Lightweight animation library
- **ReportLab** - PDF generation toolkit


---

## Contact & Support

- **GitHub Issues**: [Report bugs or request features](https://github.com/Priyanshurajpoot/PTEXTOR/issues)
- **Documentation**: [Full documentation](https://github.com/Priyanshurajpoot/PTEXTOR)
- **Email**: priyanshux5xraj@gmail.com
---

## Roadmap

### Upcoming Features
- [ ] Multiple themes (dark mode, light mode)
- [ ] More animation effects (rotate, flip, etc.)
- [ ] Text formatting (bold, italic, underline)
- [ ] Image embedding support
- [ ] Audio narration integration
- [ ] Cloud storage integration
- [ ] Collaborative editing
- [ ] Mobile companion app
- [ ] Web-based editor

### Version History
- **v1.0.0** - Initial release with core features , currently released and available.


---

AUTRHOR 
- PRIYANSHU RAJPOOT

*Transform your words into captivating visual experiences with PTEXTOR*
