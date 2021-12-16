from pygame import mixer
print("---------------------------------------------------")
print("      !MÜZİK ÇALAR PROJESİNE HOŞ GELDİNİZ!         ")
print("         !PROJE SAHİBİ : VASİF OSMANOV!            ")
print("           !PROJE FİKRİ : W1SE!                    ")
print("---------------------------------------------------")
durum = print("1.EFKAR\n"
      "2.NORMAL\n"
      "3.RAHATLATICI\n")
secim =  int(input("Türü seçin (örn:1) :"))
if secim == 1:
            print("1.Müslüm Baba\n"
                  "2.Ferdi Tayfur\n"
                  "3.Ahmet Kaya\n")
            sarkicisecim = int(input("Şarkıcıyı seçin (örn:1) :"))
            if sarkicisecim==1:
                  print("1.Affet\n"
                        "2.Unutmadım\n"
                        "3.Sigara\n")
            sarkisecim = int(input("Şarkıyı seçin (örn:1) :"))
            if sarkisecim == 1:
                  print("Şarkı Başlıyor")
                  muzik = "C:\muzik\mbaffet.mp3"
                  mixer.init()
                  mixer.music.load(muzik)
                  mixer.music.set_volume(0.7)
                  mixer.music.play()

                  while True:
                        print("P tuşuna basarak durdurun,\n"
                              " R tuşu ile devam ettirebilirsiniz\n")
                        print("E tuşu ile programı sonlandırabilirsiniz")
                        query = input(" ")
                        if query == 'p':
                              mixer.music.pause()
                        elif query == 'r':
                              mixer.music.unpause()
                        elif query == 'e':
                              mixer.music.stop()
                              break
            elif sarkisecim == 2:
                  print("Şarkı Başlıyor")
                  muzik = "C:\muzik\mbunutmadim.mp3"
                  mixer.init()
                  mixer.music.load(muzik)
                  mixer.music.set_volume(0.7)
                  mixer.music.play()

                  while True:
                        print("P tuşuna basarak durdurun\n R tuşu ile devam ettirebilirsiniz\n")
                        print("E tuşu ile programı sonlandırabilirsiniz")
                        query = input(" ")
                        if query == 'p':
                              mixer.music.pause()
                        elif query == 'r':
                              mixer.music.unpause()
                        elif query == 'e':
                              mixer.music.stop()
                              break
            elif sarkisecim == 3:
                  print("Şarkı Başlıyor")
                  muzik = "C:\muzik\mbsigara.mp3"
                  mixer.init()
                  mixer.music.load(muzik)
                  mixer.music.set_volume(0.7)
                  mixer.music.play()

                  while True:
                        print("P tuşuna basarak durdurun\n R tuşu ile devam ettirebilirsiniz\n")
                        print("E tuşu ile programı sonlandırabilirsiniz")
                        query = input(" ")
                        if query == 'p':
                              mixer.music.pause()
                        elif query == 'r':
                              mixer.music.unpause()
                        elif query == 'e':
                              mixer.music.stop()
                              break

            if sarkicisecim == 2:
                  print("1.Bana Sor\n"
                  "2.Geçen Yıl\n"
                  "3.İçim Yanar\n")
            sarkisecim1 = int(input("Şarkıyı seçin (örn:1):"))
            if sarkisecim1 == 1:
                  print("Şarkı Başlıyor")
                  muzik = "C:\muzik\mbanasor.mp3"
                  mixer.init()
                  mixer.music.load(muzik)
                  mixer.music.set_volume(0.7)
                  mixer.music.play()

                  while True:
                        print("P tuşuna basarak durdurun\n R tuşu ile devam ettirebilirsiniz\n")
                        print("E tuşu ile programı sonlandırabilirsiniz")
                        query = input(" ")
                        if query == 'p':
                              mixer.music.pause()
                        elif query == 'r':
                              mixer.music.unpause()
                        elif query == 'e':
                              mixer.music.stop()
                              break
            if sarkisecim1 == 2:
                  print("Şarkı Başlıyor")
                  muzik = "C:\muzik\gecenyil.mp3"
                  mixer.init()
                  mixer.music.load(muzik)
                  mixer.music.set_volume(0.7)
                  mixer.music.play()

                  while True:
                        print("P tuşuna basarak durdurun\n R tuşu ile devam ettirebilirsiniz\n")
                        print("E tuşu ile programı sonlandırabilirsiniz")
                        query = input(" ")
                        if query == 'p':
                              mixer.music.pause()
                        elif query == 'r':
                              mixer.music.unpause()
                        elif query == 'e':
                              mixer.music.stop()
                              break
            if sarkisecim1 == 3:
                  print("Şarkı Başlıyor")
                  muzik = "C:\muzik\icimyanar.mp3"
                  mixer.init()
                  mixer.music.load(muzik)
                  mixer.music.set_volume(0.7)
                  mixer.music.play()

                  while True:
                        print("P tuşuna basarak durdurun\n R tuşu ile devam ettirebilirsiniz\n")
                        print("E tuşu ile programı sonlandırabilirsiniz")
                        query = input(" ")
                        if query == 'p':
                              mixer.music.pause()
                        elif query == 'r':
                              mixer.music.unpause()
                        elif query == 'e':
                              mixer.music.stop()
                              break
            if sarkicisecim == 3:
                  print("1.Penceresiz Kaldım Anne\n"
                        "2.Söyle\n"
                        "3.Nereden Bileceksiniz")
                  sarkisecim2 = int(input("Şarkıyı seçin (örn:1):"))
                  if sarkisecim1 == 1:
                        print("Şarkı Başlıyor")
                  muzik = "C:\muzik\penceresizkaldim.mp3"
                  mixer.init()
                  mixer.music.load(muzik)
                  mixer.music.set_volume(0.7)
                  mixer.music.play()

                  while True:
                        print("P tuşuna basarak durdurun\n R tuşu ile devam ettirebilirsiniz\n")
                        print("E tuşu ile programı sonlandırabilirsiniz")
                        query = input(" ")
                        if query == 'p':
                              mixer.music.pause()
                        elif query == 'r':
                              mixer.music.unpause()
                        elif query == 'e':
                              mixer.music.stop()
                              break
            if sarkisecim2 == 2:
                  print("Şarkı Başlıyor")
                  muzik = "C:\muzik\soyle.mp3"
                  mixer.init()
                  mixer.music.load(muzik)
                  mixer.music.set_volume(0.7)
                  mixer.music.play()

                  while True:
                        print("P tuşuna basarak durdurun\n R tuşu ile devam ettirebilirsiniz\n")
                        print("E tuşu ile programı sonlandırabilirsiniz")
                        query = input(" ")
                        if query == 'p':
                              mixer.music.pause()
                        elif query == 'r':
                              mixer.music.unpause()
                        elif query == 'e':
                              mixer.music.stop()
                              break
            if sarkisecim2 == 3:
                  print("Şarkı Başlıyor")
                  muzik = "C:\muzik\gnerdenbileceksiniz.mp3"
                  mixer.init()
                  mixer.music.load(muzik)
                  mixer.music.set_volume(0.7)
                  mixer.music.play()

                  while True:
                        print("P tuşuna basarak durdurun\n R tuşu ile devam ettirebilirsiniz\n")
                        print("E tuşu ile programı sonlandırabilirsiniz")
                        query = input(" ")
                        if query == 'p':
                              mixer.music.pause()
                        elif query == 'r':
                              mixer.music.unpause()
                        elif query == 'e':
                              mixer.music.stop()
                              break
