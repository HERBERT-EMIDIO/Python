# Ada - Let's Code
Santander Coders
# Aula 01 - Estados do Git

## Untracked (não rastreado)
- Arquivos novos que foram adicionados ao diretório do projeto, mas que ainda não foram adicionados ao controle de versão do Git.
- O Git não inclui esses arquivos nas operações de commit até que sejam explicitamente adicionados.

## Unmodified (não modificado)
- Arquivos que estão no repositório do Git e não foram alterados desde o último commit.
- Estes arquivos estão sincronizados com o repositório.

## Modified (modificado)
- Arquivos que foram alterados após o último commit, mas ainda não foram adicionados ao índice (staging area).
- Essas alterações estão apenas no seu diretório de trabalho e ainda não fazem parte da história do Git.

## Staged (indexado)
- Arquivos que foram modificados e, em seguida, adicionados ao índice usando `git add`.
- Esses arquivos estão preparados para o próximo commit. As mudanças nesses arquivos serão incluídas no próximo snapshot do repositório.

## Committed (comitado)
- As mudanças nos arquivos indexados foram salvas no repositório.
- Um commit cria um ponto de verificação permanente no histórico do repositório, com um identificador único (hash) associado.

## Fluxo de Trabalho Típico

1. **Criar ou modificar um arquivo**: O arquivo começa como **untracked** se for novo, ou **modified** se for um arquivo existente.
2. **Adicionar o arquivo ao índice**: Usa-se o comando `git add <arquivo>`. O arquivo passa para o estado **staged**.
3. **Comitar as mudanças**: Usa-se o comando `git commit -m "mensagem do commit"`. O arquivo passa para o estado **committed** e **unmodified** até que seja alterado novamente.


## Comando usado em aula - git:
** git status **
** git add .\nome.md **
** git diff **
** git diff --staged **
** git log **
** git restore .\nome.md **
** git restore --staged .\nome.md **
** git commit -m "nome do commit" **
** git remote **
** git push origin main **
** git pull **
