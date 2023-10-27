# Example R Script 1

# Generate some random data
set.seed(123)
data <- data.frame(
  ID = 1:10,
  Age = rnorm(10, 30, 5),
  Income = rnorm(10, 50000, 10000)
)

# Print summary statistics
summary(data)

# Create a histogram of Age
hist(data$Age, main = "Age Distribution", xlab = "Age", ylab = "Frequency")

# Save the plot as a PNG file
png("hist_age.png")
hist(data$Age, main = "Age Distribution", xlab = "Age", ylab = "Frequency")
dev.off()

# Print a message
cat("Example R Script 1 completed successfully!\n")
