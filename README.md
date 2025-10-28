Nama        : Mohammad Andry Pratama
NIM         : 231011403261
Mata Kuliah : Pengolahan Citra Digital

Pembersihan noise citra restorasi foto hitam putih pada pewarnaan citra otomatis menggunakan Grayscale Gaussian Filter.

Gaussian Filter merupakan teknik noise reduction yang bekerja dengan melakukan konvolusi citra menggunakan kernel berbentuk distribusi Gaussian. Tujuannya menghaluskan variasi intensitas piksel sehingga noise berkurang tanpa menghilangkan detail penting. Langkah ini diperlukan sebelum proses pewarnaan otomatis agar hasil warna lebih bersih dan tidak berbintik.

Langkah Pengerjaan

1. Persiapan Lingkungan

Instal Python dan Visual Studio Code
Tambahkan extension Python di VS Code
Instal library pemrosesan citra melalui terminal:

  pip install opencv-python numpy matplotlib

2. Input Citra

* Siapkan gambar hitam putih yang akan direstorasi (format JPG/PNG)
* Baca citra menggunakan OpenCV

3. Konversi ke Grayscale

Jika citra masih RGB, ubah menjadi grayscale agar fokus pada intensitas cahaya

4. Pembersihan Noise

Terapkan Gaussian Blur dengan kernel (misal 7×7)
Fungsi utama: mengurangi noise dan artefak sebelum pewarnaan

5. Evaluasi dan Simpan Hasil
Tampilkan perbandingan citra asli dan hasil filter
Simpan citra hasil noise removal sebagai input pewarnaan otomatis

6.Hasil

<img width="1200" height="500" alt="Figure_1" src="https://github.com/user-attachments/assets/21f18594-fd01-43b8-9e3c-e90f33e58ca9" />


