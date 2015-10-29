e <- function(data1,k,centroid_array,new_centroid_array,count, flag,tow,l)
{
  
  if (count == 0){
  centroid_array <- calc_centroids(data1,k)
  prev_centroid_array <- calc_centroids(data1,k)
  }
  else{
    prev_centroid_array <- centroid_array
  
    centroid_array<-new_centroid_array    
  }
 array_dist <- 0
 vectorofdata <- vector(mode ="list",length = k)
  for (i in 1:nrow(data1)){
    array_dist <- calc_distance_array(unlist(data1[i,][],use.names = FALSE),centroid_array)
  index_min <- which.min(array_dist)
     if(length(vectorofdata[[index_min]])==0)
   {
     vectorofdata[[index_min]] <- unlist(data1[i,][],use.names = FALSE)
   }
    vectorofdata[[index_min]] <-   rbind(vectorofdata[[index_min]],unlist(data1[i,][],use.names=FALSE))
    ###########Code for assigning data as per l ########################
    for ( i in 2:l){
    array_dist[index_min] <- 5000
    index_min <- which.min(array_dist)
    if(length(vectorofdata[[index_min]])==0)
    {
      vectorofdata[[index_min]] <- unlist(data1[i,][],use.names = FALSE)
    }
    vectorofdata[[index_min]] <-   rbind(vectorofdata[[index_min]],unlist(data1[i,][],use.names=FALSE))
    }
    ###################################################################
    }
    
cat("Current Centroid Values:","\n")
 print (centroid_array)
 for ( i in 1:length(vectorofdata))
 {
   cat("\n","Cluster for Centroid: ",i,"\n")
   #print(vectorofdata[[i]])
   cat("\n","Total Data Allocated:", nrow(vectorofdata[[i]]))
   }
 cat("\n","Calculating next centroids  ......")
new_centroid_array <- matrix(nrow=k,ncol=9)
 for ( i in 1:length(vectorofdata)){
   new_centroid_array[i,][] <- round((colSums(vectorofdata[[i]])/nrow(vectorofdata[[i]])),3)
 }
 cat("New Centroids:","\n")
print(new_centroid_array)
 current_tow <- calc_tow(prev_centroid_array,centroid_array,new_centroid_array)
 cat("\n", "Current Value of TOW: ",current_tow)
    if (count == flag) {
    cat(' ',"\n")
    cat('Stopping as we have reached Maximum Iterations....................................',"\n")
    tryCatch(stop(),error=function(w){
      stop("This is not the error. Clustering stopped becuase it reached Max_iterations")
    });
  }
 count <- count + 1
 cat("\n","iteration: ",count,"\n")
 if(current_tow>tow)
 {
   e(data1,k,centroid_array,new_centroid_array,count,flag,tow,l)
 }
 else{
   cat("\n", "Current Value of TOW: ",current_tow)
   if(current_tow == 0 || prev_centroid_array == new_centroid_array){
     cat("\n", "Program Converged as i cant find any change in the centroids")
   }
   else{ 
     cat("\n","We have got the best partition according to the value of TOW......Hence no more clustering required","\n")
   }
   cat("\n","Total Iterations :",count) 
 } 
}



distance <- function(x,y){
  euc = 0
  temp = unlist(y)
  for (i in 1:9){
    euc = euc+sqrt((x[i]-temp[i])^2)
  }
  return (euc)
}

kmean <- function(max_iter,tow,k,l){
  bcd_test <- read.table("breast-cancer-wisconsin.data",sep = ',',header=FALSE)
  bcd_test1 <- head(subset(bcd_test,bcd_test$V7 != "?"))
  
  e(bcd_test[][,2:10],k,0,0,0,max_iter,tow,l)
}

calc_centroids <- function(data1, k)
{
  temp <- data1[sample(nrow(data1),k),]
 temp_array <- unlist(temp[1,][],use.names = FALSE)
 for (i in 2:nrow(temp)){
 temp_array <- rbind(temp_array,unlist(temp[i,][],use.names = FALSE))  
 }
 
return (temp_array)  
}
  calc_distance_array <- function(data_row, centroid_array){
  distance_array <- 0
  distance_array <- (distance(data_row,centroid_array[1,][]))
  for (i in 2:nrow(centroid_array) ){
    distance_array <- c(distance_array,distance(data_row,centroid_array[i,][])) 
    }
  return (distance_array)
}
calc_tow <-function(prev_centroid,current_centroid,next_centroid)
{
  sum1 <- 0
  sum2 <- 0
  for (i in 1:nrow(prev_centroid)){
    for (j in 1:nrow(current_centroid)){
      sum1 <- sum1+distance(prev_centroid[i,][],current_centroid[j,][])
    }
  }
  for (i in 1:nrow(current_centroid)){
    for (j in nrow(next_centroid)){
      sum2 <- sum2+distance(current_centroid[i,][],next_centroid[j,][])
      }
  }
return ((abs(sum1-sum2)/sum1))
  }

 
