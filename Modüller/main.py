#import mustafamodule
#mustafamodule.example_func()


from mustafamodule import example_func
example_func()


#kütüphaneler için daha çok bilgi almak için pypi kullanabilirim.


#mustafamodule olarak bir tane kendimiz kütüphane oluşturduk. Bu kütüphaneye example_func() olarak bir tane fonksiyon tanımladık.
#Daha sonra import mustafamodule diyerek bu kütüpheneye mainime ekledim. Ama ben kütüpheneyi değil de kütüphanedeki fonksiyonu yüklemek isteseydim
#from mustafamodule import example_func diyerek sadece kütüphenedeki fonksiyonu yükledim.Bu arasındaki ayrım çok önemli



from AnimalPackage import info
info.info()

from AnimalPackage.CatPackage import miav

miav.testFunc()

# import ettim ama kullanmasam bile miav dosyasındaki if else den dolayı import edildiği yazdırılır.
