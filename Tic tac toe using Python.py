print("\n")
print("Tic tac toe board")
li = [['-', '-', '-'],
      ['-', '-', '-'],
      ['-', '-', '-']]
for row in li :
    print(row)
print("\n")
print("             PLAYER 1 == x    PLAYER 2 == O")

print("\n")
print("Index for player || Don't use same index twice ")
ls = [[0.0, 0.1, 0.2],
      [1.0, 1.1, 1.2],
      [2.0, 2.1, 2.2]]
for row in ls:
    print(row)

print("\n")
#asking for choices
print("Player 1")
li[int(input("enter your ist index   "))][int(input("enter your 2nd index  "))] = str(input("Your turn enter value: "))
print("\n")
print("Tic tac toe board")
for row in li :
     print(row)

print("\n")
print("Index for player || Don't use same index twice  ")
ls = [[0.0, 0.1, 0.2],
      [1.0, 1.1, 1.2],
      [2.0, 2.1, 2.2]]
for row in ls:
    print(row)

print("\n")
print("Player 2")
li[int(input("enter your ist index   "))][int(input("enter your 2nd index  "))] = str(input("Your turn enter value: "))
print("\n")
print("Tic tac toe board")
for row in li :
    print(row)

print("\n")
print("Index for player  || Don't use same index twice ")
ls = [[0.0, 0.1, 0.2],
      [1.0, 1.1, 1.2],
      [2.0, 2.1, 2.2]]
for row in ls:
    print(row)

print("\n")
print("Player 1")
li[int(input("enter your ist index   "))][int(input("enter your 2nd index  "))] = str(input("Your turn enter value: "))
print("\n")
print("Tic tac toe board")
for row in li :
    print(row)

print("\n")
print("Index for player || Don't use same index twice  ")
ls = [[0.0, 0.1, 0.2],
      [1.0, 1.1, 1.2],
      [2.0, 2.1, 2.2]]
for row in ls:
    print(row)

print("\n")
print("Player 2")
li[int(input("enter your ist index   "))][int(input("enter your 2nd index  "))] = str(input("Your turn enter value: "))
print("\n")
print("Tic tac toe board")
for row in li :
    print(row)

print("\n")
print("Index for player  || Don't use same index twice ")
ls = [[0.0, 0.1, 0.2],
      [1.0, 1.1, 1.2],
      [2.0, 2.1, 2.2]]
for row in ls:
    print(row)

print("\n")
print("Player 1")
li[int(input("enter your ist index   "))][int(input("enter your 2nd index  "))] = str(input("Your turn enter value: "))
print("\n")
print("Tic tac toe board")
for row in li :
    print(row)

#condition for player 1 = p1
for p1 in li :
    if li[0][0] == li[0][1] == li[0][2] == 'x':
        print("\n")
        print("\t")
        print("player 1 won")
        break
    if li[1][0] == li[1][1] == li[1][2] == 'x':
        print("\n")
        print("\t")
        print("player 1 won")
        break
    if li[2][0] == li[2][1] == li[2][2] == 'x':
        print("\n")
        print("\t")
        print("player 1 won")
        break
    if li[0][0] == li[1][0] == li[2][0] == 'x':
        print("\n")
        print("\t")
        print("player 1 won")
        break
    if li[0][1] == li[1][1] == li[2][1] == 'x':
        print("\n")
        print("\t")
        print("player 1 won")
        break
    if li[0][2] == li[1][2] == li[2][2] == 'x':
        print("\n")
        print("\t")
        print("player 1 won")
        break
    if li[0][0] == li[1][1] == li[2][2] == 'x':
        print("\n")
        print("\t")
        print("player 1 won")
        break
    if li[0][2] == li[1][1] == li[2][0] == 'x':
        print("\n")
        print("\t")
        print("player 1 won")
        break

print("\n")
print("Index for player  || Don't use same index twice ")
ls = [[0.0, 0.1, 0.2],
      [1.0, 1.1, 1.2],
      [2.0, 2.1, 2.2]]
for row in ls:
    print(row)

print("\n")
print("Player 2")
li[int(input("enter your ist index   "))][int(input("enter your 2nd index  "))] = str(input("Your turn enter value: "))
print("\n")
print("Tic tac toe board")
for row in li :
    print(row)

#condidtion for player 2 = p2    
for p2 in li :
    if li[0][0] == li[0][1] == li[0][2] == 'O':
        print("\n")
        print("\t")
        print("player  won")
        break
    if li[1][0] == li[1][1] == li[1][2] == 'O':
        print("\n")
        print("\t")
        print("player 2 won")
        break
    if li[2][0] == li[2][1] == li[2][2] == 'O':
        print("\n")
        print("\t")
        print("player 2 won")
        break
    if li[0][0] == li[1][0] == li[2][0] == 'O':
        print("\n")
        print("\t")
        print("player 2 won")
        break
    if li[0][1] == li[1][1] == li[2][1] == 'O':
        print("\n")
        print("\t")
        print("player 2 won")
        break
    if li[0][2] == li[1][2] == li[2][2] == 'O':
        print("\n")
        print("\t")
        print("player 2 won")
        break
    if li[0][0] == li[1][1] == li[2][2] == 'O':
        print("\n")
        print("\t")
        print("player 2 won")
        break
    if li[0][2] == li[1][1] == li[2][0] == 'O':
        print("\n")
        print("\t")
        print("player 2 won")
        break

print("\n")
print("Index for player || Don't use same index twice  ")
ls = [[0.0, 0.1, 0.2],
      [1.0, 1.1, 1.2],
      [2.0, 2.1, 2.2]]
for row in ls:
    print(row)

