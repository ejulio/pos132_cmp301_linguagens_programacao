library(tidyverse)

source("dataset.R")

df <- ler_dados()
df <- drop_na(df)
df <- as.tibble(df)

histograma <- function(df) {
  ggplot(df, aes(x = Voltage)) +
    geom_histogram(bins = 30) +
    labs(
      title = "Histograma de Voltage",
      y = "Quantidade observações"
    )
}

scatter <- function(df) {
  df %>%
    mutate(hora = str_sub(Time, 1, 2)) %>%
    mutate(hora = as.numeric(hora)) %>%
    ggplot(aes(hora, Voltage)) +
      geom_point(alpha = 0.1) +
      labs(
        title = "Scatter de Voltage por hora"
      )
}

linha <- function(df) {
  df %>%
    mutate(dia = str_split(Date, "/") %>% map_chr(., 1)) %>%
    mutate(dia = as.integer(dia)) %>%
    mutate(mes = str_split(Date, "/") %>% map_chr(., 2)) %>%
    mutate(mes = as.integer(mes)) %>%
    group_by(mes, dia) %>%
    summarise(max_voltage = max(Voltage, na.rm = TRUE)) %>%
    ungroup() %>%
    transmute(
      mes_dia = paste(mes, dia, sep = '_'),
      max_voltage
    ) %>%
    ggplot(aes(mes_dia, max_voltage, group = 1)) +
      geom_line() +
      theme(axis.text.x = element_text(angle = 90))
}

linha(df)

sessionInfo()
