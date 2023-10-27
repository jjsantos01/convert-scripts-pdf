// Example Do-File 1

clear all
set more off

// Generate some random data
set seed 123
gen id = _n
gen age = rnormal(30, 5)
gen income = rnormal(50000, 10000)

// Summarize the data
summarize

// Create a histogram of age
histogram age, title("Age Distribution") xtitle("Age") ytitle("Frequency") name(hist_age, replace)

// Export the histogram as a PNG file
graph export "hist_age.png", replace

// Print a message
di "Example Do-File 1 completed successfully!"
