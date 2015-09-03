con <- file("stdin")
open(con)
nRows <- 0
line <- readLines(con,n=1, warn = FALSE)
nRows <- as.numeric(unlist(strsplit(line, "\\s+")))
data <- read.table(con,header=FALSE)
cat(colnames(data))