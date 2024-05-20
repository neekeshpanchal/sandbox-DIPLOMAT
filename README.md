# DIPLOMAT

**Deep learning-based Identity Preserving Labeled-Object Multi-Animal Tracking**

---

### About

DIPLOMAT is a cutting-edge tool for multi-animal tracking that utilizes deep learning to preserve individual identities across frames. It integrates seamlessly with leading tracking frameworks like DeepLabCut and SLEAP. This tool distinguishes itself by processing confidence maps directly, which enhances the tracking accuracy over traditional peak detection methods.

<div style="display: flex; justify-content: space-between; gap: 20px; margin-bottom: 20px;">
    <img src="https://raw.githubusercontent.com/TravisWheelerLab/DIPLOMAT/main/docs/source/_static/imgs/example1.png" alt="Tracking 2 Degus" style="width: 48%;">
    <img src="https://raw.githubusercontent.com/TravisWheelerLab/DIPLOMAT/main/docs/source/_static/imgs/example2.png" alt="Tracking 3 Rats" style="width: 48%;">
</div>

<div>
    <img src="https://raw.githubusercontent.com/TravisWheelerLab/DIPLOMAT/main/docs/source/_static/imgs/UIDemo.png" alt="UI Demo" style="width: 100%; height: auto;">
    <figcaption>Interactive UI for precise tracking adjustments.</figcaption>
</div>

---

### Installation

**Prerequisites:** [Mamba](https://mamba.readthedocs.io/en/latest/installation/mamba-installation.html) with [Miniforge](https://github.com/conda-forge/miniforge).

<div style="background: #F9F9F9; padding: 10px; border-left: 5px solid #2B6CB0;">
    <h3>Environment Setup:</h3>
    <code>## DeepLabCut with GPU support<br>
    mamba env create -f https://raw.githubusercontent.com/TravisWheelerLab/DIPLOMAT/main/conda-environments/DIPLOMAT-DEEPLABCUT.yaml</code>
    <code>## DeepLabCut with CPU only<br>
    mamba env create -f https://raw.githubusercontent.com/TravisWheelerLab/DIPLOMAT/main/conda-environments/DIPLOMAT-DEEPLABCUT-CPU.yaml</code>
    <code>## SLEAP with GPU support<br>
    mamba env create -f https://raw.githubusercontent.com/TravisWheelerLab/DIPLOMAT/main/conda-environments/DIPLOMAT-SLEAP.yaml</code>
    <code>## SLEAP with CPU only<br>
    mamba env create -f https://raw.githubusercontent.com/TravisWheelerLab/DIPLOMAT/main/conda-environments/DIPLOMAT-SLEAP-CPU.yaml</code>
</div>

<div style="background: #E2E8F0; padding: 10px; border-left: 5px solid #2C7A7B;">
    <h3>Activation:</h3>
    <code>mamba activate DIPLOMAT-DEEPLABCUT</code><br>
    <code>mamba activate DIPLOMAT-SLEAP</code>
</div>

> [Full Installation Guide](https://diplomat.readthedocs.io/en/latest/installation.html)

---

### Usage

<div style="background: #FFF5F5; padding: 10px; border-left: 5px solid #C53030;">
    <h3>Tracking and Annotation Commands:</h3>
    <code>diplomat track -c path/to/config -v path/to/video</code> <!-- Track without UI --><br>
    <code>diplomat track_and_interact -c path/to/config -v path/to/video</code> <!-- Track with interactive UI --><br>
    <code>diplomat annotate -c path/to/config -v path/to/video</code> <!-- Annotate video --><br>
    <code>diplomat interact -s path/to/ui_state.dipui</code> <!-- Reopen UI for major modifications --><br>
    <code>diplomat tweak -c path/to/config -v path/to/video</code> <!-- Minor tweaks to tracking -->
</div>

> [Documentation and Basic Usage](https://diplomat.readthedocs.io/en/latest/basic_usage.html)

---

### Support

<div style="background: #EBF8FF; padding: 10px; border-left: 5px solid #3182CE;">
    <h3>Get Help:</h3>
    <code>diplomat --help</code><br>
    <code>diplomat track --help</code><br>
    <code>diplomat predictors --help</code>
</div>

<div style="background: #F7FAFC; padding: 10px

; border-left: 5px solid #CBD5E0;">
    <h3>Development and Contributions:</h3>
    For those interested in contributing, refer to the [Development Usage](https://diplomat.readthedocs.io/en/latest/advanced_usage.html#development-usage) guide. Feel free to submit pull requests or reach out directly to Isaac Robinson via email.
</div>

---

### License and Authors

<div style="background: #EDF2F7; padding: 10px; border-left: 5px solid #E2E8F0;">
    <h3>License:</h3>
    Available in the project's [LICENSE](#) file.
</div>

<div style="background: #FAF5FF; padding: 10px; border-left: 5px solid #D6BCFA;">
    <h3>Team:</h3>
    A comprehensive list of contributors can be found in the project's [AUTHORS](#) file. For inquiries, contact [Isaac Robinson](mailto:isaac.k.robinson2000@gmail.com).
</div>

---

**Note:** DIPLOMAT is currently in alpha; it may exhibit minor bugs and usability issues.
