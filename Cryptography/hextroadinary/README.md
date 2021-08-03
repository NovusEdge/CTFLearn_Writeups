### CTF Statement:
```txt
Meet ROXy, a coder obsessed with being exclusively the worlds best hacker. She
specializes in short cryptic hard to decipher secret codes. The below hex
values for example, she did something with them to generate a secret code, can
you figure out what? Your answer should start with 0x.

0xc4115 0x4cf8
```

---

We're given 2 numbers represented in base 16 i.e `hexadecimal numbers`.

Let's decode them first...

```zsh
$ echo $((0xc4115))
803093

$ echo $((0x4cf8))
19704
```

And there they are, `803093` and `19704`.

Looking carefully at the challenge(the entity: ROXy), it becomes evident that "ROXy" reversed is simply: "yXOR", and the capitalized "XOR" tells us about the encoding of the data . It is encrypted using xor. So we'll try and decode it:

```zsh
$ echo $((19704 ^ 803093))
789997

$ echo $((803093 ^ 19704))
789997
```

A clean and nice example of [`symmetric cryptography`](https://www.ibm.com/docs/en/ztpf/1.1.0.14?topic=concepts-symmetric-cryptography)


Let's convert the data we got back to hex:

```zsh
$ python3 -c "print(hex(789997))"
0xc0ded
```

---

#### The Flag:
    CTFLearn{0xc0ded}


Link to the challenge: [Hextroadinary](https://ctflearn.com/challenge/158)
