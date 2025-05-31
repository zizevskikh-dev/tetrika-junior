# 🐍 Python Utilities Project

## A collection of Python exercises and utilities demonstrating

- 𖦹 Runtime type checking via decorator
- 🦝 Parsing structured data (e.g., animal info from Wikipedia)
- ⏳ Lesson duration validation using JSON

---

## ⚙️ Requirements

- 🐍 Python **3.12+** ([Download Python](https://www.python.org/downloads/))
- ♻️ [Poetry](https://python-poetry.org/docs/#installation) for dependency management (or standard `venv`)

---

## 📦 Installation

> The project is managed using [Poetry](https://python-poetry.org/) for packaging and dependency management.
> 
> Alternatively, you can use standard `venv` and install dependencies from `requirements.txt`.

1. **Clone the repository:** 
    ```bash  
    git clone https://github.com/zizevskikh-dev/tetrika-junior
    ```  

2. **Navigate to the project directory:** 
    ```bash  
    cd tetrika-junior
    ```

3. **Install dependencies:**  
	- **Using Poetry**:  
  
        ```bash
        poetry install  
        ```

	- **Using pip (with venv):**
		```bash
		python3 -m venv .venv
		```

		- *Unix:*
			```bash
			source .venv/bin/activate
			```

		- Windows:
			```bash
			.venv\Scripts\activate
			```

		```bash
		pip install -r requirements.txt
		```

---

## 🚀 Usage Guide

### 1. Type Hints Decorator

Runtime enforcement of type hints using a custom `@strict` decorator:
```bash
python3 type_hints_decorator.py
```

### 2. Animal Crossing

Fetches animal data (e.g. from Wikipedia):
```bash
python3 animal_crossing.py
```

### 3. Lessons Duration

Validates class durations using test data in `task3/test_data.json`:
```bash
python3 lessons_duration.py
```

---

## 🛠️ Project Info

- **Version:** 1.0.1
- **Maintainer:** [Aleksander Zizevskikh](https://t.me/zizevskikh_me)
- **License:** MIT
