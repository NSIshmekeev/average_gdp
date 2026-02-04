import pytest
from argparse import Namespace

from src.main import parse_arguments


def test_pars_arguments_files_report():
    args = ['--files', 'file1.csv', 'file2.csv', '--report', 'avg']
    result = parse_arguments(args)
    assert result.files == ['file1.csv', 'file2.csv']
    assert result.report == 'avg'
    assert isinstance(result, Namespace)


def test_parse_arguments_no_files():
    args = ['--report', 'avg']
    with pytest.raises(SystemExit):
        parse_arguments(args)


def test_parse_arguments_no_wrong_arguments():
    args = ['--wrong', 'avg']
    with pytest.raises(SystemExit):
        parse_arguments(args)
