import nfc
import binascii
import os
import dbReaderWriter

dataBank_path = os.environ["ZAISEKIKUN_PATH"] + "touchUI/dataBank.txt"


class CardReader(object):
    def __init__(self):
        self.mode = 0

    def on_connect(self, tag):
        self.idm = binascii.hexlify(tag.idm)
        return True

    def read_id(self):
        clf = nfc.ContactlessFrontend('usb')
        try:
            clf.connect(rdwr={'on-connect': self.on_connect})
        finally:
            clf.close()

    def readLoop(self):
        db = dbReaderWriter.ReaderWriter()
        while True:
            self.read_id()
            self.getEnvData()
            db.ConnectToDB()
            print "Get IDm : " + self.idm
            print "Mode : " + self.mode
            if int(self.mode) == 1:
                print "Change Condition"
                db.ChangeCondition(self.idm, self.condition_to)
            else:
                print "Toggle Condition"
                db.ToggleCondition(self.idm)
            db.Close()
            self.resetEnvData()

    def getEnvData(self):
        with open(dataBank_path) as target:
            self.mode = target.readline()
            self.condition_to = target.readline()

    def resetEnvData(self):
        with open(dataBank_path, mode='w') as target:
            target.writelines("0\n")
            target.writelines("0")


def main():
    cr = CardReader()
    cr.readLoop()


if __name__ == '__main__':
    main()
