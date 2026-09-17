#!/usr/bin/env python3
"""
tools/export_web_index.py
Compiles certified instrument data and plate definitions into a unified 
JSON payload for 'The Untuned Ordinal Zero Index' interactive web canvas.
"""

import json
import os
import sys

# Ensure local repo modules can be reached
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def compile_master_index():
    print("Initializing The Untuned Ordinal Zero Index compilation pipeline...")

    # Root tree structure representing the Singularity (Macro-view)
    master_tree = {
        "meta": {
            "title": "The Untuned Ordinal Zero Index",
            "version": "1.6",
            "benchmark": "E=0 geometric closure",
            "philosophy": "Discrete coordinate vectors across a higher-dimensional manifold"
        },
        "singularity": {
            "id": "root-singularity",
            "name": "Meta-Index Root",
            "coordinates": "D = 4 ... 11",
            "closure_status": "E=0",
            "description": "High-dimensional macro-view and spacetime metric closure point.",
            "children": []
        }
    }

    # 1. The Channel Index (channels.py)
    # Extracted from spectra.py, holding 209 distinct channel shapes.
    channels_node = {
        "id": "channels",
        "name": "The Channel Index",
        "instrument": "channels.py",
        "arity": 3,
        "total_cells": 209,
        "description": "Spectroscopic channel shapes governed by orbital angular momentum (l), Pauli bound (B), and multiplicity (mult).",
        "coordinates_def": {
            "l": {"what": "orbital angular momentum", "values": [0,1,2,3,4,5,6,7]},
            "B": {"what": "Pauli bound", "values": [0,1,2,3,4,5,6,7]},
            "mult": {"what": "multiplicity", "values": [1,2,3,4,5,6,7,8,9]}
        },
        "sample_cell": {"l": 0, "B": 16, "mult": 24},
        "verdicts": {
            "order": "does not close",
            "algebra": "does not close",
            "geometry": "does not close",
            "information": "does not close",
            "statistics": "does not close"
        }
    }
    master_tree["singularity"]["children"].append(channels_node)

    # 2. Higher-Dimensional Gravity Plate (gravity.py)
    gravity_node = {
        "id": "gravity",
        "name": "Higher-Dimensional Metric & Gravity Index",
        "instrument": "gravity.py",
        "description": "Evaluates ultraspinning thresholds and metric distortions across D >= 6 dimensions.",
        "closure_status": "Conditional closure under extreme spin parameters"
    }
    master_tree["singularity"]["children"].append(gravity_node)

    # 3. Nuclear Shell & Superheavy / Eka-Matrix Plate (nucshell.py)
    nuclear_node = {
        "id": "nucshell",
        "name": "Nuclear Subshell & Eka-Matrix Predictor",
        "instrument": "nucshell.py",
        "description": "Maps magic numbers (N = 184) and superheavy stability corridors (e.g., Z = 115 / Moscovium isomers).",
        "target_coordinates": {"Z": 115, "N": 184, "isotope": "299-Mc"}
    }
    master_tree["singularity"]["children"].append(nuclear_node)

    # 4. Additional Plates (fibred.py, madrule.py, terms.py)
    support_plates = [
        {"id": "fibred", "name": "Fibred Lattice Index", "instrument": "fibred.py"},
        {"id": "madrule", "name": "Madelung Exception Registry", "instrument": "madrule.py"},
        {"id": "terms", "name": "Russell-Saunders Term Manifolds", "instrument": "terms.py"}
    ]
    for plate in support_plates:
        master_tree["singularity"]["children"].append(plate)

    # Output path for frontend consumption
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../public'))
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'master_index.json')

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(master_tree, f, indent=2)

    print(f"Successfully compiled Master Index payload to: {output_path}")

if __name__ == '__main__':
    compile_master_index()
