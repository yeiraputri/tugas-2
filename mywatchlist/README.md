# Tugas 3

[Heroku](https://tugas-2-ypn.herokuapp.com/) |
[MyWatchList](https://tugas-2-ypn.herokuapp.com/mywatchlist)

### Perbedaan antara JSON, XML, dan HTML
#### JSON
JSON adalah format yang digunakan untuk menukar informasi yang berasal dari _web server_ sehingga pengguna dapat membacanya. JSON akan membuat elemen yang disimpan menjadi lebih efisien meski tidak rapi saat dilihat.

#### XML
XML adalah format yang digunakan dalam menyederhanakan proses pertukaran dan penyimpanan data. Berbalikan dengan JSON, XML akan membuat data yang disimpan lebih rapi meski kurang efisien.

#### HTML
HTML adalah markup language yang digunakan dalam merepresentasikan data ke dalam _element tree_. Data tersebut nantinya akan ditampilkan dalam bentuk _web page_ yang dapat dikustomisasi.


### Mengapa perlu _data delivery_ dalam pengimplementasian sebuah platform?
Ketika membangun sebuah _platform_, kita ingin menyampaikan data ke _user_. Kegiatan tersebut membuat terciptanya sebuah _platform_ yaitu, bertukar informasi antara server dan user dan _data delivery_ penting dalam pengimplementasiannya.


### Implementasi Watchlist
Pertama-tama, saya membuat aplikasi baru bernama mywatchlist di proyek Django Tugas 2. Pembuatan aplikasi dapat dibuat dengan perintah python manage.py startapp mywatchlist. Saya juga menambahkan path mywatchlist sehingga dapat diakses melalui http://localhost:8000/mywatchlist dengan menambahkan path path('mywatchlist/', include('mywatchlist.urls')) pada urls.py di folder project_django.

Saya membuat model MyWatchList dengan atribut watched, title, release date, dan review. Saya pun membuat class MyWatchList di models.py dengan menuliskannya sebagai berikut.
class MyWatchList(models.Model):
    watched = models.BooleanField()
    title = models.TextField()
    rating = models.IntegerField()
    release_date = models.IntegerField()
    review = models.TextField()

Saya mengimplementasikan fitur untuk menyajikan data yang saya buat dengan format HTML, XML, dan JSON dengan membuat function di views.py dan menambahkan path untuk tiap format pada urls.py. Kemudian saya menjalankan python manage.py makemigrations dan python manage.py migrate dan melakukan deployment ke Heroku


### Postman
HTML
![HTML](https://github.com/yeiraputri/tugas-2/blob/main/mywatchlist/Postman/Screenshot%202022-09-22%20104037.png)

JSON
![JSON](https://github.com/yeiraputri/tugas-2/blob/main/mywatchlist/Postman/Screenshot%202022-09-22%20104250.png)

XML
![XML](https://github.com/yeiraputri/tugas-2/blob/main/mywatchlist/Postman/Screenshot%202022-09-22%20104057.png)



