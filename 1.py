from browser import document, console, alert

input = document['input']
button = document['btn']
output = document['output']
select = document['select']

def getNum(a):
    temp = a
    try:
        temp = int(a)
    except ValueError:
        temp = float(a)
    finally:
        if temp != '' and type(temp) is str:
            alert('Harap masukkan jari jari')
            temp = ''
            input.value = temp
            return temp
        else:
            return temp

phi = 3.14;

def rumus(a, r):
    match a:
        case 'Luas Bola':
            return 4/3 * phi * r * r * r
        case 'Volume Bola':
            return r * r * phi * 4
        case _:        
            return 0


def main(ar):
    num = getNum(input.value)
    result = rumus(select.value, num)
    output.textContent = str(result)

def keyEnter(ar):
    console.log(f"{ar.code}")
    traceKey = f"{ar.code}"
    if traceKey == 'Enter':
        main(0)

button.bind('click', main)
input.bind("keypress", keyEnter)
