# Platon_pipeline_run
# 🌍 PLATON Exoplanet Atmosphere Pipeline (Custom Offline Setup)

This repository contains a fully working version of the PLATON atmospheric modeling tool modified to run with a local dataset — useful for systems with limited internet or reproducibility needs.

## 🔧 What’s Included

- Patched PLATON core (`_get_data.py`) to avoid re-downloading 10GB datasets.
- Scripts for transit depth calculation, eclipse modeling, and surface emission.
- Visualizer example to render transit views of exoplanets.
- Output plots and retrieval results.
- Local path configuration for Mac M1 compatibility.

## 📁 Directory Guide

| Folder/File     | Description |
|-----------------|-------------|
| `platon/`       | Source code (cloned or forked, with patches). |
| `data/`         | Pre-downloaded 10GB dataset (not included in repo). |
| `examples/`     | Modified examples for retrieval and visualization. |
| `tests/`        | Sanity check for data availability. |
| `outputs/`      | Sample figures generated. |

## ▶️ Quick Start

```bash
conda create -n platon_env python=3.9
conda activate platon_env
pip install -e ./platon
python examples/transit_depth_example.py
