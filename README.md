# Machine Problem: cat

## The Linux/Unix cat command

The cat command is short for “concatenate,” and it’s most commonly used to display the contents of a ﬁle to the screen. You use it like this:

```
  cat somefile.txt
```

This command will display out the contents of somefile.txt. That’s not actually its original purpose. Originally it was for combining more than one ﬁle—thus it was called cat. To do that simply add each ﬁle to cat:

```
  cat A.txt B.txt C.txt
```

The cat command will then go through each ﬁle, write its contents out, and then exit when it has gone through all of them. The problem is, how does this possibly concatenate ﬁles? To do that you’ll also need to use the ﬁle redirection feature via the greater than sign ">":

```
  cat A.txt B.txt C.txt > D.txt
```
## The cat Python program

The code inside the python program shows the basic functionalites that you can also do with the **cat** command. It can read file(s) and write/append into another file using the output of the cat command.








