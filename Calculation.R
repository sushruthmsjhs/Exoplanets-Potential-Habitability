mydata <-read.csv("/Users/sushruth/Desktop/ASDRP/ExoplanetsUpdated.csv", header = TRUE)



table <- mydata[,c("rowid","pl_name", "pl_orbsmax", "pl_orbeccen", "pl_bmasse", "pl_rade")]
#table <-na.omit(table)
table[c("pl_orbsmin")]<-0
table$pl_orbsmin <- sqrt(abs(table$pl_orbsmax**2-table$pl_orbeccen**2))
table(c("pl_avgorb"))<-0
for(i in 0:3972)
{
    table$pl_avgorb <- (table$pl_orbsmax+table$pl_orbsmin)/2
  
}
table(c("pl_density"))<-0
for(i in 0:3972)
{
  table$pl_density <- (table$pl_bmasse*5.972*10**27/((table$pl_rade*6.371*10**8)**3*4/3*pi))
}


View(table)
