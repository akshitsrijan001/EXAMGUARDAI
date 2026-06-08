import sqlite3

DB_NAME = "database/examguard.db"


def init_db():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS exam_reports(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        candidate_name TEXT,
        face_count INTEGER,
        violations INTEGER,
        evidence_count INTEGER,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def save_report(
    candidate_name,
    face_count,
    violations,
    evidence_count
):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO exam_reports(
        candidate_name,
        face_count,
        violations,
        evidence_count
    )
    VALUES (?, ?, ?, ?)
    """, (
        candidate_name,
        face_count,
        violations,
        evidence_count
    ))

    conn.commit()
    conn.close()


def get_all_reports():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        id,
        candidate_name,
        face_count,
        violations,
        evidence_count,
        timestamp
    FROM exam_reports
    ORDER BY id DESC
    """)

    reports = cursor.fetchall()

    conn.close()

    return reports