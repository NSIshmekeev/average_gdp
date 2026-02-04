from src.main import AverageGpd


def test_parse_arguments():
    rows = [
        {"country": "A", "gdp": "100"},
        {"country": "B", "gdp": "50"},
        {"country": "A", "gdp": "50"},
    ]
    report = AverageGpd()
    headers, table = report.generate_report(rows)
    assert headers == ['country', 'avg_gdp']
    assert table == [["A", 75.0], ["B", 50.0]]
