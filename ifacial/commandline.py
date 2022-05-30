
import getopt
import sys


class CommandLine:
    ''' CommandLine util.
        Parse command line params.
    '''

    def __init__(self):
        opts, args = getopt.getopt(sys.argv[1:], 'c:')
        opts = dict(opts)
        self.exit = True

        if '-h' in opts:
            self.printHelp()
            return

        if '-c' in opts:
            self.udp_address = opts['-c']
        else:
            print("*** ERROR: must specify UDP address (opt: -c ADDRESS) ***",
                  file=sys.stderr)
            self.printHelp()
            return

        self.exit = False

    def printHelp(self):
        progname = sys.argv[0]
        progname = progname.split('/')[-1]  # strip off extended path
        help = __doc__.replace('<PROGNAME>', progname)
        print(help, file=sys.stderr)
