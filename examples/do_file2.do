// Example Do-File 2

clear all
set more off

// Generate some random data
set seed 456
gen id = _n
gen height = rnormal(170, 10)
gen weight = rnormal(70, 5)

// Summarize the data
summarize

// Create a scatter plot of height vs. weight
scatter weight height, title("Height vs. Weight") xtitle("Weight (kg)") ytitle("Height (cm)") name(scatter_hw, replace)

// Export the scatter plot as a PNG file
graph export "scatter_hw.png", replace

// Print a message
di "Example Do-File 2 completed successfully!"
