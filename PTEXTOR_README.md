# PTEXTOR - Animated Story Creator

<img width="111" height="111" alt="PTEXTOR" src="https://github.com/user-attachments/assets/527cd015-3f05-4db8-9100-50c2282f5e5c" />

**PTEXTOR** is a lightweight desktop application for writers and storytellers, designed to create, edit, and share animated stories using custom file formats with beautiful visual effects.

[![Version](https://img.shields.io/badge/version-1.0-blue)](https://github.com/Priyanshurajpoot/PTEXTOR/releases)
[![Python](https://img.shields.io/badge/python-3.7+-green)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Windows-lightgrey)](https://github.com/Priyanshurajpoot/PTEXTOR/releases)
[![License](https://img.shields.io/badge/license-MIT-orange)](https://opensource.org/licenses/MIT)
[![GitHub Issues](https://img.shields.io/github/issues/Priyanshurajpoot/PTEXTOR)](https://github.com/Priyanshurajpoot/PTEXTOR/issues)

---

## 👨‍💻 About the Developer

**Priyanshu Rajpoot**  
*MCA Post Graduate | Python Developer | Prompt Engineer | AI Enthusiast*

- 🔗 **LinkedIn**: [priyanshux5](https://linkedin.com/in/priyanshux5)
- 💻 **GitHub**: [Priyanshurajpoot](https://github.com/Priyanshurajpoot)
- 📧 **Email**: priyanshux5xraj@gmail.com

**Core Interests**: Prompt Engineering, Artificial Intelligence, Machine Learning, NLP, Generative AI  
**Primary Skills**: Python, PyQt5, PyTorch, Transformers, OpenCV, Chrome Extension API, OAuth 2.0, Data Analysis, GUI Development

---

## ✨ Features

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

## 🚀 Quick Start

### Download & Install

#### Method 1: Installer (Recommended)
1. Download **[PTEXTOR-Setup.exe](https://github.com/Priyanshurajpoot/PTEXTOR/releases)** from Releases
2. Run the installer and follow the setup wizard
3. Launch PTEXTOR from Start Menu or Desktop

#### Method 2: Portable Version
1. Download **[PTEXTOR-Portable.zip](https://github.com/Priyanshurajpoot/PTEXTOR/releases)**
2. Extract to any folder
3. Run `PTEXTOR.exe`

#### Method 3: From Source
```bash
# Clone repository
git clone https://github.com/Priyanshurajpoot/PTEXTOR.git
cd PTEXTOR

# Install dependencies
pip install -r requirements.txt

# Run application
python main.py
```

### Create Your First Animated Story

1. **Launch PTEXTOR**
2. **Type your story** in the editor
3. **Add animation tags**:
   ```ptxt
   [effect=fade-in duration=2000]
   Once upon a time in a digital realm...
   ```
4. **Click Preview (▶️)** to see animations
5. **Save as .ptxt** or **Export as HTML**

---

## 📖 Usage Guide

### Creating Stories

#### Basic Writing
- Type directly in the editor
- Press Enter for new paragraphs
- Use toolbar to add effects and fonts

#### Toolbar Functions
- **📂 Open** - Load `.ptxt` or `.pdoc` files
- **💾 Save** - Save as `.ptxt` format
- **🌐 Export HTML** - Create standalone web page
- **📄 Export PDF** - Generate PDF document
- **📦 Export PDOC** - Package with HTML
- **🔗 Register File Types** - Windows integration

### Animation Examples

#### Fade-in Effect
```ptxt
[effect=fade-in duration=2000]
Your text appears gradually
```

#### Slide-up with Custom Font
```ptxt
[font name=Georgia]
[effect=slide-up duration=1500]
Text rises with elegant typography
```

#### Bounce Effect
```ptxt
[effect=bounce duration=2000]
Exciting text that bounces in!
```

#### Wave Animation
```ptxt
[effect=wave]
Character-by-character typewriter effect
```

### Complete Story Example

```ptxt
[effect=fade-in duration=2000]
Chapter One: The Digital Odyssey

[effect=slide-up duration=1500]
In a world where code breathed life into dreams...

[font name=Courier New]
[effect=bounce duration=2000]
"System activated!" the console blinked.

[effect=wave]
Each line of code unfolded a new possibility.

[effect=zoom duration=1800]
And so the adventure through cyberspace began...
```

---

## 📁 File Formats

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
- Easy to edit anywhere
- Version control friendly
- Small file size

### .pdoc (PTEXTOR Document)
Compressed package containing:
- `story.ptxt` - Source text with tags
- `story.html` - Pre-rendered HTML
- `metadata.json` - Document information

**Advantages:**
- Self-contained package
- Includes rendered HTML
- Preserves metadata
- Easy sharing

---

## 📤 Export Options

### HTML Export
- Standalone HTML file with embedded animations
- Works in any modern browser
- Beautiful gradient background
- Embedded Anime.js library

### PDF Export
- Professional A4 page format
- Clean text formatting
- Automatic page breaks
- Print-ready documents

### PDOC Export
- Packaged document format
- Contains both source and rendered versions
- Easy sharing and archiving

---

## 🎯 Tag Syntax Reference

### Effect Tags
```ptxt
[effect=EFFECT_NAME duration=MILLISECONDS]
Your text here
```

**Available Effects:**
- `fade-in` - Smooth opacity transition
- `slide-up` - Upward slide animation  
- `bounce` - Elastic bounce effect
- `zoom` - Scale-in animation
- `wave` - Character-by-character reveal

**Duration Guidelines:**
- `500ms` - Very fast
- `1000ms` - Fast
- `1500ms` - Normal (default)
- `2000ms` - Slow
- `3000+ms` - Very slow

### Font Tags
```ptxt
[font name=FONT_NAME]
Your styled text here
```

**Supported Fonts:** Arial, Helvetica, Times New Roman, Georgia, Courier New, Verdana, and more Windows fonts.

### Multiple Tags
```ptxt
[effect=fade-in duration=2000]
[font name=Georgia]
Combined effect and font styling
```

---

## 🏗️ Project Structure

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

```txt
PyQt5>=5.15.9              # GUI framework
PyQtWebEngine>=5.15.7      # Web rendering for preview
reportlab>=4.0             # PDF generation
```

---

## 🔧 Development

### Building from Source

#### Prerequisites
- Python 3.7 or higher
- PyInstaller for executable building

#### Build Steps
```bash
# Clone repository
git clone https://github.com/Priyanshurajpoot/PTEXTOR.git
cd PTEXTOR

# Install dependencies
pip install -r requirements.txt

# Build executable
pyinstaller --name PTEXTOR \
    --windowed \
    --onefile \
    --icon=assets/PTEXTOR.ico \
    --add-data "assets;assets" \
    --add-data "src;src" \
    main.py
```

### Architecture

**Key Components:**
- `PTextor` - Main application window
- `PreviewWindow` - Animation preview window  
- `ToolBarManager` - Toolbar controls and actions
- `FileAssociationManager` - Windows file type registration
- `PtxtParser` - Text parsing and HTML generation

---

## 🐛 Troubleshooting

### Common Issues & Solutions

**Preview Window Shows Empty Content**
- Ensure template.html is in correct location
- Try exporting as HTML first to verify

**Animations Not Working** 
- Check internet connection (Anime.js loads from CDN)
- Preview in browser to verify functionality

**File Association Not Working**
- Run as administrator when registering
- Restart Windows Explorer after registration

**PDF Export Fails**
- Ensure ReportLab is installed: `pip install reportlab>=4.0`

**App Won't Start**
- Install Microsoft Visual C++ Redistributable
- Verify Python version (3.7+ required)

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Reporting Bugs
1. [Open an issue](https://github.com/Priyanshurajpoot/PTEXTOR/issues) with detailed description
2. Include steps to reproduce and system information

### Suggesting Features
1. Create feature request with use cases
2. Explain benefits for users

### Pull Requests
1. Fork the repository
2. Create feature branch
3. Make changes with clear commits
4. Test thoroughly
5. Submit pull request

### Development Guidelines
- Follow PEP 8 style guide
- Add comments for complex logic
- Update documentation for new features
- Test on Windows 10/11
- Ensure backward compatibility

---

## 📝 Roadmap

### Upcoming Features
- [ ] **Multiple Themes** - Dark mode, light mode options
- [ ] **More Animations** - Rotate, flip, and additional effects
- [ ] **Text Formatting** - Bold, italic, underline support
- [ ] **Image Embedding** - Support for images in stories
- [ ] **Audio Integration** - Narration and sound effects
- [ ] **Cloud Storage** - Save and sync across devices
- [ ] **Collaborative Editing** - Real-time collaboration
- [ ] **Mobile Companion** - Companion app for mobile devices

### Version History
- **v1.0.0** - Initial release with core animation features

---

## 📄 License

This project is licensed under the MIT License:

```text
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
```

---

## 📞 Support & Contact

- **🐛 Report Issues**: [GitHub Issues](https://github.com/Priyanshurajpoot/PTEXTOR/issues)
- **🚀 Downloads**: [GitHub Releases](https://github.com/Priyanshurajpoot/PTEXTOR/releases)
- **📧 Email**: priyanshux5xraj@gmail.com
- **👨‍💻 Developer**: [Priyanshu Rajpoot](https://linkedin.com/in/priyanshux5)

---

## 🙏 Acknowledgments

Built with:
- **PyQt5** - Cross-platform GUI framework
- **Anime.js** - Lightweight animation library  
- **ReportLab** - PDF generation toolkit
- **PyInstaller** - Application packaging

Special thanks to:
- The open-source community
- Beta testers and early users
- Contributors and supporters

---

## 🔗 Quick Links

- **📂 Repository**: [PTEXTOR on GitHub](https://github.com/Priyanshurajpoot/PTEXTOR.git)
- **🚀 Releases**: [Latest Releases](https://github.com/Priyanshurajpoot/PTEXTOR/releases)
- **🐛 Issues**: [Report Issues](https://github.com/Priyanshurajpoot/PTEXTOR/issues)
- **👨‍💻 Developer**: [Priyanshu Rajpoot](https://linkedin.com/in/priyanshux5)

---

**Python Developer | Prompt Engineer | AI Enthusiast**  
*Transforming words into captivating visual experiences*

---

## AUTHOR
**Priyanshu Rajpoot**  
*MCA Post Graduate | Python Developer | Creative Software Engineer*