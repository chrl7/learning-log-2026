# Core Concepts

Table = Spreadsheet
A database is a collection of tables, similar to a workbook with multiple sheets in Excel. Each table holds one type of data (e.g. 'pelanggan' for customers, 'produk' for products).

Rows & Columns

- Column = a fixed category of data (e.g. 'nama', 'kota', 'umur') — like a spreadsheet header.
- Row = one complete record/entry (e.g. one customer's full data).

## Primary Key (PK)

A column whose value is unique for every row, used as the row's identity — similar to an ID card (KTP). We can't rely on a column like 'nama' as identity since names can duplicate; a PK (e.g. 'id_pelanggan', 'id_produk') guarantees uniqueness.

## Foreign Key (FK)

A column in one table that references the Primary Key of another table — this is what makes a database "relational" (tables connected to each other).

Example: the 'pesanan' (orders) table has 'id_pelanggan' and 'id_produk' columns, which reference 'pelanggan(id_pelanggan)' and 'produk(id_produk) respectively — instead of repeating full customer/product details in every order row.

---

### Sample Dataset ("Wonosobo Mart")

Three related tables used throughout this module:

- `pelanggan` (customers): id_pelanggan (PK), nama, kota, umur
- `produk` (products): id_produk (PK), nama_produk, kategori, harga, stok
- `pesanan` (orders): id_pesanan (PK), id_pelanggan (FK), id_produk (FK), jumlah, tanggal

---

### SQL Commands Learned

SELECT — choose which columns to display

```sql
SELECT * FROM pelanggan;
SELECT nama, kota FROM pelanggan;
```

WHERE — filter which rows to display (like a spreadsheet filter)

```sql
SELECT * FROM pelanggan WHERE kota = 'Wonosobo';
```

ORDER BY — sort rows

```sql
SELECT * FROM produk ORDER BY harga ASC;
SELECT * FROM produk ORDER BY harga DESC;
```

LIMIT — restrict number of rows returned

```sql
SELECT * FROM produk ORDER BY harga DESC LIMIT 3;
```

Combined example

```sql
SELECT nama_produk, harga
FROM produk
WHERE kategori = 'Minuman'
ORDER BY harga DESC
LIMIT 2;
```

AND — all conditions must be true

```sql
SELECT * FROM pelanggan WHERE kota = 'Wonosobo' AND umur > 25;
```

OR — at least one condition must be true

```sql
SELECT * FROM pelanggan WHERE kota = 'Wonosobo' OR kota = 'Semarang';
```

IN — checks if a value matches any value in a list (shorthand for repeated OR)

```sql
SELECT * FROM pelanggan WHERE kota IN ('Wonosobo', 'Semarang', 'Yogyakarta');
```

BETWEEN — range check, inclusive of both bounds

```sql
SELECT * FROM produk WHERE harga BETWEEN 3000 AND 5000;
```

LIKE — pattern matching on text using `%` as wildcard

```sql
SELECT * FROM produk WHERE nama_produk LIKE 'Teh%';    -- starts with "Teh"
SELECT * FROM produk WHERE nama_produk LIKE '%Botol%'; -- contains "Botol"
SELECT * FROM produk WHERE nama_produk LIKE '%Instan'; -- ends with "Instan"
```

### Aggregate Functions & GROUP BY

Aggregate functions — collapse many rows into a single summary value

```sql
SELECT COUNT(*) FROM pelanggan;   -- count rows
SELECT SUM(harga) FROM produk;    -- sum values
SELECT AVG(harga) FROM produk;    -- average
SELECT MAX(harga) FROM produk;    -- highest value
SELECT MIN(harga) FROM produk;    -- lowest value
```

GROUP BY — summarize data per category/group rather than as one grand total

```sql
SELECT kategori, COUNT(*) AS jumlah_produk
FROM produk
GROUP BY kategori;
```

Rule: any non-aggregate column in SELECT must also appear in GROUP BY.

AS — alias to rename a result column for readability

```sql
SELECT kategori, AVG(harga) AS rata_rata_harga FROM produk GROUP BY kategori;
```

HAVING — filters grouped/aggregated results (runs _after_ grouping), as opposed to WHERE which filters rows _before_ grouping

```sql
SELECT kategori, COUNT(*) AS jumlah_produk
FROM produk
GROUP BY kategori
HAVING COUNT(*) > 1;
```

Why `WHERE` can't filter on aggregate results (e.g. `WHERE AVG(harga) > 4000`):
`WHERE` executes row-by-row, _before_ rows are grouped — at that stage, an aggregate like `AVG()` can't be computed yet since it needs a collection of already-grouped rows. `HAVING` runs _after_ `GROUP BY` has grouped and aggregated the data, so it's the correct clause for filtering on aggregate results.

Pattern: WHERE + GROUP BY + HAVING + ORDER BY combined\*\*

```sql
SELECT kota, COUNT(*) AS jumlah_pelanggan
FROM pelanggan
GROUP BY kota
HAVING COUNT(*) > 1
ORDER BY jumlah_pelanggan DESC;
```

Execution order (conceptually): WHERE (filter rows) → GROUP BY (group) → aggregate functions computed → HAVING (filter groups) → ORDER BY (sort final result).

### JOIN — Combining Data Across Tables

Why JOIN is needed:Querying a table with foreign keys alone only returns raw IDs (e.g. `id_pelanggan = 1`), which isn't human-readable. JOIN combines rows from two or more tables based on a related column — typically matching a foreign key to a primary key.

INNER JOIN — basic syntax

```sql
SELECT pesanan.id_pesanan, pelanggan.nama, pesanan.jumlah
FROM pesanan
INNER JOIN pelanggan ON pesanan.id_pelanggan = pelanggan.id_pelanggan;
```

Reads as: start from `pesanan`, join with `pelanggan` by matching `id_pelanggan` in both tables, then select the desired columns from either table.

Joining 3 tables

```sql
SELECT pelanggan.nama, produk.nama_produk, pesanan.jumlah, pesanan.tanggal
FROM pesanan
INNER JOIN pelanggan ON pesanan.id_pelanggan = pelanggan.id_pelanggan
INNER JOIN produk ON pesanan.id_produk = produk.id_produk;
```

`table.column` notation: Needed when multiple tables share a column name (e.g. `id_pelanggan` exists in both `pelanggan` and `pesanan`), to disambiguate which table's column is being referenced.

Table aliases — shorten table names for readability

```sql
SELECT p.nama, pr.nama_produk, ps.jumlah
FROM pesanan ps
INNER JOIN pelanggan p ON ps.id_pelanggan = p.id_pelanggan
INNER JOIN produk pr ON ps.id_produk = pr.id_produk;
```

### LEFT JOIN & NULL

LEFT JOIN — returns _all_ rows from the left (first-named) table, even when there's no matching row in the right table. Unmatched columns from the right table are filled with "NULL".

```sql
SELECT pelanggan.nama, pesanan.jumlah
FROM pelanggan
LEFT JOIN pesanan ON pelanggan.id_pelanggan = pesanan.id_pelanggan;
```

Contrast with "INNER JOIN", which only returns rows that have a match in both tables — rows without a match (e.g. a customer who never ordered) are silently excluded.

NULL — represents "no value," distinct from 0 or an empty string. Must be checked with `IS NULL` / `IS NOT NULL`, never `= NULL` (which never evaluates as expected in SQL).

```sql
SELECT * FROM pelanggan
LEFT JOIN pesanan ON pelanggan.id_pelanggan = pesanan.id_pelanggan
WHERE pesanan.id_pesanan IS NULL;
```

This pattern finds "orphan" rows in the left table — records with no matching counterpart in the right table (e.g. customers who never placed an order).

When to use which:

- `INNER JOIN` — only care about rows with a complete match in both tables (e.g. sales reports).
- `LEFT JOIN` — need all rows from the main table regardless of match (e.g. customer engagement reports, including those with zero activity).
