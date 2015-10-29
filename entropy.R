p <-0
for(j in 2:10){
  p<- 0
for (i in 1:10){

k <- nrow(subset(bcd_test,bcd_test[][,j]==i)) /nrow(bcd_test)
p <- p+(k*log(k,base=2))

}
  print (-p)
}

