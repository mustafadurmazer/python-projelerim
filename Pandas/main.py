import pytube



url = input("enter video url: ")

#parantezin içine path yazarsam dosyayı mainin kaydedildiği klasöre indirir.
path = ""

pytube.YouTube(url).streams.get_highest_resolution().download(path)

