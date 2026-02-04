import argparse
import csv
import sys
from pathlib import Path
from typing import Iterable
from dataclasses import dataclass

from tabulate import tabulate

Row = dict[str, str]


@dataclass(frozen=True)
class AverageGpd:
    name: str = 'average-gdp'

    def generate_report(
            self, rows: Iterable[Row]
    ) -> tuple[list[str], list[list[object]]]:
        sums: dict[str, float] = {}
        counts: dict[str, int] = {}

        for row in rows:
            country = row["country"]
            gdp = float(row["gdp"])
            sums[country] = sums.get(country, 0.0) + gdp
            counts[country] = counts.get(country, 0) + 1

        table = [[c, sums[c] / counts[c]] for c in sums.keys()]
        table.sort(key=lambda x: x[1], reverse=True)
        headers = ["country", "avg_gdp"]
        return headers, table


REPORTS = {
    'average-gdp': AverageGpd(),
}


def parse_arguments(args: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('--files', nargs='+',
                        required=True, help='CSV file(s) to parse')
    parser.add_argument('--report', required=True, help='CSV output file')
    return parser.parse_args(args)


def reading_csv(files: list[str]) -> list[Row]:
    rows: list[Row] = []
    for file in files:
        path = Path(file)
        if not path.exists():
            raise FileNotFoundError(f"File {path.name} does not exist")
        with path.open('r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            rows.extend(reader)
    return rows


def main(args: list[str] | None = None) -> int:
    ns = parse_arguments(sys.argv[1:] if args is None else args)

    report = REPORTS.get(ns.report, None)
    if report is None:
        print(f"Unknown report: {ns.report}. "
              f"Available: {', '.join(sorted(REPORTS))}", file=sys.stderr)
        return 2
    try:
        rows = reading_csv(ns.files)
    except FileNotFoundError as e:
        print(str(e), file=sys.stderr)
        return 2

    headers, table = report.generate_report(rows)
    print(tabulate(table, headers=headers, tablefmt='github'))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
