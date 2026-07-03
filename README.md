# Arquitetura de Dados — modelo Medalhão (DBT + Python + DuckDB)

Descrição
---------
Este repositório contém uma arquitetura de dados baseada no modelo medalhão (bronze, silver, gold), implementada com DBT, scripts em Python e DuckDB como engine de processamento/desenvolvimento.

Componentes principais
- Bronze: ingestão e armazenamento bruto dos dados (ponto de entrada, mínima transformação).
- Silver: limpeza, deduplicação e enriquecimento dos dados para análise.
- Gold: modelos prontos para consumo (relatórios, dashboards, ML features).

Tecnologias
- DBT: orquestração e transformação modularizada dos modelos SQL (versões, testes, documentação).
- Python: scripts de ingestão, validação e tarefas auxiliares (pré-processamento, chamadas a APIs, jobs agendados).
- DuckDB: motor SQL embutido, leve e rápido para desenvolvimento e testes de pipeline.

Como usar (resumo)
1. Preparar o ambiente: instalar dependências (DBT, DuckDB, bibliotecas Python).
2. Executar ingestão: scripts Python para popular a camada bronze.
3. Rodar DBT: executar os modelos por camada (bronze -> silver -> gold) com dbt run e dbt test.
4. Validar: conferir testes e amostras de saída no DuckDB.

Boas práticas
- Versionamento de modelos DBT e testes automatizados.
- Separação clara entre camadas (bronze/silver/gold) para rastreabilidade.
- Uso de DuckDB para desenvolvimento local e migração para engines maiores em produção.

Este README deve ser complementado com instruções específicas de setup, dependências e exemplos de execução conforme o projeto evolui.

