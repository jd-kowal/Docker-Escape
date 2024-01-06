# Docker-Escape
This project shows vulnerability how to escape from Docker container in which web application is running. <br />

## About
This project is made for academic purposes during one of our courses at the AGH University of Krakow. <br />
We present security issues in Docker. We show vulnerabilities of this software and best practices related to them. Below we also include case-studies showing how to get into the server from the user level of a web application, how to escape from this container and the possibilities that open up to us after such an escape.<br />

  
## Authors:
[Huber Mąka](https://github.com/norka02) <br />
[Karol Makara](https://github.com/KarolMakara) <br />
[Jakub Kowal](https://github.com/jd-kowal) <br />

*** 

# Tasks
* [Task 0](#Task-0)
* [Task 1](#Task-1)
* [Task 2](#Task-2)
* [Task 3](#Task-3)
* [Task 4](#Task-4)



## Task 0 - Przygotowanie środowiska
Aby rozpocząć wykonywanie zadań sklonujcie repozytorium. <br />
Będziemy używać Dockera (kontener w kontenerze). Całość jest przygotowana w docker.file. <br />
Następnie wykonaj poniższe komendy. <br />
Build:<br />
```bash docker build -t ubuntu-dind```<br />
Run:<br />
```bash docker run -d -p 5000:5000 --privileged --hostname ubuntu-dind --name ubuntu-dind ubuntu-dind```<br />
Enter:<br />
```bash docker exec -itu adam ubuntu-dind bash```<br />
<br />
**TIP** - w przypadku problemów -> zresetuj kontener <br />

## Task 1 - Dostęp do serwera z perspektywy użytkownika aplikacji webowej
Na kontenerze jest uruchomiona aplikacja webowa. Znając jej podatność omówioną podczas prezentacji spróbuj za pomocą preparacji url-a wykonać podstawowy pentesting (np. podawany podczas prezentacji przykład wyrażenia 7*7). <br />
Następnie ... <br />
<br />
**Odpowiedź** - <br />

## Task 2 - Docker Escape & Privilege Escalation
**TIP** - proponujemy przejście z wykonywaniem zadań do terminala. <br />
Ucieczkę z kontenera umożliwia nam złe skonfigurowanie kontenera. <br />
<br />
**Odpowiedź** - wyślij ss potwierdzającego twoje uprawnienia root-a. <br />

## Task 3 - Mini-CTF
Mając uprawnienia root-a możesz poruszać się bezproblemowo po systemie. Znajdź katalog, który nie powinien znajdować się w systemie/wyróżnia się spośród pozostałych. W nim znajdować plik z flagą. Zmodyfikuj znaleziony plik dodając swoje imię i nazwisko. <br />
<br />
**Odpowiedź** - wyślij widoczną zmodyfikowaną flagę wraz z dopisanym unikalnym tekstem wymienionym wyżej oraz ścieżkę do katalogu, w którym znajduje się znaleziona flaga. <br />

## Task 4 - Tworzenie Bezpiecznego Kontenera
Posiadając całą wiedzę zdobytą podczas prezentacji oraz poprzednich tasków zastanów się w jaki sposób możesz zabezpieczyć kontener przed różnymi wektorami ataków. <br />
Stwórz kontener, który spełnia wszystkie best-practice dot. bezpiecznego tworzenia kontenera Dockera. <br />
<br />
**Odpowiedź** - wyślij widoczną komendę, która tworzy **Bezpieczny Kontener**. <br />
