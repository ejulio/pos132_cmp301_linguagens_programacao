ler_dados <- function() {
  dataset_file <- "household_power_consumption.txt"
  
  if (!file.exists(dataset_file)) {
    download.file(
      "https://archive.ics.uci.edu/ml/machine-learning-databases/00235/household_power_consumption.zip",
      "household_power_consumption.zip"
    )
    
    unzip(
      "household_power_consumption.zip",
      exdir="./"
    )
  }
  
  # a última expressão da função é o valor retornado
  # mas pode usar o return(valor) também
  read.csv(
    dataset_file,
    # nrows=500000,
    na.strings = c("?"),
    sep = ";"
  )
}