# BetaFintrack - Financial Tracking Application

## ✨ Fitur Utama

- **Autentikasi Pengguna**
  - Registrasi akun baru dengan username dan password
  - Login dengan validasi username dan password
  - Sistem manajemen session pengguna

- **Dashboard Interaktif**
  - Tampilan dashboard dengan greeting pengguna
  - Real-time clock display
  - Quote motivasi finansial yang berubah-ubah

- **Manajemen Transaksi Keuangan (CRUD)**
  - **Create**: Tambah transaksi income/expense baru
  - **Read**:  Lihat semua transaksi dalam tabel
  - **Update**: Edit transaksi yang sudah tercatat
  - **Delete**:  Hapus transaksi dengan konfirmasi
  - **Search**: Cari transaksi berdasarkan tanggal

- **Kategori Transaksi**
  - Income (Pemasukan)
  - Expense (Pengeluaran)

- **Statistik & Laporan**
  - Total pemasukan (income) real-time
  - Total pengeluaran (expense) real-time
  - Tracking dengan daftar lengkap

- **Antarmuka Modern**
  - Desain GUI yang menarik dengan CustomTkinter
  - Color-coded input fields
  - Responsive layout
  - Logo dan imagery yang terintegrasi

## 🛠 Teknologi yang Digunakan

| Teknologi | Versi | Keterangan |
|-----------|-------|-----------|
| Python | 3.8+ | Bahasa pemrograman utama |
| CustomTkinter | Latest | Framework GUI modern |
| Tkinter | Built-in | GUI toolkit dasar |
| Pillow (PIL) | Latest | Pemrosesan gambar |
| tkcalendar | Latest | Widget date picker |
| SQLite3 | Built-in | Database management |
| Docker | Latest | Container untuk deployment |

## 📋 Prasyarat

- **Python 3.8 atau lebih baru**
  ```bash
  python --version
  ```
- **pip** (Package manager Python)
- **Virtual Environment** (direkomendasikan)
- **(Opsional) Docker** jika ingin menjalankan dalam container

## 🚀 Instalasi

### 1. Clone Repository
```bash
git clone https://github.com/daffadermawan30/Simple-Project.git
cd Simple-Project
```

### 2. Buat Virtual Environment (Direkomendasikan)
```bash
# Linux / macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Instalasi Dependencies
```bash
pip install -r requirements.txt
```

Atau instalasi manual jika tidak ada `requirements.txt`:
```bash
pip install customtkinter pillow tkcalendar
```

### 4. Verifikasi Gambar Assets
Pastikan file-file gambar berikut ada di root directory:
- `logo.png`
- `finance. png`
- `dashboard.png`
- `header.png`
- `income. png`
- `expense.png`
- `logout.png`

## ⚙️ Konfigurasi

### Database Initialization
Aplikasi akan otomatis membuat database SQLite pada startup: 
- Database file: `fintrack.db`
- Tabel otomatis dibuat: 
  - `account` — menyimpan username dan password
  - `financial_record` — menyimpan transaksi keuangan

### Kustomisasi (Opsional)
Anda dapat mengubah beberapa konfigurasi di dalam `BetaFintrack. py`:

```python
# Ukuran window
self.window. geometry("1024x576")

# Tema warna
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

# Daftar quotes motivasi
self.quotes = [
    "Save first, spend later.  - Unknown",
    # ...  tambah lebih banyak
]
```

## 📖 Penggunaan

### Menjalankan Aplikasi (Lokal)
```bash
python BetaFintrack.py
```

### Langkah-Langkah Penggunaan

#### 1. **Registrasi / Login**
- Pilih "Register account" untuk membuat akun baru
- Atau gunakan existing account untuk login
- Masukkan username dan password, tekan Enter atau klik tombol

#### 2. **Dashboard**
- Setelah login, Anda akan masuk ke halaman dashboard
- Lihat greeting dengan nama pengguna Anda
- Observasi real-time clock di pojok atas kiri
- Baca quote motivasi finansial

#### 3. **Tambah Transaksi**
- Di panel kanan, pilih **Date** (tanggal transaksi)
- Isi **Nominal** (jumlah uang)
- Isi **Description** (deskripsi transaksi)
- Pilih **Type** — Income atau Expense
- Klik tombol **Add**

#### 4. **Lihat Transaksi**
- Semua transaksi Anda ditampilkan di tabel bawah
- Total income dan expense dihitung otomatis
- Klik pada baris transaksi untuk memilih/edit

#### 5. **Edit Transaksi**
- Klik baris transaksi di tabel
- Data akan ter-load otomatis di form
- Ubah data sesuai kebutuhan
- Klik tombol **Update** untuk menyimpan perubahan

#### 6. **Hapus Transaksi**
- Klik baris transaksi di tabel
- Klik tombol **Delete**
- Konfirmasi penghapusan
- Transaksi akan dihapus dari database

#### 7. **Cari Transaksi**
- Pilih tanggal di field Date Finder
- Klik tombol **Find**
- Tabel akan menampilkan transaksi pada tanggal tersebut

#### 8. **Logout**
- Klik tombol Logout (icon di sidebar)
- Anda akan kembali ke halaman login

## 📁 Struktur Proyek

```
Simple-Project/
├── BetaFintrack.py          # File utama aplikasi
├── Dockerfile               # Konfigurasi Docker
├── docker-compose.yml       # Konfigurasi Docker Compose
├── fintrack.db              # Database SQLite (auto-generated)
├── requirements.txt         # Daftar dependencies Python
├── . dockerignore            # File yang diabaikan Docker
├── README.md                # File dokumentasi ini
├── logo.png                 # Asset gambar
├── finance.png              # Asset gambar
├── dashboard.png            # Asset gambar
├── header.png               # Asset gambar
├── income.png               # Asset gambar
├── expense.png              # Asset gambar
└── logout.png               # Asset gambar
```

## 🔮 Fitur yang Akan Datang

Sesuai dengan "Comingsoon" button di aplikasi: 
- [ ] Analitik & Grafik Laporan Keuangan
- [ ] Export data ke CSV/PDF
- [ ] Budget tracking dan notifikasi
- [ ] Multi-currency support
- [ ] Cloud backup & sync
- [ ] Mobile version

## 🐳 Menjalankan dengan Docker

### Build & Run dengan Docker
```bash
# Build image
docker build -t betafintrack: latest .

