
# Korean International Trade Scraper

Este projeto é um scraper desenvolvido em Python que coleta informações sobre estatísticas de comércio entre a Coréia do Sul e países estrangeiros do site [TradeData](https://tradedata.go.kr/cts/index_eng.do#tabHsSgn2). Ele foi projetado para lidar com múltiplas páginas e utiliza uma API oculta, descoberta através da inspeção da página, para realizar requisições assíncronas de forma eficiente.

## Funcionalidades

- **Raspagem de Dados:** Coleta informações sobre importação e exportação entre a Coréia do Sul e países estrangeiros.
- **Requisições Assíncronas:** Utiliza `aiohttp` e `asyncio` para melhorar o desempenho do scraper, especialmente ao lidar com múltiplas páginas.
- **Geração de DataFrame:** Os dados coletados são organizados em um `pandas DataFrame`.
- **Armazenamento em CSV:** Os dados são salvos em um arquivo CSV estruturado para análise posterior.

## Dados Coletados

O scraper coleta as seguintes informações do site:

- **Período:** Ano em que o comércio ocorreu.
- **País:** País com o qual a Coréia comercializou.
- **Mercadorias:** Mercadorias que foram comercializadas.
- **Peso de Exportação:** Peso das exportações em toneladas.
- **Valor de Exportação:** Valor monetário das exportações em dólares.
- **Peso de Importação:** Peso das importações em toneladas.
- **Valor de Importação:** Valor monetário das importações em dólares.
- **Balança Comercial:** Diferença entre o valor das exportações e importações.

## Tecnologias Utilizadas

- **Python 3.x**
- **aiohttp**: Para requisições HTTP assíncronas.
- **asyncio**: Para gerenciar a execução assíncrona.
- **pandas**: Para manipulação e análise de dados.
- **CSV**: Para armazenamento de dados.

## Como Usar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu_usuario/nome_do_repositorio.git
   cd nome_do_repositorio
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute o scraper:**
   ```bash
   python scrape/scrapy.py "nome_do_arquivo_de_saida"
   ```

4. **Acesse os dados:**

   Os dados coletados estarão disponíveis no arquivo `nome_informado.csv` gerado na raiz do projeto.

## Estrutura do Projeto

- `scrape`: Modulo que armazena os arquivos fontes do projeto, como o script e uma amostra dos dados raspados.
- `scrapy.py`: Script principal que realiza a raspagem e salva os dados.
- `requirements.txt`: Lista de dependências do projeto.
- `nome_informado.csv`: Arquivo gerado com os dados coletados.

## Contribuições

Este projeto foi desenvolvido como parte do meu portfólio pessoal para demonstrar minhas habilidades técnicas. Se você encontrar algo que possa ser melhorado ou tiver ideias para expandir o projeto, sinta-se à vontade para contribuir ou compartilhar feedback.

## Licença

Este projeto é livre para uso, modificação e distribuição. Não há uma licença específica associada a este projeto, portanto, sinta-se à vontade para utilizá-lo como preferir.
