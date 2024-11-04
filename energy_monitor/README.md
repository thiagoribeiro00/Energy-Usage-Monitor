# Monitoramento de Consumo de Energia

Este é um aplicativo de monitoramento e análise de dados de consumo de energia, desenvolvido com **Streamlit** e **OpenAI**. O objetivo é fornecer uma interface interativa para visualizar, filtrar e realizar perguntas sobre dados de consumo de energia, utilizando um modelo de linguagem para responder a consultas sobre os dados.

## Descrição do Projeto

O aplicativo permite aos usuários filtrar dados históricos de consumo de energia com base em datas, ID da casa, status de ocupação e tipo de casa. Além de exibir uma tabela de dados filtrados, o aplicativo oferece visualizações gráficas e uma seção de perguntas, onde o modelo de linguagem da OpenAI pode responder a perguntas específicas sobre o conjunto de dados exibido.

### Funcionalidades Principais

- **Filtros Personalizados**: Possibilidade de filtrar dados por intervalo de datas, ID da casa, status de ocupação e tipo de casa.
- **Visualização Gráfica**: Gráfico de linha que mostra o consumo de energia ao longo do tempo para o intervalo selecionado.
- **Perguntas Inteligentes**: Utilização da API da OpenAI para responder a perguntas sobre os dados filtrados, permitindo obter insights de maneira interativa.

## Estrutura do Aplicativo

- **Filtros na Sidebar**: Permite ajustar o intervalo de datas, ID da casa, status de ocupação e tipo de casa para refinar a visualização dos dados.
- **Tabela de Dados Filtrados**: Exibe os dados de consumo de energia com base nos filtros selecionados.
- **Gráfico de Consumo ao Longo do Tempo**: Exibe um gráfico de linha que permite identificar picos e tendências no consumo de energia.
- **Seção de Perguntas**: Possibilita ao usuário fazer perguntas sobre os dados e receber respostas do modelo da OpenAI.

## Objetivos do Projeto

O projeto tem como objetivo fornecer uma plataforma de análise que auxilie na visualização e compreensão do consumo de energia em diferentes residências. As funcionalidades permitem que analistas e gestores de energia:

1. **Identifiquem Padrões de Consumo**: Analisem os picos de consumo e as tendências ao longo do tempo.
2. **Respondam a Perguntas Complexas**: Façam perguntas detalhadas sobre os dados e obtenham respostas com o uso de inteligência artificial.
3. **Explore Diferentes Segmentações de Dados**: Filtre o consumo por status de ocupação e tipo de residência para explorar como esses fatores influenciam o consumo.

## Possíveis Insights

Este aplicativo pode fornecer insights valiosos, incluindo:

- **Identificação de Picos de Consumo**: Facilita a identificação de picos sazonais e diários de consumo.
- **Análise por Status de Ocupação e Tipo de Residência**: Mostra como diferentes status de ocupação ou tipos de residência afetam o consumo.
- **Tendências de Consumo ao Longo do Tempo**: Auxilia no monitoramento de padrões e mudanças no consumo de energia.
