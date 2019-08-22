import vlc
import pafy

url = "https://www.youtube.com/watch?v=1yNfzVABvCM"
video = pafy.new(url)
best = video.getbest()
media = vlc.MediaPlayer(best.url)
media.play()

# medi = vlc.MediaPlayer(" D:/박준욱/## 00.BIT_PROJECT/albamonSample.mp4")
# medi.play()