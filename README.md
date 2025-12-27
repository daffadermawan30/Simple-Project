# FinTrack Desktop App (Dockerized)

FinTrack adalah aplikasi desktop berbasis **Python GUI (Tkinter)** yang dijalankan di dalam **Docker container** menggunakan **Ubuntu Desktop LXDE + VNC**, sehingga aplikasi dapat diakses melalui browser tanpa perlu instalasi langsung di sistem host.

Project ini dibuat untuk memenuhi kebutuhan **Ujian Akhir Semester (UAS)** dengan fokus pada implementasi Docker, image build, container runtime, serta dokumentasi teknis yang jelas.

---

## 📌 Fitur Utama
- Aplikasi desktop berbasis Python (Tkinter)
- UI modern menggunakan CustomTkinter
- Dapat dijalankan di browser melalui VNC
- Environment terisolasi menggunakan Docker
- Mudah dijalankan di berbagai sistem operasi

---

## 🛠️ Teknologi yang Digunakan
- **Docker**
- **Ubuntu Desktop LXDE**
- **Python 3**
- **Tkinter**
- **CustomTkinter**
- **Pillow**
- **TkCalendar**

---

## 📂 Struktur Project


---

## 🐳 Penjelasan Dockerfile (Ringkas)
Dockerfile pada project ini berfungsi untuk:
- Menggunakan base image Ubuntu Desktop dengan LXDE dan VNC
- Menghapus repository Google Chrome yang bermasalah
- Menginstall Python dan dependensi GUI
- Menyalin source code aplikasi ke container
- Menjalankan aplikasi secara otomatis saat container aktif

---

## ⚙️ Cara Build Docker Image
Pastikan Docker sudah terinstall, lalu jalankan:

```bash
docker build -t fintrack:1.0.1 .