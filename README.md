# System rezerwacji dla salonów fryzjerskich

## O projekcie

Aplikacja webowa, która umożliwia rezerwację wizyt online do salonu fryzjerskiego. Klient ma możliwość wyboru salonu fryzjerskiego, zapoznania się z oferowanymi przez salon usługami oraz ich ceną i czasem trwania. Rezerwacja odbywa się poprzez naciśnięcie przycisku „umów” znajdującego się przy konkretnej usłudze. Następnie klient musi uzupełnić niezbędne dane w formularzu, m.in. musi wybrać fryzjera, rodzaj usługi, datę oraz godzinę. System wprowadza ograniczenie rezerwacji na konkretny termin, blokując wybór daty i godziny, która została już zarezerwowana przez innego użytkownika.

Do implementacji systemu wykorzystano nowoczesne technologie. Back-end aplikacji został stworzony za pomocą frameworka Django, napisanym w języku Python, z wykorzystaniem Django REST framework. Natomiast do napisania front-endu posłużył język JavaScript z wykorzystaniem biblioteki React.js. Na relacyjną bazę danych wybrano PostgreSQL.

### Przygotowanie
Przed rozpoczęciem konfiguracji projektu należy zainstalować 
Python 3.8 oraz PostgreSQL. Następnie należy uworzyć bazę danych o nazwie `salonfy`.

### Konfiguracja projektu - Backend
Sklonuj repozytorium z kodem
```
git clone https://github.com/kamillon/HairdresserBookingSystem-Backend.git
```
Utwórz wirtualne środowisko Pythona (wewnątrz folderu repozytorium)
```
python -m venv env
```
Aktywacja środowiska wirtualnego
```
.\env\Scripts\activate.bat
```
Instalowanie wymaganych zależności projektu
```
pip install -r requirements.txt
```
Stosowanie migracji bazy danych
```
python manage.py migrate
```
Utworzenie superużytkownika
```
python manage.py createsuperuser
```
Uruchom projekt na swoim komputerze
```
python manage.py runserver
```
Żeby sprawdzić czy serwer Django działa nalezy wejść na adres: `https://localhost:8000`

## Funkcjonalności
- logowanie i rejestracja w systemie nowych użytkowników,
- możliwość rezerwacji wizyty poprzez stronę internetową,
- możliwość tworzenia nowych rezerwacji bez konieczności użycia aplikacji przez klienta,
- wyświetlenie listy salonów fryzjerskich wraz z listą oferowanych usług,
- możliwość filtrowania listy salonów fryzjerskich po miejscowości oraz rodzaju usługi,
- możliwość  dokonania  rezerwacji  wizyty  w  wybranym  terminie, pod warunkiem że jest on wtedy dostępny,
- zarządzanie rezerwacjami (CRUD),
- podgląd historii wizyt przez klienta oraz możliwość anulowania wizyty,
- wysyłanie użytkownikom wiadomości e-mail z potwierdzeniem rezerwacji,
- zarządzanie użytkownikami (CRUD),
- zarządzanie pracownikami (CRUD),
- zarządzanie salonami fryzjerskimi (CRUD),
- zarządzanie usługami (CRUD),
- edycja danych konta użytkownika,
- walidacja poprawności wprowadzonych danych

## Część kliencka
https://github.com/kamillon/HBS-Frontend