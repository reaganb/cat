class Cat:

    def __init__(self,*files,dest_file = ''):
        self.source_files = files
        self.dest_file = dest_file
        self.out = ''

        for f in self.source_files:
            try:
                with open(f, 'r') as op:
                    self.out += ''.join(op.readlines())
                self.out += '\n'
            except FileNotFoundError:
                pass

    def print(self,enum=False):
        if enum:
            for a,b in enumerate(self.out.split('\n')):
                if a != len(self.out.split('\n'))-1:
                    print('{} {}'.format(a+1,b))
            return
        print(self.out)

    def writeToDest(self,mode='write',enum=False):
        if self.dest_file:
            if mode == 'add':
                if enum:
                    with open(self.dest_file,'a+') as op:
                        op.writelines(['{} {}\n'.format(a,b) for a,b in enumerate(self.out.split('\n'))])
                    return
                with open(self.dest_file, 'a+') as op:
                    op.write(self.out)
                return
            with open(self.dest_file,'w+') as op:
                op.write(self.out)





cat  = Cat('file1.txt','file2.txt',dest_file='out.txt')     # Initialize cat object

cat.print()                                                 # cat file1.txt file2.txt               # read files(s)

cat.print(enum=True)                                        # cat -n file1.txt file2.txt            # read enumerated file(s)

cat.writeToDest()                                           # cat file1.txt file2.txt > out.txt     # write content of file(s) to another file using '>' redirect

cat.writeToDest(mode='add',enum=True)                       # cat -n file1.txt file2.txt > out.txt  # append enumerated content of file(s) to another file using '>>' redirect


