# Site institucional — Unité

Landing page estática (HTML + CSS puro, sem build) do studio Unité - Centro de Reestruturação Corporal.

- **Produção:** unitepilates.com.br (após configuração de DNS)
- **Botão "Acessar Sistema"** aponta para `app.unitepilates.com.br` — o sistema de gestão (repositório separado: `pilates-unite`), que será movido para esse subdomínio.

## Estrutura

- `index.html` — todo o conteúdo da página (seção única, âncoras internas)
- `style.css` — estilos
- `img/` — fotos otimizadas para web, usadas pelo site
- `fotos-originais/`, `fotos/`, `preparar_imagens.py` — não versionados (`.gitignore`); material bruto e script usado para gerar as imagens finais em `img/`, caso precise regenerar com fotos novas

## Publicando mudanças

Como é um site estático puro, não há build: qualquer alteração em `index.html`/`style.css`/`img/` já é o resultado final. Basta commitar e enviar (`git push`) — o Render reimplanta automaticamente.
