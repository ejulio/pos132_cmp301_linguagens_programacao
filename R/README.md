# 1 Primeiros passos

## Instalação

A linguagem `R` pode ser instalada através do pacote `r-base` no Ubuntu (`apt-get install r-base`),
ou no Windows através de [instalador](https://cran.r-project.org/bin/windows/base/).
Quando a instalação terminar, é possível abrir um `shell` interativo pela linha de comando digitando apenas `R`.
A partir desse momento é possível começar a escrever e expressões na linguagem e ver os resultados.

Um ponto interessante, é que a `R` tem uma IDE que pode ajudar na 
hora de escrever scripts, o [`R Studio`](https://rstudio.com/).

## Instalação de pacotes

Para instalar um pacote é necessário o `shell` do `R` e executar `install.packages("<nome do pacote>")`.
Entretanto, esse modo de instalar pacotes, coloca eles em nível global do sistema.
Assim, é possível ter conflitos entre pacotes entre projetos.
Para evitar esse problema, o pacote [`packrat`](https://rstudio.github.io/packrat/)
cria ambientes isolados para cada projeto.
Portanto, em uma sessão do `shell` do `R` execute `install.packages("packarat)`.
Porém, ainda é necessário iniciar o ambiente dentro do seu projeto com `packrat::init()`.
Uma vez que o ambiente foi iniciado, um novo diretório `packrat`
é criado no seu projeto para gerenciar as dependências do seu projeto.
A partir desse momento, basta apenas instalar bibliotecas normalmente com `install.packages("<nome do pacote>")`

Referências:
* [Advanced R](http://adv-r.had.co.nz/)
* [R for Data Science](https://r4ds.had.co.nz/index.html)
* [Quick-R by DataCamp](https://www.statmethods.net/index.html)
* [RStudio Cheat Sheets](https://rstudio.com/resources/cheatsheets/)