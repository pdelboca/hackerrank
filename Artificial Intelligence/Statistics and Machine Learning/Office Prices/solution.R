# Enter your code here. Read input from STDIN. Print output to STDOUT
setwd("~/Repos/hackerrank/Artificial Intelligence/Statistics and Machine Learning/Office Prices")
loadData <- function() {
  con <- file("stdin")
  #con <- file("./data//data.txt", open='r')
  open(con)
  f <- 0
  nRows <- 0
  predLines <- 0
  lineData <- c()
  dataset <- data.frame()
  predData <- data.frame()
  lineNumber <- 1
  while(length(line <- readLines(con,n=1, warn = FALSE)) > 0) {
    if(lineNumber == 1){
      data <- as.numeric(unlist(strsplit(line, "\\s+")))
      f <- data[1]
      nRows <- data[2]  
    }
    #Offset +1 due to the first line being metadata
    if(lineNumber > 1 & lineNumber <= nRows + 1){
      line <- as.numeric(unlist(strsplit(line, "\\s+")))
      dataset <- rbind(dataset, line)      
    }
    if(lineNumber == (nRows + 2)){
      predLines <- as.numeric(unlist(strsplit(line, "\\s+")))
    }
    if(lineNumber > nRows + 2){
      line <- as.numeric(unlist(strsplit(line, "\\s+")))
      predData <- rbind(predData, line)
    }
    
    lineNumber <- lineNumber + 1
  }
  close(con)
  # R cannot return two values -.-
  return(list(f = f, dataset = dataset,predData = predData))  
}

predictOfficePrices <- function(){
  result <- loadData()
  features <- as.numeric(result['f'])
  
  dataset <- as.data.frame(result['dataset'])
  colnames(dataset) <- c(paste("feat", seq(1:features), sep=""), "target")
  predData <- as.data.frame(result['predData'])
  colnames(predData) <- paste("feat", seq(1:features),sep="")
  
  # Very basic exploration for best model
  train <- dataset[1:70,]
  test <- dataset[71:100,]
  error <- NULL
  for(i in seq(1:20)){
    fit <- lm(target ~ poly(feat1 + feat2,i), data=dataset)
    predict <- predict(fit, test[1:2,])
    error <- c(error, sum(abs(predict - test[,3])/test[,3]))    
  }
  best_exponent <- which.min(error)
  
  polynomic_term <- paste(paste('poly(',colnames(dataset)[1:2],",", best_exponent,')',sep=""),collapse="+")  
  formula <- as.formula(paste(colnames(dataset)[features+1],
                              "~",
                              ". + ",
                              polynomic_term,                              
                              sep = ""))
  fit <- lm(formula, data=dataset)
  predicted <- predict.lm(fit, predData)
  predicted  
}

predicted <- predictOfficePrices()

cat(predicted, sep="\n")
