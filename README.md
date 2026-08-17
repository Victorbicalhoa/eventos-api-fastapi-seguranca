# Eventos API — FastAPI e Segurança

Projeto acadêmico de uma API REST para gerenciamento de eventos, desenvolvido com FastAPI e organizado para demonstrar fundamentos de desenvolvimento seguro.

## Principais conceitos demonstrados

- rotas modulares com `APIRouter`;
- contratos Pydantic separados para entrada, armazenamento interno e resposta pública;
- filtragem de campos sensíveis com `response_model`;
- páginas HTML com Jinja2, auto-escape e herança de templates;
- separação entre `routes`, `models` e `database`;
- análise da tríade CIA;
- DFD com trust boundaries e fluxo de dados sensíveis;
- associação de controles à OWASP API Security, NIST SSDF e MITRE CWE.

> [!WARNING]
> A rota `POST /eventos/sem-response-model` é deliberadamente insegura e existe somente para demonstrar exposição excessiva de dados. O projeto não deve ser implantado publicamente sem remover essa rota e implementar autenticação, autorização e controles de disponibilidade.

## Estrutura

```text
eventos-api-fastapi-seguranca/
├── app/
│   ├── database/       # armazenamento simulado e operações de dados
│   ├── models/         # contratos Pydantic de entrada, internos e públicos
│   ├── routes/         # rotas JSON e páginas HTML
│   └── templates/      # templates Jinja2 e layout compartilhado
├── docs/
│   ├── dfd_eventos.md
│   └── tabela_frameworks.md
├── main.py
└── requirements.txt
```

## Executando localmente

Requer Python 3.14 ou uma versão compatível.

```powershell
python -m virtualenv .venv
```

No PowerShell, ative o ambiente:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instale as dependências e inicie o servidor:

```powershell
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload
```

Acesse:

- Swagger UI: `http://127.0.0.1:8000/docs`
- API: `http://127.0.0.1:8000/eventos`
- página HTML: `http://127.0.0.1:8000/painel/eventos`

## Endpoints

| Método | Caminho | Finalidade |
|---|---|---|
| `GET` | `/` | Estado básico do serviço |
| `GET` | `/eventos` | Lista os eventos com modelo público |
| `GET` | `/eventos/{evento_id}` | Consulta um evento pelo ID |
| `POST` | `/eventos` | Cria um evento e filtra a resposta |
| `POST` | `/eventos/sem-response-model` | Demonstração acadêmica de vazamento de campos internos |
| `GET` | `/painel/eventos` | Lista eventos em HTML |
| `GET` | `/painel/eventos/{evento_id}` | Exibe detalhes de um evento em HTML |

Exemplo de criação:

```json
{
  "name": "Conferência de Segurança",
  "data": "2026-09-15",
  "organizador": "Equipe de Eventos"
}
```

## Segurança

O modelo interno contém `organizador_id` e `token_auditoria`, mas os endpoints normais utilizam `EventoPublico` para impedir que esses campos sejam enviados ao cliente. Nos templates, entradas do usuário são renderizadas com auto-escape e sem o filtro `safe`.

O [DFD](docs/dfd_eventos.md) registra as fronteiras de confiança e os fluxos sensíveis. A [tabela de frameworks](docs/tabela_frameworks.md) relaciona os controles implementados à OWASP, ao NIST SSDF e à MITRE CWE.

## Limitações conhecidas

- armazenamento apenas em memória;
- ausência de autenticação e autorização;
- ausência de rate limiting;
- identificadores simplificados;
- rota vulnerável mantida para demonstração;
- testes ainda manuais.

## Próximas evoluções

- adicionar testes automatizados com `pytest`;
- persistir os dados com SQLAlchemy e SQLite ou PostgreSQL;
- implementar autenticação e autorização;
- validar limites dos campos de entrada;
- remover a rota demonstrativa antes de qualquer implantação.
