library(plyr)
merged_data<<-NULL
input<-function(clean_data_A){
  all_date<-unique(clean_data_A$observed_date)
  bus_counter <- 1
  for (cur_date in all_date){
    temp <- subset(clean_data_A,clean_data_A$observed_date==cur_date)
    all_busid<-unique(temp$bus_id)
      for (cur_busid in all_busid){
        temp<-subset(clean_data_A,clean_data_A$bus_id==cur_busid & clean_data_A$observed_date==cur_date)
        temp <- data.frame(lapply(temp, as.character), stringsAsFactors=TRUE)
        all_bus_no<-levels(factor(temp$Bus_no))
        temp <- data.frame(lapply(temp, as.character), stringsAsFactors=FALSE)
        for (cur_bus_no in all_bus_no){
          temp<-subset(clean_data_A,clean_data_A$bus_id==cur_busid & clean_data_A$observed_date==cur_date & clean_data_A$Bus_no==cur_bus_no)
          temp <- data.frame(lapply(temp, as.character), stringsAsFactors=TRUE)
          all_shift<-levels(factor(temp$Shift))
          temp <- data.frame(lapply(temp, as.character), stringsAsFactors=FALSE)
          for (cur_shift in all_shift){
            temp<-subset(clean_data_A,clean_data_A$bus_id==cur_busid & clean_data_A$observed_date==cur_date & clean_data_A$Bus_no==cur_bus_no & clean_data_A$Shift==cur_shift)
        temp$trip_id<-NA
        temp<-arrange(temp,observed_time)
        temp<-generate_tripid(temp)
        schedule_temp<-schedule_temp_function(cur_bus_no)
        if (schedule_temp==0){
          next()
        }
        schedule_temp<-rename(schedule_temp,c("Time"="Scheduled_time","Stop"="From","trip"="trip_id"))
        temp<-merge(temp,schedule_temp,c("From","trip_id"))
        temp<-arrange(temp,id)
        temp$route_id<-NULL
        temp$k<-NULL
        #temp<-(temp[c(5,6,4,3,8,1,9,12,14,15,16,17,11,19)])
        temp$time_diff<-NA
        temp$time_diff<- difftime(strptime(temp$observed_time,format="%H:%M:%S"),strptime(temp$Scheduled_time,format = "%H:%M:%S"),units = "mins")
        temp$time_diff<-round(temp$time_diff,2)
       
        merged_data<<-rbind(merged_data,temp)
          }
        }
        
        
        
      }
    print(cur_date)
    
  }
  merged_data<<-arrange(merged_data,id)
  print("Done merging data with time diff")
}

unique<-function(array_val){
b<-c(array_val[1])  
for (i in 1:length(array_val)){
  if(array_val[i] %in% b ){
    next()
  }
  b<-append(b,array_val[i])
}
  return(b)
}





