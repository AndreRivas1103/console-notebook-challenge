from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from app.notebook import Notebook


class ConsoleUI:
    def __init__(self):
        self.notebook = Notebook()
        self.console = Console()
        self.main_menu()

    def main_menu(self):
        while True:
            self.console.clear()  #
            self.console.print("[bold blue]Cuaderno de Notas[/bold blue]", justify="center")
            self.console.print("[green]1.[/green] Agregar Nota")
            self.console.print("[green]2.[/green] Listar Notas")
            self.console.print("[green]3.[/green] Agregar Etiqueta a Nota")
            self.console.print("[green]4.[/green] Listar Notas Importantes")
            self.console.print("[green]5.[/green] Eliminar Nota")
            self.console.print("[green]6.[/green] Mostrar Notas por Etiqueta")
            self.console.print("[green]7.[/green] Mostrar Etiqueta con Más Notas")
            self.console.print("[red]8.[/red] Salir")

            choice = Prompt.ask("Selecciona una opción", choices=["1", "2", "3", "4", "5", "6", "7", "8"])

            if choice == "1":
                self.add_note()
            elif choice == "2":
                self.list_notes()
            elif choice == "3":
                self.add_tag_to_note()
            elif choice == "4":
                self.list_important_notes()
            elif choice == "5":
                self.delete_note()
            elif choice == "6":
                self.show_notes_by_tag()
            elif choice == "7":
                self.show_tag_with_most_notes()
            elif choice == "8":
                self.console.print("Saliendo...", style="bold red")
                break


