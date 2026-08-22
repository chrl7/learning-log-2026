## Module 2 — Database Design & Normalization

### Normalization: 1NF, 2NF, 3NF

**1NF (First Normal Form):** Every column must hold a single, atomic value —
no lists or comma-separated values in one cell. Fix: split multi-valued
columns into separate rows.

**2NF (Second Normal Form):** Applies to tables with a composite primary key.
Every non-key column must depend on the _entire_ key, not just part of it.
A column depending on only part of a composite key is a "partial dependency" —
fix by moving it to its own table.

**3NF (Third Normal Form):** Non-key columns must depend directly on the
primary key, not on another non-key column. A chain like
`order_id → product → category` is a "transitive dependency" — fix by
moving the transitively-dependent data into its own table.

**Practical takeaway:** Normalization prevents update anomalies (e.g.,
having to update the same customer address in multiple rows) by giving
each table a single responsibility.