generate_tripid<-function(temp){
  a <- c('Stadium (A)','Stadium ()')
  counter = 0
  for  (i in 1:nrow(temp))
  {
    
    temp$trip_id[i]<- counter
    
    if (temp$From[i] %in% a){
      counter = counter+1
      temp$trip_id[i]= counter
      if (temp$From[i-1] %in% a && i!=1){
        counter = counter-1
        temp$trip_id[i]= counter
      }
    }
}
  return (temp)
  
}
schedule_temp_function<-function(bus_counter){
  bus_id<- bus_counter
  if (bus_id %in% schedule_data$Route){
  schedule_temp<-subset(schedule_data,schedule_data$Route==bus_id)
  schedule_temp<- data.frame(lapply(schedule_temp, as.character), stringsAsFactors=FALSE)
  schedule_temp$Stop = replace(schedule_temp$Stop,schedule_temp$Stop=="Stadium","Stadium (A)")
  schedule_temp<- data.frame(lapply(schedule_temp, as.character), stringsAsFactors=FALSE)
  schedule_temp$trip<-NA
 # schedule_temp$shift<-NA
  schedule_temp<-generate_tripid_schedule(schedule_temp)
  #schedule_temp<-generate_shift_schedule(schedule_temp,bus_counter)
  
  return (schedule_temp)
  }
  else{
    return (0)
  }
}
generate_tripid_schedule<-function(schedule_temp){
  counter = 1
  for (i in 1:nrow(schedule_temp)){
    if (toString(schedule_temp$Stop[i])=='Stadium ()' && i!=nrow(schedule_temp)){
      schedule_temp$trip[i]<- counter
      counter = counter +1
      i = i+1
    }
    schedule_temp$trip[i]=counter
    if (i==161){
      a=1
    }
  }
  return (schedule_temp)
}
generate_shift_schedule<-function(schedule_temp,bus_counter){
  if (bus_counter==1){
  counter = 1
  for (i in 1:nrow(schedule_temp)){
    if (toString(schedule_temp$Time[i]) == "12:37:00"){
      counter = counter + 1
    }
    if (toString(schedule_temp$Time[i]) == "16:50:00"){
      counter = counter + 1
    }
    if (toString(schedule_temp$Time[i]) == "20:47:00"){
      counter = counter + 1
    }
    schedule_temp$shift[i]= counter
  }}
  if (bus_counter==2){
    counter = 1
    for (i in 1:nrow(schedule_temp)){
      if (toString(schedule_temp$Time[i]) == "12:37:00"){
        counter = counter + 1
      }
      if (toString(schedule_temp$Time[i]) == "16:50:00"){
        counter = counter + 1
      }
      if (toString(schedule_temp$Time[i]) == "20:47:00"){
        counter = counter + 1
      }
      schedule_temp$shift[i]= counter
    }
  }
  if (bus_counter==3){
    counter = 1
    for (i in 1:nrow(schedule_temp)){
      if (toString(schedule_temp$Time[i]) == "12:22:00"){
        counter = counter + 1
      }
      if (toString(schedule_temp$Time[i]) == "16:34:00"){
        counter = counter + 1
      }
      schedule_temp$shift[i]= counter
    }
  }
  if (bus_counter==3){
    counter = 1
    for (i in 1:nrow(schedule_temp)){
      if (toString(schedule_temp$Time[i]) == "12:56:00"){
        counter = counter + 1
      }
      if (toString(schedule_temp$Time[i]) == "16:26:00"){
        counter = counter + 1
      }
      schedule_temp$shift[i]= counter
    }
  }
  if (bus_counter==4){
    counter = 1
    for (i in 1:nrow(schedule_temp)){
      if (toString(schedule_temp$Time[i]) == "12:43:00"){
        counter = counter + 1
      }
      if (toString(schedule_temp$Time[i]) == "16:57:00"){
        counter = counter + 1
      }
      schedule_temp$shift[i]= counter
    }
  }
  if (bus_counter==5){
    counter = 1
    for (i in 1:nrow(schedule_temp)){
      if (toString(schedule_temp$Time[i]) == "14:39:00"){
        counter = counter + 1
      }
      schedule_temp$shift[i]= counter
    }
  }
  if (bus_counter==6){
    counter = 1
    for (i in 1:nrow(schedule_temp)){
      if (toString(schedule_temp$Time[i]) == "12:07:00"){
        counter = counter + 1
      }
     schedule_temp$shift[i]= counter
    }
  }
return (schedule_temp)
}

merge_time<-function(temp,schedule_temp){
  temp$schedule_time<-NA
  for (i in 1:nrow(temp)){
    for (j in 1:nrow(schedule_temp))
    {
      if (temp$trip_id[i]==schedule_temp$Trip[j] && toString(temp$to[i])==toString(schedule_temp$Stop[j])){
        print (temp$Time[j])
        temp$scheduled_time[i] = toString(schedule_temp$Time[j])
      }
    }
    return (temp)
  }
  
  
  
}
