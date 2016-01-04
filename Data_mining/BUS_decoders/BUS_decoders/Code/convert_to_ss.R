hms_to_s<-function(string){
  hms <- strsplit(string,":")
  hh <- as.numeric(hms[[1]][1])
  mm <- as.numeric(hms[[1]][2])
  ss <- as.numeric(hms[[1]][3])
  return (hh*3600+mm*60+ss)
}