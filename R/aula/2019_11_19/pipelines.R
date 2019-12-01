library(tidyverse)

mpg %>%
  select(manufacturer, model) %>%
  filter(model == "a4")

# forma sem %>%
select(
  filter(
    mpg,
    model == "a4"
  ),
  manufacturer, model
)

mpg %>%
  filter(model == "a4",
         displ > 2)

mpg %>%
  filter(
    model == "a4" | displ > 2
  )

mpg %>%
  filter(year == 1999) %>%
  select(manufacturer, displ) %>%
  View()

mpg %>%
  filter(year == 1999) %>%
  ggplot(aes(displ, hwy)) +
    geom_point()

mpg %>%
  arrange(model, manufacturer)

mpg %>%
  filter(
    between(displ, 1.5, 2.5)
  )

mpg %>%
  filter(drv %in% c("f", "r"))

# mod
5 %/% 4

mpg %>%
  select(-year)

mpg %>%
  select(-(year:class))

mpg %>%
  transmute(
    ratio = hwy / cty,
    hwy = hwy,
    cty = cty,
    ratio_2 = ratio * 2
  )


mpg %>%
  mutate(
    ratio = hwy / cty,
    ratio_2 = ratio * 2
  )

mpg %>%
  count(manufacturer) %>%
  arrange(-n) %>%
  top_n(5)

mpg %>%
  group_by(model) %>%
  summarise(
    hwy_medio = mean(hwy),
    cty_medio = mean(cty)
  )

mpg %>%
  count(manufacturer) %>%
  spread(manufacturer, n) %>%
  View()

mpg %>%
  count(year) %>%
  spread(year, n) %>%
  gather(
    `1999`, `2008`,
    key = "year",
    value = "n"
  ) %>%
  View()

