"""
My first application
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER, ROW


class listaTelefonica(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

        title_label = toga.Label(
            'Informe os dados para cadastro', 
            style=Pack(padding=(0, 5), font_size=20, text_align=CENTER)
        )

        # Caixa para o campo de nome
        name_box = toga.Box(style=Pack(direction=COLUMN, padding=5))
        name_label = toga.Label('Nome: ', style=Pack(padding=(0, 5)))
        self.name_input = toga.TextInput(style=Pack(flex=1, padding=(0, 5)))
        name_box.add(name_label)
        name_box.add(self.name_input)

        # Caixa para o campo de telefone
        telefone_box = toga.Box(style=Pack(direction=COLUMN, padding=5))
        telefone_label = toga.Label('Telefone: ', style=Pack(padding=(0, 5)))
        self.telefone_input = toga.TextInput(style=Pack(flex=1, padding=(0, 5)))
        telefone_box.add(telefone_label)
        telefone_box.add(self.telefone_input)

        button = toga.Button('Adicionar novo contato', on_press=self.add_contact, style=Pack(padding=5))

        # Tabela para a lista de contatos
        self.contact_table = toga.Table(
            headings=['Nome', 'Telefone'],
            style=Pack(flex=1),
            on_select=self.on_select_row  # Evento on_select adicionado
        )

        # Botões para editar e excluir
        self.edit_button = toga.Button('Editar', on_press=self.edit_contact, style=Pack(padding=5), enabled=False)
        self.delete_button = toga.Button('Excluir', on_press=self.delete_contact, style=Pack(padding=5), enabled=False)

        # Adiciona o título, os campos de entrada e a tabela à caixa principal
        main_box.add(title_label)
        main_box.add(name_box)
        main_box.add(telefone_box)
        main_box.add(button)
        main_box.add(self.contact_table)
        main_box.add(self.edit_button)
        main_box.add(self.delete_button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def add_contact(self, widget):
        # Recupera os valores dos campos de entrada
        name = self.name_input.value
        telefone = self.telefone_input.value

        # Adiciona uma nova linha à tabela de contatos
        self.contact_table.data.append((name, telefone))

        # Atualiza a interface gráfica para refletir as mudanças
        self.main_window.content.refresh()

        # Limpa os campos de entrada
        self.name_input.value = ''
        self.telefone_input.value = ''

    def on_select_row(self, widget, row=None):
        # Verifica se uma linha está selecionada diretamente
        selected_row = self.contact_table.selection
        print(f'Row selected: {selected_row}')
        
        # Habilita os botões de editar e excluir quando uma linha é selecionada
        if selected_row:
            self.edit_button.enabled = True
            self.delete_button.enabled = True
        else:
            self.edit_button.enabled = False
            self.delete_button.enabled = False

    def edit_contact(self, widget):
        # Recupera a linha selecionada
        row = self.contact_table.selection

        if row:
        # Acesse os valores da linha selecionada usando os nomes dos campos
            self.name_input.value = row.nome  # Acesse o valor do campo 'nome'
            self.telefone_input.value = row.telefone  # Acesse o valor do campo 'telefone'

            # Remove a linha selecionada da tabela para permitir a atualização
            self.contact_table.data.remove(row)

            # Desabilita os botões de editar e excluir até que uma nova linha seja selecionada
            self.edit_button.enabled = False
            self.delete_button.enabled = False

    def delete_contact(self, widget):
        # Recupera a linha selecionada
        row = self.contact_table.selection

        if row:
            # Remove a linha selecionada da tabela
            self.contact_table.data.remove(row)

            # Desabilita os botões de editar e excluir até que uma nova linha seja selecionada
            self.edit_button.enabled = False
            self.delete_button.enabled = False


def main():
    return listaTelefonica()
