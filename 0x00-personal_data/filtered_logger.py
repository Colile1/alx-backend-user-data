#!/usr/bin/env python3
"""
Module for filtering and logging personal data with redaction and secure DB
connection.
"""
import re
import logging
import os
import mysql.connector
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Obfuscates values of specified fields in a log message."""
    pattern = rf'({'|'.join(fields)})=.*?{separator}'
    return re.sub(
        pattern,
        lambda m: f"{m.group(1)}={redaction}{separator}",
        message
    )


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class for logging PII fields. """
    REDACTION = "***"
    FORMAT = (
        "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    )
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        original = super().format(record)
        return filter_datum(
            self.fields, self.REDACTION, original, self.SEPARATOR
        )


PII_FIELDS = (
    "name",
    "email",
    "phone",
    "ssn",
    "password"
)


def get_logger() -> logging.Logger:
    """Creates and configures a logger for user data with redaction."""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    if not logger.handlers:
        logger.addHandler(handler)
    return logger


def get_db():
    """Connects to a secure MySQL database using environment variables."""
    return mysql.connector.connect(
        user=os.getenv("PERSONAL_DATA_DB_USERNAME", "root"),
        password=os.getenv("PERSONAL_DATA_DB_PASSWORD", ""),
        host=os.getenv("PERSONAL_DATA_DB_HOST", "localhost"),
        database=os.getenv("PERSONAL_DATA_DB_NAME")
    )


def main():
    """Fetches all users from the DB and logs each row with PII redacted."""
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    fields = [i[0] for i in cursor.description]
    logger = get_logger()
    for row in cursor:
        msg = "; ".join(
            f"{k}={v}" for k, v in zip(fields, row)
        ) + ";"
        logger.info(msg)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
