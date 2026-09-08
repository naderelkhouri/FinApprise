# FinApprise - Especificação Técnica e Arquitetura

## 1. Visão Geral do Sistema
O **FinApprise** é uma plataforma de gestão financeira e contábil desenvolvida em Python (Django), empacotada para execução tanto como aplicação desktop nativa (Linux GTK3 + WebKit2) quanto como aplicação web.

## 2. Estrutura Modular (Django Apps)
- **`apps.users`**: Gerenciamento de credenciais, autenticação e perfis de operadores.
- **`apps.clients`**: Cadastro e manutenção de clientes comerciais, validação de CPF/CNPJ (`docbr.py`).
- **`apps.suppliers`**: Gestão de fornecedores de mercadorias e prestadores de serviços.
- **`apps.revenues`**: Registro e acompanhamento de receitas, categorias contábeis e subcategorias.
- **`apps.utilities`**: Funções compartilhadas, contexto de usuário e formatadores.
- **`apps.index`**: Dashboard e visualização consolidada dos fluxos financeiros.

## 3. Execução Desktop
- **Launcher Nativo (`gui.py`)**:
  - Inicia o servidor Django em porta dinâmica (`127.0.0.1:8000+`).
  - Renderiza a aplicação via `WebKit2.WebView` integrado ao `Gtk.Window`.
  - Atribui ícone oficial, título e atalhos de controle (`Ctrl +/-/0`, `F11`, `F5`).
  - Encerra de forma limpa os processos subordinados na saída (`destroy`).
- **Atalhos do Sistema**:
  - `~/.local/share/applications/finapprise.desktop` (Menu do sistema).
  - `/home/nader/Desktop/finapprise.desktop` (Área de Trabalho).
  - `/home/nader/.local/bin/finapprise` (Terminal global).

## 4. Banco de Dados e Migrações
- **Padrão:** SQLite local em `db.sqlite3` com auto-migração e seeding de dados via `init_db.py`.
- **Corporativo:** Suporte chaveado via variável de ambiente `DB_ENGINE=mssql` para Microsoft SQL Server via ODBC.
