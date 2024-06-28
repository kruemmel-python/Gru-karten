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
- [gui_component.py auf GitHub](https://github.com/kruemmel-python/Gru-karten/gui_component.py)

## Beitrag

Beiträge sind willkommen! Bitte öffnen Sie ein Issue oder reichen Sie einen Pull-Request mit Ihren Änderungen ein.

## Kontakt

Für Anfragen bezüglich dieser Anwendung oder der Nutzung von PySide6, kontaktieren Sie bitte:

Ralf Krümmel