elif secim == 2:
      print("1.Ceza\n"
            "2.Ben Fero\n"
            "3.Gazapizm\n")
      sarkicisecim1 = int(input("Şarkıcıyı seçin (örn:1) :"))
      if sarkicisecim1 == 1:
            print("1.Suspus\n"
                  "2.Yerli Plaka\n"
                  "3.Neyim var ki\n")
            sarkisecim3 = int(input("Şarkıyı seçin (örn:1) :"))
            if sarkisecim3 == 1:
                  print("Şarkı Başlıyor")
                  muzik = "C:\muzik\Ceza Suspus.mp3"
                  mixer.init()
                  mixer.music.load(muzik)
                  mixer.music.set_volume(0.7)
                  mixer.music.play()

                  while True:
                        print("P tuşuna basarak durdurun\n R tuşu ile devam ettirebilirsiniz\n")
                        print("E tuşu ile programı sonlandırabilirsiniz")
                        query = input(" ")
                        if query == 'p':
                              mixer.music.pause()
                        elif query == 'r':
                              mixer.music.unpause()
                        elif query == 'e':
                              mixer.music.stop()
                        break
            if sarkisecim3 == 2:
                  print("Şarkı Başlıyor")
                  muzik = "C:\muzik\Ceza Yerli Plaka Videoklip (1080p  HD).mp3"
                  mmixer.init()
                  mixer.music.load(muzik)
                  mixer.music.set_volume(0.7)
                  mixer.music.play()

                  while True:
                        print("P tuşuna basarak durdurun\n R tuşu ile devam ettirebilirsiniz\n")
                        print("E tuşu ile programı sonlandırabilirsiniz")
                        query = input(" ")
                        if query == 'p':
                              mixer.music.pause()
                        elif query == 'r':
                              mixer.music.unpause()
                        elif query == 'e':
                              mixer.music.stop()
                        break
            if sarkisecim3 == 3:
                  print("Şarkı Başlıyor")
                  muzik = "C:\muzik\CEZA - Neyim Var ki feat. Sagopa K (Official Audio).mp3"
                  mixer.init()
                  mixer.music.load(muzik)
                  mixer.music.set_volume(0.7)
                  mixer.music.play()

                  while True:
                        print("P tuşuna basarak durdurun\n R tuşu ile devam ettirebilirsiniz\n")
                        print("E tuşu ile programı sonlandırabilirsiniz")
                        query = input(" ")
                        if query == 'p':
                              mixer.music.pause()
                        elif query == 'r':
                              mixer.music.unpause()
                        elif query == 'e':
                              mixer.music.stop()
                        break

      if sarkicisecim1 == 2:
            print("1.Demet Akalın\n"
            "2.3 2 1\n"
            "3.Biladerim için\n")
            sarkisecim4 = int(input("Şarkıyı seçin (örn:1):"))
            if sarkisecim4 == 1:
                  print("Şarkı Başlıyor")
                  muzik = "C:\muzik\Ben Fero - Demet Akalın [Official Video].mp3"
                  mixer.init()
                  mixer.music.load(muzik)
                  mixer.music.set_volume(0.7)
                  mixer.music.play()

                  while True:
                        print("P tuşuna basarak durdurun\n R tuşu ile devam ettirebilirsiniz\n")
                        print("E tuşu ile programı sonlandırabilirsiniz")
                        query = input(" ")
                        if query == 'p':
                              mixer.music.pause()
                        elif query == 'r':
                              mixer.music.unpause()
                        elif query == 'e':
                              mixer.music.stop()
                        break
            if sarkisecim4 == 2:
                  print("Şarkı Başlıyor")
                  muzik = "C:\muzik\Ben Fero - 3 2 1 [Official Video].mp3"
                  mixer.init()
                  mixer.music.load(muzik)
                  mixer.music.set_volume(0.7)
                  mixer.music.play()

                  while True:
                        print("P tuşuna basarak durdurun\n R tuşu ile devam ettirebilirsiniz\n")
                        print("E tuşu ile programı sonlandırabilirsiniz")
                        query = input(" ")
                        if query == 'p':
                              mixer.music.pause()
                        elif query == 'r':
                              mixer.music.unpause()
                        elif query == 'e':
                              mixer.music.stop()
                        break
            if sarkisecim4 == 3:
                  print("Şarkı Başlıyor")
                  muzik = "C:\muzik\Ben Fero - Biladerim İçin [Official Audio]"
                  mixer.init()
                  mixer.music.load(muzik)
                  mixer.music.set_volume(0.7)
                  mixer.music.play()

                  while True:
                        print("P tuşuna basarak durdurun\n R tuşu ile devam ettirebilirsiniz\n")
                        print("E tuşu ile programı sonlandırabilirsiniz")
                        query = input(" ")
                        if query == 'p':
                              mixer.music.pause()
                        elif query == 'r':
                              mixer.music.unpause()
                        elif query == 'e':
                              mixer.music.stop()
                              break
      if sarkicisecim1 == 3:
            print("1.Unutulacak Dünler\n"
            "2.Kalbin Çukurda\n"
            "3.Memleketsiz")
            sarkisecim5 = int(input("Şarkıyı seçin (örn:1):"))
            if sarkisecim5 == 1:
                  print("Şarkı Başlıyor")
                  muzik = "C:\muzik\Gazapizm - Unutulacak Dünler.mp3"
                  mixer.init()
                  mixer.music.load(muzik)
                  mixer.music.set_volume(0.7)
                  mixer.music.play()

                  while True:
                        print("P tuşuna basarak durdurun\n R tuşu ile devam ettirebilirsiniz\n")
                        print("E tuşu ile programı sonlandırabilirsiniz")
                        query = input(" ")
                        if query == 'p':
                              mixer.music.pause()
                        elif query == 'r':
                              mixer.music.unpause()
                        elif query == 'e':
                              mixer.music.stop()
                        break
      if sarkisecim5 == 2:
            print("Şarkı Başlıyor")
            muzik = "C:\muzik\Gazapizm - Kalbin Çukurda ft. Cem Adrian.mp3"
            mixer.init()
            mixer.music.load(muzik)
            mixer.music.set_volume(0.7)
            mixer.music.play()

            while True:
                  print("P tuşuna basarak durdurun\n R tuşu ile devam ettirebilirsiniz\n")
                  print("E tuşu ile programı sonlandırabilirsiniz")
                  query = input(" ")
                  if query == 'p':
                        mixer.music.pause()
                  elif query == 'r':
                        mixer.music.unpause()
                  elif query == 'e':
                        mixer.music.stop()
                  break
      if sarkisecim5 == 3:
            print("Şarkı Başlıyor")
            muzik = "C:\muzik\Gazapizm - Memleketsiz (Official Video) GazapizmMemleketsiz.mp3"
            mixer.init()
            mixer.music.load(muzik)
            mixer.music.set_volume(0.7)
            mixer.music.play()

            while True:
                  print("P tuşuna basarak durdurun\n R tuşu ile devam ettirebilirsiniz\n")
                  print("E tuşu ile programı sonlandırabilirsiniz")
                  query = input(" ")
                  if query == 'p':
                        mixer.music.pause()
                  elif query == 'r':
                        mixer.music.unpause()
                  elif query == 'e':
                        mixer.music.stop()
                  break
