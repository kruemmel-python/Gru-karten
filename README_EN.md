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



