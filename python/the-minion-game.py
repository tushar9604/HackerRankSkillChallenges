def minion_game(string):
    # your code goes here
    v = 'AEIOU'
   # string = string.upper()
    
    kevSc = 0
    stuSc = 0
    for i in range(len(string)):
        if (string[i] in v):
            kevSc += (len(string) - i)
        else:
            stuSc += (len(string) - i)
          
    if (kevSc > stuSc):
        print('Kevin',kevSc)
    elif (stuSc > kevSc):
        print('Stuart',stuSc)
    else:
        print("Draw")
    

if __name__ == '__main__':
    s = input()
    minion_game(s)