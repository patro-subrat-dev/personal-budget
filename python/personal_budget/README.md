# Personal Budget Tracker

A simple, beginner-friendly Python CLI to track income and expenses. Data is stored in a local SQLite database (`budget.db`).

## Features ✅

- Add income/expense transactions
- List recent transactions
- Monthly summary (total income, total expense, net)

## Quick start 🚀

1. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

1. Initialize the DB (first run will create `budget.db` automatically):

```bash
python -m personal_budget.main add --type expense --amount 12.50 --category Food --desc "Lunch"
```

1. List transactions:

```bash
python -m personal_budget.main list
```

1. Monthly summary:

```bash
python -m personal_budget.main summary --year 2026 --month 1
```

---

## Streamlit UI (optional)

Start the simple web UI with Streamlit:

```bash
# from workspace root
streamlit run python/personal_budget/personal_budget/streamlit_app.py
```

This opens a small web UI where you can add transactions and view summaries.

---

## CSV import/export

A sample CSV template is available: `PERSONAL_BUDGET_TEMPLATE.csv` (headers: `date,amount,category,description,type`). You can download it from the Streamlit UI and upload CSVs to import transactions. The importer reports how many rows were imported and shows row-level errors for bad rows.

---

## Docker

Run the app with Docker:

```bash
# build image
docker build -t personal-budget .

# run container
docker run -p 8501:8501 personal-budget
```

Or with Docker Compose:

```bash
docker-compose up --build
```

## Tests

Run tests with:

```bash
pytest -q
```

## License

MIT
