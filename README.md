# Shielded notes <!-- omit in toc -->

Końcowy projekt na _Ochronę Danych w Systemach Informatycznych_.

## Cel projektu

Przygotowanie bezpiecznej aplikacji webowej. Aplikacja będzie pozwalała na wymianę i upublicznianie sformatowanych notatek.

## Spis treści

- [Cel projektu](#cel-projektu)
- [Spis treści](#spis-treści)
- [Podstawowe wymagania](#podstawowe-wymagania)

## Podstawowe wymagania

Napisz aplikację WWW realizującą uwierzytelnianie w oparciu o tajne hasło. Zwróć uwagę na:

- **(niezbędne)** restrykcyjna weryfikacje danych pochodzących z formularza login-hasło,
- :white_check_mark: **(niezbędne)** przechowywanie hasła chronione funkcją hash i solą,
- **(niezbędne)** możliwość umieszczenia na serwerze notatek dostępnych publicznie lub dla określonych - użytkowników,
- :white_check_mark: **(niezbędne)** zabezpieczenie transmisji poprzez wykorzystanie protokołu https,
- **(niezbędne)** możliwość zmiany hasła,
- :white_check_mark: dodatkowa kontrola spójności sesji (przeciw atakom XSRF),
- :white_check_mark: wielokrotne wykorzystanie funkcji hash, żeby wydłużyć ataki brute-force na hash (wolna funkcja hash),
- weryfikacja liczby nieudanych prób logowania,
- dodanie opóźnienia przy weryfikacji hasła w celu wydłużenia ataków zdalnych,
- sprawdzanie jakości hasła (jego entropii),
- możliwość odzyskania dostępu w przypadku utraty hasła,
- informowanie użytkownika o nowych podłączeniach do jego konta.
