PYTHON = python

install:
	cat requirements/*.txt > requirements.txt
	pip install -r requirements.txt

	bundle install --path vendor/bundle

	make sass

run:
	$(PYTHON) -m candis

clean:
	find . | grep -E "__pycache__|\.pyc|\.pyo" | xargs rm -rf

all:
	make run clean
