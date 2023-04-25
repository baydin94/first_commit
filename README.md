# first_commit
Sql olarak database paylaşılmıştır. Mysql'e çevirmek için:

-Kullanıcılar, indirdikleri SQL dosyasını kendi MySQL sunucularında geri yükleyerek veritabanını kullanabilirler. Bunun için aşağıdaki komutu kullanmalıdırlar:

cmd:
mysql -u kullanici_adi -p schooldb < schooldb.sql


-Bu komut, 'schooldb.sql' dosyasındaki verileri 'schooldb' adlı veritabanına geri yükler. Kullanıcılar, bu komutu çalıştırdıktan sonra veritabanını kullanabilirler.


Eğer aşağıdaki bir hatayla karşılaşılırsa
	'mysqldump' is not recognized as an internal or external command,
	operable program or batch file.

MySQL'in yüklü olduğu klasörün sistem PATH değişkenine eklenmemiş olmasından kaynaklanır. Sorunu çözmek için aşağıdaki adımları izleyin:

MySQL'in yüklü olduğu klasörü bulun:
MySQL'in yüklü olduğu klasörü, genellikle C:\Program Files\MySQL\MySQL Server x.x\bin veya C:\xampp\mysql\bin gibi bir yerde bulunur (x.x, MySQL'in sürüm numarasıdır).

Sistem PATH değişkenine MySQL'in yüklü olduğu klasörü ekleyin:

Windows:

a. Denetim Masası'nı açın ve 'Sistem' öğesini seçin.

b. 'Gelişmiş sistem ayarları'na tıklayın.

c. 'Gelişmiş' sekmesinde 'Ortam Değişkenleri' düğmesine tıklayın.

d. 'Sistem değişkenleri' altında 'Path' değişkenini bulun ve 'Düzenle' düğmesine tıklayın.

e. 'Yeni' düğmesine tıklayın ve MySQL'in yüklü olduğu klasörün yolunu (örneğin, C:\Program Files\MySQL\MySQL Server x.x\bin) ekleyin.

f. 'Tamam' düğmesine tıklayarak tüm açık pencereleri kapatın ve değişiklikleri kaydedin.
