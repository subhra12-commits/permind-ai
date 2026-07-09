"""
Universal schema for all interview datasets.

Every dataset will be converted to this format before merging.
"""

MASTER_COLUMNS = [

    # Unique Information
    "id",

    # Interview Data
    "question",
    "answer",

    # Classification
    "category",
    "subcategory",
    "difficulty",

    # Metadata
    "source",
    "dataset_name",
    "interview_type",
    "language",

    # AI Features
    "tags",

    # Timestamp
    "created_at"

]