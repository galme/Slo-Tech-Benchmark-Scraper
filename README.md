# Slo-Tech-Benchmark-Scraper

web-scraper teme iz podforuma navijanje na spletni strani www.slo-tech.com, ki vsebuje rezultate benchmarka.
Rezultat je HTML lestvica, primer izhoda je "LEADERBOARDS.txt".

Avtor: **galme**, 2017
# Uporabljena orodja:
- PyCharm
- Python 3.6
- Scrapy 1.3 (https://scrapy.org/)

# Kako uporabljati:
primer (iz "testrun.bat"):

    python main.py -URL=https://slo-tech.com/forum/t698837/0 -labels 1080p 4k 8k -outputformat NAMED LEADERBOARD

Pomen _label_ je uvrščanje rezultata iz posta v ustrezno lestvico (ki je določena z _labelo_). Pomembno samo takrat, ko je v eni temi več lestvic. Primer:

    1080p: # to je uporabno za labelo. Primer labele bi bil: "1080p"
    19.11 | 14.99 | R9 290 (1069/1250 MHz) | i5 2500K (4.8GHz) | 12GB 1866MHz | 2555

Posebej pomemben vhodni parameter je _scoreindex_:

    -scoreindex=[int] # določa indeks rezultata v formuli. Default je -1 (zadnje mesto v formuli).
    -scoreindex=0 # <-- primer. Nastavi pozicijo na začetek

Več informacij:

    python main.py -h