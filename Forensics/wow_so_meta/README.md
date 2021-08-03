### CTF Statement:
```txt
This photo was taken by our target. See what you can find out about him from it.

https://mega.nz/#!ifA2QAwQ!WF-S-MtWHugj8lx1QanGG7V91R-S1ng7dDRSV25iFbk
```

_[File Link](https://mega.nz/#!ifA2QAwQ!WF-S-MtWHugj8lx1QanGG7V91R-S1ng7dDRSV25iFbk)_

---

We've been given an image: `3UWLBAUCb9Z2.jpg`.
Let's first check the file's details:

```zsh
$ file 3UWLBAUCb9Z2.jpg
3UWLBAUCb9Z2.jpg: JPEG image data, JFIF standard 1.01, resolution (DPI), density 72x72, segment length 16, Exif Standard: [TIFF image data, big-endian, direntries=8, orientation=
upper-left, xresolution=2170, yresolution=2178, resolutionunit=2, software=Photos 1.5, datetime=2014:12:27 16:45:55], baseline, precision 8, 800x307, components 3
```

Now, since there's not much to go by, we can try and view the image in different formats like: text, hex, etc.

When trying to view it as text and searching for keywords like "flag", we get:

```zsh
$ cat 3UWLBAUCb9Z2.jpg > image_text.txt
$ grep "flag" image_text.txt --text
                <rdf:Description xmlns:MicrosoftPhoto="http://ns.microsoft.com/photo/1.0/"><MicrosoftPhoto:CameraSerialNumber>flag{EEe_x_I_FFf}</MicrosoftPhoto:CameraSerialNumber
></rdf:Description></rdf:RDF>
```
---

And there it is! :D

#### The Flag:
    CTFLearn{EEe_x_I_FFf}


Link to the challenge: [Wow... So Meta](https://ctflearn.com/challenge/348)
