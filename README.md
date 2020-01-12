# Shielded notes <!-- omit in toc -->

Końcowy projekt na _Ochronę Danych w Systemach Informatycznych_.

## Cel projektu

Przygotowanie bezpiecznej aplikacji webowej. Aplikacja będzie pozwalała na wymianę i upublicznianie sformatowanych notatek.

## Spis treści

- [Cel projektu](#cel-projektu)
- [Spis treści](#spis-treści)
- [Uruchamianie projektu](#uruchamianie-projektu)
- [Podstawowe wymagania](#podstawowe-wymagania)

## Uruchamianie projektu

By uruchomić projekt wystarczy wykonać `docker-compose up` w głównym katalogu. Projekt będzie widoczny pod adresem [https://localhost](htts://localhost).  
Do uruchomienia projektu w ten sposób wymagany jest [Docker](https://www.docker.com/).

## Podstawowe wymagania

Napisz aplikację WWW realizującą uwierzytelnianie w oparciu o tajne hasło. Zwróć uwagę na:

- :white_check_mark: **(niezbędne)** restrykcyjna weryfikacje danych pochodzących z formularza login-hasło,
- :white_check_mark: **(niezbędne)** przechowywanie hasła chronione funkcją hash i solą,
- :white_check_mark: **(niezbędne)** możliwość umieszczenia na serwerze notatek dostępnych publicznie lub dla określonych - użytkowników,
- :white_check_mark: **(niezbędne)** zabezpieczenie transmisji poprzez wykorzystanie protokołu https,
- :white_check_mark: **(niezbędne)** możliwość zmiany hasła,
- :white_check_mark: dodatkowa kontrola spójności sesji (przeciw atakom XSRF),
- :white_check_mark: wielokrotne wykorzystanie funkcji hash, żeby wydłużyć ataki brute-force na hash (wolna funkcja hash),
- :white_check_mark: weryfikacja liczby nieudanych prób logowania,
- dodanie opóźnienia przy weryfikacji hasła w celu wydłużenia ataków zdalnych,
- :white_check_mark: sprawdzanie jakości hasła (jego entropii),
- możliwość odzyskania dostępu w przypadku utraty hasła,
- :white_check_mark: informowanie użytkownika o nowych podłączeniach do jego konta.
