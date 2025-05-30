# 🐍 Python Utilities Project

---

## A collection of Python exercises and utilities demonstrating:

𖦹 Runtime type checking via decorator
🦝 Parsing structured data (e.g., animal info from Wikipedia)
⏳ Lesson duration validation using JSON

---

## Requirements

- 🐍 Python **3.12+** ([Download Python](https://www.python.org/downloads/))
- ♻️ [Poetry](https://python-poetry.org/docs/#installation) for dependency management

---

## 📦 Installation

> The project is managed using [Poetry](https://python-poetry.org/) for packaging and dependency management.

1. Clone the repository:
	```bash
	git clone https://github.com/zizevskikh-dev/tetrika-junior
	```

2. Navigate to the project directory:
	```bash
	cd tetrika-junior
	```

3. Install dependencies via Poetry:
	```
	poetry install
	```

---

## 🚀 Usage Guide

### 1. Type Hint Decorator

Runtime enforcement of type hints using a custom `@strict` decorator:
```bash
poetry run python type_hints_decorator.py
```

### 2. Animal Crossing Parser

Fetches animal data (e.g. from Wikipedia):
```bash
poetry run python animal_crossing.py
```

### 3. Lesson Duration Validator

Validates class durations using test data in `task3/test_data.json`:
```bash
poetry run python lessons_duration.py
```

---

## 🛠️ Project Info

- **Version:** 1.0.1
- **Maintainer:** [Aleksander Zizevskikh](https://t.me/zizevskikh_me)
- **License:** MIT
