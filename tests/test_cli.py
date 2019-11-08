import subprocess
import pytest

def test_version():
    subprocess.check_output(
        "plottymcplotface --version",
        shell=True
    )

def test_debug():
    capture = subprocess.check_output(
        "plottymcplotface --version --debug",
        shell=True
    )
    assert b"debug mode" in capture


def test_bad_command():
    with pytest.raises(subprocess.CalledProcessError):
        subprocess.check_output(
            "plottymcplotface --bad-command",
            shell=True
        )

def test_output_file():
    try:
        capture = subprocess.check_output(
            "plottymcplotface --output-file testplot.html",
            shell=True
        )
        assert b"created" in capture
    except Exception as e:
        print("stf")
