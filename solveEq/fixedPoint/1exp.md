# Fixed Point Method

is a method to solve equations of the form $f(x)=0$ by changing it to the form of $g(x)=x$. It is a root finding method that uses a fixed point of the function $g(x)$ as the starting point for iteration. The fixed point of a function $g(x)$ is a value $x$ such that $g(x)=x$. The fixed point iteration method is defined as follows:

1. write $f(x)=0$ as $g(x)=x$
2. verify that $|{g'(x)}|<1$ for all $x$ in the domain of $g(x)$
3. choose an initial value $x_0$ and a tolerance $\epsilon$
4. repeat until $|{x_{n+1}-x_n}|<\epsilon$:
    1. $x_{n+1}=g(x_n)$

## Example

We want to solve the equation $\log(x) - x^2 + 2 = 0$.

1. we can define various $g(x)$ functions
    1. $g_1(x)=\exp(x^2 - 2)$
    2. $g_2(x)=\sqrt {\log(x) + 2}$
    3. $g_3(x)=-\sqrt {\log(x) + 2}$

2. we can verify that $|{g'(x)}|<1$ for all $x$ in the domain of $g(x)$ as we can see in the following graph:

```{r}
library(ggplot2)
library(dplyr)
library(tidyr)
library(magrittr)

x <- seq(-10, 10, length.out = 1000)
g1 <- function(x) exp(x^2 - 2)
g2 <- function(x) sqrt(log(x) + 2)
g3 <- function(x) -sqrt(log(x) + 2)

df <- data.frame(x = x, g1 = g1(x), g2 = g2(x), g3 = g3(x)) %>%
  gather(key = "g", value = "y", g1, g2, g3)

ggplot(df, aes(x = x, y = y)) +
    geom_line(aes(color = g)) +
    geom_hline(yintercept = 0, linetype = "dashed") +
    geom_vline(xintercept = 0, linetype = "dashed") +
    scale_color_discrete(name = "g(x)") +
    labs(title = "g(x) functions", x = "x", y = "y") +
    theme_bw()
    ```
    