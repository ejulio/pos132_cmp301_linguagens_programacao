library(tidyverse)
library(modelr)

mpg %>%
  ggplot(aes(displ, hwy)) +
  geom_point()

# y = mx + b
# hwy ~ w * displ + b
model <- lm(hwy ~ displ,
            data = mpg)
model
predict(model, mpg)

mpg %>%
  add_predictions(model) %>%
  ggplot(aes(x = displ)) +
    geom_point(
      aes(y = hwy)
    ) +
    geom_point(
      aes(y = pred),
      color = "red"
    )

mpg %>%
  add_residuals(model) %>%
  ggplot(aes(displ, resid)) +
    geom_point()

# y = mx + b
# hwy ~ w1 * displ + w2 * cyl + b
model <- lm(
  hwy ~ displ + cyl + drv,
  data = mpg
)
model

# hwy ~ w1 * displ + w2 * cyl + w3 * displ * cyl
model <- lm(
  hwy ~ displ * cyl,
  data = mpg
)

# hwy ~ w1 * displ ^ 2
model <- lm(
  hwy ~ I(displ ^ 2),
  data = mpg
)

# hwy ~ w1 * displ + w2 * displ ^ 2 + w3 * displ ^ 3
model <- lm(
  hwy ~ poly(displ, 3),
  data = mpg
)