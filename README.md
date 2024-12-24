# Projeto de Transformação de Imagens: Tons de cinza e binárias

Este projeto aplica técnicas de processamento de imagem para transformar uma imagem colorida em tons de cinza e binarizada (preto e branco). O código permite ajustar os thresholds para binarização e visualiza os resultados em tempo real.

## Tecnologias Utilizadas

- Python
- OpenCV
- Matplotlib
- NumPy
- IPyWidgets (para interatividade)

## Como Executar

### Passo 1: Clone o repositório

Clone o repositório para sua máquina local:

```
git clone https://github.com/seu-usuario/repo-nome.git
cd repo-nome
```

### Passo 2: Instale as Dependências

Instale as dependências do projeto com o pip:

```
pip install -r requirements.txt
```

### Passo 3: Execute o Notebook

Execute o notebook [analysis](./notebooks/analysis.ipynb). Abra no Jupyter ou no Google Colab para interagir com as imagens e ajustar os thresholds de binarização.

### Passo 4: Adicione sua Imagem

Suba sua imagem para ser processada e veja os resultados das transformações.

## Estrutura do Projeto

```
├── notebooks/                # Jupyter Notebooks
│   └── image_processing.ipynb # Notebook de processamento de imagem
├── src/                      # Código-fonte
│   ├── __init__.py
│   ├── process_image.py      # Funções para processamento de imagem
├── data/                     # Dados (imagens) e resultados processados
│   └── processed_images/     # Imagens processadas
├── requirements.txt          # Dependências
├── .gitignore                # Arquivos a serem ignorados pelo Git
├── README.md                 # Documentação do projeto
```

### Funcionalidades

- Transformação para Tons de Cinza: Converte a imagem original para uma escala de cinza.
- Binarização: Aplica um threshold para converter a imagem em preto e branco.
- Ajuste de Threshold: Permite alterar o valor do threshold para experimentar diferentes resultados de binarização.
- Interatividade: Use widgets para ajustar o threshold e ver os resultados em tempo real.

### Contribuições

Se você deseja contribuir para o projeto, fique à vontade para fazer um fork, adicionar suas melhorias e criar um pull request!
