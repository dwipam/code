for (i in 1:nrow(clean_data_A_657_shift1)){
  for (j in 1:nrow(schedule_data_A1))
  {
    if (clean_data_A_657_shift1$trip_id[i]==schedule_data_A1$Trip[j] && toString(clean_data_A_657_shift1$to[i])==toString(schedule_data_A1$Stop[j])){
      print (schedule_data_A1$Time[j])
      clean_data_A_657_shift1$scheduled_time[i] = toString(schedule_data_A1$Time[j])
    }
  }
}