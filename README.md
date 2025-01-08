# Interior Designer AI Assistant

Este projeto é uma aplicação interativa que utiliza IA para gerar sugestões personalizadas de design de interiores. A interface é construída com Streamlit, permitindo que os usuários forneçam imagens de referência e requisitos de design para obter sugestões visuais que correspondam aos seus gostos e necessidades específicas.

## Funcionalidades

- **Upload de Imagens**: Envie uma imagem de um cômodo vazio e uma imagem de estilo de design de referência.
- **Escolha do Tipo de Cômodo**: Selecione o tipo de cômodo (ex.: sala de estar, cozinha, quarto, etc.).
- **Especificações de Design**: Insira detalhes e requisitos específicos para o design do interior.
- **Geração de Design**: A IA processa as entradas e gera imagens de designs sugeridos com base nas suas preferências.
- **Exibição Dinâmica**: Visualize as imagens geradas em uma grade, diretamente na interface do Streamlit.

## Tecnologias Utilizadas

- **Python 3.8+**
- **Streamlit**: Framework para construção de interfaces web interativas.
- **Pillow**: Biblioteca para manipulação de imagens.
- **Requests**: Para o download de imagens a partir de URLs fornecidas.
- **Dotenv**: Carrega variáveis de ambiente de um arquivo `.env`.
- **Agente de IA**: O módulo `interior_design_for` gera o design de interiores com base nos dados de entrada.

## Pré-requisitos

- **Python 3.8+**
- **Pip** para instalar as dependências.

## Instalação

1. Clone o repositório:
    ```
    git clone https://github.com/seu-repositorio/interior-designer-ai-assistant.git
    ```

2. Navegue até o diretório do projeto:
    ```
    cd interior-designer-ai-assistant
    ```

3. Crie um ambiente virtual (opcional, mas recomendado):
    ```
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

4. Instale as dependências necessárias:
    ```
    pip install -r requirements.txt
    ```

5. Crie um arquivo `.env` com as variáveis de ambiente necessárias (se aplicável).

6. Execute a aplicação:
    ```
    streamlit run app.py
    ```

7. Acesse o aplicativo no navegador no endereço padrão: `http://localhost:8501`.

## Como Usar

1. **Imagem do Cômodo Vazio**: Insira a URL de uma imagem de um cômodo vazio no campo correspondente na barra lateral.
   
2. **Tipo de Cômodo**: Selecione o tipo de cômodo que deseja projetar a partir da lista fornecida.

3. **Imagem de Referência de Estilo**: Insira a URL de uma imagem de referência de estilo que deseja aplicar ao design do cômodo.

4. **Requisitos de Design**: Digite os detalhes e exigências específicas do design, como cores preferidas, tipos de móveis, iluminação, etc.

5. **Gerar Design**: Quando todas as informações forem fornecidas, clique no botão "Generate" na barra lateral para iniciar o processo de geração de design de interiores.

6. **Visualizar o Resultado**: Após a geração, as imagens dos designs sugeridos serão exibidas em uma grade na página principal do aplicativo.

## Estrutura de Pastas

```
├── app.py                # Arquivo principal da aplicação Streamlit
├── agents.py             # Módulo que contém a função de geração de design
├── requirements.txt      # Arquivo com as dependências do projeto
├── .env                  # Variáveis de ambiente (não incluído no repositório)
└── output/               # Pasta onde as imagens geradas são salvas
```

## Tratamento de Erros

- Se o aplicativo não conseguir baixar as imagens a partir das URLs fornecidas, uma mensagem de erro será exibida.
- Certifique-se de que todas as entradas (URL de imagens, requisitos e tipo de cômodo) estejam preenchidas para habilitar o botão "Generate".

## Contribuições

Contribuições são bem-vindas! Para contribuir, siga os passos abaixo:

1. Faça um fork deste repositório.
2. Crie uma nova branch com suas alterações: `git checkout -b minha-nova-funcionalidade`.
3. Commit suas mudanças: `git commit -m 'Adiciona nova funcionalidade'`.
4. Envie para o branch original: `git push origin minha-nova-funcionalidade`.
5. Abra um pull request.

## Licença

Este projeto está licenciado sob os termos da licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais informações.

---

Se precisar de ajustes ou mais informações, é só avisar!
