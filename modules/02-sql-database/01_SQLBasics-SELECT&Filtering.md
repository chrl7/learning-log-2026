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

'ORDER BY' — sort rows

```sql
SELECT * FROM produk ORDER BY harga ASC;
SELECT * FROM produk ORDER BY harga DESC;
```

'LIMIT' — restrict number of rows returned

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

---
