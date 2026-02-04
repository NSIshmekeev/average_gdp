from src.main import main


def test_main_succes(capsys):
    args = ['--files', 'data/economic1.csv',
            'data/economic2.csv', '--report', 'average-gdp']
    code = main(args)
    assert code == 0
    captured = capsys.readouterr()
    assert 'country' in captured.out
    assert 'avg_gdp' in captured.out


def test_main_unknown_report(capsys):
    args = ['--files', 'data/economic1.csv',
            'data/economic2.csv', '--report', 'nope']
    code = main(args)
    assert code == 2
    captured = capsys.readouterr()
    assert 'Unknown report: nope' in captured.err


def test_main_file_not_found(capsys):
    args = ['--files', 'data/test_error.csv',
            '--report', 'average-gdp']
    code = main(args)
    assert code == 2
    captured = capsys.readouterr()
    assert 'File test_error.csv does not exist' in captured.err
