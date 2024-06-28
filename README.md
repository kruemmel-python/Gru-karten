# Grußkarten-Generator

Der Grußkarten-Generator ist eine Python-Anwendung, die es Benutzern ermöglicht, anpassbare Grußkarten zu erstellen. Die Anwendung bietet verschiedene Designoptionen, einschließlich textbasierter Designs, Rahmen sowie Sterne und Wolken. Benutzer können die Hintergrundfarbe, Schriftfarbe, Rahmentyp und mehr anpassen.

## Funktionen

- **Textbasierte Designs**: Erstellen Sie Grußkarten mit anpassbarem Text, Schriftart, Größe und Ausrichtung.
- **Rahmen**: Wählen Sie aus verschiedenen Rahmentypen (gerade, zickzack, wellenförmig, geschlungen) und passen Sie die Rahmenfarbe und den Schatten an.
- **Sterne und Wolken**: Fügen Sie Sterne und Wolken zu Ihrem Grußkartendesign hinzu.
- **Vorschau**: Vorschau der Grußkarte vor der endgültigen Erstellung.
- **Anpassung**: Passen Sie die Hintergrundfarbe, Schriftfarbe und mehr an.

## Installation

1. **Repository klonen**:

   ```sh
   git clone https://github.com/kruemmel-python/Gru-karten
   cd greeting-card-generator
   ```

2. **Erforderliche Abhängigkeiten installieren**:

   ```sh
   pip install -r requirements.txt
   ```

3. **`gui_component.py` mit Cython bauen**:

   Erstellen Sie eine `setup.py`-Datei mit folgendem Inhalt:

   ```python
   from setuptools import setup, Extension
   from Cython.Build import cythonize

   extensions = [
       Extension("gui_component", ["gui_component.py"]),
   ]

   setup(
       name="GreetingCardApp",
       ext_modules=cythonize(extensions, compiler_directives={'language_level': "3"}),
   )
   ```

   Führen Sie den folgenden Befehl aus, um die Erweiterung zu bauen:

   ```sh
   python setup.py build_ext --inplace
   ```

4. **Erstellen Sie die ausführbare Datei mit PyInstaller**:

   Erstellen Sie eine `main.spec`-Datei mit folgendem Inhalt:

   ```python
   # -*- mode: python ; coding: utf-8 -*-

   block_cipher = None

   a = Analysis(
       ['main.py'],
       pathex=[],
       binaries=[('gui_component.*.pyd', '.')],
       datas=[('LICENSE.txt', '.')],
       hiddenimports=[],
       hookspath=[],
       runtime_hooks=[],
       excludes=[],
       win_no_prefer_redirects=False,
       win_private_assemblies=False,
       cipher=block_cipher,
   )
   pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
   exe = EXE(
       pyz,
       a.scripts,
       [],
       exclude_binaries=True,
       name='main',
       debug=False,
       bootloader_ignore_signals=False,
       strip=False,
       upx=True,
       upx_exclude=[],
       runtime_tmpdir=None,
       console=True,
   )
   coll = COLLECT(
       exe,
       a.binaries,
       a.zipfiles,
       a.datas,
       strip=False,
       upx=True,
       upx_exclude=[],
       name='main',
   )
   ```

   Führen Sie den folgenden Befehl aus, um die ausführbare Datei zu erstellen:

   ```sh
   pyinstaller main.spec
   ```

## Nutzung

1. **Starten Sie die Anwendung**:

   ```sh
   python main.py
   ```

2. **Erstellen Sie eine Grußkarte**:
   - Geben Sie den Grußtext ein.
   - Wählen Sie die Schriftart, Schriftgröße und Schriftfarbe.
   - Wählen Sie die Textausrichtung.
   - Wählen Sie das Design (textbasiert, Rahmen oder Sterne und Wolken).
   - Passen Sie die Hintergrundfarbe an.
   - Vorschau der Karte und ggf. Anpassungen vornehmen.
   - Erstellen Sie das endgültige Bild.

## Lizenzierung

Diese Anwendung verwendet PySide6, das unter der GNU Lesser General Public License Version 3 (LGPLv3) lizenziert ist.

