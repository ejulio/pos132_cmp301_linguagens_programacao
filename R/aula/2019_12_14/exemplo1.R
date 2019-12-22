library(tidyverse)

#View(mpg)

mpg2 <- transmute(mpg,
  manufacturer = manufacturer,
  model = model,
  year = year,
  engine_displacement = displ,
  cylinders = cyl,
  transmission = trans,
  drive = drv,
  fuel_type = fl,
  class = class,
  city_miles_per_gallon = cty,
  highway_miles_per_gallon = hwy
)
View(mpg2)

mpg_ <- select(
  mpg2,
  year,
  model,
  city_miles_per_gallon
)

mpg2 %>%
  select(
    year, 
    model, 
    city_miles_per_gallon
  ) %>%
  arrange(-year) %>%
  View()


mpg2 %>%
  count(manufacturer, year) %>%
  arrange(n) %>%
  spread(year, n) %>%
  View()

mpg2 %>%
  group_by(manufacturer, year) %>%
  summarise(
    media_cidade = mean(city_miles_per_gallon),
    media_via = mean(highway_miles_per_gallon),
  ) %>%
  mutate(
    diff_media = media_via - media_cidade,
    x2_media = diff_media * 2
  ) %>%
  arrange(diff_media) %>%
  filter(
    media_cidade > 20,
    media_cidade < 24
  ) %>%
  View()


mpg2 %>%
  ggplot(aes(x = manufacturer)) +
    geom_bar() +
    coord_flip()
  

mpg2 %>%
  group_by(manufacturer) %>%
  summarise(
    media_cidade = mean(city_miles_per_gallon)
  ) %>%
  ggplot(
    aes(x = manufacturer, y = media_cidade)
  ) +
  geom_bar(stat = "identity") +
  labs(
    x = "Fabricante",
    y = "Media na cidade",
    title = "Consumo medio na cidade por fabricante"
  )

?right_join

mpg2 %>%
  filter(drive == "4") %>%
  ggplot(aes(city_miles_per_gallon)) +
    geom_histogram(bins=30, fill="red")

ggplot() +
  mpg2 %>%
    filter(drive == "r") %>%
    geom_histogram(aes(city_miles_per_gallon), data = ., fill="red", alpha = 0.3) +
  mpg2 %>%
    filter(drive == "4") %>%
    geom_histogram(aes(city_miles_per_gallon), data = ., fill="blue", alpha = 0.3) +
  mpg2 %>%
    filter(drive == "f") %>%
    geom_histogram(aes(city_miles_per_gallon), data = ., fill="green", alpha = 0.3)
  

mpg2 %>%
  group_by(drive) %>%
  ggplot(aes(city_miles_per_gallon, fill = drive)) +
    geom_histogram(bins = 30)



mpg2 %>%
  ggplot(aes(city_miles_per_gallon)) +
    geom_density(bins = 30) +
    facet_wrap(~drive)

mpg2 %>%
  ggplot(aes(city_miles_per_gallon)) +
  geom_density(bins = 30) +
  facet_grid(fuel_type ~ drive)


mpg2 %>%
  ggplot(aes(engine_displacement, city_miles_per_gallon)) +
    geom_point(alpha = 0.5) +
    geom_smooth(se = FALSE) +
    facet_wrap(~drive)


modelo <- lm(
  city_miles_per_gallon ~ engine_displacement * drive,
  mpg2
)
modelo$coefficients

library(modelr)

mpg2 <- mpg2 %>%
  add_predictions(modelo)

mpg2 %>%
  ggplot(aes(engine_displacement)) +
    geom_point(aes(y = city_miles_per_gallon), color = "red") +
    geom_point(aes(y = pred), color = "blue") +
    facet_wrap(~drive)


mpg2 <- mpg2 %>%
  add_residuals(modelo)
mpg2$resid

mpg2 %>%
  ggplot(aes(city_miles_per_gallon, resid)) +
  geom_point(aes(color = drive))
  