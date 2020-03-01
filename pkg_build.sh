
# Build .tar.gz and .whl files
echo Building....
python setup.py sdist bdist_wheel

# check the build files
echo
echo Checking build..
twine check dist/*
