-- ============================================
-- DATABASE LOGIKA FUZZY - VARIABEL USIA
-- ============================================

CREATE DATABASE IF NOT EXISTS fuzzy_usia;
USE fuzzy_usia;

-- ============================================
-- TABEL KATEGORI USIA
-- ============================================

CREATE TABLE kategori_usia (
    id_kategori INT AUTO_INCREMENT PRIMARY KEY,
    nama_kategori VARCHAR(50) NOT NULL,
    nama_inggris VARCHAR(50),
    rentang_usia VARCHAR(50),
    titik_a DECIMAL(5,2) NOT NULL,
    titik_b DECIMAL(5,2) NOT NULL,
    titik_c DECIMAL(5,2) NOT NULL,
    keterangan TEXT
);

-- ============================================
-- DATA KATEGORI FUZZY
-- ============================================

INSERT INTO kategori_usia
(nama_kategori, nama_inggris, rentang_usia, titik_a, titik_b, titik_c, keterangan)
VALUES
(
    'Bayi/Anak Usia Dini',
    'Baby/Early Childhood',
    '0-5 tahun',
    0,
    2.5,
    5,
    'Fungsi keanggotaan segitiga untuk usia bayi atau anak usia dini'
),
(
    'Anak-anak',
    'Children',
    '6-11 tahun',
    5,
    8.5,
    11,
    'Fungsi keanggotaan segitiga untuk usia anak-anak'
),
(
    'Remaja',
    'Adolescent',
    '10-19 tahun',
    10,
    14.5,
    19,
    'Fungsi keanggotaan segitiga untuk usia remaja'
),
(
    'Pemuda',
    'Youth',
    '15-24 tahun',
    15,
    19.5,
    24,
    'Fungsi keanggotaan segitiga untuk usia pemuda'
),
(
    'Dewasa',
    'Adult',
    '20-65 tahun',
    20,
    42.5,
    65,
    'Fungsi keanggotaan segitiga untuk usia dewasa'
),
(
    'Lanjut Usia',
    'Elderly/Lansia',
    '60-80 tahun',
    60,
    70,
    80,
    'Fungsi keanggotaan segitiga untuk usia lanjut'
);

-- ============================================
-- TABEL DATA USIA
-- ============================================

CREATE TABLE data_usia (
    id_usia INT AUTO_INCREMENT PRIMARY KEY,
    usia INT NOT NULL,
    keterangan VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================
-- CONTOH DATA USIA
-- ============================================

INSERT INTO data_usia (usia, keterangan) VALUES
(2, 'Bayi/Anak Usia Dini'),
(5, 'Bayi/Anak Usia Dini'),
(7, 'Anak-anak'),
(9, 'Anak-anak'),
(11, 'Anak-anak'),
(13, 'Remaja'),
(15, 'Remaja'),
(17, 'Remaja'),
(19, 'Remaja'),
(20, 'Pemuda'),
(22, 'Pemuda'),
(24, 'Pemuda'),
(25, 'Dewasa'),
(30, 'Dewasa'),
(40, 'Dewasa'),
(50, 'Dewasa'),
(60, 'Dewasa'),
(65, 'Dewasa'),
(70, 'Lanjut Usia'),
(75, 'Lanjut Usia'),
(80, 'Lanjut Usia');

-- ============================================
-- TABEL HASIL PERHITUNGAN FUZZY
-- ============================================

CREATE TABLE hasil_fuzzy (
    id_hasil INT AUTO_INCREMENT PRIMARY KEY,
    usia INT NOT NULL,
    id_kategori INT NOT NULL,
    nilai_keanggotaan DECIMAL(5,2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (id_kategori)
        REFERENCES kategori_usia(id_kategori)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- ============================================
-- CONTOH HASIL FUZZY
-- ============================================

INSERT INTO hasil_fuzzy
(usia, id_kategori, nilai_keanggotaan)
VALUES
(13, 3, 0.67);

-- ============================================
-- CEK DATA
-- ============================================

SELECT * FROM kategori_usia;

SELECT * FROM data_usia;

SELECT
    hf.id_hasil,
    hf.usia,
    ku.nama_kategori,
    hf.nilai_keanggotaan
FROM hasil_fuzzy hf
JOIN kategori_usia ku
ON hf.id_kategori = ku.id_kategori;
