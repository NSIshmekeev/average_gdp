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

Для начала в файле src/main.py добавим в словарь название и класс отвечающий логике отчёта
```python
REPORTS = {
    'average-gdp': AverageGpd(),
    'new-report': NewReport(),
}
```
далее создаем dataclass по аналогии с AverageGdp
```python
@dataclass(frozen=True)
class NewReport:
    name: str = 'new-report'

    def generate_report(
            self, rows: Iterable[Row]
    ) -> tuple[list[str], list[list[object]]]:
        ...
        return headers, table
```
Теперь через строку мы можем запусить скрипт с новым отчетом
```bash
python src/main.py --files data/economic1.csv data/economic2.csv --report new-report
```
