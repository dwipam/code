schedule_data <- read.table("schedule_data.data",sep="")
temp <- strptime(schedule_data$Time,format='%I:%M %p')
temp <- substr(temp,12,19)
temp <- type.convert(temp)
schedule_data$Time <- temp