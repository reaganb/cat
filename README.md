# Machine Problem: cat

## The Linux/Unix cat command

The cat command is short for “concatenate,” and it’s most commonly used to display the contents of a ﬁle to the screen. You use it like this:

```
$ cat somefile.txt
```

This command will display out the contents of somefile.txt. That’s not actually its original purpose. Originally it was for combining more than one ﬁle—thus it was called cat. To do that simply add each ﬁle to cat:

```
$ cat A.txt B.txt C.txt
```

The cat command will then go through each ﬁle, write its contents out, and then exit when it has gone through all of them. The problem is, how does this possibly concatenate ﬁles? To do that you’ll also need to use the ﬁle redirection feature via the greater than sign ">":

```
$ cat A.txt B.txt C.txt > D.txt
```
## The cat.py python script

The python script code shows the basic functionalites that you can also do with the **cat** command in Linux. It can read file(s) and write/append into another file using the output of the cat command.

### Prerequisite
1. Windows/Linux OS
2. Python 3

### Usage
The script will work as long as there is Python 3 installed on the system.
Check if it is installed by executing the following command on the terminal.
```
$ python --version
```

### Modes

**READ** - This is the default mode. the basic usage of the cat command by displaying the content of the file(s).

**WRITE** - The script expects a source file and a destination file in this mode. It will write the contents of the source file to the destination file.

**APPEND** - Same functionality with the write mode but it will only add contents to the destination file.

#### Run a basic example:
```
$ python cat.py file1.txt
# "cat file1.txt" in Linux cat
```
output:
```
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```
Note: The first argument does not just expect a single file, inputting multiple files are also possible.
```
$ python cat.py file1.txt file2.txt 
# "cat file1.txt file2.txt" in Linux cat 
```
output:
```
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
of those!Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more
```

#### Writing to a file using the output of the source file(s):
```
$ python cat.py file1.txt -a write -d out.txt
# "cat file1.txt > out.txt" in Linux cat 
```
#### Appending to a file using the output of the source file(s):
```
$ python cat.py file2.txt -a append -d out.txt
# "cat file2.txt >> out.txt" in Linux cat
```
The **-a** option is the mode for redirecting outputs. It expects the words **write**,**read**, or **append** as an argument.

The **-d** option expects the destination file to be written/appended to.
#### Enabling the number (-n) flag for enumerated display:
```
$ python cat.py -n out.txt
# "cat -n out.txt" in Linux cat
```
output:
```
1 The Zen of Python, by Tim Peters
2
3 Beautiful is better than ugly.
4 Explicit is better than implicit.
5 Simple is better than complex.
6 Complex is better than complicated.
7 Flat is better than nested.
8 Sparse is better than dense.
9 Readability counts.
10 Special cases aren't special enough to break the rules.
11 Although practicality beats purity.
12 Errors should never pass silently.
13 Unless explicitly silenced.
14 In the face of ambiguity, refuse the temptation to guess.
15 There should be one-- and preferably only one --obvious way to do it.
16 Although that way may not be obvious at first unless you're Dutch.
17 Now is better than never.
18 Although never is often better than *right* now.
19 If the implementation is hard to explain, it's a bad idea.
20 If the implementation is easy to explain, it may be a good idea.
21 Namespaces are one honking great idea -- let's do more of those!
22 of those!Errors should never pass silently.
23 Unless explicitly silenced.
24 In the face of ambiguity, refuse the temptation to guess.
25 There should be one-- and preferably only one --obvious way to do it.
26 Although that way may not be obvious at first unless you're Dutch.
27 Now is better than never.
28 Although never is often better than *right* now.
29 If the implementation is hard to explain, it's a bad idea.
30 If the implementation is easy to explain, it may be a good idea.
31 Namespaces are one honking great idea -- let's do more
```
Note: This flag can also be used in write or append mode.

#### Getting Help
To know more about the script, execute the following command
```
$ python cat.py -h
```

#### Remarks
The example provided is from the PEP 20 - The Zen of Python by Tim Peters.






















