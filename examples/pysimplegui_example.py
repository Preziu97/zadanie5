import PySimpleGUI as sg

class TodoApp:
    def __init__(self):
        # Ustawiamy motyw graficzny aplikacji
        sg.theme('LightBlue')

        # Tworzymy układ elementów graficznego interfejsu (layout)
        layout = [
            [sg.Text("Wpisz zadanie do wykonania:")],  # Etykieta z instrukcją
            [sg.InputText(key='-TASK-', size=(40,1)), sg.Button("Dodaj zadanie")],  # Pole tekstowe + przycisk dodaj
            [sg.Listbox(values=[], key='-TASK LIST-', size=(50, 10), select_mode=sg.LISTBOX_SELECT_MODE_EXTENDED)],  # Listbox zadań
            [sg.Button("Usuń zaznaczone"), sg.Button("Wyczyść listę"), sg.Button("Wyjście")],  # Przyciski operacji
            [sg.Text("Liczba zadań: 0", key='-STATUS-', size=(40,1))]  # Pasek statusu z liczbą zadań
        ]

        # Tworzymy główne okno aplikacji na podstawie układu
        self.window = sg.Window("Prosta aplikacja Lista Zadań", layout, finalize=True)

    def run(self):
        # Pętla zdarzeń - okno czeka na akcje użytkownika
        while True:
            event, values = self.window.read()

            # Jeśli użytkownik zamknie okno lub kliknie "Wyjście" - przerywamy pętlę
            if event == sg.WINDOW_CLOSED or event == "Wyjście":
                break

            # Dodawanie nowego zadania
            elif event == "Dodaj zadanie":
                task = values['-TASK-'].strip()  # Pobieramy tekst z pola wejściowego
                if task:
                    current_tasks = self.window['-TASK LIST-'].get_list_values()  # Pobieramy aktualną listę zadań
                    current_tasks.append(task)  # Dodajemy nowe zadanie do listy
                    self.window['-TASK LIST-'].update(current_tasks)  # Aktualizujemy listbox
                    self.window['-TASK-'].update('')  # Czyścimy pole wejściowe
                    self.update_status()  # Aktualizujemy pasek statusu
                else:
                    # Jeśli puste zadanie - wyświetlamy okno ostrzeżenia
                    sg.popup("Uwaga", "Nie można dodać pustego zadania!")

            # Usuwanie zaznaczonych zadań
            elif event == "Usuń zaznaczone":
                selected_tasks = values['-TASK LIST-']  # Pobieramy zaznaczone elementy
                if not selected_tasks:
                    # Jeśli nic nie zaznaczono - informujemy użytkownika
                    sg.popup("Info", "Wybierz zadanie do usunięcia.")
                else:
                    current_tasks = self.window['-TASK LIST-'].get_list_values()  # Pobieramy pełną listę zadań
                    # Tworzymy nową listę, pomijając zaznaczone elementy
                    new_tasks = [task for task in current_tasks if task not in selected_tasks]
                    self.window['-TASK LIST-'].update(new_tasks)  # Aktualizujemy listbox
                    self.update_status()  # Aktualizujemy pasek statusu

            # Czyszczenie całej listy zadań
            elif event == "Wyczyść listę":
                # Pytamy użytkownika o potwierdzenie operacji
                confirm = sg.popup_yes_no("Czy na pewno chcesz wyczyścić listę zadań?")
                if confirm == "Yes":
                    self.window['-TASK LIST-'].update([])  # Usuwamy wszystkie elementy z listboxa
                    self.update_status()  # Aktualizujemy pasek statusu

        # Zamykamy okno po wyjściu z pętli
        self.window.close()

    def update_status(self):
        # Aktualizujemy tekst paska statusu z liczbą zadań na liście
        count = len(self.window['-TASK LIST-'].get_list_values())
        self.window['-STATUS-'].update(f"Liczba zadań: {count}")

if __name__ == "__main__":
    # Tworzymy instancję aplikacji i uruchamiamy pętlę zdarzen
    app = TodoApp()
    app.run()
