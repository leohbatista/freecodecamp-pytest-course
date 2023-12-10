# _freeCodeCamp_ pytest course

Demo project built on _freeCodeCamp_ "Testing in Python with Pytest" course.

- [Article](https://www.freecodecamp.org/news/testing-in-python-with-pytest/)
- [YouTube Video](https://www.youtube.com/watch?v=cHYq1MRoyI0)

## Usage

Inside the project folder:

1. Create virtual environment:

```
python -m venv venv
```

2. Activate the virtual environment:

```
source venv/bin/activate
```

3. Install `pip-tools`

```
pip install pip-tools
```

4. Sync dependencies:

```
pip-sync requirements.txt
```

**ALL DONE!**

## Maintenance

To install a new dependency, put it on `requirements.in` file and the run:

```
pip-compile requirements.in
pip-sync requirements.txt
```
