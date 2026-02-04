### CLI скрипт для анализ макроэкономических данных

Скрипт читает файлы с экономическими данными и формирует отчеты

Пример выполнения кода:
<img width="868" height="503" alt="image" src="https://github.com/user-attachments/assets/3c223676-8fde-4fda-8f4f-1e8d369d7bf5" />

## Установка
```bash
git clone https://github.com/NSIshmekeev/average_gdp.git
```
В папке с проектом
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Запуск программы 
```bash
python src/main.py --files data/economic1.csv data/economic2.csv --report average-gdp
```

## Запуск тестов
Для запуска тестов достаточно в папке с проектом выполнить команду:
```bash
pytest
```

## Дополнительные возможности
В коде предусмотрена возоможность добавлять свои отчеты. 
Например:
в файле src/main.py добавим в словарь 
```python
REPORTS = {
    'average-gdp': AverageGpd(),
    'new-report': NewReport(),
}
```

