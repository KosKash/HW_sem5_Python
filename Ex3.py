# Архив
tx = 'daaaabbbcccccaaadddddde' #1d4a3b5c3a6d1e
tx2 = '1d4a3b5c3a6d1e' #daaaabbbcccccaaadddddde
def to_in(text:str) -> str:
    swap = ''
    cnt = 1
    for i in range(len(text)-1):
        if text[i] == text[i+1]:
            cnt+=1
        else:
            swap +=(f'{cnt}{text[i]}')
            cnt = 1
        if  i == (len(text)-2):
            if cnt == 1:
                swap += (f'{cnt}{text[i+1]}')
    return swap

def to_out(text:str) -> str:
    text = list(text.strip())
    out = ''
    for i in range(0,len(text),2):
        out+=str(text[i+1]*int(text[i]))
    return out
        
def test(st:str)->str:
    if st == to_out(to_in(st)):
        print('Test: Passed')
    else:
        print('Test: Failed')  

test(tx)

print(to_in(tx))

print(to_out(tx2))
