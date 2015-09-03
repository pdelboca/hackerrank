setwd("~/Repos/hackerrank/Artificial Intelligence/Statistics and Machine Learning/Computing the Correlation")
loadData <- function() {
  con <- file("stdin")
  open(con)
  # Read first line containing number of observatios
  line <- readLines(con,n=1, warn = FALSE)
  # Read the whole table, (for lacks of performance)
  m <- read.table(con, header=FALSE)
  close(con)
  m  
}

# (Mathematics, Physics and Chemistry)
data <- loadData()

#Correlation coefficient between Mathematics and Physics scores.
est <- cor.test(data[,1], data[,2])$estimate 
cat(round(est, digits=2), '\n')
#Correlation coefficient between Physics and Chemistry scores. 
est2 <- cor.test(data[,2], data[,3])$estimate
cat(round(est2, digits=2), '\n')
#Correlation coefficient between Chemistry and Mathematics scores.
est3 <- cor.test(data[,3], data[,1])$estimate
cat(round(est3, digits=2), '\n')