# ESS 563 Assignment 1: Synthetic Seismogram Generation

This repository contains a Jupyter notebook implementing synthetic seismogram generation using the Aki-Richards formulation for earthquake source modeling. The implementation addresses all requirements of ESS 563 Assignment 1.

## Files in this Repository

- `synth-seismo.ipynb` - Main Jupyter notebook with complete implementation
- `config.json` - Configuration file containing all simulation parameters
- `config_setup.py` - Python module for loading configuration data

## Overview

The notebook implements a comprehensive seismological modeling framework that generates synthetic seismograms for earthquake sources using the Aki-Richards formulation. It includes both theoretical displacement calculations and array-based strain analysis.

## Key Features

### Part A: Theoretical Displacement Seismogram
- **Brune-type source time function**: Implements `m'(t)` with configurable corner frequency
- **Fault mechanics**: Full strike/dip/rake parameterization for double-couple sources
- **Multi-field seismograms**: Near-field, intermediate-field, and far-field displacement terms
- **3-component output**: Complete P, SV, and SH wave displacement time series

### Part D: Source at Depth with General Moment Tensor
- **Arbitrary source positioning**: Sources placed at depth with horizontal offset
- **Double-couple and full tensor**: Support for both pure double-couple and general moment tensors
- **Bandwidth analysis**: Multiple corner frequency values to probe resolution limits

### Part E: Surface Arrays
- **Rectangular station grids**: Configurable aperture and station spacing
- **Displacement simulation**: Full 3-component ground motion at each station
- **Strain computation**: Theoretical strain tensor calculation

### Part F: Array-Derived Strain
- **Finite difference gradients**: Centered difference scheme for spatial derivatives
- **Symmetric strain tensor**: Proper strain tensor formation from displacement gradients
- **Performance analysis**: MSE-based comparison of theoretical vs. finite-difference strain

## Configuration Parameters

The `config.json` file contains all simulation parameters organized into logical groups:

### Elastic Constants
- **ρ (rho)**: 2700 kg/m³ - Crustal density
- **α (alpha)**: 6000 m/s - P-wave velocity  
- **β (beta)**: 3464 m/s - S-wave velocity

### Source Parameters
- **M₀**: 10¹⁵ N⋅m - Seismic moment
- **fc**: 2.0 Hz - Default corner frequency
- **zs**: 5000 m - Source depth

### Array Geometry
- **Basic arrays**: Fixed spacing/aperture combinations
- **Lambda-based arrays**: Wavelength-dependent configurations
- **Center position**: [15000, 0, 0] m from origin

### Simulation Parameters
- **dt**: 0.01 s - Time step
- **duration**: 10.0 s - Total simulation time
- **taper_length**: 1.0 s - Signal tapering

## Notebook Structure

1. **Setup and Configuration** - Parameter loading and validation
2. **Theoretical Functions** - Aki-Richards implementation
3. **Source Mechanics** - Strike/dip/rake and moment tensor handling  
4. **Seismogram Generation** - Multi-component displacement calculation
5. **Array Processing** - Station grid setup and data simulation
6. **Strain Analysis** - Theoretical and finite-difference strain comparison
7. **Performance Evaluation** - MSE analysis and optimization

## Key Algorithms

### Aki-Richards Formulation
The notebook implements the complete Aki-Richards equations for displacement due to a point source:

```
u(x,t) = (1/4πρ) * [Near-field + Intermediate-field + Far-field terms]
```

### Strain Tensor Calculation
Both theoretical (analytical) and numerical (finite-difference) strain tensors:

```
ε_ij = (1/2) * (∂u_i/∂x_j + ∂u_j/∂x_i)
```

### Performance Metrics
- **Mean Squared Error (MSE)**: Primary error metric
- **Correlation analysis**: Waveform similarity assessment
- **Optimization**: Best array configuration identification

## Usage

1. **Install dependencies**:
   ```bash
   pip install numpy matplotlib scipy pandas
   ```

2. **Run the notebook**:
   ```bash
   jupyter notebook synth-seismo.ipynb
   ```

3. **Modify parameters**: Edit `config.json` to change simulation parameters

4. **Execute cells sequentially**: The notebook is designed to run from top to bottom

## Results and Analysis

The notebook generates:
- **3-component seismograms** for various source-receiver configurations
- **Strain tensor time series** from both theoretical and finite-difference methods
- **Performance plots** showing MSE vs. array parameters
- **Optimal array configurations** for strain estimation

## Educational Value

This implementation serves as a comprehensive example of:
- Earthquake source modeling using elastodynamic theory
- Numerical seismology techniques
- Array seismology and strain analysis
- Scientific computing with Python

## Dependencies

- `numpy` - Numerical computing
- `matplotlib` - Plotting and visualization
- `scipy` - Scientific computing (signal processing, interpolation)
- `pandas` - Data analysis and manipulation

## Author

Created for ESS 563 - Earthquake Seismology  
Implementation based on Aki & Richards (2002) theoretical framework

## References

- Aki, K., & Richards, P. G. (2002). *Quantitative Seismology* (2nd ed.). University Science Books.
- Brune, J. N. (1970). Tectonic stress and the spectra of seismic shear waves from earthquakes. *Journal of Geophysical Research*, 75(26), 4997-5009.