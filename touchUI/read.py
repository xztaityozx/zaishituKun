import nfc
import binascii


class CardReader(object):
    def on_connect(self, tag):
        self.idm = binascii.hexlify(tag.idm)
        return True

    def read_id(self):
        clf = nfc.ContactlessFrontend('usb')
        try:
            clf.connect(rdwr={'on-connect': self.on_connect})
        finally:
            clf.close()

def main():
    cr=CardReader()
    cr.read_id()
    print cr.idm

if __name__ == '__main__':
    main()