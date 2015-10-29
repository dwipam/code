val <- 0
e <- function(x){
  
  for (i in 1:length(x)){
    val <- val +((x[i]-mean(x))^2)/length(x)
    
  }
  cat("Variance: ",val)
  
}

