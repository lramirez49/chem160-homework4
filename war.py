from card import *
adeck=deck()
bdeck=deck()
while adeck.cards(eff)>0:
    acard=adeck.dealcards()
    if acard.value()>bcard.value():
        acard+=2
    if acard.value()<bcard.value():
        bcard+=2
    if acard.value()==bcard.value():
        acard+=1
        bcard+=1
    print((acard-bcard))
    index=abs(acard-bcard)//2
    diff[index]+=1