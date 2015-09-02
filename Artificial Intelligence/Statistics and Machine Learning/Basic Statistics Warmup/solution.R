# Enter your code here. Read input from STDIN. Print output to STDOUT
f <- file("stdin")
open(f)
data <- c()
while(length(line <- readLines(f,n=1, warn = FALSE)) > 0) {
  data <- c(data, line)
}
data <- as.numeric(unlist(strsplit(data, "\\s+")))
cant <- data[1]
numbers <- data[-1]

# Mean
my_mean <- mean(numbers) 
cat(my_mean, sep="\n")
# Median
my_median <- median(numbers)
cat(my_median, sep="\n")
# Mode
my_mode <- as.numeric(names(table(numbers))[which.max(table(numbers))]) 
cat(my_mode, sep="\n")
# Standard Deviation (SD).
# sd() from R uses (N - 1)
my_sd <- sqrt(sum((numbers - my_mean)^2) / (cant))
cat(my_sd, sep="\n")
# Lower and Upper Boundary of the 95% Confidence Interval for the mean
left <- my_mean - 1.96 * my_sd / sqrt(cant)
right <- my_mean + 1.96 * my_sd / sqrt(cant)
cat(left, right, sep=" ")