# Run container
docker run --rm -it \
  -v $(pwd):/app \
  -p 7900:7900 \
  betafintrack: latest
```

### Menggunakan Docker Compose
```bash
# Build dan jalankan dengan docker-compose
docker-compose up --build

# Akses VNC di browser:  http://localhost:7900
```

**Note**: Dockerfile ini menggunakan `dorowu/ubuntu-desktop-lxde-vnc` untuk remote desktop access. 

## 🐛 Troubleshooting

### Issue:  ModuleNotFoundError:  No module named 'customtkinter'
**Solusi**:
```bash
pip install customtkinter --upgrade
```

### Issue: FileNotFoundError untuk image files
**Solusi**:  Pastikan semua file `.png` ada di root directory yang sama dengan `BetaFintrack.py`

### Issue: Database locked
**Solusi**: Tutup semua instance aplikasi dan coba jalankan kembali.  Jika persisten, hapus `fintrack.db` dan biarkan aplikasi membuat yang baru.

### Issue: Virtual environment tidak ter-activate
**Solusi**:
```bash
# Linux / macOS
source venv/bin/activate

# Windows (PowerShell)
venv\Scripts\Activate.ps1

# Windows (CMD)
venv\Scripts\activate. bat
```

## 🤝 Kontribusi

Kontribusi sangat diterima! Untuk berkontribusi:

1. Fork repository ini
2. Buat branch untuk fitur Anda: 
   ```bash
   git checkout -b feat/nama-fitur
   ```
3. Commit perubahan:
   ```bash
   git commit -m "Tambah:  deskripsi fitur"
   ```
4. Push ke branch: 
   ```bash
   git push origin feat/nama-fitur
   ```
5. Buat Pull Request

### Format Commit Message
- `Feat: ` untuk fitur baru
- `Fix:` untuk perbaikan bug
- `Docs:` untuk dokumentasi
- `Style:` untuk styling/formatting
- `Refactor:` untuk refactoring kode

## 📝 Informasi Penugasan

**Status**:  Tugas UAS Semester 1 ✅

| Detail | Keterangan |
|--------|-----------|
| Nama Mahasiswa | Daffadermawan |
| NIM | [Masukkan NIM] |
| Mata Kuliah | [Masukkan Mata Kuliah] |
| Dosen Pengampu | [Masukkan Nama Dosen] |
| Semester | 1 (Ganjil) |
| Tahun Akademik | [Masukkan Tahun] |
| Tanggal Pengumpulan | [Masukkan Tanggal] |

## 👤 Penulis

**Daffadermawan30**
- GitHub: [@daffadermawan30](https://github.com/daffadermawan30)
- Repository: [Simple-Project](https://github.com/daffadermawan30/Simple-Project)

## 📄 Lisensi

Proyek ini tidak memiliki lisensi khusus. Silakan tambahkan file `LICENSE` jika diperlukan.

---

## 📞 Support

Jika Anda memiliki pertanyaan atau mengalami masalah: 
- Buka [GitHub Issues](https://github.com/daffadermawan30/Simple-Project/issues)
- Hubungi penulis melalui GitHub

## 🙏 Terima Kasih

Terima kasih telah menggunakan BetaFintrack! Semoga aplikasi ini membantu Anda mengelola keuangan pribadi dengan lebih baik. 

---

**Last Updated**: 27 Desember 2025
