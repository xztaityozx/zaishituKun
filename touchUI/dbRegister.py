import sys
import dbReaderWriter
import CardRead

args = sys.argv

cr = CardRead.CardReader()
print "Please touch Card"
cr.read_id()
card_id = cr.idm
print "Card IDm : " + card_id

yorn = 'n'
while yorn != 'y':
    print "----------------------\nPlease input Name"
    name = raw_input()
    print "name : " + name + "  OK?(y/n)"
    yorn = raw_input()

db = dbReaderWriter.ReaderWriter()
db.ConnectToDB()
db.Regist(card_id, name)
db.Close()
print "Success Register!"
