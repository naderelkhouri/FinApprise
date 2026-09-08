# Graph Report - FinApprise  (2026-09-08)

## Corpus Check
- 92 files · ~17,070 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 263 nodes · 268 edges · 61 communities (46 shown, 15 thin omitted)
- Extraction: 96% EXTRACTED · 4% INFERRED · 0% AMBIGUOUS · INFERRED: 11 edges (avg confidence: 0.5)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `646bf97d`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 10|Community 10]]
- [[_COMMUNITY_Community 11|Community 11]]
- [[_COMMUNITY_Community 12|Community 12]]
- [[_COMMUNITY_Community 13|Community 13]]
- [[_COMMUNITY_Community 14|Community 14]]
- [[_COMMUNITY_Community 15|Community 15]]
- [[_COMMUNITY_Community 16|Community 16]]
- [[_COMMUNITY_Community 17|Community 17]]
- [[_COMMUNITY_Community 18|Community 18]]
- [[_COMMUNITY_Community 19|Community 19]]
- [[_COMMUNITY_Community 22|Community 22]]
- [[_COMMUNITY_Community 23|Community 23]]
- [[_COMMUNITY_Community 24|Community 24]]
- [[_COMMUNITY_Community 25|Community 25]]
- [[_COMMUNITY_Community 26|Community 26]]
- [[_COMMUNITY_Community 27|Community 27]]
- [[_COMMUNITY_Community 28|Community 28]]

## God Nodes (most connected - your core abstractions)
1. `Clients` - 19 edges
2. `name_hello()` - 11 edges
3. `ClientsForms` - 9 edges
4. `Suppliers` - 8 edges
5. `ModelsClientsRegisterTestCase` - 7 edges
6. `ViewsClientsRegisterTestCase` - 7 edges
7. `SupplierForms` - 7 edges
8. `FinAppriseDesktop` - 7 edges
9. `BaseModelWithAutor` - 6 edges
10. `RecipeCategoriesRevenues` - 6 edges

## Surprising Connections (you probably didn't know these)
- `Meta` --uses--> `Clients`  [INFERRED]
  apps/revenues/models.py → apps/clients/models.py
- `ListingClient` --uses--> `Clients`  [INFERRED]
  apps/clients/admin.py → apps/clients/models.py
- `Meta` --uses--> `Clients`  [INFERRED]
  apps/clients/forms.py → apps/clients/models.py
- `BaseModelWithAutor` --uses--> `Clients`  [INFERRED]
  apps/revenues/models.py → apps/clients/models.py
- `NewRevenues` --uses--> `Clients`  [INFERRED]
  apps/revenues/models.py → apps/clients/models.py

## Import Cycles
- None detected.

## Communities (61 total, 15 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.08
Nodes (14): ListingClient, ClientsForms, Meta, Cria uma máscara padrão para salvar os contatos no banco de dados, Cria uma máscara padrão para salvar o CNPJ ou CPF no banco de dados, Clients, Exibe a view do registro de clientes e verifica os dados inseridos pelo usuário, register_client() (+6 more)

### Community 1 - "Community 1"
Cohesion: 0.08
Nodes (17): BaseTestCase, ModelsNewRevenuesTestCase, ModelsRecipeCategoriesRevenuesTestCase, ModelsRecipeSubcategoriesRevenuesTestCase, Verifica se os campos com unique=True estão funcionando, a função espera uma fal, Contém todos os testes referentes à classe NewRevenues do modelo de receitas, Serve como base para todos as classes de testes que vamos usar, Verifica se os atributos dos campos do model de nova receita estão funcionando c (+9 more)

### Community 2 - "Community 2"
Cohesion: 0.10
Nodes (15): _clean(), validate(), validate_cnpj(), validate_cpf(), ListingSuppliers, Meta, Cria uma máscara padrão para salvar os contatos no banco de dados, Cria uma máscara padrão para salvar o CNPJ ou CPF no banco de dados (+7 more)

