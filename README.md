# b3-stock-tracker

> API em Python com histórico de preços e indicadores de ações da B3.

**Status:** em desenvolvimento. Hoje o projeto só busca o histórico de preços de fechamento; a API e os indicadores ainda não existem.

## Pré-requisitos

- [Python](https://www.python.org/downloads/) 3.13 ou superior (na instalação, marque **"Add python.exe to PATH"**)
- [Git](https://git-scm.com/downloads)

Os comandos abaixo foram escritos para **Windows (PowerShell)**.

## Como rodar

1. Clone o repositório e entre na pasta:

   ```powershell
   git clone https://github.com/Apollo-stack/b3-stock-tracker.git
   cd b3-stock-tracker
   ```

2. Crie o ambiente virtual:

   ```powershell
   py -m venv .venv
   ```

3. Ative o ambiente virtual:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

4. Instale as dependências:

   ```powershell
   pip install -r requirements.txt
   ```

## Como usar

Na raiz do projeto, crie um arquivo (por exemplo `exemplo.py`) com:

```python
from src.data_fetcher import price_series

prices = price_series("PETR4")
print(prices)
```

Rode com `python exemplo.py`. O resultado são os preços de fechamento dos últimos 5 dias.

Informe apenas o código da ação, **sem** o `.SA`: a função adiciona o sufixo sozinha. Se o código não existir ou não tiver dados, a função lança um `ValueError`.

## Limitações conhecidas

- Os dados vêm da biblioteca `yfinance`, que é não oficial e pode falhar ou mudar sem aviso.
- O período está fixo em 5 dias.

## Licença

Distribuído sob a licença MIT. Veja o arquivo `LICENSE`.