Für weitere Informationen über PySide6 und dessen Lizenzierung, besuchen Sie bitte:
- Die Seite der Qt Company zu PySide6: [Qt for Python](https://www.qt.io/qt-for-python)
- PySide6 GitHub-Repository: [PySide6 auf GitHub](https://github.com/qt/qt5/tree/pyside6)

Der Quellcode für die in dieser Anwendung verwendete `gui_component.py` ist verfügbar unter:
- [gui_component.py auf GitHub](https://github.com/kruemmel-python/Gru-karten/blob/main/gui_component.py)

## Beitrag

Beiträge sind willkommen! Bitte öffnen Sie ein Issue oder reichen Sie einen Pull-Request mit Ihren Änderungen ein.

## Kontakt

Für Anfragen bezüglich dieser Anwendung oder der Nutzung von PySide6, kontaktieren Sie bitte:

Ralf Krümmel





# Greeting Card Generator

Greeting Card Generator is a Python application that allows users to create customizable greeting cards. The application provides various design options, including text-based designs, frames, and stars and clouds. Users can customize the background color, font color, frame type, and more.

## Features

- **Text-based Designs**: Create greeting cards with customizable text, font, size, and alignment.
- **Frames**: Choose from different frame types (straight, zigzag, wavy, looped) and customize the frame color and shadow.
- **Stars and Clouds**: Add stars and clouds to your greeting card design.
- **Preview**: Preview the greeting card before creating the final image.
- **Customization**: Customize the background color, font color, and more.

## Installation

1. **Clone the repository**:

   ```sh
   git clone https://github.com/kruemmel-python/Gru-karten
   cd greeting-card-generator
   ```

2. **Install the required dependencies**:

   ```sh
   pip install -r requirements.txt
   ```

3. **Build the `gui_component.py` using Cython**:

   Create a `setup.py` file with the following content:

   ```python
   from setuptools import setup, Extension
   from Cython.Build import cythonize

   extensions = [
       Extension("gui_component", ["gui_component.py"]),
   ]

   setup(
       name="GreetingCardApp",
       ext_modules=cythonize(extensions, compiler_directives={'language_level': "3"}),
   )
   ```

   Run the following command to build the extension:

   ```sh
   python setup.py build_ext --inplace
   ```

4. **Create the executable using PyInstaller**:

   Create a `main.spec` file with the following content:

   ```python
   # -*- mode: python ; coding: utf-8 -*-

   block_cipher = None

   a = Analysis(
       ['main.py'],
       pathex=[],
       binaries=[('gui_component.*.pyd', '.')],
       datas=[('LICENSE.txt', '.')],
       hiddenimports=[],
       hookspath=[],
       runtime_hooks=[],
       excludes=[],
       win_no_prefer_redirects=False,
       win_private_assemblies=False,
       cipher=block_cipher,
   )
   pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
   exe = EXE(
       pyz,
       a.scripts,
       [],
       exclude_binaries=True,
       name='main',
       debug=False,
       bootloader_ignore_signals=False,
       strip=False,
       upx=True,
       upx_exclude=[],
       runtime_tmpdir=None,
       console=True,
   )
   coll = COLLECT(
       exe,
       a.binaries,
       a.zipfiles,
       a.datas,
       strip=False,
       upx=True,
       upx_exclude=[],
       name='main',
   )
   ```

   Run the following command to create the executable:

   ```sh
   pyinstaller main.spec
   ```

## Usage

1. **Run the application**:

   ```sh
   python main.py
   ```

2. **Create a greeting card**:
   - Enter the greeting text.
   - Select the font, font size, and font color.
   - Select the text alignment.
   - Choose the design (text-based, frame, or stars and clouds).
   - Customize the background color.
   - Preview the card and make adjustments as needed.
   - Create the final image.

## Licensing

This application uses PySide6, which is licensed under the GNU Lesser General Public License version 3 (LGPLv3).

For more information about PySide6 and its licensing, please visit:
- The Qt Company's PySide6 page: [Qt for Python](https://www.qt.io/qt-for-python)
- PySide6 GitHub repository: [PySide6 on GitHub](https://github.com/qt/qt5/tree/pyside6)

The source code for the `gui_component.py` used in this application is available at:
- [gui_component.py on GitHub](https://github.com/kruemmel-python/Gru-karten/gui_component.py)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with your changes.

## Contact

For any inquiries regarding this application or the use of PySide6, please contact:

Ralf Krümmel  


