// Define the simulation grid
setgridsize(256, 64, 10) // Adjust grid size as needed
setcellsize(2e-9, 2e-9, 2e-9) // Adjust cell size according to physical dimensions

// Material parameters
Msat = 800e3  // Saturation magnetization (A/m), adjust for each layer if needed
Aex = 15e-12 // Exchange stiffness (J/m), predefined system variable
alpha = 0.01 // Gilbert damping, predefined system variable

// Define regions for each layer
defRegion(0, layer(0)) // Reference layer, rigid, not affected by STT
defRegion(1, layer(1)) // Free layer
defRegion(2, layer(2)) // Exchange-coupling layer
defRegion(3, layer(3)) // Granular layer

// Granular layer tessellation parameters
grainSize := 40e-9 // Average grain size in meters
numGrains := 100 // Adjust based on the desired number of grains
randomSeed := 123456 // Seed for random generator to ensure reproducibility

// Apply tessellation to create granular structure
ext_makegrains(grainSize, numGrains, randomSeed)

// Initialize magnetization
m.setRegion(0, uniform(1, 0, 0)) // Reference layer magnetization
m.setRegion(1, uniform(0, 1, 0)) // Free layer initial magnetization
// Granular layer will have its magnetization defined by the grain structure

// define constants and set slonczewksi parameters
SOTxi        := -2
AlphaH       := 0.15
Pol           = alphaH
Lambda        = 1
Epsilonprime  = alphaH*SOTxi/2
Fixedlayer    = vector(0,-1,0)

// define current
J  = vector(0,0,2e11)


// Simulation run control
autosave(m, 1e-12)
tableautosave(1e-12)
run(1e-9) // Run time, adjust as needed

