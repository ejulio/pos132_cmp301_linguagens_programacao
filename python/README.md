# 1 Primeiros passos

## Instalação

O `python` pode ser baixado [aqui](https://www.python.org/downloads/).
Em abientes _Linux_, é possível instalar pelo gerenciador de pacotes.
No _Ubuntu_, `sudo apt-get install python3`.
Junto com o `python`, precisamos de um gerenciador de pacotes.
O mais comum, é o `pip`, mas existem outros, como o [`anaconda`](https://www.anaconda.com/distribution/).
No _Windows_, o `pip` já deve vir junto com a instalação do `python`.
No _Linux_, pode ser necessário instalar separadamente.
No _Ubuntu_, `sudo apt-get install python3-pip`.

### Verificando a instalação.

Execute `python --version` no terminal.

> Pode ser necessário executar `python3 --version`.

Execute `pip --version` no terminal.

> Pode ser necessário executar `pip3 --version`.

## Ambientes virtuais

A instalação de pacotes no `python` é feita em nível global.
Ou seja, o mesmo pacote é compartilhado entre várias aplicações.
Isso pode ser um problema em alguns casos.
Imagine que a _Aplicação A_ precisa da biblioteca `numpy 1.17.0` enquanto a _Aplicação B_ precisa do `numpy 1.10.0`.
Nesse caso, é provável que uma das aplicações não funcione como esperado.
Outro ponto importante é que o sistema operacional pode usar o `python` e determinadas biblitecas para a sua operação.
Assim, ao instalar ou atualizar uma biblioteca, quebramos o funcionamento do sistema operacional.
Para evitar esses problemas, precisamos de _ambientes virtuais_.

Existem vários gerenciadores de _ambiente virutal_ no `python.
Os mais comuns são:
* [`venv`](https://docs.python.org/3/library/venv.html)
    * Já vem com o `python 3`, mas pode ser necessário instalar: [Windows](https://programwithus.com/learn-to-code/Pip-and-virtualenv-on-Windows/) ou `sudo apt-get install python3-venv` no Ubuntu
* [`pipenv`](https://docs.pipenv.org/en/latest/)
* [`pyenv`](https://github.com/pyenv/pyenv)
* [`anaconda`](https://www.anaconda.com/)

Cada um desses gerenciadores tem uma forma de trabalhar, e fica muito ao gosto do usuário qual deles utilizar.
No restante desse material, utilizaremos o `venv`.

### Iniciando um _ambiente virtual_

No terminal, execute `python3 -m venv .venv`.
`-m venv` importa o módulo do `venv` e `.venv` é o diretório que desejamos criar esse ambiente.
Note que `.venv` é apenas uma convenção, mas você pode colocar o nome que desejar.
Nesse momento, o nosso _ambiente virtual_ já está criado, mas se instalarmos um pacote, ele ainda será instalado no sistema global.
Após criar o _ambiente virtual_, é necessário ativá-lo: `source .venv/bin/activate` e você poderá notar que o terminal mudou, adicionando `(.venv)` ao início da linha.
A partir de agora, toda instalação de pacote feita nessa sessão do terminal será feita dentro do ambiente virtual e os pacotes globais ficarão intactos.

> Para sair do _ambiente virtual_ basta executar `deactivate`

## Instalando pacotes

A instalação de pacotes no `python` é feita pelo `pip`.
Para instalar um pacote, execute `pip install <nome do pacote>`.
Por exemplo, para instalar o `numpy`, basta executar `pip install numpy`.

Além da instalação de pacotes, o `pip` também permite consultar os pacotes instalados com `pip list`.
No `python` é comum listar as suas dependências em um arquivo `requirements.txt`, assim outros desenvolvedores conseguem instalar as mesmas bibliotecas que você.
Por exemplo, veja o arquivo [`requirements.txt` do `scrapy`](https://github.com/scrapy/scrapy/blob/master/requirements-py3.txt).
Normalmente, esse arquivo vai conter apenas as dependências do seu projeto, e não todos os pacotes instalados.
Entretanto, se quiser listar todos os pacotes instalados no formato do `requirements.txt`, basta executar `pip freeze`.

> Para instalar os pacotes a partir do `requirements.txt`, execute `pip install -r requirements.txt`

> Os pacotes são obtidos do [`pypi`](https://pypi.org/), mas existem outros repositórios como o [`conda-forge`](https://conda-forge.org/)

# 2 Gráficos (diretório `graficos`)

Dataset https://archive.ics.uci.edu/ml/datasets/Individual+household+electric+power+consumption

Para iniciar:
* Mude para o diretório `graficos`
* Crie e ative um ambiente virtual para esse exemplo
* Instale as dependencias `pip install -r requirements.txt`

Execue `python main.py`.
Note que é necessário informar dois parâmetros `--grafico` e `arquivo-saida`.
Informe o gráfico desejado em `--grafico` e qualquer caminho válido no seu sistema em `--arquivo-saida`.

Esse programa demonstra, principalmente, o uso da biblioteca `matplotlib` para criar gráficos.
Porém, também vemos a biblioteca `pandas` para manipulação de dados tabulares.
`requests` para fazer requisições _http_.
Sem contar algumas estruturas da linguagem `python` e a sua bibliteca padrão (_standard library_).

# 3 Estatísticas

TBD

# 4 Detecção de anomalias (Exercício)

https://archive.ics.uci.edu/ml/datasets/Individual+household+electric+power+consumption

# 5 Processamento de imagens

TBD

# 6 Classificação de spam

TBD

# 7 Regressão linear

TDB

# 8  K-Nearest Neighbor (Exercício)

https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Diagnostic%29
