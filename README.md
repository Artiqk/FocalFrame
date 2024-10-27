# Focal Frame Calculator

## Overview

The **Focal Frame Calculator** is a desktop application developed using PySide6 that allows users to calculate and visualize the angles and frame dimensions based on camera specifications. It supports different sensor formats and provides a user-friendly interface for quick calculations. 

### Features
- Input focal length in mm.
- Select sensor formats from a dropdown list.
- Enter the distance in meters.
- Automatically calculates and displays:
  - Horizontal and vertical angles in degrees.
  - Frame width and height in meters.
  
## Requirements

To run the application, you need the following Python packages:

- `PySide6==6.8.0.2`
- `PySide6_Addons==6.8.0.2`
- `PySide6_Essentials==6.8.0.2`
- `shiboken6==6.8.0.2`

You can find the complete list of dependencies in the `requirements.txt` file.

## Installation

1. **Clone the repository**:
```bash
git clone https://github.com/yourusername/focal-frame-calculator.git
cd focal-frame-calculator
```

2. **Create a virtual environment (optional but recommended)**:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. **Install the required packages**:
```bash
pip install -r requirements.txt
```

4. **Run the application**:
```bash
python main.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.