# AFM-CV-CA MeasurementApp

**A PyQt5 application combining AFM, CV, and CA modules in a tabbed interface**

---

## Overview

This project provides a unified GUI front-end for Atomic Force Microscopy (AFM) scanning, Cyclic Voltammetry (CV), and Chronoamperometry (CA) measurements. It leverages the API developed by Marcos Penedo (RePySPM) with custom extensions, and combines three separate GUI modules into a single tabbed application.

### Key Points

- **Core API**: Based on Marcos Penedo’s RePySPM library for AFM control and data acquisition.
- **Custom Extensions**: Additional functions built on top of the RePySPM system to support application-specific workflows.
- **Three GUI Modules**:
  1. **Main**: Scanning parameters, scan mode selection, auto-save controls, and real-time status.
  2. **CV Module**: Cyclic voltammetry parameters and real-time CV plots.
  3. **CA Module**: Chronoamperometry parameters, step sequences, and real-time CA plots.
- **Design Workflow**:
  - The *Main* GUI layout was designed in Qt Designer inside the `maintab_gui` folder. Functional connections were implemented in `lnet_main.py`.
  - The CV and CA GUIs combine both layout and logic in single Python modules (`CVp2p.py`, `CAp2p.py`).
  - A `gui_main.py` file defines the tabbed container (three tabs). The final `main.py` instantiates each GUI into its respective tab.
  - All windows are designed to be resizable (stretchable) for a flexible user experience.

---

## Project Structure

```
TabbedMeasurementApp/
├─ main.py              # Entry script: instantiates tabs and runs QApplication
├─ gui_main.py          # Qt Designer–generated tab container UI
├─ CVp2p.py             # CV tab: UI + logic
├─ CAp2p.py             # CA tab: UI + logic
├─ lnet_main.py         # Main tab: UI hooks for AFM operations
├─ setup.py             # Dependency installer and script installer
├─ README.md            # This file
└─ external_libs/       # (Optional) RePySPM and other external libraries
```

> **Note:** External dependencies (RePySPM, EC-LAB packages) are not hosted in this repo. Using `setup.py` with `pip install .` will automatically install PyPI dependencies; external libraries must be installed manually or via their own install scripts when cloning.

---

## Installation

1. **Clone the repository**:

   ```bash
   git clone <repository_url>
   cd TabbedMeasurementApp
   ```

2. **Create and activate a virtual environment** (recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate    # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install --upgrade pip
   pip install .
   ```

   This will install:

   - `PyQt5>=5.15,<6.0`
   - `matplotlib>=3.6`
   - `numpy>=1.24`

   If any dependency fails to install, you may need to install it manually:

   ```bash
   pip install <package_name>
   ```

4. **Install external libraries**:

   - **RePySPM**: THe original repo is [RePySPM GitHub](https://github.com/marcospenedo/RePySPM) but some functions are redesigned and also new functions are defined. Therefore, the updated version is given as a folder.
   - **EC-LAB Development Package**: Place its Python examples (e.g. in `external_libs/`) or set `PYTHONPATH` accordingly.

---

## Usage

After installation, launch the application:

```bash
python main.py
```

or, if you configured `entry_points` in `setup.py`, simply:

```bash
main-app
```

The GUI will open with three tabs:

1. **Main Tab**: Select scan parameters (width, height, pixels, speed), scan mode (TopDown, DownUp, Bouncing), auto-save options, and monitor real-time status.
2. **CV Tab**: Configure cyclic voltammetry parameters and view live CV plots at each pixel.
3. **CA Tab**: Define chronoamperometry step sequences, configure acquisition rate, and view live CA traces.

### Temporary UI Notes

- Some buttons and controls in the Main tab are currently disabled (greyed out) for development. These can be activated by implementing or enabling their callback functions.
- In the Saving section, file path and file name configuration via Python may conflict with LabVIEW cross‑checks. For full compatibility, handling of path and file naming in LabVIEW is recommended when using both systems together.

---

## User Manual

Welcome to LNET. Please follow the steps below carefully to initialize and operate the application:

1. Close all open LabVIEW files (verify both LabVIEW versions are closed).
2. Launch LabVIEW 2022 manually.
3. Open the OpenSPM Project located in the C module (not the D module).
4. Run `menu.vi`.
5. From within `menu.vi`, open both the LV Bridge and Z Scan modules.
6. Finally, run the Python script to begin operation (`python main.py`).

> **Support:** If you encounter unexpected behavior or errors, please contact:
>
> - German Garcia Martinez: [german.garciamartinez@epfl.ch](mailto\:german.garciamartinez@epfl.ch)
> - Osman Ornek: [osman.ornek@epfl.ch](mailto\:osman.ornek@epfl.ch)

---

## Benefits of This Design

- **Python Flexibility**: Easy customization, rapid development, and rich plotting via Matplotlib.
- **LabVIEW Cross‑Check**: Running the same operations in LabVIEW and Python ensures measurement reliability and validation.

## License

This project is licensed under the MIT License © Osman Ornek

