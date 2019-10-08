# 1 Primeiros passos

## Instalação

O `python` pode ser baixado [aqui](https://www.python.org/downloads/).
Em ambientes _Linux_, é possível instalar pelo gerenciador de pacotes.
No _Ubuntu_, `sudo apt-get install python3`.
Junto com o `python`, precisamos de um gerenciador de pacotes.
O mais comum é o `pip`, mas existem outros, como o [`anaconda`](https://www.anaconda.com/distribution/).
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
Outro ponto importante é que o sistema operacional pode usar o `python` e determinadas bibliotecas para a sua operação.
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
* Instale as dependências `pip install -r requirements.txt`

Execute `python main.py`.
Note que é necessário informar dois parâmetros `--grafico` e `arquivo-saida`.
Informe o gráfico desejado em `--grafico` e qualquer caminho válido no seu sistema em `--arquivo-saida`.

Esse programa demonstra, principalmente, o uso da biblioteca `matplotlib` para criar gráficos.
Porém, também vemos a biblioteca `pandas` para manipulação de dados tabulares.
`requests` para fazer requisições _http_.
Sem contar algumas estruturas da linguagem `python` e a sua biblioteca padrão (_standard library_).

# 3 Estatísticas (diretório `estatisticas`)

Dataset https://archive.ics.uci.edu/ml/datasets/Individual+household+electric+power+consumption

Para iniciar:
* Mude para o diretório `estatisticas`
* Crie e ative um ambiente virtual para esse exemplo
* Instale as dependencias `pip install -r requirements.txt`

Execute `python main.py`.
Informe uma das colunas do _dataset_.
Veja as estatísticas.

Esse programa demonstra um pouco mais da biblioteca `pandas` e das funcionalidades disponíveis para trabalhar com estatística.

# 4 Detecção de anomalias (Exercício)

Dataset https://archive.ics.uci.edu/ml/datasets/Individual+household+electric+power+consumption

O _dataset_ dos exemplos anteriores também será utilizado nesse exercício.
A ideia é detectar se houve alguma anomalia no consumo de `Voltage` no ano de 2010.
Portanto, é necessário carregar a base e separar em dois conjuntos.
O primeiro contém todas as observações até 2009 e o segundo contém apenas as de 2010.
Assim, como na vida real, o modelo será construído com base nas informações até um ponto (supondo que elas existam apenas até 2009) e serão testados no futuro (supondo que 2010 está acontecendo).
Nesse exercício a ideia de uma anomalia parte de um ponto fora de uma distribuição normal (Gaussiana).
Para simplificar o exercício, os dados na coluna `Voltage` já seguem essa distribuição.

Uma anomalia é definida como um valor distante da média acima de dois desvios padrões.
Em termos matemáticos `|x - mu| > 2 * std`, sendo:
* `x` o valor observado (qualquer linha no ano de 2010, nesse exemplo)
* `mu` a média dos valores de 2006 à 2009
* `|.|` operação de valor absoluto (pega sempre o valor positivo)
* `std` o desvio padrão dos valores de 2006 à 2009

Após verificar quais observações são anomalias e quais não são, persista o resultado em um arquivo `csv`.
A primeira coluna desse arquivo deve conter o índice (linha) da observação no _dataset_ e a segunda coluna deve conter o valor `0 se não for uma anomalia` e `1 se for uma anomalia`.

**Opcional 1**: Compute as estimativas para cada ano. Por exemplo, use 2006 como base e detecte anomalias em 2007. Depois use 2006 e 2007 como base e detecte anomalias em 2008. Assim por diante até usar os anos de 2006 até 2009 como base e detectar as anomalias em 2010.

**Opcional 2**: Como seria uma alteração no programa para receber dois parâmetros da linha de comando: `--anos-anteriores 2006,2007` e `--anos-deteccao 2008` para calcular a estatística com os anos de 2006 e 2007, e prever para o ano de 2008.

A solução proposta para esse exercício está no diretório `deteccao_anomalia`.
Antes de verificar a solução, tente resolver o problema.
Se tiver alguma dúvida, pergunte ou procure na internet antes de verificar a solução.
Ao final, compare a solução proposta com a sua.

Lembre-se de criar o ambiente virtual para o exercício e instalar as bibliotecas necessárias.

Algumas referências:
* https://pt.wikipedia.org/wiki/Detec%C3%A7%C3%A3o_de_anomalias
* https://blog.dp6.com.br/t%C3%A9cnicas-de-detec%C3%A7%C3%A3o-de-anomalias-3d9e216bf82e

# 5 Processamento de imagens (diretório `processamento_imagens`)

Nenhum _dataset_ será usado aqui, apenas imagens já disponíveis na biblioteca `scikit-image` para exemplos.

Para iniciar:
* Mude para o diretório `processamento_imagens`
* Crie e ative um ambiente virtual para esse exemplo
* Instale as dependências `pip install -r requirements.txt`
* Execute `python processamento_images.py` com o exemplo desejado

Este programa demonstra o uso da biblioteca `scikit-image` para trabalhar com imagens no `python`.
As imagens são `numpy` arrays e por isso podem ser carregadas e reutilizadas em várias bibliotecas, facilitando a integração.
Note que existem outras bibliotecas para processamento de imagens no `python`, como: `Open CV`, `mahotas`, `PIL` e `Pillow`.

Algumas funções extras para conferir:

* `resize`, `rescale`, `rotate`: https://scikit-image.org/docs/stable/api/skimage.transform.html
* `Otsu's threshold`, `Gaussian Blur`: https://scikit-image.org/docs/stable/api/skimage.filters.html
* Desenho: https://scikit-image.org/docs/stable/api/skimage.draw.html

Para mais exemplos sobre processamento de imagens com `python`, veja https://github.com/ejulio/talks/blob/master/processamento-imagens-python/Processamento%20de%20imagens%20com%20python.ipynb

# 6 Regressão linear (diretório `regressao_linear`)

Dataset https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html#sklearn.datasets.load_diabetes

Assim como o `scikit-image` contém imagens na biblioteca para testes, o `scikit-learn` possui alguns _datasets_ para testes.

Para iniciar:
* Mude para o diretório `regressao_linear`
* Crie e ative um ambiente virtual para esse exemplo
* Instale as dependencias `pip install -r requirements.txt`
* Execute `python regressao.py`

Esse programa demonstra o uso da biblioteca `scikit-learn` para otimizar um modelo de Regressão Linear.
Esse é um modelo simples de _machine learning_, mas já o suficiente para mostrar como a biblioteca funciona e pode ser utilizada.
Existem muitos algoritmos disponíveis nessa biblioteca (SVM, Rede Neural, Bayes, K-Means, outros) que variam entre aprendizado supervisionado e não-supervisionado.
De forma geral, ela é um bom ponto de partida para essas atividades.
Sem contar que funciona muito bem com `numpy` arrays e `pd.DataFrame` ajudando a trabalhar com outras bibliotecas e facilitando a compatibilidade.
Além dos algoritmos/modelos de _machine learning_ a biblioteca também provê funções para normalizar dados e ajudar nos experimentos.
Ao explorar a biblioteca (https://scikit-learn.org/stable/modules/classes.html) é possível ver que as possibilidades são inúmeras.
Um detalhe importante é que todos os algoritmos seguem a mesma interface/API, ou seja, para treinar é apenas necessário executar `fit(X, y)` e para obter os resultados `predict(X)`.
Se precisar de uma métrica de avaliação, pode usar `score(X, y)`.
Além de todos os detalhes já mencionados, também existe um módulo exclusivo para métricas dentro do `scikit-learn`, o [`metrics`](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics).

Algumas referências:
* Kaggle Courses https://www.kaggle.com/learn/overview
    * Aconselho ver [esse material](https://www.kaggle.com/learn/machine-learning-explainability) após as aulas de Aprendizado Supervisionado 
* Utilidades: https://rasbt.github.io/mlxtend/, https://www.scikit-yb.org/en/latest/
* Interpretação: https://eli5.readthedocs.io/en/latest/

# 7  K-Nearest Neighbor (Exercício)

Dataset: Iris (incluso no `scikit-learn`)

A ideia desse exercício é implementar um algoritmo simples de _machine learning_ conhecido como
_K-Nearest Neighbors_ (KNN).
Este algoritmo é baseado na ideia que amostras similares estão próximas (curta distância) em um determinado espaço.
Portanto, a ideia do algoritmo é calcular a distância de uma amostra `x` contra todas as amostras que existem na base.
A partir dessas distâncias calculadas, as `k` menores distâncias são selecionadas.
Com base nas `k` menores distância, conta-se qual a classe/_label_ mais frequente e este é usado como label para a classe.
O cálculo de distância mais comum, é a distância Euclidiana, dada por `c = sqrt((p1 - p2 ^ 2))`, sendo:
* `sqrt` a raiz quadrada
* `p1 - p2` a subtração de dois vetores, portanto deve ser feita a subtração item a item do vetor
* `^ 2` valor ao quadrado

Note que, como o interesse é apenas em qual amostra está mais próxima, e não a real distância entre os pontos, a operação de raiz quadrada pode ser descartada.

Algumas outras dicas:
* Carregue o _dataset_ com [`load_iris`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris)
* Separe um conjunto para treino e outro para teste
* Comece com `k=5`, mas depois pense nesse valor como um parâmetro que pode ser alterado
* Calcule a acurácia com [`accuracy_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#sklearn.metrics.accuracy_score)

Como no exercício anterior, uma solução proposta para este exemplo está disponível no diretório `knn`.
A ideia é tentar resolver problema e só verificar a solução proposta ao final, ou se ficar paralisado em alguma dúvida.
Ao fim, compare a sua solução com a proposta.
Lembre-se que essa solução é apenas proposta e não existe uma melhor solução, o objetivo é ter a comparação para aprendizado.
