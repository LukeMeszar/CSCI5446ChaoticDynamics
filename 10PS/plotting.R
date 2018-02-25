boxCounting = read.table('fractal15000.txt', header = FALSE)
plot(boxCounting$V2, boxCounting$V1, main='Results of Box Counting for 15000 Points', xlab = expression(paste("log(1/", epsilon, ")")),ylab=expression(paste("N(", epsilon, ")")), xaxp  = c(as.integer(min(boxCounting$V2)), as.integer(max(boxCounting$V2)), 10), yaxp = c(as.integer(min(boxCounting$V1)), as.integer(max(boxCounting$V1)), 10))
boxCounting3 = read.table('fractal100000.txt', header = FALSE)
plot(boxCounting3$V2, boxCounting3$V1, main='Results of Box Counting for 100000 Points', xlab = expression(paste("log(1/", epsilon, ")")),ylab=expression(paste("N(", epsilon, ")")),xaxp  = c(as.integer(min(boxCounting3$V2)), as.integer(max(boxCounting3$V2)), 10), yaxp = c(as.integer(min(boxCounting3$V1)), as.integer(max(boxCounting3$V1)), 10))
boxCounting4 = read.table('fractalEmbedded.txt', header = FALSE)
plot(boxCounting4$V2, boxCounting4$V1, main='Results of Box Counting for Embedded Data', xlab = expression(paste("log(1/", epsilon, ")")),ylab=expression(paste("N(", epsilon, ")")), xaxp  = c(as.integer(min(boxCounting4$V2)), as.integer(max(boxCounting4$V2)), 10), yaxp = c(as.integer(min(boxCounting4$V1)), as.integer(max(boxCounting4$V1)), 10))
c2 = read.table('correlation.c2', header = FALSE)
plot(log(c2$V1),log(c2$V2), main = "Correlation Sums for Lorenz Data", xlab = expression(paste(epsilon)), ylab = expression(paste("C(",epsilon,")")), cex = 0.25)
d2 = read.table('correlation.d2', header = FALSE)

for (i in 1:18){
  plot(d2$V1[(1+99*i):(99+99*i)], d2$V2[(1+99*i):(99+99*i)], main = "Slope of Sums for Lorenz Data", xlab = expression(paste(epsilon)), ylab = expression(paste("D(", epsilon, ")")), cex = 1)
}
