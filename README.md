Tugas Analisis

pertanyaan

1. Apa yang terjadi jika kamu mengubah hero1.hp menjadi 500 setelah baris 
hero1 = Hero...? Coba lakukan print(hero1.hp).

2. Perhatikan parameter lawan pada method serang. Parameter tersebut 
menerima sebuah objek utuh, bukan hanya string nama. Mengapa ini 
penting?

3a. Error apa yang muncul saat kamu mencoba melihat info Eudora 
(eudora.info())? Mengapa error tersebut mengatakan Mage object has no 
attribute 'name', padahal kita sudah mengirim nama "Eudora" saat 
pembuatan objek? 

3b. Jelaskan peran fungsi super() dalam menghubungkan data dari class Anak ke 
class Induk! 

4a. Percobaan Hacking: Coba tambahkan baris kode berikut di bagian paling 
bawah (luar class):  
print(f"Mencoba akses paksa: {hero1._Hero__hp}")
Pertanyaan: Apakah nilai HP muncul atau Error? Jika muncul, diskusikan dengan 
temanmy mengapa Python masih mengizinkan akses ini (konsep Name Mangling) 
dan mengapa kita tetap tidak boleh melakukannya dalam standar pemrograman 
yang baik.

4b. Uji Validasi: Hapus logika if dan elif di dalam method set_hp, sehingga isinya 
hanya self.__hp = nilai_baru.  
Pertanyaan: Kemudian lakukan hero1.set_hp(-100).  
Apa yang terjadi pada data HP Hero? Jelaskan mengapa keberadaan method 
Setter sangat penting untuk menjaga integritas data dalam game! 

5a. Melanggar Kontrak: Pada class Hero, hapus (atau jadikan komentar #) seluruh 
blok method def serang(self, target):. Jalankan programnya. 
Pertanyaan: Error apa yang muncul? Jelaskan dengan bahasamu sendiri, apa arti 
pesan error Can't instantiate abstract class Hero with abstract 
method...?  
Apa konsekuensinya jika kita lupa membuat method yang sudah dijanjikan di 
Interface? 

5b. Mencetak Cetakan: Coba aktifkan baris kode unit = GameUnit(). 
Pertanyaan: Mengapa class GameUnit dilarang untuk dibuat menjadi objek?  
Apa gunanya ada class GameUnit jika tidak bisa dibuat menjadi objek nyata?

6a. Uji Skalabilitas (Kemudahan Menambah Fitur): Tanpa mengubah satu huruf 
pun pada kode Looping (for pahlawan in pasukan:), buatlah satu class 
baru bernama Healer(Hero). 
Isi method serang milik Healer dengan: print(f"{self.name} tidak 
menyerang, tapi menyembuhkan teman!"). 
Masukkan objek Healer ke dalam list pasukan.  
o Pertanyaan: Apakah program berjalan lancar?  
o Kesimpulannya, apa keuntungan Polimorfisme bagi seorang programmer 
ketika harus mengupdate game dengan karakter baru di masa depan? 

6b. Konsistensi Penamaan: Ubah nama method serang pada class Archer 
menjadi tembak_panah. Jalankan program.  
Pertanyaan: Apa yang terjadi?  
Mengapa dalam konsep Polimorfisme, nama method antara Parent Class dan 
berbagai Child Class harus persis sama?


JAWABAN:
1. yang terjadi adalah hp hero1 berubah karena itu adalah atribut yang bersifat publik. nilainya masih bisa diganti
2. Karena objek memiliki atribut dan method. Dengan menerima objek lawan, method serang dapat mengakses atribut seperti lawan.hp dan memanggil method lawan.diserang(). Jika hanya menggunakan string nama, maka tidak bisa dilakukan interaksi antar objek, sehingga logika pertarungan tidak dapat berjalan
3.  - error tersebut terjadi karena constructor punyanya class induk(hero) tidak dijalankan.Akibatnya atribut seperti name,hp,dan attack_power tidak dibuat pada objek Mage.
    - Fungsi super() digunakan untuk memanggil constructor class induk agar data dan atribut dari parent dapat diwariskan dan digunakan oleh class anak.
4. - bisa,karena python menggunakan name mangling.yaitu mengubah nama __hp menjadi _Hero__hp.meskipun bisa diakses. ini tidak dianjurkan karena melanggar prinsip enkapulasi.
   - Nilai HP menjadi negatif. ini membuktikan peran method setter yang sangat penting untuk menjaaga integritas data.agar tidak ada manupulasi hp secara sembarangan

5. - error tersebut berarti class Hero belum memenuhi kontrak dari abstract class GameUnit. karena method "serang()" dijanjikan di interface tetapi tidak dibuat, maka Python melarang pembuatan objek Hero. Konsekuensinya, program tidak dapat dijalankan.
   - karena GameUnit hanyalah  kerangka.class ini berfungsi sebgai standar agar semua turunannya memiliki method tertentu. berguna untuk memastikan konsistensi dan struktur program.

6. - Ya, program berjalan dengan lancar. Hal ini membuktikan konsep Polymorphism, di mana satu method dengan nama yang sama (serang) dapat memiliki perilaku berbeda pada setiap class.
   - Program mengalami error karena loop memanggil method serang(), sementara class tersebut tidak lagi memilikinya. Dalam polymorphism, nama method harus sama agar objek yang berbeda dapat dipanggil dengan cara yang seragam.
    
