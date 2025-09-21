import sys, os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPlainTextEdit
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from ptxt_parser import parse_ptxt
from toolbar import ToolBarManager
from util import resource_path  # ✅ use resource_path for PyInstaller


class PreviewWindow(QWidget):
    def __init__(self, html_content, template_path):
        super().__init__()
        self.setWindowTitle("PTEXTOR Preview")
        self.setGeometry(150, 150, 900, 600)
        
        # Set window icon
        icon_path = resource_path("assets/PTEXTOR.ico")
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.webview = QWebEngineView()
        layout.addWidget(self.webview)

        # Load HTML with content
        try:
            with open(template_path, "r", encoding="utf-8") as f:
                template = f.read()
            
            # Replace the placeholder with actual content
            final_html = template.replace("<!--CONTENT-->", html_content)
            
            # Set base URL for proper resource loading
            base_url = QUrl.fromLocalFile(os.path.dirname(template_path) + "/")
            self.webview.setHtml(final_html, base_url)
            
        except Exception as e:
            print(f"Error loading template: {e}")
            # Fallback HTML
            fallback_html = f"""
            <!DOCTYPE html>
            <html><head><title>Error</title></head>
            <body>
            <h2>Template Error</h2>
            <p>Could not load template. Raw content:</p>
            <pre>{html_content}</pre>
            </body></html>
            """
            self.webview.setHtml(fallback_html)


class PTextor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PTEXTOR")
        self.setGeometry(100, 100, 1000, 700)
        
        # Set application icon
        self.icon_path = resource_path("assets/PTEXTOR.ico")
        if os.path.exists(self.icon_path):
            self.setWindowIcon(QIcon(self.icon_path))

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # Editor
        self.editor = QPlainTextEdit()
        self.editor.setPlaceholderText(
            "Enter your text here...\n\n"
            "Use tags like:\n"
            "[effect=fade-in duration=2000]\n"
            "Your text here\n\n"
            "[font name=Arial]\n"
            "Text with custom font"
        )
        main_layout.addWidget(self.editor)

        # ✅ Always use resource_path for template.html
        self.template_path = resource_path("src/template.html")
        
        if not os.path.exists(self.template_path):
            print(f"Warning: Template not found at {self.template_path}")

        # Track preview window for proper cleanup
        self.preview_window = None

        # Toolbar Manager
        self.toolbar_manager = ToolBarManager(
            parent=self,
            editor=self.editor,
            template_path=self.template_path,
            preview_callback=self.show_preview
        )
        main_layout.insertLayout(0, self.toolbar_manager.layout)

    def show_preview(self):
        try:
            # Close existing preview window
            if self.preview_window:
                self.preview_window.close()
                
            text = self.editor.toPlainText()
            if not text.strip():
                text = "No content to preview"
                
            html_content = parse_ptxt(text, self.template_path)
            self.preview_window = PreviewWindow(html_content, self.template_path)
            self.preview_window.show()
            
        except Exception as e:
            print(f"Error showing preview: {e}")

    def closeEvent(self, event):
        """Clean up when main window closes"""
        if self.preview_window:
            self.preview_window.close()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Set application icon globally
    icon_path = resource_path("assets/PTEXTOR.ico")
    if os.path.exists(icon_path):
        app.setWindowIcon(QIcon(icon_path))
    
    window = PTextor()
    window.show()
    sys.exit(app.exec_())
