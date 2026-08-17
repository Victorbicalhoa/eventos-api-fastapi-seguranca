# Associação entre frameworks e controles

| Referencial | Controle concreto no projeto | Relação de segurança | Limitação atual |
|---|---|---|---|
| OWASP API Security — API3:2023, Broken Object Property Level Authorization | `response_model=EventoPublico` nos endpoints normais | Define explicitamente os campos permitidos na saída e impede que `organizador_id` e `token_auditoria` sejam serializados para o cliente. | A rota acadêmica `/eventos/sem-response-model` preserva intencionalmente o vazamento e deve ser removida antes de produção. |
| NIST SSDF SP 800-218 — PW.4.1 | Ambiente `.venv` isolado e versões registradas em `requirements.txt` | Apoia a aquisição e manutenção controlada de componentes de terceiros, reduzindo conflitos e permitindo reproduzir o conjunto de dependências. | Isolamento e registro de versões não bastam para conformidade: ainda faltam análise de vulnerabilidades, origem confiável e processo de atualização. |
| MITRE CWE-79 — Improper Neutralization of Input During Web Page Generation | Auto-escape do Jinja2 e ausência do filtro `safe` para dados do usuário | Caracteres especiais do nome do evento são codificados antes de entrar no HTML, mitigando a execução de um payload XSS. | A proteção pode ser anulada se um valor não confiável for marcado como seguro ou inserido em contexto inadequado; por isso, o uso futuro dos templates deve ser revisado. |

## Referências

- [OWASP API3:2023 — Broken Object Property Level Authorization](https://owasp.org/API-Security/editions/2023/en/0xa3-broken-object-property-level-authorization/)
- [NIST SP 800-218 — Secure Software Development Framework 1.1](https://csrc.nist.gov/pubs/sp/800/218/final)
- [MITRE CWE-79 — Cross-site Scripting](https://cwe.mitre.org/data/definitions/79.html)

As associações indicam aderência pontual dos controles implementados; não constituem certificação ou conformidade integral com os referenciais.
