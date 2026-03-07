# Estudos sobre métodos de import em python

## Introdução
A linguagem de programação python possibilita que os desenvolvedores utilizem códigos de terceiros durante o desenvolvimento de aplicações, assim como permite o importe de trechos de códigos criados pelo próprio desenvolvedor.

Essa funcionalidade permite melhor organização do código criado, uma vez que possibilita a divisão do código em multiplos arquivos, e pastas, segregados por funcionalidades específicas.

## Dicionátio de termos utilizados
__módulo:__ um único arquivo contendo código python.

__pacote:__ pasta contendo um, ou mais, arquivos python. 

## Tipos de importes python
O python possui duas sintaxes para importe de código.

### Importe de todo o módulo

```
import modulo
```

**ex:** import math

Carrega todo o pacote math para o código.

### Importe de partes de um módulo

```
from modulo import funcionalidade
```

**ex:** from math import pow

Carrega apenas a função pow para o código. 

## Exemplo de projeto com import
### Projeto Import
#### Descrição do projeto
A pasta **projeto_import** possui a seguinte arquitetura.

```
projeto_import/
|src/
||calc/
|||__init__.py
|||operation.py
||valid/
|||__init__.py
|||uteis.py
|||validacao.py
||main01.py
||main02.py
```

#### Importe direto das funcionalidades
O arquivo main01.py importa as funções **soma**, **subtracao**, **multiplicacao** e **divisao** do pacote **calc** da seguinte forma.

```
from calc import soma, subtracao, multiplicacao, divisao
```

Nesta modalidade de importe, o interpretador carrega apenas as funcionalidades **soma**, **subtracao**, **multiplicacao** e **divisao** do arquivo operation.py. Possibilitanto sua utilização dentro do arquivo main01.py sem a necessidade de referenciar o módulo de origem.

#### Importe de todo o módulo
O arquivo main02.py importa todas as funcionalidades presentes no pacote **calc** da seguinte forma.

```
import calc
```

Nesta modalidade de importe, o interpretador carrega todas as funcionalidades presentes no arquivo operation.py. Sendo necessário referenciar o módulo de origem.

#### Utilidade do arquivo __init__.py 
Para que o importe seja executado no projeto, a pasta calc possui um arquivo ____init__.py__ com o seguinte código:

```
from .operation import soma, subtracao, multiplicacao, divisao
```

Ele executa o importe das funções **soma**, **subtracao**, **multiplicacao** e **divisao** presentes no arquivo operation.py. Isto é possível pois o python executa o arquivo ____init__.py__ antes de realizar a importação das funcionalidades **soma**, **subtracao**, **multiplicacao** e **divisao**.

Até então o pytthon não sabe onde estão essas funcionalidades. A partir da execução do código presente no arquivo ____init__.py__, o python passa a conhecer a localização das funções. Sem ele o interpretador python apresentaria erro de import.

### Projeto testes_import
Este projeto foi criado com o intuito de explorar as modalidades de importações de códigos no python.

#### Importe com from
- main01.py

Utiliza ```from testes01 import eu_sou``` para o importe de todo o módulo **eu_sou.py** da pasta **teste01**. O arquivo __init__.py dentro da pasta pode ser removido, pois método de importe utilizado no arquivo **main01.py** define toda a estrutuda de pastas até alcançar o módulo desejado.
A utilização das funcionalidades importadas precisam ser precedidas do módulo de origem.

- main02.py

Utiliza ```from testes02.eu_sou import eu_sou_teste01, eu_sou_teste02``` para o importe das funcionalidades desejadas do módulo **eu_sou.py** presente na pasta **teste02**. O arquivo __init__.py dentro da pasta pode ser removido, pois método de importe utilizado no arquivo **main02.py** define toda a estrutuda de pastas até alcançar o módulo desejado.
As funcionalidades importadas devem ser utilizadas sem a identificação do módulo de origem.

- main03.py

Utiliza ```from testes03.subtest0301 import eu_sousubtest0301``` para o importe das funcionalidades desejadas do módulo **eu_sousubtest0301.py** presente na pasta **teste03/subtest0301**. Os arquivos __init__.py dentro da pasta, e sub-pasta podem ser removidos, pois método de importe utilizado no arquivo **main03.py** define toda a estrutuda de pastas até alcançar o módulo desejado.
A utilização das funcionalidades importadas precisam ser precedidas do módulo de origem.

- main04.py

Utiliza ```from testes04 import eu_sou_subteste01, eu_sou_subteste02``` para o importe das funcionalidades desejadas do módulo **eu_sousubtest0401.py** presente na pasta **teste04/subtest0401**. O arquivo __init__.py dentro da pasta **teste04** define o caminho do módulo desejado pelo arquivo **main03.py**.
As funcionalidades importadas devem ser utilizadas sem a identificação do módulo de origem.

#### Importe com import

- main10.py

Utiliza ```import testes10.eu_sou``` para o importe das funcionalidades desejadas do módulo **eu_sou.py** presente na pasta **teste10**. O arquivo __init__.py dentro da pasta pode ser removido, pois método de importe utilizado no arquivo **main10.py** define toda a estrutuda de pastas até alcançar o módulo desejado.
A utilização das funcionalidades importadas precisam ser precedidas do módulo de origem.

- main11.py

Utiliza ```import testes11``` para o importe das funcionalidades desejadas do módulo **eu_sou.py** presente na pasta **teste11**. O arquivo __init__.py dentro da pasta define o caminho para o interpretador alcançar o módulo desejado pelo arquivo **main11.py**.
As funcionalidades importadas podem ser utilizadas sem a identificação do módulo de origem.

## Opinião
As formas de importar de metodos python não se limitam às exemplificadas acima e cada uma delas possui pontos fortes e fracos a serem considerados durante o desenvolvimento dos projetos. Entretanto, focarei na utilização do arquivo **main04.py**. 

Este método deixa a utilização das funcionalidades imporadas mais concisa e organizada.

## Bibliografia de referência
- <a href="https://www.youtube.com/watch?v=H7rINLV6e0I">[YouTube]: O que é o arquivo __init__.py</a>
- <a href="https://www.youtube.com/watch?v=spXh5vDKaZU">[YouTube]: Importanto arqivos de hierarquias diferentes</a>
- <a href="https://www.youtube.com/watch?v=a5R5dvim6TQ">[YouTube]: Sistemas de imports, como o python importa código?</a>
- <a href="https://www.youtube.com/watch?v=_bZe0sh0tCs">[YouTube]: Modularização com python</a>
- <a href="https://docs.python.org/pt-br/dev/reference/import.html">[docs python]: O sistema de importação</a>
- <a href="https://docs.python.org/3/tutorial/modules.html">[docs python]: Módulos</a>
