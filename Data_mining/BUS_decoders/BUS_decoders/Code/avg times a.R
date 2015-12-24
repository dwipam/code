# stadium to alumni enter
stal <- subset(A_bus,A_bus$From=="Stadium ()" & A_bus$to=="Alumni Center")
View(stal)
mean(stal$time) #390.3099
#kelley to wells
kelwell <- subset(A_bus,A_bus$From=="Kelley School" & A_bus$to=="Well's Library")
View(kelwell)
mean(kelwell$time) #112.114
#neal to 3rd n J
neal3j <- neal3j <- subset(A_bus,A_bus$From=="Neal Marshall" & A_bus$to=="3rd & Jordan")
mean(neal3j$time) #115.685
#kirkwood to IMU
kirkimu <- subset(A_bus,A_bus$From=="Kirkwood & Indiana" & A_bus$to=="IMU")
 mean(kirkimu$time) #110.8068

#B route
#Balfour to Kappa Sigma
balkappa <- subset(B_bus,B_bus$From=="Balfour" & B_bus$to=="Kappa Sigma")
View(balkappa)
mean(balkappa$time) #42.89831
#kappa sigma to jordan & 7th
kappajord7 <- subset(B_bus,B_bus$to=="Jordan & 7th" & B_bus$From=="Kappa Sigma")
mean(kappajord7$time) #42.91712
#lingelback to Kappa delta
lingkappad <- subset(B_bus,B_bus$From =="Lingelbach" & B_bus$to=="Kappa Delta")
mean(lingkappad$time) #48.06276
#kappa delta to 10th & jordan
kappad10nj <- subset(B_bus,B_bus$From=="Kappa Delta" & B_bus$to=="10th & Jordan")
mean(kappad10nj$time) #55.83386

#E route
#everrmann to union & 10th
campunion10 <- subset(E_bus,E_bus$From=="Campus View" & E_bus$to=="Union & 10th")
mean(campunion10$time) #89.90136

#wilkie to 3rd and jordan
wil3rd<-subset(E_bus,E_bus$From=="Wilkie" | E_bus$to=="Forest" | E_bus$to=="3rd & Jordan")
View(wil3rd)
mean(wil3rd$time) #60.98682
#imu to wells
imuwell<-subset(E_bus,E_bus$From=="IMU" | E_bus$to=="10th & Woodlawn" | E_bus$to=="Psychology" |  E_bus$to=="Well's Library")
View(imuwell)
mean(imuwell$time) #60.69838

#X route
#IMU to audtorium(X)
imuaud <- subset(X_bus,X_bus$From=="I M U (X)"& X_bus$to=="Auditorium (X)")
View(imuaud)
mean(imuaud$time) #92.56108

# stadium(x) to 7th & woddlawn
stad7th <- subset(X_bus,X_bus$From=="Stadium (x)"& X_bus$to=="7th & Woodlawn")
mean(stad7th$time) #560.0949

