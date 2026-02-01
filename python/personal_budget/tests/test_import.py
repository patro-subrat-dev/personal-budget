import sys
from pathlib import Path
import tempfile

# Ensure package import works when running tests from repo root
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from personal_budget import db


def test_import_valid_and_invalid(tmp_path):
    db_file = tmp_path / "imp_budget.db"
    conn = db.get_connection(str(db_file))
    db.init_db(conn)
    csv_text = """date,amount,category,description,type
2026-01-01,1000,Salary,Jan salary,income
,50,Food,Missing date,expense
2026-01-05,notanumber,Groceries,Bad amount,expense
2026-01-10,20,,Coffee,expense
2026-01-15,200,Gift,,income
"""
    res = db.import_transactions_from_csv(conn, csv_text)
    assert res["imported"] == 3
    assert len(res["errors"]) == 2


def test_import_empty(tmp_path):
    db_file = tmp_path / "imp_budget2.db"
    conn = db.get_connection(str(db_file))
    db.init_db(conn)
    csv_text = "date,amount,category,description,type\n"
    res = db.import_transactions_from_csv(conn, csv_text)
    assert res["imported"] == 0
    assert len(res["errors"]) == 0
