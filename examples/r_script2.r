# Example R Script 2

# Generate some random data
set.seed(456)
data <- data.frame(
  ID = 1:10,
  Height = rnorm(10, 170, 10),
  Weight = rnorm(10, 70, 5)
)

# Print summary statistics
summary(data)

# Create a scatter plot of Height vs. Weight
plot(data$Weight, data$Height, main = "Height vs. Weight", xlab = "Weight (kg)", ylab = "Height (cm)")

# Save the plot as a PNG file
png("scatter_hw.png")
plot(data$Weight, data$Height, main = "Height vs. Weight", xlab = "Weight (kg)", ylab = "Height (cm)")
dev.off()

# Print a message
cat("Example R Script 2 completed successfully!\n")
