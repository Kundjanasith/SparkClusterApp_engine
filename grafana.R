file_b <- read.table("file_b.txt",sep=",",header=TRUE)
file_b$USED <- mean(file_b$USED)
file_b$FREE <- mean(file_b$FREE)
file_m <- read.table("file_m.txt",sep=",",header=TRUE)
file_m$USED <- mean(file_m$USED)
file_m$FREE <- mean(file_m$FREE)
file_b <- file_b[1,]
file_m <- file_m[1,]
write.csv(file_b,file="MEMORY_API/file_b.csv",row.names=FALSE)
write.csv(file_m,file="MEMORY_API/file_m.csv",row.names=FALSE)
