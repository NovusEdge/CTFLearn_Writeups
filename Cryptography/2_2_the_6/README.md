### CTF Statement:
```txt
There are so many different ways of encoding and decoding information nowadays... One of them will work!

Q1RGe0ZsYWdneVdhZ2d5UmFnZ3l9
```

---

As the ctf title tells us: `2 2 the 6` i.e. "2 to the 6th power" or, in other words, 64, tells us that the string in the ctf discription is [`base64`](https://en.wikipedia.org/wiki/Base64) encrypted.

To decode it, we can use [`base64`](https://linux.die.net/man/1/base64):

```zsh
$ echo "Q1RGe0ZsYWdneVdhZ2d5UmFnZ3l9" | base64 --decode
CTF{FlaggyWaggyRaggy}
```


---

#### The Flag:
    CTF{FlaggyWaggyRaggy}


Link to the challenge: [2 2 the 6](https://ctflearn.com/challenge/192)
