# data_sprint
Case técnico da data sprint

Foi utilizado o Python 3.8.8 para realização do case técnico.

Para utilização do código é necessário o pacote pandas instalado, e foi utilizado a interface Jupyter Notebook para visualização dos gráficos.

Como foi rodado o código em partes, é necessário executar cada função plot() separadamente para aparecer os gráficos corretamente.

Primeiramente, é importado a biblioteca pandas e a datetime. Depois é lido os JSON's disponibilizados com os nomes de: 'data-sample_data-nyctaxi-trips-20XX-json_corrigido.json', onde os XX podem ser trocados de acordo com o ano.

Depois disso, foi feito a separação dos dados para análise de acordo com o case técnico.

1. Qual a distância média percorrida por viagens com no máximo 2 passageiros;

Para isso, foi feito uma separação dos dados das corridas com 2 ou menos passageiros.

Depois foi feito em cada dataframe a média da distância percorrida, e depois novamente a média de todas as médias.

O resultado foi: 2.662526996203298. Como os dados são de Nova Iorque, deduzo que essa métrica esteja em milhas.

2. Quais os 3 maiores vendors em quantidade total de dinheiro arrecadado;

Para isso, foi agrupado os dados por 'vendor_id', e feito a soma das colunas, depois é gerado o gráfico com o total das vendas e os id dos vendedores. Os gráficos gerados foram os seguintes:

2009: ![alt text](https://imgur.com/hHlPVXl)
