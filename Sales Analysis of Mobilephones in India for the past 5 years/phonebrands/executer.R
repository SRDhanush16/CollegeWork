library(readxl)
msdf <- read_excel("D:\\Dhanush Folder\\VIT\\VIT courses\\SEM4 Courses - WINTER SEM 22-23\\PROBABILITY N STATISTICS\\LAB PROJECT\\phonebrands.xlsx")
head(msdf)
library(readxl)
pt<-read_excel("D:\\Dhanush Folder\\VIT\\VIT courses\\SEM4 Courses - WINTER SEM 22-23\\PROBABILITY N STATISTICS\\LAB PROJECT\\phonetrans.xlsx")
head(pt)

barplot(msdf$Micromax,main="% market share of micromax from 1/2017 - 2/2023",col = "orange")
barplot(pdc,main="probability distribution curve of micromax in 2017",col="orange")
barplot(msdf$Micromax[60:72]/100,main="probability distribution curve of micromax in 2022",col="orange")

barplot(msdf$Micromax[39:54]/100,main="probability distribution curve for micromax during COVID-19 phase",col="orange")

barplot(msdf$Micromax/100,main="Overall probability distribution curve for micromax from 2017 to 2022",col='orange')

pie(msdf$Micromax)

jan17 = c(27.18,
          7.74,
          5.90,
          8.21,
          3.56,
          6.76,
          2.31,
          0.00,
          2.91,
          0.00,
          0.00,
          1.70,
          0.69,
          0.38,
          0.24,
          0.99,
          0.04,
          0.27,
          0.77,
          2.20,
          28.03)

names = c('Samsung'	,'Nokia'	,'Xiaomi',	'Micromax',	'Oppo'	,'Lenovo'	,'Apple',	'Mobicel'	,'Motorola'	,'Vivo'	,'Realme',	'Sony',	'Huawei',	'OnePlus',	'Google',	'Reliance Digital',	'Karbonn',	'Xolo',	'Lava',	'Lyf',	'others')

pie(pt$`2017-01`)



