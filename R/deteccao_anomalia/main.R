library(tidyverse)

source("dataset.R")

df <- ler_dados() %>%
  drop_na() %>%
  as.tibble()

df <- df %>%
  mutate(ano = str_split(Date, "/") %>% map_chr(., 3)) %>%
  mutate(ano = as.integer(ano))

df_2006_2009 <- df %>%
  filter(between(ano, 2006, 2009))

df_2010 <- df %>%
  filter(ano == 2010)

mu = mean(df_2006_2009$Voltage)
std = sd(df_2006_2009$Voltage)

df_2010 <- df_2010 %>%
  mutate(
    anomalia = abs(Voltage - mu) > 2 * std
  )
