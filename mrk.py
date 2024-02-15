# Abrir o arquivo .toc e ler as informações do sumário
with open('python/python.toc', 'r') as toc_file:
    toc_lines = toc_file.readlines()
    print(toc_lines)
# Extrair os títulos das seções do sumário
def extract_section_title(line):
# Encontrar a posição do primeiro '{'
    start_index = line.find('n')
    if start_index == -1:
        return None  # Se não encontrar '{', retornar None
    # Encontrar a posição do primeiro '}'
    end_index = line.find('%')
    if end_index == -1:
        return None  # Se não encontrar '}', retornar None
    # Extrair o título da seção
    title = line[start_index + 1:end_index]
    return title

#section_titles = [line.split('}')[1] for line in toc_lines if 'section' in line]
section_titles = [extract_section_title(line) for line in toc_lines]
print(section_titles)

# Formatando para Markdown
markdown_toc = "## Sumario\n\n"
for title in section_titles:
    # Calculando o nível da seção
    level = title.count('sub') + 1
    # Convertendo para Markdown, adicionando a devida indentação
    markdown_toc += f"{'###' * level} {title}\n\n"

# Escrevendo o sumário formatado para Markdown em um arquivo
with open('README.md', 'w') as markdown_file:
    markdown_file.write(markdown_toc)
