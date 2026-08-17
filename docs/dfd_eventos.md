# DFD — Eventos API

Este diagrama representa o fluxo de dados atual da aplicação. As linhas `TB-1` e `TB-2` são fronteiras de confiança: sempre que um fluxo as atravessa, os dados devem ser validados, filtrados ou protegidos conforme sua sensibilidade.

```mermaid
flowchart LR
    subgraph Z1["Zona externa — não confiável"]
        U["E1 — Usuário / organizador<br/>Navegador ou cliente da API"]
    end

    subgraph Z2["Zona da aplicação — confiável"]
        R["P1 — Rotas FastAPI<br/>JSON e HTML"]
        V["P2 — Pydantic<br/>validação e response_model"]
        J["P3 — Jinja2<br/>renderização com auto-escape"]
    end

    subgraph Z3["Zona de armazenamento interno"]
        D[("D1 — _eventos<br/>armazenamento em memória")]
    end

    U -->|"F1 — POST JSON: nome, data e organizador<br/>atravessa TB-1"| R
    R -->|"dados de entrada"| V
    V -->|"F2 — EventoInterno: dados do organizador<br/>e token de auditoria — SENSÍVEL<br/>atravessa TB-2"| D
    D -->|"F3 — leitura de EventoInterno — SENSÍVEL<br/>atravessa TB-2"| R
    R -->|"dados para resposta JSON"| V
    V -->|"F4 — JSON público filtrado<br/>atravessa TB-1"| U
    R -->|"dados para a página"| J
    J -->|"F5 — HTML com conteúdo escapado<br/>atravessa TB-1"| U
    R -.->|"F6 — rota acadêmica sem response_model<br/>RISCO: campos internos atravessam TB-1"| U

    classDef sensitive fill:#ffe0e0,stroke:#b71c1c,color:#5f0000,stroke-width:2px;
    classDef control fill:#e3f2fd,stroke:#1565c0,color:#0d2740;
    classDef external fill:#fff3e0,stroke:#e65100,color:#4e2600;
    class D sensitive;
    class V,J control;
    class U external;
```

## Fronteiras de confiança

- **TB-1 — Cliente ↔ aplicação:** separa o navegador ou cliente da API, que não é confiável, do processo FastAPI. A entrada precisa ser validada pelo Pydantic; na saída, o `response_model` filtra o JSON e o Jinja2 escapa conteúdo inserido no HTML.
- **TB-2 — aplicação ↔ armazenamento:** separa logicamente o processamento HTTP da camada de dados. No protótipo, o armazenamento está no mesmo processo, mas o limite continua relevante porque a aplicação grava e recupera objetos que contêm campos internos.

## Fluxos sensíveis

O fluxo **F2** leva `organizador`, `organizador_id` e `token_auditoria` ao armazenamento, atravessando a TB-2. O fluxo **F3** devolve esse objeto interno para processamento. Antes de qualquer saída pela TB-1, o fluxo normal passa pelo `EventoPublico`, que remove `organizador_id` e `token_auditoria`. O fluxo demonstrativo **F6** evidencia a falha: sem `response_model`, esses campos internos cruzam a fronteira externa e chegam ao cliente.

## Legenda

- `E1`: entidade externa;
- `P1` a `P3`: processos;
- `D1`: armazenamento de dados;
- `F1` a `F6`: fluxos de dados;
- seta tracejada: fluxo deliberadamente inseguro mantido apenas para demonstração acadêmica.
