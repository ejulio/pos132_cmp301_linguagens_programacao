library(tidyverse)


# ver estatísticas do dataset
summary(mpg)

mean(mpg$hwy)
sd(mpg$hwy)

idades <- c(27, 23, NA)
mean(idades, na.rm = TRUE)
sd(idades, na.rm = TRUE)

media <- function(arr) {
  c <- 0
  s <- 0
  for (v in arr) {
    if (!is.na(v)) {
      s <- s + v
      c <- c + 1
    }
  }
  return(s / c)
}
media(idades)

i <- 0
while (i < 10) {
  i <- i + 1
  print(i)
}

a <- list("0", 1, 3)

pessoa <- list(
  nome=c("Júlio", "Maria"),
  idade=c(27, 23)
)
pessoa$nome[1]
