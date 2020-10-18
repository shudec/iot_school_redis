class DataLoader(object):

    filename=''

    def __init__ (self, filename):
        self.filename = filename

    def load (self, header=False):
        data = []
        try:
            dataFile = open(self.filename, mode='r', encoding='utf-8')
            for line in dataFile:
                linedata = line.split(';')
                data.append(linedata)
            if header:
                data.pop(0)    
        finally:
            dataFile.close
        return data