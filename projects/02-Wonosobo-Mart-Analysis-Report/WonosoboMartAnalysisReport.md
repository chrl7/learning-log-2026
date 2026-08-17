# Project: Wonosobo Mart Analysis Report

Module: SQL & Databases (Module 2)
Tools: MySQL via XAMPP + SQLyog
Dataset: 3 related tables — `pelanggan`, `produk`, `pesanan`

## Overview

A set of 6 analytical SQL reports simulating a request from a small online store owner, built to consolidate everything learned in Module 2: relational concepts, filtering, aggregation, JOINs, LEFT JOINs, and subqueries — applied together rather than in isolation.

---

## Report 1: Top Spending Customers

Business question: Which customers generate the most revenue, and where are they located?

```sql
SELECT pelanggan.nama, pelanggan.kota, SUM(pesanan.jumlah * produk.harga) AS total_belanja
FROM pesanan
INNER JOIN pelanggan ON pesanan.id_pelanggan = pelanggan.id_pelanggan
INNER JOIN produk ON pesanan.id_produk = produk.id_produk
GROUP BY pelanggan.id_pelanggan, pelanggan.nama, pelanggan.kota
ORDER BY total_belanja DESC;
```

Notes: Uses `INNER JOIN` intentionally — this report is specifically about customers who _have_ purchased, so customers with zero orders are correctly excluded here (see Report 3 for the inactive-customer complement).

---

## Report 2: Best-Selling Product per Category

Business question: Within each product category, which single product sells the most units?

```sql
WITH ranking_penjualan AS (
    SELECT
        produk.kategori,
        produk.nama_produk,
        SUM(pesanan.jumlah) AS total_terjual,
        RANK() OVER (
            PARTITION BY produk.kategori
            ORDER BY SUM(pesanan.jumlah) DESC
        ) AS peringkat
    FROM produk
    JOIN pesanan ON produk.id_produk = pesanan.id_produk
    GROUP BY produk.kategori, produk.id_produk, produk.nama_produk
)
SELECT kategori, nama_produk, total_terjual
FROM ranking_penjualan
WHERE peringkat = 1;
```

Notes: Uses a CTE (`WITH`) and the `RANK() OVER (PARTITION BY ...)` window function — techniques beyond the core Module 2 curriculum, self-taught while working on this report. Unlike `GROUP BY`, a window function ranks rows _within_ each category without collapsing them into a single summary row, which is what makes "best per group" queries possible in one pass.

---

## Report 3: Inactive Customers (solved two ways)

Business question: Which customers have never placed an order, so they can be followed up with?

```sql
-- Approach A: LEFT JOIN + IS NULL
SELECT pelanggan.nama, pelanggan.kota
FROM pelanggan
LEFT JOIN pesanan ON pelanggan.id_pelanggan = pesanan.id_pelanggan
WHERE pesanan.id_pesanan IS NULL;

-- Approach B: Subquery with NOT IN
SELECT nama, kota
FROM pelanggan
WHERE id_pelanggan NOT IN (
    SELECT id_pelanggan FROM pesanan WHERE id_pelanggan IS NOT NULL
);
```

Notes: Both approaches return the same result, confirming they're logically equivalent for this case. The `WHERE id_pelanggan IS NOT NULL` inside the subquery guards against a well-known SQL pitfall: if a `NOT IN` subquery's result set contains even one `NULL`, the entire `NOT IN` comparison silently returns zero rows (since SQL can't determine "not equal to NULL/unknown"). Defensive habit worth keeping whenever `NOT IN` wraps a subquery.

---

## Report 4: Products Priced Above Their Category Average

Business question: Which products are priced above the average for their _own_ category (not the overall average)?

```sql
SELECT p1.nama_produk, p1.kategori, p1.harga
FROM produk p1
WHERE p1.harga > (
    SELECT AVG(p2.harga) FROM produk p2 WHERE p2.kategori = p1.kategori
);
```

Notes: This is a _correlated subquery_ — the inner query references the outer query's current row (`p1.kategori`), so it re-evaluates per row rather than running once. Two aliases (`p1`, `p2`) of the same table are needed to distinguish "the row being checked" from "the rows being averaged."

---

## Report 5: City Summary (cities with 2+ customers)

Business question: For cities with a meaningful customer base (2+), what's the combined revenue?

```sql
SELECT pelanggan.kota,
       COUNT(DISTINCT pelanggan.id_pelanggan) AS jumlah_pelanggan,
       COALESCE(SUM(pesanan.jumlah * produk.harga), 0) AS total_belanja
FROM pelanggan
LEFT JOIN pesanan ON pelanggan.id_pelanggan = pesanan.id_pelanggan
LEFT JOIN produk ON pesanan.id_produk = produk.id_produk
GROUP BY pelanggan.kota
HAVING COUNT(DISTINCT pelanggan.id_pelanggan) >= 2;
```

Notes: `COUNT(DISTINCT ...)` is essential here, not just `COUNT(...)` — because of the double `LEFT JOIN` (through `pesanan` into `produk`), a customer with multiple orders appears as multiple rows. Without `DISTINCT`, that customer would be miscounted as multiple customers.

---

## Report 6: Above-Average-Age Customers Who Are Active Buyers

Business question: Among older customers (above average age), which ones are actually engaged (have purchased at least once)?

```sql
SELECT id_pelanggan, nama, umur
FROM pelanggan
WHERE umur > (SELECT AVG(umur) FROM pelanggan)
  AND id_pelanggan IN (SELECT id_pelanggan FROM pesanan);
```

Notes: Combines two independent filter conditions (`AND`) — one direct comparison against a scalar subquery, one membership check against a list subquery.

---
