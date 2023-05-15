#!/usr/bin/python3
"""
initialize models package
"""

from models.engine.file_storage import FileStorage

store = FileStorage()
store.reload()
