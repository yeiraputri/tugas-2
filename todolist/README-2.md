[Heroku](https://tugas-2-ypn.herokuapp.com/) |
[Todolist](https://tugas-2-ypn.herokuapp.com/todolist)

### Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
#### Asynchronous programming adalah ketika tugas kedua dapat mulai dieksekusi secara paralel, tanpa menunggu tugas sebelumnya selesai. Synchronous programming adalah ketika tugas pertama dalam suatu program harus menyelesaikan pemrosesannya sebelum melanjutkan ke tugas berikutnya.

### Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
#### Event-driven programming adalah paradigma pemrograman yang digunakan untuk menyinkron terjadi beberapa peristiwa dan membuat program sesederhana. Komponen dasar dari Event-Driven Programming adalah: 
* Fungsi callback ( disebut event handler) dipanggil saat event dipicu.
* Event loop yang mendengarkan pemicu event dan memanggil event handler yang sesuai untuk event tersebut.
#### Contoh penerapan di tugas ini adalah tombol button `Add Task` yang akan berjalan pada saat button diclick.

### Jelaskan penerapan asynchronous programming pada AJAX.
#### Saat user pada client memiliki sebuah event atau permintaan ke server, maka event dari user akan ditampung ke mesin AJAX. Mesin AJAX akan menampung semua event dari user dan melakukan transfer data. Data akan diproses secara server-side dengan metode asynchronous. Hasil dari proses data ini akan mengupdate halaman website secara langsung tanpa perlu adanya refresh lagi dari user.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas
#### 
1. Membuat fungsi show_json pada views.py untuk return data yang dibuat oleh user
2. Membuat fungsi add_task pada views.py dan menambahkannya ke routing pada file urls.py
3. Menyesuaikan html dengan fungsi baru yang telah dibuat