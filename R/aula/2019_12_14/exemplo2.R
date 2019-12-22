# install.packages("tidyverse")

a <- 10
a <- a * 9
# mod %
a <- a %/% 9

nome <- "Júlio"
nome <- 'Júlio'

nomes <- c("nome 1", "nome 2")
nomes
nomes[2]

nomes <- list("nome 1", 1)
nomes[[2]]

bool <- TRUE
bool <- FALSE
bool <- NA

turma.1 <- 1
turma.1

is.na(turma.1)

idades <- c(
  12, 14, 11, 23, NA,
  23, 24, 25, 11, 10
)

media <- function(numeros) {
  soma <- 0
  qtd <- 0
  for (i in seq_along(numeros)) {
    if (!is.na(numeros[i])) {
      soma <- soma + numeros[i]
      qtd <- qtd + 1
    }
  }
  return(soma / qtd)
}
media(idades)

mean(idades, na.rm = TRUE)
sd(idades, na.rm = TRUE)
median(idades, na.rm = TRUE)

