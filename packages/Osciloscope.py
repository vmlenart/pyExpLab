class Usbtmc(object):
    terminator = '\n'

    def __init__(self):

        try:
            devs = glob.glob('/dev/usbtmc*')
            if devs == []:
                raise ValueError('Erro de procura usbtmc* em /dev.')
            for dev_name in devs:
                self.dev  = open(dev_name, 'wb+')
                answer = self.ask('*IDN?').split(',')[1]
                if answer:
                    print ' %s encontrado.' % answer
                    self.idn = answer
                    break
        except ValueError:
            print 'Osciloscópio não encontrado.'
            self.idn = ''


    def write(self, command):
        self.dev.write(command + self.terminator)

    def readline(self):
        return self.dev.readline()

    def read(self, n):
        return self.dev.read(n)

    def ask(self, command):
        self.write(command)
        return self.readline()


class Tek_withoutvisa(object):

    channels = ('CH1', 'CH2', 'MATH', 'REFA')

    def __init__(self):
        self.tek = Usbtmc()
        self.idn = self.tek.idn
        if self.idn:
            self.setup()

    def setup(self, recordlenght='2500', start = '0', stop = '2500'):
        try:
            self.tek.write("DATA:ENCDG SRPbinary;WIDTH 1")
            self.tek.ask("DATA:ENCDG?")
            self.tek.write("HORIZONTAL:RECORDLENGHT " + recordlenght)
            self.tek.write('DATA:START ' + start)
            self.tek.write('DATA:STOP ' + stop)
            self.tek.write('HEADER OFF')
        except:
            print 'Osciloscópio desligado!'

    def selected_channels(self):
        answer =  ''.join(self.tek.ask('SEL?').strip().split(';'))
        selected = [ self.channels[x] for x in range(5) if answer[x] == '1']
        return selected


    def acquire(self, channel):
        try:
            self.tek.write('LOCK')
            self.tek.write("DATA:SOURCE " + channel)
            self.tek.write("ACQUIRE:STATE RUN")
            self.time_stamp = time.strftime("%g%m%d%H%M%S")
            self.tek.write("CURVE?")
            raw = self.tek.readline()
            self.yoff = float(self.tek.ask('WFMP:YOF?'))
            self.ymult = float(self.tek.ask('WFMP:YMULT?'))
            self.xincr = float(self.tek.ask('WFMP:XIN?'))
            self.xunit = self.tek.ask('WFMP:XUNIT?')
            self.yunit =self.tek.ask('WFMP:YUNIT?')
            self.tek.write('UNLOCK')
            y_raw = np.frombuffer(raw, dtype = np.uint8,count=2500, offset = 5)
            y = (y_raw - self.yoff) * self.ymult
            x = np.array(range(2500)) * self.xincr
            return x,y

        except IndexError:
            return 0,0
