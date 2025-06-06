# Project1_Systems

# Parker Solar Probe FPGA Electronic Design

## Overview

NASA's **Parker Solar Probe** mission uses electronic components specifically designed to withstand the extreme conditions near the Sun, including intense radiation and high temperatures.

## FPGA Design

- The mission employs **radiation-hardened (rad-hard) FPGAs** from the **Microsemi RTAX4000 family**, fabricated with a 0.15 μm process technology.
- These FPGAs feature **triply redundant flip-flops**, providing **Triple Modular Redundancy (TMR)** benefits without the usual overhead.
- An **internal scrubber** is included to detect and correct potential errors in the SRAM memory.
- The FPGAs use a **metal-to-metal anti-fuse interconnect** configuration, which offers high resistance to ion impacts.

## Application in FIELDS Instrument

- The **FIELDS (Electric and Magnetic Field Investigation)** instrument uses RTAX4000 FPGAs on the **Digital Fields Board (DFB)**.
- These FPGAs process signals from electric and magnetic field sensors, converting digitized data into time-domain and spectral-domain products.
- A **32-bit ColdFire processor**, implemented on another RTAX4000 FPGA, controls the instrument, manages memory, and interfaces with the spacecraft.

## Technical Documentation and Resources

For detailed technical information about the mission's electronic design and FPGA use, consult the following:

- [Technical Article on Parker Solar Probe FPGAs - eejournal.com](https://www.eejournal.com/article/the-solar-systems-fastest-fpgas-journey-to-the-sun-carrying-a-microprocessor-relic-on-board/)
- [FIELDS Instrument Documentation - ssl.berkeley.edu](https://www.ssl.berkeley.edu/sun-heliophysics/psp-fields/)
- [NASA FPGA Insertion Guide - nepp.nasa.gov](https://nepp.nasa.gov/files/13656/07_101%20Sheldon%20JPL%20FPGA%20%28CL-08_1741%29.pdf)

## Summary

This design approach ensures robust FPGA operation in the harsh solar environment, leveraging advanced rad-hard technology, redundancy, and error correction mechanisms for reliable long-duration missions.

---

*Sources:*  
- jhuapl.edu  
- parkersolarprobe.jhuapl.edu  
- frontgrade.com  
- eejournal.com  
- sweap.cfa.harvard.edu  
- ssl.berkeley.edu  
- link.springer.com  
- nepp.nasa.gov

## 2. Propulsion System Design: Materials and Manufacturing Processes

### General Objective  
Create a propulsion system combining mechanical strength, thermal efficiency, and advanced metallic materials properties obtained through rolling and advanced manufacturing processes. The design is robust for withstanding high pressures, temperatures, and dynamic forces, suitable for demanding aerospace or industrial applications.

### Materials and Processes Used  
- **Main material:** Titanium alloy reinforced with boron carbide and graphene nanoparticles for high strength and low weight.  
- **Initial Processing:**  
  - Hot rolling for basic parts (cylinders, discs, tubes).  
  - Shape rolling to form complex aerodynamic shapes (nozzles, housings, internal supports).  
  - Cold rolling for parts requiring high dimensional precision and surface finish (seals, contact surfaces).  
  - Heat treatments (hardening, annealing, aging) to optimize microstructure.  
  - Laser welding with atmosphere control to avoid embrittlement in critical joints.  
  - Aluminum nitride-based ceramic coatings for corrosion and thermal wear protection.  

### Main Components  
- **Combustion chamber and nozzle:**  
  Manufactured using shape rolling from reinforced alloy, designed for high pressure/temperature tolerance with variable cross-section for efficient gas flow and thrust control.  
- **Shaft and rotor:**  
  Constructed with shape-rolled tubes/bars, optimized for torque and high-speed rotation; central shaft precision-machined via cold rolling for tight tolerances and reduced friction.  
- **Integrated cooling system:**  
  Internal ducts made with shape-rolled tubes for coolant circulation, with thermal coatings to maintain structural integrity.  
- **Structural supports:**  
  Shape-rolled I-beams and reinforcement rings (ring rolling) for maximum rigidity and load distribution.  

### Future Innovations  
- Embedded sensors with microchannels for real-time thermal and vibration monitoring.  
- Modular design for rapid maintenance and part replacement; couplings designed by relief rolling.  
- Aerodynamic optimization via CFD simulations and post-machining to reduce turbulence and increase efficiency.  
- Adaptive lubrication and tensioning system controlled electronically for wear minimization.  

### Manufacturing Process Summary  
1. Selection and mixing of special alloys; continuous casting and ingot formation.  
2. Hot rolling for initial forming.  
3. Shape rolling for complex components (nozzles, rings, supports).  
4. Cold rolling for critical tolerance parts (shaft, seals).  
5. Heat treatments to optimize strength and ductility.  
6. Assembly via laser welding and dimensional control.  
7. Application of thermal/protective coatings.  
8. Sensor and electronic system integration.  
9. Non-destructive testing and final calibration.  

### Modeling and Implementation  
- Mechanical and thermal models designed in Python using PyCharm for development.  
- Electronic designs and small processors/sensors implemented using Microblaze and VHDL.  
- Documentation provided for sensor integration and satellite/spacecraft interfacing (Parker Solar Probe or similar).  

---

### Extrusion Processes Overview  

Three basic extrusion types:  

- **Direct (forward) extrusion:**  
  Billet placed in chamber, forced through die by piston. Die shape defines extrudate profile. Dummy block protects press rod.  
- **Indirect (inverted/retro) extrusion:**  
  Die moves toward billet.  
- **Hydrostatic extrusion:**  
  Billet in fluid-filled chamber, pressure applied by piston; billet stationary relative to chamber, minimizing friction.  
- **Lateral (side) extrusion:** Less common variant.  

### Extrusion Process Variables  
- Die angle, cross-sectional area reduction, extrusion speed, billet temperature, lubrication affect extrusion pressure and force.  
- Extrusion force \(F\) estimated by:  
  \[
  F = k \cdot A_0 \cdot \ln\left(\frac{A_0}{A_f}\right)
  \]
  Where:  
  - \(k\) = extrusion constant (experimentally determined)  
  - \(A_0\) = billet cross-sectional area  
  - \(A_f\) = extrudate cross-sectional area  

Values of \(k\) vary by metal and temperature (e.g., 12.522 psi at given extrusion temperature for a specific material).  

Example calculation:  
- \(F = 1.26 \times 10^6 \, \text{lb} = 630 \, \text{tons} = 5.5 \, \text{MN}\)  

### Metal Flow in Extrusion  
- Metal flows longitudinally like an incompressible fluid, producing elongated grain structures with preferred orientation.  
- Improper flow leads to defects.  
- Investigated by splitting and scoring billets, then analyzing flow patterns after extrusion.  
- Dead metal zones appear near corners, analogous to fluid stagnation in sharp turns.  

---

*This section outlines advanced material and manufacturing techniques relevant to aerospace propulsion systems and components, suitable for integration with FPGA-based control and sensor systems in space missions such as the Parker Solar Probe.*

