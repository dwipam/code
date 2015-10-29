bcd_test
kl <- matrix( nrow = 9,ncol=9)
col_arr <- c('V1','V2','V3','V4','V5','V6','V7','V8','V9')
for (i in 1:9){
  for (j in 1:9){
    kl[i,j] <- KL.plugin(bcd_test[][,i],bcd_test[][,j])
    
  }
}
