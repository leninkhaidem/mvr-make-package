import hashlib
import os
import pathlib
import shutil
import subprocess

import pytest
from cookiecutter.main import cookiecutter

import mvr_make_package

template_path = pathlib.Path(pathlib.Path(mvr_make_package.__file__).parent,
                             "mvr-template").absolute().as_posix()

# Define the base path to the generated folder and expected files with their hash values
BASE_PATH = "mvr-package-name"
EXPECTED_FILES = {
    "package-meta-data.xml": "f208bdaeb5a8e500b057a3ae89513c503b2aba60a64332e251a21e91b5b8434c",
    "python/mvr_package_name/__init__.py": "6693de99707265d8fcafd204fe255f6a889698602853e8f04ee0d3d68739e7f0",
    "python/mvr_package_name/correlators/__init__.py": "5237e86ddee7798f0799c55f6d1076107195cb3485bb7101824a9a9cb4a3f4ad",
    "python/mvr_package_name/correlators/c_1.py": "344c79f0a3533f65644df6a29d636019eeb4231a56647844edc17b3fb6877c09",
    "python/mvr_package_name/extractions/__init__.py": "ad68b66ca46abb5bb7a2b24991233040ae28d485c0f6804b51ae1265c6fd9940",
    "python/mvr_package_name/extractions/dx_1.py": "51b85647e1a0511ed5c97f71fb6f025ae92918624ce56390bb4e9d03200ff3be",
    "python/mvr_package_name/extractions/dx_2.py": "03ee4f0bce66cc6d1950901e05b63c399cb3ffbfbf56764bb53b2627b5d5918f",
    "python/mvr_package_name/mvr_package_name.py": "9459613c8bc6f47c6aee88e2424ad9dc0ff8b53eba43665306482cce467b8d5c",
    "python/mvr_package_name/template_engines.py": "ee04ca9123e8e1e2c2d40b5dfaae0b864e1862249e778e14cbcf3d65ae25fc5f",
    "python/mvr_package_name/yang_inputs.py": "889acc11e52b654c77483976b8d96ee84f4c604b236ea42971847ad65fb04be0",
    "src/Makefile": "20d6355a62973fdca0e6fcc61e16e60a77468def252e7d993c6eecda0a76e943",
    "src/yang/mvr-package-name.yang": "63a4da84409b628211a0f8a0daf8fad63b77e899f3c83d6bead45f6e05ac4fa8",
    "templates/mvr-package-name-template.xml": "4461c12fe9b8f71d57ee939820b87dda9452605848212330bf122c4270fab723",
}


def hash_file(filepath):
    """Computes SHA256 hash of the given file."""
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


@pytest.fixture(scope="session", autouse=True)
def generate_package():
    """Fixture to generate the package before running tests."""
    # Clean up the directory if it already exists (optional)
    if os.path.exists(BASE_PATH):
        subprocess.run(["rm", "-rf", BASE_PATH])
    extra_context = {
        "package_name": "mvr-package-name",
        "ncs_version": "5.0",
        "description": "some description"
    }
    cookiecutter(template_path, no_input=True, extra_context=extra_context)

    # Verify the package directory was created
    assert os.path.isdir(
        BASE_PATH), f"Failed to generate package at {BASE_PATH}"
    yield
    if os.path.exists(BASE_PATH):
        shutil.rmtree(BASE_PATH)


@pytest.mark.parametrize("relative_path, expected_hash", EXPECTED_FILES.items())
def test_generated_files_exist_and_match_hash(relative_path, expected_hash, generate_package):
    """Test that each expected file exists and its content matches the expected hash."""
    file_path = os.path.join(BASE_PATH, relative_path)

    # Check if file exists
    assert os.path.isfile(file_path), f"{file_path} does not exist"

    # Verify content hash
    actual_hash = hash_file(file_path)
    assert actual_hash == expected_hash, f"Hash mismatch for {file_path}"
