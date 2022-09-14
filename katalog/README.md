# Tugas 2

[Heroku](https://tugas-2-ypn.herokuapp.com/) |
[Katalog](https://tugas-2-ypn.herokuapp.com/katalog)

#### Bagan
![Blank diagram (13)](https://user-images.githubusercontent.com/112608722/190231387-51fdb0ab-84b5-478e-9287-420070d3a732.png)

User akan meminta request kepada URLs dan akan berlanjut menuju views. Di views, fungsi yang sesuai request akan dipanggil. Setelah itu, data dari models.py akan diambil oleh views.py dan diakhiri dengan mengembalikan response yang nantinya akan dirender kemudian dimunculkan ke client.


#### Mengapa menggunakan virtual environment?
Virtual environment akan membuat project yang dikerjakan terisolasi dari project lain. Virtual environment packages dan packages yang dipakai membuat project tidak akan tercampur project lain. Penggunaan tersebut akan berguna ketika beberapa project perlu package dengan versi yang berbeda.


#### Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Ya, hal tersebut dapat dilakukan. Apabila tidak menggunakannya, ketika kita melakukan update terhadap packages atau dependencies yang digunakan di projek Django, dapat terjadi perubahan yang tidak diinginkan, seperti packages yang berubah version, dan lain-lain.


#### Implementasi poin 1-4
#### 1. Views.py
Di dalam file ini dibuat sebuah fungsi yang menerima argument berupa request yang bernama show_katalog. Fungsi ini akan mengambil data yang ada di dalam database dan disimpan di variabel context. Adapun terdapat tambahan atribut lain yaitu nama dan npm.

#### 2. Urls.py
Di file ini ditambahkan sebuah routing terhadap katalog berupa path di urlpattern pada folder product-django dengan kode ('katalog/', include('katalog.url')).

#### 3. Pemetaan data ke HTML (katalog.html)
Di file ini akan ditambahkan {{nama}} dan {{npm}} dari fungsi show_katalog. File ini juga akan ditambahkan loop untuk memunculkan data dari list_katalog.

#### 4. Deploy
Aplikasi baru dibuat di Heroku yang nantinya dihubungkan dengan github melalui secrets dengan HEROKU_APP_NAME dan HEROKU_API_KEY.
