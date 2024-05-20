# DIPLOMAT

**Deep learning-based Identity Preserving Labeled-Object Multi-Animal Tracking**

---

### About

DIPLOMAT is an advanced multi-animal tracking software that leverages the power of deep learning to maintain individual identities across various environments. It integrates seamlessly with major tracking packages like DeepLabCut and SLEAP, offering a sophisticated yet user-friendly solution for researchers. By utilizing confidence maps rather than traditional peak detection methods, DIPLOMAT ensures more accurate and nuanced tracking results.

<div style="display: flex; justify-content: space-between; align-items: center;">
    <img src="https://raw.githubusercontent.com/TravisWheelerLab/DIPLOMAT/main/docs/source/_static/imgs/example1.png" alt="Tracking 2 Degus" width="45%">
    <img src="https://raw.githubusercontent.com/TravisWheelerLab/DIPLOMAT/main/docs/source/_static/imgs/example2.png" alt="Tracking 3 Rats" width="45%">
</div>

<figure>
    <img src="https://raw.githubusercontent.com/TravisWheelerLab/DIPLOMAT/main/docs/source/_static/imgs/UIDemo.png" alt="UI Demo">
    <figcaption>Interactive UI for precise tracking adjustments.</figcaption>
</figure>

---

### Installation

**Prerequisites:** [Mamba](https://mamba.readthedocs.io/en/latest/installation/mamba-installation.html) with [Miniforge](https://github.com/conda-forge/miniforge).

**Environment Setup:**

```bash
# For DeepLabCut with GPU support
mamba env create -f https://raw.githubusercontent.com/TravisWheelerLab/DIPLOMAT/main/conda-environments/DIPLOMAT-DEEPLABCUT.yaml

# For DeepLabCut with CPU only
mamba env create -f https://raw.githubusercontent.com/TravisWheelerLab/DIPLOMAT/main/conda-environments/DIPLOMAT-DEEPLABCUT-CPU.yaml

# For SLEAP with GPU support
mamba env create -f https://raw.githubusercontent.com/TravisWheelerLab/DIPLOMAT/main/conda-environments/DIPLOMAT-SLEAP.yaml

# For SLEAP with CPU only
mamba env create -f https://raw.githubusercontent.com/TravisWheelerLab/DIPLOMAT/main/conda-environments/DIPLOMAT-SLEAP-CPU.yaml
```

**Activation:**

```bash
mamba activate DIPLOMAT-DEEPLABCUT
# or
mamba activate DIPLOMAT-SLEAP
```

> [Full Installation Guide](https://diplomat.readthedocs.io/en/latest/installation.html)

---

### Usage

**Tracking and Annotation:**

```bash
# Track without UI
diplomat track -c path/to/config -v path/to/video

# Track with interactive UI
diplomat track_and_interact -c path/to/config -v path/to/video

# Annotate video
diplomat annotate -c path/to/config -v path/to/video

# Reopen UI for major modifications
diplomat interact -s path/to/ui_state.dipui

# Minor tweaks to tracking
diplomat tweak -c path/to/config -v path/to/video
```

> [Documentation and Basic Usage](https://diplomat.readthedocs.io/en/latest/basic_usage.html)

---

### Support

**Get Help:**

```bash
diplomat --help
diplomat track --help
diplomat predictors --help
```

**Development and Contributions:**

Interested in contributing? Please see the [Development Usage](https://diplomat.readthedocs.io/en/latest/advanced_usage.html#development-usage) guide and feel free to submit pull requests or reach out directly to Isaac Robinson via email.

---

### License and Authors

**License:** Available in the project's [LICENSE](#) file.

**Team:** A comprehensive list of contributors can be found in the project's [AUTHORS](#) file. For inquiries, contact [Isaac Robinson](mailto:isaac.k.robinson2000@gmail.com).

---

**Note:** DIPLOMAT is currently in alpha; it may exhibit minor bugs and usability issues.
