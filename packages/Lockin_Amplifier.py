class Lia():
    
    def __init__(self):
        try:
            self.sro830 = serial.Serial('COM17', baudrate=19200,
                                        parity=serial.PARITY_NONE,
                                        stopbits=serial.STOPBITS_ONE,
                                        bytesize=serial.EIGHTBITS,
                                        timeout=1)
            self.model = self.asklia('*IDN?')
        except IOError:
            print( 'Lock-in não encontrado!')
        except ValueError:
            print ('Lock-in drive não encontrado!')
        
    def asklia(self, cmd):
        self.sro830.write(cmd+'\n')
        self.sro830.flush()
        answer = self.sro830.readline()
        return answer
                                    
    def configlia(self, cmd):
        self.sr830.write(cmd+'\n')

    def measure(self):
        try:
            lockin = self.asklia("SNAP?1,2,3,4")
            x = float(lockin.split(',')[0])
            y = float(lockin.split(',')[1])
            amp = float(lockin.split(',')[2])
            phas = float(lockin.split(',')[3])
            return x, y, amp, phas
        except ValueError:
            pass