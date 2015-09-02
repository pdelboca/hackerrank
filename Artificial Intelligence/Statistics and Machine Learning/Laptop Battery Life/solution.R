# Enter your code here. Read input from STDIN. Print output to STDOUT
f <- file("stdin")
open(f)
data <- c()
while(length(line <- readLines(f,n=1, warn = FALSE)) > 0) {
  data <- c(data, line)
}

time_charged <- as.numeric(data)
battery_lasted <- ifelse(time_charged < 4, time_charged * 2, 8)
cat(battery_lasted)