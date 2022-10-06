[Heroku](https://tugas-2-ypn.herokuapp.com/) |
[MyWatchList](https://tugas-2-ypn.herokuapp.com/todolist)

### Apa kegunaan {% csrf_token %} pada elemen ? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen ?
#### Serangan CSRF (Cross-Site Request Forgery) adalah serangan yang membuat end-user diharsukan untuk mengeksekusi action pada aplikasi web dimana user sudah mengauntentikasi dirinya. Attacker dapat dengan mudah memanfaatkan user yang sudah terauntentikasi dengan mengubah request yang dikirim oleh user. Maka dari itu, Django memiliki tag {% csrf_token %} yang akan mengenerate token pada server-side saat me-render halaman dan akan kembali memeriksa token tersebut setiap request yang datang. Apabila requesr tidak memiliki token tersebut, request tidak akan dieksekusi.

### Apakah kita dapat membuat elemen secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat secara manual.
#### Dalam membuat form, dapat memanfaatkan elemen `<table>`. Table digunakan dalam membuat field untuk user dalam mengisi data yang diinginkan dengan menggunakan `<input>` dan `<input type = 'submit'>` yang digunakan untuk mengirim data dari form yang sudah diisi

### Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
#### Ketika user menekan tombol submit, data yang dikumpulkan akan dikirim ke program lain untuk diproses. Element `form` mempunyai dua atribut yang memiliki kontrol terhadap aktivitas setelah form disubmit, yaitu `action` dan `method`. Atribut `action` akan mengontrol ke mana program mana data akan dikirimkan. Atribut `method` memiliki dua value, yaitu `GET` dan `POST`. `GET` akan mengumpulkan data yang sudah dikumpulkan menjadi string dan string tersebut akan digunakan untuk membuat URL yang berisi alamat dimana data akan dikirimkan serta data keys maupun values. Ketika login form di-return menggunakan `POST`, browser akan mengumpulkan data, meng-encode untuk transmisi, mengirimkannya ke server, dan menerima respons kembali.

### Implementasi checklist
#### Pertama
Menjalankan `py manage.py startapp todolist`

#### Kedua
Menambahkan todolist ke dalam `urls.py` pada folder `project_django`

#### Ketiga
Membuat model `Task` pada `models.py` dengan atribut `user`, `date`, `title`, `descripton` dan `is_finished`.

#### Keempat
Membuat fungsi login, logout, register dan menghubungkannya dengan html masing-masing. Kemudian menambahkan sebuah restriksi agar user harus login terlebih dahulu sebelum dapat mengakses fungsi lain
```

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist = Task.objects.filter(user = request.user)
    context = {
    'username': request.user,
    'list_barang': data_todolist,
    'nama': 'Yeira',
    'id': '2106751726',
    'last_login': request.COOKIES['last_login'],
    'task_count': data_todolist.count()
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login_user')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) 
            response.set_cookie('last_login', str(datetime.datetime.now())) 
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login_user'))
    response.delete_cookie('last_login')
    return response
    
```

#### Kelima
Membuat halaman utama pada web
```
<div>
    <div class="header" style="text-align: center">
        <p>Hello {{username}}</p>
    </div>
  
    <table style="border:1px ;margin-left:auto;margin-right:auto;">
        {% if task_count > 0 %}
        <tr>
            <th>Date</th>
            <th>Task</th>
            <th>Description</th>
            <th>Status</th>
        </tr>
        {% else %}
  
      
        <tr>
            <th>Belum ada task yang dibuat</th>
        </tr>
        {% endif %}
  
  
        {% comment %} Add the data below this line {% endcomment %}
        {% for todo in list_barang %}
        <tr>
            <th>{{todo.date}}</th>
            <th>{{todo.title}}</th>
            <th>{{todo.description}}</th>
            <th>
                {% if todo.is_finished %}
                Selesai
                {% else %}
                Belum Selesai
                {% endif %}
            </th>
          
            <th>
            <button><a href="{% url 'todolist:change' todo.id %}" title="">Change Status</a></button>
            <button><a href="{% url 'todolist:delete' todo.id %}" title="">Delete</a></button>
            </th>
        </tr>
        {% endfor %}
    </table>

    <br>
    <div style="text-align: center">
        <button onclick="location.href='/todolist/create-task'">Create New Task</button>
        <button><a href="{% url 'todolist:logout_user' %}">Logout</a></button>
        <h5>Sesi terakhir login: {{ last_login }}</h5>

    </div>
</div>
```

#### Keenam
Membuat html yang menampilkan form untuk menambahkan form baru
```
<div>
    <div class="header" style="text-align: center">
        <p>Hello {{username}}</p>
    </div>
  
    <table style="border:1px ;margin-left:auto;margin-right:auto;">
        {% if task_count > 0 %}
        <tr>
            <th>Date</th>
            <th>Task</th>
            <th>Description</th>
            <th>Status</th>
        </tr>
        {% else %}
  
      
        <tr>
            <th>Belum ada task yang dibuat</th>
        </tr>
        {% endif %}
  
  
        {% comment %} Add the data below this line {% endcomment %}
        {% for todo in list_barang %}
        <tr>
            <th>{{todo.date}}</th>
            <th>{{todo.title}}</th>
            <th>{{todo.description}}</th>
            <th>
                {% if todo.is_finished %}
                Selesai
                {% else %}
                Belum Selesai
                {% endif %}
            </th>
          
            <th>
            <button><a href="{% url 'todolist:change' todo.id %}" title="">Change Status</a></button>
            <button><a href="{% url 'todolist:delete' todo.id %}" title="">Delete</a></button>
            </th>
        </tr>
        {% endfor %}
    </table>

    <br>
    <div style="text-align: center">
        <button onclick="location.href='/todolist/create-task'">Create New Task</button>
        <button><a href="{% url 'todolist:logout_user' %}">Logout</a></button>
        <h5>Sesi terakhir login: {{ last_login }}</h5>

    </div>
</div>
```

#### Ketujuh
Menambahkan routing untuk semua fungsi pada `views.py` ke dalam `urls.py` pada folder `todolist`
---

# Tugas 5

### Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
* Inline : kode CSS diletakkan dalam tag elemen HTML dengan atribut 'style'. Kelebihan : Perubahan dapat dengan mudah dilakukan dan style dapat dengan mudah diuji coba. 
Kekurangan : Ketika menerapkan style yang sama ke elemen yang berbeda kurang efektif yang membuat file HTML menjadi penuh dan kurang rapi
* Internal : kode CSS diletakkan dalam bagian <head> di file HTML dalam tag <style></style> 
Kelebihan : style dapat dengan mudah untuk diterapkan di suatu halaman HTML sehingga tidak bercampur-campur dengan HTML lain. 
Kekurangan : melambatnya loading time karena ketika menambahkan kode CSS ke dalam file akan memperbesar ukuran memori dari HTML yang membuat 
* External : kode CSS diletakkan di file khusus .css dan dihubungkan ke file HTML dengan mencantumkan link atau file .css 
Kelebihan :  kode CSS dapat digunakan untuk beberapa halaman HTML 
Kekurangan : ketika ada perubahan, halaman HTML berpotensi tidak dapat dirender dengan benar.

### Jelaskan tag HTML5 yang kamu ketahui.
* <b>: Membuat text menjadi bold
* <br>: Menambahkan break line
* <button>: Membuat button
* <p> : Menambahkan text atau paragraf
* <data>: Me-link konten dengan terjemahan yang bisa dibaca mesin
* <form>: Mendefinisikan form HTML untuk input user
* <html>: Mendefinisikan root dokumen HTML

### Jelaskan tipe-tipe CSS selector yang kamu ketahui
* Selektor Class: Diberikan titik di depannya di nama elemen untuk selektor yang akan diberikan elemen
* Selektor Tag dapat disebut sebagai type selector dan memiliki elemen berdasarkan nama tag.
* Selektor Atribut: Mirip dengan selektor Tag, selektor Atribut memiliki elemen berdasarkan atribut.
* Selektor ID: Mirip dengan selektor Class, tetapi hanya dapat digunakan oleh satu elemen saja (unik) yang ditandai dengan tanda # didepannya.
* Selektor Universal: Selektor yang digunakan untuk menyeleksi elemen pada scope tertentu
* Pseudo Selektor: Selektor untuk menyeleksi elemen-elemen semu seperti state dari suatu elemen, elemen before dan after, dsb. Terdapat 2 macam pseudo selektor, yaitu pseudo class selektor untuk state elemen dan pseudo-element selektor untuk elemen semu di HTML.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Menambahkan styling terhadap semua file html, berupa border, background, font, alignment, dan lainnya.
Pada file todolist.html membuat card untuk menampilkan masing-masing task yang terdapat pada setiap akun.
