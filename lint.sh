pyright ./$1
flake8 ./$1
black ./$1 --check
isort --profile black ./$1 --check-only
