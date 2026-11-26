# FakeStoreAPI to PostgreSQL ETL Pipeline

An end-to-end Python ETL (Extract, Transform, Load) pipeline that ingests product and user records from the [FakeStoreAPI](https://fakestoreapi.com/), flattens and standardizes the nested JSON payloads using **pandas**, and loads the clean relational tables into **PostgreSQL** via **SQLAlchemy**.

---

## Architecture & Workflow

```text
[FakeStoreAPI (REST JSON)] ──► [Extract (requests + pandas)] ──► [Transform (pandas)] ──► [Load (SQLAlchemy + PostgreSQL)]

fake-api-project/
├── etl/
│   ├── extract.py        # API extraction logic
│   ├── transform.py      # Data cleaning & JSON flattening
│   └── load.py           # PostgreSQL connection & table loading
├── main.py               # Pipeline entry point
├── .env                  # Local database credentials (ignored by Git)
├── .gitignore            # Git exclusion rules
└── README.md             # Project documentation
