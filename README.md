# FinTrack - Financial Tracker Application 💰

![Dashboard Preview](dashboard.png)
*(Pastikan file gambar dashboard.png ada di folder agar preview muncul di sini)*

**FinTrack** adalah aplikasi desktop sederhana berbasis Python yang dirancang untuk membantu pengguna mencatat dan memantau arus kas keuangan pribadi (Pemasukan & Pengeluaran). Proyek ini dikembangkan sebagai bagian dari **Final Project Cloud Computing** untuk mendemonstrasikan implementasi **Kontainerisasi Aplikasi GUI** menggunakan Docker.

---

## 🚀 Fitur Utama

* **User Authentication**: Sistem Login dan Register akun baru yang aman.
* **Dashboard**: Ringkasan total Pemasukan (Income) dan Pengeluaran (Expense).
* **Transaction Management (CRUD)**:
    * Menambah data transaksi harian.
    * Melihat riwayat transaksi.
    * Mengedit dan Menghapus data transaksi.
* **Database Lokal**: Penyimpanan data menggunakan SQLite (`fintrack.db`).
* **Dockerized Environment**: Aplikasi berjalan di dalam container Ubuntu dengan akses GUI via Browser (VNC).

---

## 🛠️ Teknologi yang Digunakan

* **Bahasa Pemrograman**: [Python 3.10](https://www.python.org/)
* **GUI Framework**: [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) & Tkinter
* **Database**: SQLite3
* **Container Engine**: [Docker](https://www.docker.com/)
* **Base Image**: `dorowu/ubuntu-desktop-lxde-vnc` (Ubuntu + LXDE + VNC)

---

## 📦 Prasyarat

Sebelum menjalankan aplikasi, pastikan komputer Anda telah terinstall:
1.  **Docker Desktop** (Pastikan Docker Engine berjalan).
2.  **Git** (Untuk meng-clone repository).
3.  **Browser Modern** (Google Chrome, Edge, Firefox) untuk mengakses VNC.

---

## ⚙️ Cara Menjalankan (Docker Mode)

Ikuti langkah-langkah berikut untuk menjalankan aplikasi menggunakan Docker (Sesuai skenario UAS):

### 1. Clone Repository
Unduh source code ke komputer Anda.
```bash
git clone [https://github.com/daffadermawan30/simple-project.git](https://github.com/daffadermawan30/simple-project.git)
cd simple-project
```

### 2. Build Docker Image
Bangun image dari Dockerfile dengan tag versi 1.0.1. (Ganti daffadermawan30 dengan username Docker Hub Anda)

```Bash
docker build -t daffadermawan30/simple-project:1.0.1 .
```

3. Jalankan Container
Jalankan container dan mapping port 80 (VNC) ke port 6080 (Localhost).

```Bash
docker run -d -p 6080:80 --name fintrack-app daffadermawan30/simple-project:1.0.1
```

4. Akses Aplikasi
- Buka browser dan kunjungi: http://localhost:6080
- Anda akan melihat tampilan desktop Ubuntu LXDE.
- Klik icon Terminal (System Tools > LXTerminal) di dalam desktop tersebut.
- Ketik perintah berikut untuk menjalankan aplikasi:
```bash
python3 BetaFintrack.py
```

🛑 Cara Menghentikan & Menghapus
Jika sudah selesai, Anda bisa membersihkan environment dengan perintah:
```Bash
# Hentikan & Hapus Container
docker stop fintrack-app
docker rm fintrack-app

# Hapus Image (Opsional)
docker rmi daffadermawan30/simple-project:1.0.1
```

---

📂 Struktur Project
Plaintext
simple-project/
├── 📄 BetaFintrack.py      # Source Code Utama Aplikasi
├── 🐳 Dockerfile           # Konfigurasi Image Docker
├── 📝 fintrack.db          # File Database SQLite
├── 🖼️ assets/              # (File gambar seperti logo.png, header.png, dll)
└── 📄 README.md            # Dokumentasi Project

---

👨‍💻 Author
Nama: Daffa Dermawan
NIM: 1124160177
Kampus: Global Institute of Technology & Business
Mata Kuliah: Pengantar Cloud Computing 