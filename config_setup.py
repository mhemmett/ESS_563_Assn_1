"""This notebook manages configuration files for the ESS563 Assignment 1 notebook. The configuration includes elastic constants, source parameters, array geometry, and analysis settings.
By: Michael Hemmett"""

# Import required libraries
import json
import os
import numpy as np
from pathlib import Path

# Load configuration from JSON file
def load_config(file_path):
    """Load configuration from JSON file."""
    try:
        with open(file_path, 'r') as f:
            config_data = json.load(f)
        print(f"✓ Configuration loaded from: {file_path}")
        return config_data
    except FileNotFoundError:
        print(f"✗ Configuration file not found: {file_path}")
        return None
    except json.JSONDecodeError as e:
        print(f"✗ Error parsing JSON file: {e}")
        return None
    except Exception as e:
        print(f"✗ Error loading configuration: {e}")
        return None