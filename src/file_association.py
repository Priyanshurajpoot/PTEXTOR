import winreg
import os
import sys
from util import resource_path  # Added for PyInstaller bundled paths

class FileAssociationManager:
    """Manages file associations for PTEXTOR custom file types"""

    def __init__(self):
        if getattr(sys, 'frozen', False):
            self.app_path = sys.executable
            self.command_template = f'"{self.app_path}" "%1"'
        else:
            project_dir = os.path.dirname(__file__)
            main_py = os.path.join(project_dir, "main.py")
            self.app_path = main_py
            self.command_template = f'"{sys.executable}" "{self.app_path}" "%1"'

        self.assets_path = resource_path("assets")

    def register_file_types(self):
        try:
            self._register_extension(
                extension=".ptxt",
                file_type="PTEXTOR.ptxt",
                description="PTEXTOR Text File",
                icon_name="ptxt.ico",
                verb="open",
                verb_description="Open with PTEXTOR"
            )
            self._register_extension(
                extension=".pdoc",
                file_type="PTEXTOR.pdoc",
                description="PTEXTOR Document Package",
                icon_name="pdoc.ico",
                verb="open",
                verb_description="Open with PTEXTOR"
            )
            print("File associations registered successfully!")
            return True
        except Exception as e:
            print(f"Error registering file types: {e}")
            return False

    def _register_extension(self, extension, file_type, description, icon_name, verb, verb_description):
        icon_path = resource_path(f"assets/{icon_name}")
        if not os.path.exists(icon_path):
            print(f"Warning: Icon not found at {icon_path}")
            icon_path = resource_path("assets/PTEXTOR.ico")

        ext_key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, extension)
        winreg.SetValue(ext_key, "", winreg.REG_SZ, file_type)
        winreg.CloseKey(ext_key)

        type_key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, file_type)
        winreg.SetValue(type_key, "", winreg.REG_SZ, description)
        winreg.CloseKey(type_key)

        icon_key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, f"{file_type}\\DefaultIcon")
        winreg.SetValue(icon_key, "", winreg.REG_SZ, f'"{icon_path}",0')
        winreg.CloseKey(icon_key)

        shell_key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, f"{file_type}\\shell")
        winreg.CloseKey(shell_key)

        open_key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, f"{file_type}\\shell\\{verb}")
        winreg.SetValue(open_key, "", winreg.REG_SZ, verb_description)
        winreg.CloseKey(open_key)

        command_key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, f"{file_type}\\shell\\{verb}\\command")
        winreg.SetValue(command_key, "", winreg.REG_SZ, self.command_template)
        winreg.CloseKey(command_key)

    def unregister_file_types(self):
        try:
            self._unregister_extension(".ptxt", "PTEXTOR.ptxt")
            self._unregister_extension(".pdoc", "PTEXTOR.pdoc")
            print("File associations unregistered successfully!")
            return True
        except Exception as e:
            print(f"Error unregistering file types: {e}")
            return False

    def _unregister_extension(self, extension, file_type):
        try:
            winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, extension)
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"Error removing extension {extension}: {e}")

        try:
            self._delete_key_recursively(winreg.HKEY_CLASSES_ROOT, file_type)
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"Error removing file type {file_type}: {e}")

    def _delete_key_recursively(self, hkey, key_path):
        try:
            key = winreg.OpenKey(hkey, key_path, 0, winreg.KEY_ALL_ACCESS)
        except FileNotFoundError:
            return

        while True:
            try:
                subkey_name = winreg.EnumKey(key, 0)
                self._delete_key_recursively(key, subkey_name)
                winreg.DeleteKey(key, subkey_name)
            except OSError:
                break

        winreg.CloseKey(key)
        winreg.DeleteKey(hkey, key_path)

    def check_associations(self):
        associations = {}
        for ext, file_type in [(".ptxt", "PTEXTOR.ptxt"), (".pdoc", "PTEXTOR.pdoc")]:
            try:
                key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, ext)
                value, _ = winreg.QueryValueEx(key, "")
                associations[ext] = value == file_type
                winreg.CloseKey(key)
            except FileNotFoundError:
                associations[ext] = False
            except Exception as e:
                print(f"Error checking {ext}: {e}")
                associations[ext] = False
        return associations


def main():
    if len(sys.argv) < 2:
        print("Usage: python file_association.py [register|unregister|check]")
        return

    manager = FileAssociationManager()
    command = sys.argv[1].lower()

    if command == "register":
        manager.register_file_types()
    elif command == "unregister":
        manager.unregister_file_types()
    elif command == "check":
        associations = manager.check_associations()
        for ext, status in associations.items():
            status_str = "✓ Registered" if status else "✗ Not registered"
            print(f"  {ext}: {status_str}")
    else:
        print("Invalid command. Use: register, unregister, or check")


if __name__ == "__main__":
    main()
