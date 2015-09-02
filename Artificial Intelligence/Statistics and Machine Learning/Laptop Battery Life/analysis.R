setwd("~/Repos/hackerrank/Artificial Intelligence/Statistics and Machine Learning/Laptop Battery Life")

train <- read.csv('data//trainingdata.txt', header = FALSE)
colnames(train) <- c("time_charged", "hour_lasted")

hist(train$time_charged, breaks = 50)
hist(train$hour_lasted, breaks = 50)
plot(train$time, train$hour_lasted)
# Linear Regression 2*x if x < 4, 8 if greater