### Community 3 - "Community 3"
Cohesion: 0.20
Nodes (5): Verifica se o login foi bem sucedido, Verifica se o username está incorreto, Verifica se o username está incorreto, Cria um cliente para atuar como um navegador da Web fictício, permite testar vis, UtilitiesTestCase

### Community 4 - "Community 4"
Cohesion: 0.13
Nodes (9): index(), Meta, RevenuesForms, new_revenue(), TestCase, Verifica se a função que insere o nome do usuário no cabeçalho está funcionando, UtilitiesTestCase, name_hello() (+1 more)

### Community 5 - "Community 5"
Cohesion: 0.15
Nodes (7): AppConfig, ClientsConfig, IndexConfig, RevenuesConfig, SuppliersConfig, UsersConfig, UtilitiesConfig

### Community 6 - "Community 6"
Cohesion: 0.35
Nodes (5): FinAppriseDesktop, find_free_port(), main(), wait_for_server(), initialize()

### Community 7 - "Community 7"
Cohesion: 0.20
Nodes (5): ModelsClientsRegisterTestCase, Verifica se os atributos dos campos do model estão funcionando corretamente quan, Verifica se os campos com blank=True estão aceitando espaços em branco, Verifica se os campos com null=True estão aceitando espaços nulos, Verifica se os campos com unique=True estão funcionando, a função espera uma fal

### Community 8 - "Community 8"
Cohesion: 0.20
Nodes (5): ModelsSuppliersRegisterTestCase, Verifica se os atributos dos campos do model estão funcionando corretamente quan, Verifica se os campos com blank=True estão aceitando espaços em branco, Verifica se os campos com null=True estão aceitando espaços nulos, Verifica se os campos com unique=True estão funcionando, a função espera uma fal

### Community 9 - "Community 9"
Cohesion: 0.17
Nodes (9): ListingCategoriesRevenues, ListingRevenues, ListingSubcategoriesRevenues, BaseModelWithAutor, Meta, NewRevenues, Utilizado para inserir o username do usuário logado nos formularios que possuem, RecipeCategoriesRevenues (+1 more)

### Community 10 - "Community 10"
Cohesion: 0.20
Nodes (5): Cria o ambiente de testes, Verifica se está sendo redirecionado para a página de index ao enviar o formulár, Verifica se está sendo redirecionado para a página de login ao enviar o formulár, Verifica se está sendo redirecionado para a página de login ao enviar o formulár, ViewsSuppliersRegisterTestCase

### Community 11 - "Community 11"
Cohesion: 0.33
Nodes (5): 1. Visão Geral do Sistema, 2. Estrutura Modular (Django Apps), 3. Execução Desktop, 4. Banco de Dados e Migrações, FinApprise - Especificação Técnica e Arquitetura

## Knowledge Gaps
- **22 isolated node(s):** `Migration`, `ListingRevenues`, `ListingSubcategoriesRevenues`, `ListingCategoriesRevenues`, `Meta` (+17 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **15 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Clients` connect `Community 0` to `Community 9`, `Community 7`?**
  _High betweenness centrality (0.169) - this node is a cross-community bridge._
- **Why does `BaseTestCase` connect `Community 1` to `Community 4`?**
  _High betweenness centrality (0.114) - this node is a cross-community bridge._
- **Why does `ModelsClientsRegisterTestCase` connect `Community 7` to `Community 0`, `Community 4`?**
  _High betweenness centrality (0.079) - this node is a cross-community bridge._
- **Are the 10 inferred relationships involving `Clients` (e.g. with `ListingClient` and `ClientsForms`) actually correct?**
  _`Clients` has 10 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `ClientsForms` (e.g. with `Clients` and `FormsClientsRegisterTestCase`) actually correct?**
  _`ClientsForms` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Cria uma máscara padrão para salvar os contatos no banco de dados`, `Cria uma máscara padrão para salvar o CNPJ ou CPF no banco de dados`, `Migration` to the rest of the system?**
  _69 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Community 0` be split into smaller, more focused modules?**
  _Cohesion score 0.08387096774193549 - nodes in this community are weakly interconnected._