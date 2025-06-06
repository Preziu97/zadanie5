# Opis wybranych bibliotek Pythona

**Autor:** Przemysław Kierasiński (98031)  
**GitHub:** https://github.com/Preziu97/zadanie5/

---

## Wstęp

W niniejszym projekcie przedstawiam opis oraz podstawowe informacje o wybranych bibliotekach Python, które są wykorzystywane lub analizowane w kontekście tworzenia aplikacji i obliczeń symbolicznych. Nie jestem autorem tych bibliotek, a jedynie dokumentuję ich funkcje, zalety i wady wraz z linkami do oficjalnych źródeł.

---

## SymPy

**Nazwa:** SymPy  
**Autorzy / Twórcy:** Ondřej Čertík i społeczność open source  
**Pierwsze wydanie:** 2006  
**Licencja:** BSD

### Przeznaczenie  
SymPy to biblioteka do symbolicznych obliczeń matematycznych, umożliwiająca manipulacje wyrażeń algebraicznych, rozwiązywanie równań, różniczkowanie, całkowanie symboliczne oraz pracę z macierzami.

### Główne funkcje  
- Symboliczne różniczkowanie i całkowanie  
- Upraszczanie wyrażeń algebraicznych  
- Rozwiązywanie równań algebraicznych i różniczkowych  
- Praca z macierzami symbolicznie  
- Generowanie kodu matematycznego (np. C, Fortran, Python)  
- Wsparcie dla matematyki dyskretnej i teorii liczb  

### Zalety  
- Pełna funkcjonalność symbolicznej matematyki w Pythonie  
- Dobrze udokumentowana i aktywnie rozwijana przez społeczność  
- Łatwa integracja z innymi bibliotekami Pythona (NumPy, Matplotlib)  
- Otwarty kod źródłowy  

### Wady  
- Wolniejsze działanie w porównaniu do narzędzi numerycznych (to naturalne dla obliczeń symbolicznych)  
- Może być mniej intuicyjna dla użytkowników przyzwyczajonych do obliczeń numerycznych  

### Wymagania systemowe  
- Python w wersji 3.6 lub wyższej  

### Instalacja  
<pre> pip install sympy </pre>

### Linki  
- Dokumentacja: https://docs.sympy.org  
- Repozytorium: https://github.com/sympy/sympy  

---

## PySimpleGUI

**Nazwa:** PySimpleGUI  
**Autor:** Mike B. (MikeTheWatchGuy)  
**Pierwsze wydanie:** 2018  
**Licencja:** Własna (proprietary)  

### Przeznaczenie  
PySimpleGUI to biblioteka upraszczająca tworzenie graficznych interfejsów użytkownika (GUI) w Pythonie. Jest warstwą abstrakcji nad Tkinter, Qt, WxPython i Remi, co pozwala szybko tworzyć aplikacje z GUI.

### Główne funkcje  
- Intuicyjny interfejs API oparty na układach (layout)  
- Obsługa wielu backendów GUI: Tkinter, Qt, WxPython, Remi  
- Szeroki wybór gotowych komponentów GUI (przyciski, pola tekstowe, listy itd.)  
- Tworzenie interfejsów jedno- i wielookienkowych  
- Łatwa integracja z innymi bibliotekami Pythona  

### Zalety  
- Niski próg wejścia dla początkujących programistów  
- Szybkie prototypowanie aplikacji GUI  
- Aktywna społeczność i regularne aktualizacje  
- Obsługa wielu platform (Windows, macOS, Linux)  
- Bogata dokumentacja i przykłady  

### Wady  
- Mniejsza elastyczność niż bezpośrednie korzystanie z Qt czy WxPython  
- Wydajność i funkcjonalność zależą od wybranego backendu  
- Zaawansowane GUI mogą wymagać przejścia na bibliotekę bazową  
- Wersja Pro jest płatna i wymaga rejestracji, co może ograniczać dostęp  

### Wymagania systemowe  
- Python w wersji 3.6 lub wyższej  

### Instalacja (z wymuszeniem najnowszej wersji oraz niestandardowym repozytorium):
<pre> python -m pip install --force-reinstall --extra-index-url https://PySimpleGUI.net/install PySimpleGUI  </pre>

---

## Faker

**Nazwa:** Faker  
**Autor:** Daniele Faraglia, społeczność open source  
**Pierwsze wydanie:** 2012  
**Licencja:** MIT  

### Przeznaczenie  
Faker to biblioteka do generowania losowych, fikcyjnych danych do celów testowych, prezentacyjnych i developerskich. Może tworzyć dane osobowe, adresowe, finansowe, firmowe, internetowe i wiele innych. Obsługuje różne języki i lokalizacje.

### Główne funkcje  
- Generowanie danych osobowych: imię, nazwisko, PESEL, e-mail, numer telefonu  
- Tworzenie adresów, miast, województw, kodów pocztowych  
- Generowanie danych firmowych: nazwy firm, NIP/VAT, IBAN  
- Tworzenie danych internetowych: loginy, domeny, adresy IP  
- Tworzenie dat, tekstów, liczb i identyfikatorów  
- Obsługa wielu lokalizacji (np. pl_PL, en_US, de_DE)  
- Możliwość rozszerzenia o własne providery danych  

### Zalety  
- Bardzo prosty w użyciu, niski próg wejścia  
- Obsługuje wiele kategorii danych i języków  
- Przydatny do testowania aplikacji, baz danych i API  
- Możliwość integracji z Pandas, CSV, JSON  
- Aktywnie rozwijany i dobrze udokumentowany  

### Wady  
- Dane są fikcyjne i niespójne logicznie (np. imię ≠ adres e-mail)  
- Nie wszystkie metody są dostępne w każdej lokalizacji  
- Brak danych realistycznych/statystycznych  
- Nie nadaje się do modelowania danych rzeczywistych  

### Wymagania systemowe  
- Python w wersji 3.6 lub wyższej  

### Instalacja
<pre>pip install faker</pre>

---

## Podsumowanie

Opisane biblioteki oferują szerokie możliwości — SymPy skupia się na obliczeniach symbolicznych, PySimpleGUI pozwala szybko tworzyć interfejsy użytkownika, a Faker ułatwia generowanie realistycznie wyglądających, fikcyjnych danych do testów i prototypowania. Wybór i zastosowanie zależy od potrzeb konkretnego projektu.

---

## Kontakt

Przemysław Kierasiński  
GitHub: https://github.com/Preziu97/zadanie5/