print("\n")
print("Player 1")
li[int(input("enter your ist index   "))][int(input("enter your 2nd index  "))] = str(input("Your turn enter value: "))
print("\n")
print("Tic tac toe board")
for row in li :
    print(row)

#condition for player = p1
for p1 in li :
    if li[0][0] == li[0][1] == li[0][2] == 'x':
        print("\n")
        print("\t")
        print("player 1 won")
        break
    if li[1][0] == li[1][1] == li[1][2] == 'x':
        print("\n")
        print("\t")
        print("player 1 won")
        break
    if li[2][0] == li[2][1] == li[2][2] == 'x':
        print("\n")
        print("\t")
        print("player 1 won")
        break
    if li[0][0] == li[1][0] == li[2][0] == 'x':
        print("\n")
        print("\t")
        print("player 1 won")
        break
    if li[0][1] == li[1][1] == li[2][1] == 'x':
        print("\n")
        print("\t")
        print("player 1 won")
        break
    if li[0][2] == li[1][2] == li[2][2] == 'x':
        print("\n")
        print("\t")
        print("player 1 won")
        break
    if li[0][0] == li[1][1] == li[2][2] == 'x':
        print("\n")
        print("\t")
        print("player 1 won")
        break
    if li[0][2] == li[1][1] == li[2][0] == 'x':
        print("\n")
        print("\t")
        print("player 1 won")
        break

print("\n")
print("Index for player || Don't use same index twice  ")
ls = [[0.0, 0.1, 0.2],
      [1.0, 1.1, 1.2],
      [2.0, 2.1, 2.2]]
for row in ls:
    print(row)

print("\n")
print("Player 2")
li[int(input("enter your ist index   "))][int(input("enter your 2nd index  "))] = str(input("Your turn enter value: "))
print("\n")
print("Tic tac toe board")
for row in li :
    print(row)

#condition for player 2 = p2
for p2 in li :
    if li[0][0] == li[0][1] == li[0][2] == 'O':
        print("\n")
        print("\t")
        print("player  won")
        break
    if li[1][0] == li[1][1] == li[1][2] == 'O':
        print("\n")
        print("\t")
        print("player 2 won")
        break
    if li[2][0] == li[2][1] == li[2][2] == 'O':
        print("\n")
        print("\t")
        print("player 2 won")
        break
    if li[0][0] == li[1][0] == li[2][0] == 'O':
        print("\n")
        print("\t")
        print("player 2 won")
        break
    if li[0][1] == li[1][1] == li[2][1] == 'O':
        print("\n")
        print("\t")
        print("player 2 won")
        break
    if li[0][2] == li[1][2] == li[2][2] == 'O':
        print("\n")
        print("\t")
        print("player 2 won")
        break
    if li[0][0] == li[1][1] == li[2][2] == 'O':
        print("\n")
        print("\t")
        print("player 2 won")
        break
    if li[0][2] == li[1][1] == li[2][0] == 'O':
        print("\n")
        print("\t")
        print("player 2 won")
        break

print("\n")
print("Index for player  || Don't use same index twice ")
ls = [[0.0, 0.1, 0.2],
      [1.0, 1.1, 1.2],
      [2.0, 2.1, 2.2]]
for row in ls:
    print(row)

print("\n")
print("Player 1")
li[int(input("enter your ist index   "))][int(input("enter your 2nd index  "))] = str(input("Your turn enter value: "))
print("\n")
print("Tic tac toe board")
for row in li :
    print(row)

#condition for player = p1
for p1 in li :
    if li[0][0] == li[0][1] == li[0][2] == 'x':
        print("\n")
        print("\t")
        print("player 1 won")
        break
    if li[1][0] == li[1][1] == li[1][2] == 'x':
        print("\n")
        print("\t")
        print("player 1 won")
        break
    if li[2][0] == li[2][1] == li[2][2] == 'x':
        print("\n")
        print("\t")
        print("player 1 won")
        break
    if li[0][0] == li[1][0] == li[2][0] == 'x':
        print("\n")
        print("\t")
        print("player 1 won")
        break
    if li[0][1] == li[1][1] == li[2][1] == 'x':
        print("\n")
        print("\t")
        print("player 1 won")
        break
    if li[0][2] == li[1][2] == li[2][2] == 'x':
        print("\n")
        print("\t")
        print("player 1 won")
        break
    if li[0][0] == li[1][1] == li[2][2] == 'x':
        print("\n")
        print("\t")
        print("player 1 won")
        break
    if li[0][2] == li[1][1] == li[2][0] == 'x':
        print("\n")
        print("\t")
        print("player 1 won")
        break

#condition for player 2 = p2
for p2 in li :
    if li[0][0] == li[0][1] == li[0][2] == 'O':
        print("\n")
        print("\t")
        print("player 2 won")
        break
    if li[1][0] == li[1][1] == li[1][2] == 'O':
        print("\n")
        print("\t")
        print("player 2 won")
        break
    if li[2][0] == li[2][1] == li[2][2] == 'O':
        print("\n")
        print("\t")
        print("player 2 won")
        break
    if li[0][0] == li[1][0] == li[2][0] == 'O':
        print("\n")
        print("\t")
        print("player 2 won")
        break
    if li[0][1] == li[1][1] == li[2][1] == 'O':
        print("\n")
        print("\t")
        print("player 2 won")
        break
    if li[0][2] == li[1][2] == li[2][2] == 'O':
        print("\n")
        print("\t")
        print("player 2 won")
        break
    if li[0][0] == li[1][1] == li[2][2] == 'O':
        print("\n")
        print("\t")
        print("player 2 won")
        break
    if li[0][2] == li[1][1] == li[2][0] == 'O':
        print("\n")
        print("\t")
        print("player 2 won")
        break