from tkinter import *
from pyzbar import pyzbar
import cv2
from datetime import date

font = "Times 22"
cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()

liste = []



grey="#A9A9A9"


pencere = Tk()
pencere.title("Akıllı Triaj")
pencere.geometry("1800x1600")






hasta_sikayet= Label(pencere,text="Hastanın şikayetleri:",font=font)
hasta_sikayet.place(x=0,y=160)

isim= Label(pencere,text="Hastanın ismi: ",font=font)
isim.place(x=0,y=0)

yas= Label(pencere,text="Hastanın yaşı: ",font=font)
yas.place(x=400,y=0)

cinsiyet = Label(pencere,text="Hastanın cinsiyeti: ",font=font)
cinsiyet.place(x=700,y=0)

corona_durumu= Label(pencere,text="Hastanın korona olma ihtimali: ",font=font)
corona_durumu.place(x=0,y=60)

hasta_genel_durum = Label(pencere,text="Hastanın genel durumu:",font=font)
hasta_genel_durum.place(x=1100,y=0)

durum= Label(pencere,height=2,width=24,bg="white")
durum.place(x=1400,y=0)









def haber():
    pencere.iconify()
    global liste
    while True:

        _, img = cap.read()

        data, bbox, _ = detector.detectAndDecode(img)

        if bbox is not None:

            for i in range(len(bbox)):
                cv2.line(img, tuple(bbox[i][0]), tuple(bbox[(i + 1) % len(bbox)][0]), color=(255, 0, 0), thickness=2)
            if data:
                pencere.deiconify()
                veri = data.replace("[", "").replace("]", "").replace('"', "")
                liste = [i.strip() for i in veri.split(",")]

                isim.config(text="Hastanın ismi: " + liste[0])
                yas.config(text="Hastanın yaşı: "+liste[1])
                cinsiyet.config(text="Hastanın cinsiyeti: "+liste[2])



                if liste[3]== "2" or liste[5] == "2":
                    durum.config(bg="red")
                elif liste[4] == "3" or liste[6]== "3":
                    durum.config(bg="yellow")
                else:
                    durum.config(bg="green")
                if liste[7] == "1" or liste[8] == "1" or liste[9] == "1" or liste[10] == "1" or liste[11] == "1" or liste[12] == "1" or liste[13] =="1" :
                    corona_durumu.config(text="Hastanın korona olma ihtimali: Yüksek ")
                else:
                    corona_durumu.config(text="Hastanın korona olma ihtimali: ")





                if liste[3] =="2" :
                    liste[3]="Hasta yakın zamanda alerjisi olduğunu bildiği veya zehirli olan bir hayvan tarafından ısırıldı."
                else:
                   pass


                if liste[4] =="3" :
                    liste[4]="Hasta vücudunda kırık olduğunu hissediyor."
                else:
                    pass


                if liste[5] =="2" :
                    liste[5]="Hasta nefes almakta zorlanıyor."
                else:
                    pass


                if liste[6] =="3" :
                    liste[6]=" Hasta yakın zamanda tansiyonununda ani bir düşüş veya çıkış gördü."
                else:
                     pass


                if liste[7] =="1" :
                    liste[7]="Hastanın ateş veya ateş öyküsü var."
                else:
                     pass


                if liste[8] =="1" :
                    liste[8]="Hastanın öksürüğü var. "
                else:
                     pass


                if liste[9] =="1" :
                    liste[9]=" Hastanın nefes darlığı, boğaz ağrısı, baş ağrısı, kas ağrıları,tat ve koku alma kaybı veya ishali var."
                else:
                    pass


                if liste[10] =="1" :
                    liste[10]=" Hasta son 14 gün içerisinde yurt dışında bulundu."

                else:
                     pass


                if liste[11] =="1" :
                    liste[11]="Son 14 gün içerisinde  hastanın ev halkından birisi yurtdışından geldi."
                else:
                     pass


                if liste[12] =="1" :
                    liste[12]="Son 14 gün içerisinde hastanın yakınlarından herhangi birisi solunum yolu hastalığı nedeni ile hastaneye yattı."
                else:
                     pass

                if liste[13] =="1" :
                    liste[13]="Son 14 gün içerisinde hastanın yakınlarından COVID-19 hastalığı tanısı olan birisi oldu."
                else:
                     pass

                liste[0]="0"
                liste[2] = "0"
                liste[1] = "0"


                belirti = Text(pencere,font="Times 16")
                for x in liste:
                    if x != "0":
                        belirti.insert(END, "•" + x + '\n\n')
                belirti.config(state="disabled")
                belirti.place(x=0, y=200)
                return liste
                break













yeni_hasta= Button(pencere,text="Yeni Hasta",width="25",bg=grey,command=haber)
yeni_hasta.place(rely=1.0, relx=1.0, x=-7, y=-65, anchor=SE)




pencere.mainloop()






