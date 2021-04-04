[![Travis][build-badge]][build]

[build-badge]: https://www.travis-ci.com/StalingradTeam/e-1.12.svg?branch=main

[build]: https://travis-ci.org/StalingradTeam/e-1.12

# ИГРА "Висилица" + тесты к ней

# Запуск

1) скачиваем файлы
2) запускаем:
   python game.py
3) запуск тестов:
   python -m venv env
   env\Scripts\activate.bat
   pip install -r requirements.txt
   pytest
   pytest --cov=game
