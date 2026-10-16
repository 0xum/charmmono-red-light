# Charmmono Red Light

Variante local baseada no **Charmmono Light 0.3.1**, de Sumangal Karan (MIT).

Mantém a estrutura, o fundo branco e as regras de sintaxe do tema original.
Substitui os destaques roxos por vermelho carmim, com seleções em vermelho
claro e superfícies levemente aquecidas. As cores de diagnósticos, Git e
ANSI do terminal mantêm seu significado original. Os ícones não são alterados.

| Uso | Cor |
| --- | --- |
| Destaque principal e funções | `#B4232D` |
| Hover e cursor | `#991B24` |
| Links ativos | `#7F1D1D` |
| Foco e abas ativas | `#C9434C` |
| Superfícies secundárias | `#FCF7F6` |
| Seleção | `#F7B9B399` |

## Instalar em outro ambiente

O pacote pronto está em `dist/charmmono-red-light-1.0.0.vsix` e pode ser
instalado no VS Code em Linux, macOS ou Windows.

Clone este repositório (depois de hospedá-lo em um servidor Git) ou copie a
pasta para o outro ambiente. No terminal, dentro desta pasta, execute:

```sh
code --install-extension dist/charmmono-red-light-1.0.0.vsix
```

Também é possível abrir **Extensions**, escolher **Install from VSIX…**
no menu `…` e selecionar esse arquivo, sem precisar do comando `code`.

Depois, abra **Preferences: Color Theme** na paleta de comandos e selecione
**Charmmono Red Light**. A instalação não exige Python nem a extensão original.

## Ajustar e reinstalar

Edite `themes/charmmono-red-light-color-theme.json` e execute nesta pasta:

```sh
python3 build.py
code --install-extension dist/charmmono-red-light-1.0.0.vsix --force
```

O empacotamento usa apenas Python 3, sem bibliotecas adicionais. No Windows,
use `py -3 build.py` se o comando `python3` não estiver disponível. O pacote
leva a versão de `package.json`; ao alterá-la, ajuste o nome no comando de instalação.

Escolha **Charmmono Red Light** em **Preferences: Color Theme**. Caso o VS Code
não atualize a extensão imediatamente, execute **Developer: Reload Window**.
Para voltar ao original, escolha **charmmono-Theme-light**.

A extensão tem identidade própria (`delta-local.charmmono-red-light`) e não
é substituída pelas atualizações do Charmmono original. É exclusivamente
de tema: não possui código de ativação, dependências ou acesso à rede.

O arquivo `LICENSE.txt` preserva a licença e a atribuição do tema original.

## Salvar alterações no Git

Depois de editar o tema, recrie o pacote com `python3 build.py` e versione
tanto o arquivo do tema quanto o `.vsix`, para manter a instalação pronta:

```sh
git add .
git commit -m "Ajusta as cores do tema"
git push
```

Para enviar este repositório a um servidor pela primeira vez, crie um
repositório vazio no serviço escolhido e configure sua URL:

```sh
git remote add origin URL_DO_REPOSITORIO
git push -u origin HEAD
```
