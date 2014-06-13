# call with `R CMD BATCH --no-save plotdxdy.R`
# specify the necessary filenames
require(ggplot2)
dxdy = read.table("./dxdy-log.txt")
png("./plotdxdy.png",width=1024,height=1024,res=100)
colnames(dxdy) <- c("dx", "dy")
d <- ggplot(dxdy, aes(x = dx, y = dy))
d + stat_bin2d(binwidth=c(0.1,0.1))
dev.off()
