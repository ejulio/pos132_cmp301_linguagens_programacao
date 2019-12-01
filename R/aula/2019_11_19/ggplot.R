library("tidyverse")

ggplot(mpg, aes(x = cyl, y = hwy)) +
  geom_point()

ggplot(mpg) +
  geom_point(aes(x = cyl, y = hwy))

ggplot(mpg, aes(x = manufacturer)) +
  geom_bar()

ggplot(mpg, aes(displ, hwy)) +
  geom_point(aes(color = drv))

ggplot(mpg, aes(displ, hwy)) +
  geom_point(aes(color = drv)) +
  geom_smooth(se = TRUE) +
  labs(
    title = "Um gráfico"
  )

ggplot(mpg, aes(displ, hwy)) +
  geom_point() +
  facet_wrap(~drv)

ggplot(mpg, aes(displ, hwy)) +
  geom_point(aes(color = manufacturer)) +
  facet_grid(drv ~ year)

mpg %>%
  ggplot(aes(displ, hwy)) +
  geom_point()

