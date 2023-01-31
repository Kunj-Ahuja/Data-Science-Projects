from response import responses 

exit = ['exit',':e', '?e']
run = True

while run: 
    q = input('>> ').lower()
    if q in exit:
        run = False
    else:
        try : 
            print(f'🔥 {responses[q].title()}\n')
        except:
            print('I dont have response for this!! Sry\n')
