import os
import zipfile
from PyQt5.QtWidgets import (
    QPushButton, QFileDialog, QComboBox, QSpacerItem, QSizePolicy, QHBoxLayout, QMessageBox
)
from PyQt5.QtCore import QThread, pyqtSignal
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from ptxt_parser import parse_ptxt, ptxt_to_html

try:
    from file_association import FileAssociationManager
    FILE_ASSOCIATIONS_AVAILABLE = True
except ImportError:
    FILE_ASSOCIATIONS_AVAILABLE = False
    print("File associations not available - file_association.py not found")


class FileAssociationThread(QThread):
    """Background thread for file association registration"""
    finished = pyqtSignal(bool)
    error = pyqtSignal(str)
    
    def __init__(self, action="register"):
        super().__init__()
        self.action = action
    
    def run(self):
        try:
            if not FILE_ASSOCIATIONS_AVAILABLE:
                self.error.emit("File association manager not available")
                return
                
            manager = FileAssociationManager()
            
            if self.action == "register":
                success = manager.register_file_types()
            elif self.action == "unregister":
                success = manager.unregister_file_types()
            else:
                success = False
                
            self.finished.emit(success)
            
        except Exception as e:
            self.error.emit(str(e))


class ToolBarManager:
    def __init__(self, parent, editor, template_path, preview_callback):
        self.parent = parent
        self.editor = editor
        self.template_path = template_path
        self.preview_callback = preview_callback

        # Layout for toolbar
        self.layout = QHBoxLayout()

        # --- File buttons ---
        self.open_button = QPushButton("📁 Open")
        self.open_button.clicked.connect(self.open_ptxt)
        self.open_button.setToolTip("Open PTXT or PDOC file")
        self.layout.addWidget(self.open_button)

        self.save_button = QPushButton("💾 Save")
        self.save_button.clicked.connect(self.save_ptxt)
        self.save_button.setToolTip("Save as PTXT file")
        self.layout.addWidget(self.save_button)

        self.export_html_button = QPushButton("🌐 Export HTML")
        self.export_html_button.clicked.connect(self.export_html)
        self.export_html_button.setToolTip("Export as standalone HTML")
        self.layout.addWidget(self.export_html_button)

        self.export_pdf_button = QPushButton("📄 Export PDF")
        self.export_pdf_button.clicked.connect(self.export_pdf)
        self.export_pdf_button.setToolTip("Export as PDF document")
        self.layout.addWidget(self.export_pdf_button)

        self.export_pdoc_button = QPushButton("📦 Export PDOC")
        self.export_pdoc_button.clicked.connect(self.export_pdoc)
        self.export_pdoc_button.setToolTip("Export as PDOC package")
        self.layout.addWidget(self.export_pdoc_button)

        # --- File Association button ---
        if FILE_ASSOCIATIONS_AVAILABLE:
            self.register_button = QPushButton("🔗 Register File Types")
            self.register_button.clicked.connect(self.register_file_types)
            self.register_button.setToolTip("Register PTXT/PDOC file types with Windows")
            self.layout.addWidget(self.register_button)

        # --- Effect selector ---
        self.effect_combo = QComboBox()
        self.effect_combo.addItem("Select Effect")
        self.effect_combo.model().item(0).setEnabled(False)
        effects = ["fade-in", "slide-up", "bounce", "zoom", "wave"]
        self.effect_combo.addItems(effects)
        self.effect_combo.setToolTip("Choose animation effect")
        self.layout.addWidget(self.effect_combo)

        # --- Font selector ---
        self.font_combo = QComboBox()
        self.font_combo.addItem("Select Font")
        self.font_combo.model().item(0).setEnabled(False)
        fonts = [
            "Arial", "Helvetica", "Courier New", "Times New Roman", 
            "Georgia", "Verdana", "Trebuchet MS", "Impact", "Comic Sans MS"
        ]
        self.font_combo.addItems(fonts)
        self.font_combo.setToolTip("Choose font family")
        self.layout.addWidget(self.font_combo)

        # --- Duration input selector ---
        self.duration_combo = QComboBox()
        self.duration_combo.addItem("Duration (ms)")
        self.duration_combo.model().item(0).setEnabled(False)
        durations = ["500", "1000", "1500", "2000", "2500", "3000", "4000", "5000"]
        self.duration_combo.addItems(durations)
        self.duration_combo.setToolTip("Animation duration in milliseconds")
        self.layout.addWidget(self.duration_combo)

        # --- Insert Tag button ---
        self.insert_button = QPushButton("🏷 Insert Tag")
        self.insert_button.clicked.connect(self.insert_tag)
        self.insert_button.setToolTip("Insert effect/font tags at cursor position")
        self.layout.addWidget(self.insert_button)

        # Spacer
        spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.layout.addSpacerItem(spacer)

        # Play button - fixed encoding
        self.play_button = QPushButton("▶️ Preview")
        self.play_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-weight: bold;
                font-size: 14px;
                padding: 8px 16px;
                border: none;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #3d8b40;
            }
        """)
        self.play_button.clicked.connect(self.preview_callback)
        self.play_button.setToolTip("Show animated preview")
        self.layout.addWidget(self.play_button)

    # ------------------------
    # File Association Methods
    # ------------------------
    def register_file_types(self):
        """Register file types with system"""
        if not FILE_ASSOCIATIONS_AVAILABLE:
            QMessageBox.warning(
                self.parent, 
                "Not Available", 
                "File association feature is not available on this system."
            )
            return
            
        reply = QMessageBox.question(
            self.parent,
            "Register File Types",
            "This will register .ptxt and .pdoc file types with Windows.\n"
            "Files will show custom icons and can be opened with PTEXTOR.\n\n"
            "Administrator privileges may be required.\n\n"
            "Continue?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.Yes
        )
        
        if reply == QMessageBox.Yes:
            self.register_button.setEnabled(False)
            self.register_button.setText("Registering...")
            
            self.association_thread = FileAssociationThread("register")
            self.association_thread.finished.connect(self.on_registration_finished)
            self.association_thread.error.connect(self.on_registration_error)
            self.association_thread.start()
    
    def on_registration_finished(self, success):
        """Handle registration completion"""
        self.register_button.setEnabled(True)
        self.register_button.setText("🔗 Register File Types")
        
        if success:
            QMessageBox.information(
                self.parent,
                "Success",
                "File types registered successfully!\n\n"
                "You may need to refresh Windows Explorer to see the new icons."
            )
        else:
            QMessageBox.warning(
                self.parent,
                "Registration Failed",
                "Failed to register file types.\n"
                "This may require administrator privileges."
            )
    
    def on_registration_error(self, error_msg):
        """Handle registration error"""
        self.register_button.setEnabled(True)
        self.register_button.setText("🔗 Register File Types")
        
        QMessageBox.critical(
            self.parent,
            "Registration Error",
            f"Error during file type registration:\n\n{error_msg}"
        )

    # ------------------------
    # Tag insertion
    # ------------------------
    def insert_tag(self):
        effect = self.effect_combo.currentText()
        font = self.font_combo.currentText()
        duration = self.duration_combo.currentText()

        tag_lines = []
        cursor = self.editor.textCursor()

        # Insert effect tag
        if effect and not effect.startswith("Select"):
            if duration and not duration.startswith("Duration"):
                tag_lines.append(f"[effect={effect} duration={duration}]")
            else:
                tag_lines.append(f"[effect={effect}]")

        # Insert font tag
        if font and not font.startswith("Select"):
            tag_lines.append(f"[font name={font}]")

        if tag_lines:
            # Add some formatting for readability
            insert_text = "\n" + "\n".join(tag_lines) + "\nYour text here\n"
            cursor.insertText(insert_text)
            
            # Move cursor to "Your text here" and select it
            cursor.movePosition(cursor.Up)
            cursor.movePosition(cursor.StartOfLine)
            cursor.movePosition(cursor.EndOfLine, cursor.KeepAnchor)
            self.editor.setTextCursor(cursor)
        else:
            QMessageBox.information(
                self.parent, 
                "No Selection", 
                "Please select an effect and/or font before inserting tags."
            )

    # ------------------------
    # File operations
    # ------------------------
    def open_ptxt(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(
            self.parent,
            "Open File",
            "",
            "PTXT/PDOC Files (*.ptxt *.pdoc);;All Files (*)",
            options=options,
        )
        if not file_path:
            return

        try:
            if file_path.endswith(".pdoc"):
                with zipfile.ZipFile(file_path, "r") as zipf:
                    with zipf.open("story.ptxt") as f:
                        text = f.read().decode("utf-8")
                        self.editor.setPlainText(text)
                QMessageBox.information(self.parent, "Success", f"Loaded PDOC: {os.path.basename(file_path)}")
            else:
                with open(file_path, "r", encoding="utf-8") as f:
                    self.editor.setPlainText(f.read())
                QMessageBox.information(self.parent, "Success", f"Loaded PTXT: {os.path.basename(file_path)}")
                
        except Exception as e:
            QMessageBox.critical(self.parent, "Error", f"Failed to open file:\n{str(e)}")

    def save_ptxt(self):
        options = QFileDialog.Options()
        default_path = os.path.join(os.path.expanduser("~"), "Documents", "story.ptxt")
        file_path, _ = QFileDialog.getSaveFileName(
            self.parent,
            "Save .ptxt file",
            default_path,
            "PTXT Files (*.ptxt);;All Files (*)",
            options=options,
        )
        if file_path:
            try:
                # Ensure directory exists
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(self.editor.toPlainText())
                QMessageBox.information(self.parent, "Success", f"Saved: {os.path.basename(file_path)}")
                
            except Exception as e:
                QMessageBox.critical(self.parent, "Error", f"Failed to save file:\n{str(e)}")

    def export_html(self):
        text = self.editor.toPlainText()
        if not text.strip():
            QMessageBox.warning(self.parent, "Warning", "No content to export!")
            return
            
        try:
            # Generate complete HTML
            with open(self.template_path, "r", encoding="utf-8") as f:
                template = f.read()
            
            html_content = ptxt_to_html(text)
            complete_html = template.replace("<!--CONTENT-->", html_content)
            
            options = QFileDialog.Options()
            default_path = os.path.join(os.path.expanduser("~"), "Documents", "story.html")
            file_path, _ = QFileDialog.getSaveFileName(
                self.parent,
                "Export HTML",
                default_path,
                "HTML Files (*.html);;All Files (*)",
                options=options,
            )
            
            if file_path:
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(complete_html)
                QMessageBox.information(self.parent, "Success", f"Exported HTML: {os.path.basename(file_path)}")
                
        except Exception as e:
            QMessageBox.critical(self.parent, "Error", f"Failed to export HTML:\n{str(e)}")

    def export_pdf(self):
        text = self.editor.toPlainText()
        if not text.strip():
            QMessageBox.warning(self.parent, "Warning", "No content to export!")
            return
            
        try:
            lines = [line.strip() for line in text.splitlines() if line.strip()]
            
            options = QFileDialog.Options()
            default_path = os.path.join(os.path.expanduser("~"), "Documents", "story.pdf")
            file_path, _ = QFileDialog.getSaveFileName(
                self.parent,
                "Export PDF",
                default_path,
                "PDF Files (*.pdf);;All Files (*)",
                options=options,
            )
            
            if file_path:
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                
                c = canvas.Canvas(file_path, pagesize=A4)
                width, height = A4
                y = height - 50
                line_height = 25
                margin_left = 50
                margin_right = 50
                max_width = width - margin_left - margin_right
                
                for line in lines:
                    # Skip tag lines in PDF export
                    if not (line.startswith("[") and line.endswith("]")):
                        if y < 100:  # Start new page if needed
                            c.showPage()
                            y = height - 50
                        
                        # Handle long lines by wrapping
                        if len(line) > 80:
                            words = line.split()
                            current_line = ""
                            for word in words:
                                if len(current_line + " " + word) <= 80:
                                    current_line += " " + word if current_line else word
                                else:
                                    if current_line:
                                        c.drawString(margin_left, y, current_line)
                                        y -= line_height
                                        if y < 100:
                                            c.showPage()
                                            y = height - 50
                                    current_line = word
                            if current_line:
                                c.drawString(margin_left, y, current_line)
                                y -= line_height
                        else:
                            c.drawString(margin_left, y, line)
                            y -= line_height
                        
                        # Add some extra space between paragraphs
                        y -= 10
                        
                c.save()
                QMessageBox.information(self.parent, "Success", f"Exported PDF: {os.path.basename(file_path)}")
                
        except Exception as e:
            QMessageBox.critical(self.parent, "Error", f"Failed to export PDF:\n{str(e)}")

    def export_pdoc(self):
        text = self.editor.toPlainText()
        if not text.strip():
            QMessageBox.warning(self.parent, "Warning", "No content to export!")
            return
            
        try:
            # Generate HTML
            with open(self.template_path, "r", encoding="utf-8") as f:
                template = f.read()
            
            html_content = ptxt_to_html(text)
            complete_html = template.replace("<!--CONTENT-->", html_content)

            options = QFileDialog.Options()
            default_path = os.path.join(os.path.expanduser("~"), "Documents", "story.pdoc")
            file_path, _ = QFileDialog.getSaveFileName(
                self.parent,
                "Export PDOC",
                default_path,
                "PDOC Files (*.pdoc);;All Files (*)",
                options=options,
            )
            
            if file_path:
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                
                with zipfile.ZipFile(file_path, "w", compression=zipfile.ZIP_DEFLATED) as zipf:
                    # Add the PTXT file
                    zipf.writestr("story.ptxt", text, compress_type=zipfile.ZIP_DEFLATED)
                    
                    # Add the complete HTML file
                    zipf.writestr("story.html", complete_html, compress_type=zipfile.ZIP_DEFLATED)
                    
                    # Add metadata file
                    metadata = f"""{{
    "title": "PTEXTOR Story",
    "created": "{self._get_current_timestamp()}",
    "version": "1.0",
    "format": "pdoc",
    "generator": "PTEXTOR"
}}"""
                    zipf.writestr("metadata.json", metadata, compress_type=zipfile.ZIP_DEFLATED)
                    
                QMessageBox.information(self.parent, "Success", f"Exported PDOC: {os.path.basename(file_path)}")
                
        except Exception as e:
            QMessageBox.critical(self.parent, "Error", f"Failed to export PDOC:\n{str(e)}")

    def _get_current_timestamp(self):
        """Get current timestamp in ISO format"""
        from datetime import datetime
        return datetime.now().isoformat()

    def reset_selectors(self):
        """Reset all combo box selections to default"""
        self.effect_combo.setCurrentIndex(0)
        self.font_combo.setCurrentIndex(0) 
        self.duration_combo.setCurrentIndex(0)

    def get_selected_values(self):
        """Get currently selected values from combo boxes"""
        effect = self.effect_combo.currentText()
        font = self.font_combo.currentText()
        duration = self.duration_combo.currentText()
        
        return {
            'effect': effect if not effect.startswith("Select") else None,
            'font': font if not font.startswith("Select") else None,
            'duration': duration if not duration.startswith("Duration") else None
        }