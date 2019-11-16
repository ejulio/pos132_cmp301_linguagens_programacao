dataset_file <- "household_power_consumption.txt"

if (!file.exists(dataset_file)) {
  print("Arquivo não existe, fazendo download...")

  download.file(
    "https://archive.ics.uci.edu/ml/machine-learning-databases/00235/household_power_consumption.zip",
    "household_power_consumption.zip"
  )

  unzip(
    "household_power_consumption.zip",
    exdir="./"
  )
  
  print("Download concluído")
} else {
  print("Arquivo já existe...")
}

df <- read.csv(
  dataset_file,
  nrows=10000,
  na.strings = c("?"),
  sep = ";"
)

coluna <- "Sub_metering_1"
print(stringr::str_interp("===== Estatísticas da coluna '${coluna}' ====="))

quantidade_na <- sum(is.na(df[[coluna]]))
print(stringr::str_interp("Quantidade Não nulos: ${quantidade_na}"))

media <- mean(df[[coluna]], na.rm = TRUE)
print(stringr::str_interp("Média: ${media}"))

desvio_padrao <- sd(df[[coluna]], na.rm = TRUE)
print(stringr::str_interp("Desvio padrão: ${desvio_padrao}"))

variancia <- var(df[[coluna]], na.rm = TRUE)
print(stringr::str_interp("Variância: ${variancia}"))

mediana <- median(df[[coluna]], na.rm = TRUE)
print(stringr::str_interp("Mediana: ${mediana}"))

cmin <- min(df[[coluna]], na.rm = TRUE)
print(stringr::str_interp("Min: ${cmin}"))

cmax <- max(df[[coluna]], na.rm = TRUE)
print(stringr::str_interp("Max: ${cmax}"))