elif secim == 3:
      print("1.Idir\n"
            "2.Bob Marley\n"
            "3.Farid Farjad\n")
      sarkicisecim2 = int(input("Şarkıcıyı seçin (örn:1) :"))
      if sarkicisecim2 == 1:
            print("1.Anda Yella\n"
                  "2.Cfiy\n"
                  "3.A vava inouva\n")
            idirsecim = int(input("Şarkıyı seçin (örn:1) :"))
            if idirsecim == 1:
                  print("Şarkı Başlıyor")
                  muzik = "C:\muzik\IDIR   ANDA YELLA.mp3"
                  mixer.init()
                  mixer.music.load(muzik)
                  mixer.music.set_volume(0.7)
                  mixer.music.play()

                  while True:
                        print("P tuşuna basarak durdurun\n R tuşu ile devam ettirebilirsiniz\n")
                        print("E tuşu ile programı sonlandırabilirsiniz")
                        query = input(" ")
                        if query == 'p':
                              mixer.music.pause()
                        elif query == 'r':
                              mixer.music.unpause()
                        elif query == 'e':
                              mixer.music.stop()
                        break
            if idirsecim == 2:
                  print("Şarkı Başlıyor")
                  muzik = "C:\muzik\Cfiy - IDIR.mp3"
                  mixer.init()
                  mixer.music.load(muzik)
                  mixer.music.set_volume(0.7)
                  mixer.music.play()

                  while True:
                        print("P tuşuna basarak durdurun\n R tuşu ile devam ettirebilirsiniz\n")
                        print("E tuşu ile programı sonlandırabilirsiniz")
                        query = input(" ")
                        if query == 'p':
                              mixer.music.pause()
                        elif query == 'r':
                              mixer.music.unpause()
                        elif query == 'e':
                              mixer.music.stop()
                        break
            if idirsecim == 3:
                  print("Şarkı Başlıyor")
                  muzik = "C:\muzik\Idir - A Vava Inouva.mp3"
                  mixer.init()
                  mixer.music.load(muzik)
                  mixer.music.set_volume(0.7)
                  mixer.music.play()

                  while True:
                        print("P tuşuna basarak durdurun\n R tuşu ile devam ettirebilirsiniz\n")
                        print("E tuşu ile programı sonlandırabilirsiniz")
                        query = input(" ")
                        if query == 'p':
                              mixer.music.pause()
                        elif query == 'r':
                              mixer.music.unpause()
                        elif query == 'e':
                              mixer.music.stop()
                        break

      if sarkicisecim2 == 2:
            print("1.Is This Love\n"
                  "2.One love\n"
                  "3.A lalala long\n")
            bmsecim = int(input("Şarkıyı seçin (örn:1):"))
            if bmsecim == 1:
                  print("Şarkı Başlıyor")
                  muzik = "C:\muzik\Bob Marley - Is this Love.mp3"
                  mixer.init()
                  mixer.music.load(muzik)
                  mixer.music.set_volume(0.7)
                  mixer.music.play()

                  while True:
                        print("P tuşuna basarak durdurun\n R tuşu ile devam ettirebilirsiniz\n")
                        print("E tuşu ile programı sonlandırabilirsiniz")
                        query = input(" ")
                        if query == 'p':
                              mixer.music.pause()
                        elif query == 'r':
                              mixer.music.unpause()
                        elif query == 'e':
                              mixer.music.stop()
                        break
            if bmsecim == 2:
                  print("Şarkı Başlıyor")
                  muzik = "C:\muzik\Bob Marley - One Love.mp3"
                  mixer.init()
                  mixer.music.load(muzik)
                  mixer.music.set_volume(0.7)
                  mixer.music.play()

                  while True:
                        print("P tuşuna basarak durdurun\n R tuşu ile devam ettirebilirsiniz\n")
                        print("E tuşu ile programı sonlandırabilirsiniz")
                        query = input(" ")
                        if query == 'p':
                              mixer.music.pause()
                        elif query == 'r':
                              mixer.music.unpause()
                        elif query == 'e':
                              mixer.music.stop()
                        break
            if bmsecim == 3:
                  print("Şarkı Başlıyor")
                  muzik = "C:\muzik\Bob Marley - A lalala long.mp3"
                  mixer.init()
                  mixer.music.load(muzik)
                  mixer.music.set_volume(0.7)
                  mixer.music.play()

                  while True:
                        print("P tuşuna basarak durdurun\n R tuşu ile devam ettirebilirsiniz\n")
                        print("E tuşu ile programı sonlandırabilirsiniz")
                        query = input(" ")
                        if query == 'p':
                              mixer.music.pause()
                        elif query == 'r':
                              mixer.music.unpause()
                        elif query == 'e':
                              mixer.music.stop()
                              break
      if sarkicisecim2 == 3:
            print("1.Keman Ağlıyor\n"
                  "2.Robabeh Jan\n"
                  "3.Kelebekler De Ağlar")
            ffsecim = int(input("Şarkıyı seçin (örn:1):"))
            if ffsecim == 1:
                  print("Şarkı Başlıyor")
                  muzik = "C:\muzik\Keman ağlıyor.mp3"
                  mixer.init()
                  mixer.music.load(muzik)
                  mixer.music.set_volume(0.7)
                  mixer.music.play()

                  while True:
                        print("P tuşuna basarak durdurun\n R tuşu ile devam ettirebilirsiniz\n")
                        print("E tuşu ile programı sonlandırabilirsiniz")
                        query = input(" ")
                        if query == 'p':
                              mixer.music.pause()
                        elif query == 'r':
                              mixer.music.unpause()
                        elif query == 'e':
                              mixer.music.stop()
                        break
            if ffsecim == 2:
                  print("Şarkı Başlıyor")
                  muzik = "C:\muzik\Farid Farjad Robabeh Jan.mp3"
                  mixer.init()
                  mixer.music.load(muzik)
                  mixer.music.set_volume(0.7)
                  mixer.music.play()

                  while True:
                        print("P tuşuna basarak durdurun\n R tuşu ile devam ettirebilirsiniz\n")
                        print("E tuşu ile programı sonlandırabilirsiniz")
                        query = input(" ")
                        if query == 'p':
                              mixer.music.pause()
                        elif query == 'r':
                              mixer.music.unpause()
                        elif query == 'e':
                              mixer.music.stop()
                        break
            if ffsecim == 3:
                  print("Şarkı Başlıyor")
                  muzik = "C:\muzik\Farid Farjad - Kelebekler De Ağlar.mp3"
                  mixer.init()
                  mixer.music.load(muzik)
                  mixer.music.set_volume(0.7)
                  mixer.music.play()

                  while True:
                        print("P tuşuna basarak durdurun\n R tuşu ile devam ettirebilirsiniz\n")
                        print("E tuşu ile programı sonlandırabilirsiniz")
                        query = input(" ")
                        if query == 'p':
                              mixer.music.pause()
                        elif query == 'r':
                              mixer.music.unpause()
                        elif query == 'e':
                              mixer.music.stop()
                        break
else:
      print("Sen öl kanka <3")