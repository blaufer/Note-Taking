#----------------------------------------------------------

class color:
    BEGINALL = '\033['
    PURPLE = '95'
    CYAN = '96'
    DARKCYAN = '36'
    BLUE = '94'
    GREEN = '92'
    YELLOW = '93'
    RED = '91'
    BOLD = '1'
    UNDERLINE = '4'
    END = '0'

    def purple(x):
        print('{0:s}{1:s}m{2:s}{3:s}{4:s}m'.format(color.BEGINALL, \
            color.PURPLE,x,color.BEGINALL,color.END))
    def cyan(x):
        print('{0:s}{1:s}m{2:s}{3:s}{4:s}m'.format(color.BEGINALL, \
            color.CYAN,x,color.BEGINALL,color.END))
    def darkcyan(x):
        print('{0:s}{1:s}m{2:s}{3:s}{4:s}m'.format(color.BEGINALL, \
            color.DARKCYAN,x,color.BEGINALL,color.END))
    def blue(x):
        print('{0:s}{1:s}m{2:s}{3:s}{4:s}m'.format(color.BEGINALL, \
            color.BLUE,x,color.BEGINALL,color.END))
    def green(x):
        print('{0:s}{1:s}m{2:s}{3:s}{4:s}m'.format(color.BEGINALL, \
            color.GREEN,x,color.BEGINALL,color.END))
    def yellow(x):
        print('{0:s}{1:s}m{2:s}{3:s}{4:s}m'.format(color.BEGINALL, \
            color.YELLOW,x,color.BEGINALL,color.END))
    def red(x):
        print('{0:s}{1:s}m{2:s}{3:s}{4:s}m'.format(color.BEGINALL, \
            color.RED,x,color.BEGINALL,color.END))
    def bold(x):
        print('{0:s}{1:s}m{2:s}{3:s}{4:s}m'.format(color.BEGINALL, \
            color.BOLD,x,color.BEGINALL,color.END))
    def underline(x):
        print('{0:s}{1:s}m{2:s}{3:s}{4:s}m'.format(color.BEGINALL, \
            color.UNDERLINE,x,color.BEGINALL,color.END))

    def two_types(one,two,x):
        if two not in (color.BOLD, color.UNDERLINE):
            color.red('Must have bold or underline as the second option')
            print(x)
        else:
            print('{0:s}{1:s};{2:s}m{3:s}{4:s}{5:s}m'.format(color.BEGINALL, \
                one,two,x,color.BEGINALL,color.END)) 

#----------------------------------------------------------
