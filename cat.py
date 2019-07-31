import argparse


class Cat:
    """
    The Cat class consists some of the basic functionality that
    the Linux cat command can do.
    """
    def __init__(self, files, dest_file='', enum=False, mode='write'):
        """ The init function consists of all the properties needed
        to perform the cat command."""
        self.source_files = files
        self.dest_file = dest_file
        self.mode = mode
        self.enumerate = enum
        self.output = ''

        # The code for reading the source files and checking for errors
        for f in self.source_files:
            try:
                with open(f, 'r') as file:
                    self.output += file.read()
                self.output += '\n'
            except FileNotFoundError:
                print(f'cat: {f}: No such file or directory')
                exit(0)
            except PermissionError:
                print(f'cat: {f}: Permission denied')
                exit(0)

    def print_source(self):
        """Printing the contents of the source file(s)."""
        if self.enumerate:
            for num, item in enumerate(self.output.split('\n')):
                if num != len(self.output.split('\n')) - 1:
                    print('{} {}'.format(num + 1, item))
            return
        print(self.output)

    def write_to_dest(self):
        """Writing the contents of the source file(s)
         to the destination file"""
        if self.enumerate:

            out_list = self.output.split('\n')
            with open(self.dest_file, 'w+') as file:
                file.writelines([f'{a} {b}\n'
                                 for a, b
                                 in enumerate(out_list)])
        else:
            with open(self.dest_file, 'w+') as file:
                file.write(self.output)

    def append_to_dest(self):
        """Appending the contents of the source file(s)
        to the destination file"""
        if self.dest_file:
            if self.enumerate:
                out_list = self.output.split('\n')
                with open(self.dest_file, 'a+') as file:
                    file.writelines([f'{a} {b}\n'
                                     for a, b
                                     in enumerate(out_list)])
            else:
                with open(self.dest_file, 'a+') as file:
                    file.write(self.output)


if __name__ == "__main__":
    # The starting point of the script and
    # the code for the command line arguments
    parser = argparse.ArgumentParser()

    parser.add_argument('source', nargs='*',
                        help="the source file(s)", )
    parser.add_argument('-a', '--action', dest='action',
                        choices=['read', 'write', 'append'], default='read',
                        help='READ from the source file(s) '
                             'or WRITE/APPEND to the destination file')
    parser.add_argument('-n', '--enumerate', dest='enumerate',
                        action='store_true',
                        help='Read the enumerated line version of the file')
    parser.add_argument('-d', '--destination',
                        help='the destination file', default='')

    args = parser.parse_args()

    # Initializing the Cat object together with its properties
    # dest_file : the destination file
    # enum :  the flag for the number option
    # mode : write,read,append
    cat = Cat(args.source,
              dest_file=args.destination,
              enum=args.enumerate,
              mode=args.action
              )

    # This is the condition for reading, writing, or appending
    if args.action == 'write':
        cat.write_to_dest()
    elif args.action == 'append':
        cat.append_to_dest()
    else:
        cat.print_source()
