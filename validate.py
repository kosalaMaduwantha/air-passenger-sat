#!/usr/bin/env python3
"""
Validation script for the Air Passenger Satisfaction Dashboard.
This script checks if all required files and dependencies are present.
"""
import os
import sys
from pathlib import Path


def check_file_exists(filepath, description):
    """Check if a file exists and report status."""
    if os.path.exists(filepath):
        print(f"✅ {description}: {filepath}")
        return True
    else:
        print(f"❌ {description} NOT FOUND: {filepath}")
        return False


def check_directory_exists(dirpath, description):
    """Check if a directory exists and report status."""
    if os.path.isdir(dirpath):
        print(f"✅ {description}: {dirpath}")
        return True
    else:
        print(f"❌ {description} NOT FOUND: {dirpath}")
        return False


def check_imports():
    """Check if all required packages can be imported."""
    print("\n📦 Checking Python packages...")
    
    required_packages = [
        ('dash', 'Dash'),
        ('dash_bootstrap_components', 'Dash Bootstrap Components'),
        ('plotly', 'Plotly'),
        ('pandas', 'Pandas'),
        ('pickle', 'Pickle'),
    ]
    
    all_imports_ok = True
    for package, name in required_packages:
        try:
            __import__(package)
            print(f"✅ {name} is installed")
        except ImportError:
            print(f"❌ {name} is NOT installed")
            all_imports_ok = False
    
    return all_imports_ok


def main():
    """Run all validation checks."""
    print("=" * 50)
    print("Air Passenger Satisfaction Dashboard - Validation")
    print("=" * 50)
    
    base_dir = Path(__file__).parent
    all_checks_passed = True
    
    print("\n📁 Checking project structure...")
    
    # Check main files
    files_to_check = [
        (base_dir / "src" / "index.py", "Main entry point"),
        (base_dir / "src" / "app.py", "App configuration"),
        (base_dir / "src" / "config" / "constants.py", "Constants file"),
        (base_dir / "src" / "utils" / "data_utils.py", "Data utilities"),
        (base_dir / "src" / "pages" / "classification.py", "Classification page"),
        (base_dir / "src" / "pages" / "pie_chart.py", "Pie chart page"),
        (base_dir / "src" / "models" / "Invistico_Airline_initial.sav", "Data file"),
        (base_dir / "requirements.txt", "Requirements file"),
        (base_dir / "Procfile", "Procfile"),
        (base_dir / "README.md", "README"),
    ]
    
    for filepath, description in files_to_check:
        if not check_file_exists(filepath, description):
            all_checks_passed = False
    
    # Check directories
    print("\n📂 Checking directories...")
    dirs_to_check = [
        (base_dir / "src", "Source directory"),
        (base_dir / "src" / "config", "Config directory"),
        (base_dir / "src" / "utils", "Utils directory"),
        (base_dir / "src" / "pages", "Pages directory"),
        (base_dir / "src" / "models", "Models directory"),
        (base_dir / "src" / "assets", "Assets directory"),
    ]
    
    for dirpath, description in dirs_to_check:
        if not check_directory_exists(dirpath, description):
            all_checks_passed = False
    
    # Check imports
    if not check_imports():
        all_checks_passed = False
    
    # Try importing project modules
    print("\n🔍 Checking project modules...")
    try:
        sys.path.insert(0, str(base_dir))
        from src.config import constants
        print("✅ Can import src.config.constants")
        
        from src.utils import data_utils
        print("✅ Can import src.utils.data_utils")
        
        from src import app
        print("✅ Can import src.app")
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        all_checks_passed = False
    
    # Final report
    print("\n" + "=" * 50)
    if all_checks_passed:
        print("✅ All validation checks passed!")
        print("\nYou can start the application with:")
        print("  python src/index.py")
        print("or:")
        print("  ./start.sh")
    else:
        print("❌ Some validation checks failed!")
        print("\nPlease fix the issues above before running the application.")
        sys.exit(1)
    print("=" * 50)


if __name__ == "__main__":
    main()
