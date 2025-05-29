import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        # Tworzymy główne okno aplikacji
        # root = tk.Tk()
        # Metoda title ustawia tytuł okna
        self.root = root
        self.root.title("Prosta aplikacja Lista Zadań")  # tytuł okna
        self.root.geometry("400x400")  # rozmiar okna: szerokość x wysokość

        # Tworzymy menu główne aplikacji
        self.menu = tk.Menu(self.root)  # tworzymy pasek menu
        self.root.config(menu=self.menu)  # podpinamy menu do głównego okna

        # Dodajemy menu "Plik" z opcjami
        file_menu = tk.Menu(self.menu, tearoff=0)  # tearoff=0 usuwa linię oddzielającą w menu
        # Dodajemy komendę w menu "Plik" - wyczyść listę
        file_menu.add_command(label="Wyczyść listę", command=self.clear_tasks)
        # Dodajemy separator (linia oddzielająca)
        file_menu.add_separator()
        # Dodajemy komendę wyjścia z aplikacji
        file_menu.add_command(label="Wyjście", command=self.root.quit)
        # Dodajemy menu "Plik" do paska menu
        self.menu.add_cascade(label="Plik", menu=file_menu)

        # Tworzymy etykietę z tekstem instrukcji
        # Label to statyczny tekst w GUI
        self.label = tk.Label(root, text="Wpisz zadanie do wykonania:")
        # Metoda pack() układa widget w oknie, pady to marginesy pionowe
        self.label.pack(pady=5)

        # Pole tekstowe Entry do wpisywania danych
        self.entry = tk.Entry(root, width=40)  # width to szerokość w znakach
        self.entry.pack(pady=5)

        # Przycisk, który wywoła metodę add_task po kliknięciu
        self.add_button = tk.Button(root, text="Dodaj zadanie", command=self.add_task)
        self.add_button.pack(pady=5)

        # Listbox wyświetla listę elementów, można zaznaczać pozycje
        self.listbox = tk.Listbox(root, width=50, height=10)
        self.listbox.pack(pady=10)

        # Przycisk usuwania zaznaczonych pozycji w listboxie
        self.delete_button = tk.Button(root, text="Usuń zaznaczone", command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Etykieta służąca jako pasek stanu (status bar)
        # bd=1 -> border width, relief -> efekt wypukłości, anchor -> wyrównanie tekstu
        self.status_label = tk.Label(root, text="Liczba zadań: 0",
                                     bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_label.pack(side=tk.BOTTOM, fill=tk.X)  # na dole, rozciąga się na całą szerokość

    def add_task(self):
        # Pobieramy tekst wpisany w pole Entry
        task = self.entry.get().strip()
        if task:
            # Dodajemy do Listbox (koniec listy: tk.END)
            self.listbox.insert(tk.END, task)
            # Czyścimy pole Entry (od znaku 0 do końca)
            self.entry.delete(0, tk.END)
            self.update_status()
        else:
            # Pokazujemy okno z ostrzeżeniem, jeśli pole jest puste
            messagebox.showwarning("Uwaga", "Nie można dodać pustego zadania!")

    def delete_task(self):
        # Pobieramy indeksy zaznaczonych elementów (krotka)
        selected_indices = self.listbox.curselection()
        if not selected_indices:
            messagebox.showinfo("Info", "Wybierz zadanie do usunięcia.")
            return
        # Usuwamy od końca, by nie przesunąć indeksów
        for index in reversed(selected_indices):
            self.listbox.delete(index)
        self.update_status()

    def clear_tasks(self):
        # Potwierdzenie czy użytkownik chce wyczyścić listę
        if messagebox.askyesno("Potwierdzenie", "Czy na pewno chcesz wyczyścić listę zadań?"):
            self.listbox.delete(0, tk.END)
            self.update_status()

    def update_status(self):
        # Aktualizacja tekstu w status_label z liczbą elementów listy
        count = self.listbox.size()
        self.status_label.config(text=f"Liczba zadań: {count}")

if __name__ == "__main__":
    # Tworzymy główne okno aplikacji
    root = tk.Tk()
    # Inicjujemy klasę TodoApp z głównym oknem
    app = TodoApp(root)
    # Uruchamiamy pętlę zdarzeń Tkinter (okno działa i czeka na interakcję)
    root.mainloop()
