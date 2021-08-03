### CTF Statement:
```txt
In the computing industry, standards are established to facilitate information interchanges among American coders.
Unfortunately, I've made communication a little bit more difficult.
Can you figure this one out?

41 42 43 54 46 7B 34 35 43 31 31 5F 31 35 5F 55 35 33 46 55 4C 7D
```

---


The given string of text in the ctf discription is clearly hex code, so to decode it, we can use [`xxd`](https://linux.die.net/man/1/xxd):

```zsh
$ echo "41 42 43 54 46 7B 34 35 43 31 31 5F 31 35 5F 55 35 33 46 55 4C 7D" | xxd -p -r
ABCTF{45C11_15_U53FUL}
```

---

#### The Flag:
    ABCTF{45C11_15_U53FUL}


Link to the challenge: [Character Encoding](https://ctflearn.com/challenge/115)
