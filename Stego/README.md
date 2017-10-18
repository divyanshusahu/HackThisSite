# Stego Missions

### Mission 1

Challenge link [here](https://www.hackthissite.org/missions/playit/stego/1)

![Mission 1](1.bmp)
This is an encoded message, the only tip you get is '2 null bytes'

The mission hint suggests that we have to look at two null bytes(00 00).
On opening the file with hex-editor, we saw the series of **16** and **17** between null-bytes.
![Solved Image](1solved.png) 
It reminds me of binary and I consider 16 as 0 and 17 as 1. But the string length is 55 which is not the multiple of 8. As we know that every 8-bit binary digits represent one ASCII character. Therefore one binary bit is missing. After some hit and trials, I found that the missing bit is the trailing 0 of the first character. Now after decoding the binary we get the password.

| binary | char |
|--------|------|
|00111000|8|
|00110011|3|
|00110111|7|
|01101000|h|
|01100001|a|
|01110011|s|
|00110110|6|

Password = **837has6**

----

### Mission 2

Challenge link [here](https://www.hackthissite.org/missions/playit/stego/2)

This time we are given with audio file. On opening the audio file with Sonic Visualiser and adding spectrogram layer, we read the password.
![Mission 2](2solved.png) 
Password = **jb298abc9qb2** 