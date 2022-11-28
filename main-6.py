from game_data import data
from art import logo
from art import vs
import random
from replit import clear

def play():
    score = 0
    game_over = False
    for n in data:
        A = (random.choice(data))
        B = (random.choice(data))
        A = list(A.values())
        B = list(B.values())
    print(f"Compare A: {A[0]} a {A[2]} from {A[3]}.")
    print (vs)
    print(f"Against B: {B[0]} a {B[2]} from {B[3]}.")
    choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    
    while game_over == False:
        if choice == 'A':
            if A[1] > B[1]:
                clear()
                score += 1
                print (logo)
                print(f"You are right! Current score: {score}")
                A = B
                while A == B:
                    for n in data:
                        B = (random.choice(data))
                        B = list(B.values())
                print(f"Compare A: {A[0]} a {A[2]} from {A[3]}.")
                print (vs)
                print(f"Against B: {B[0]} a {B[2]} from {B[3]}.")
                choice = input("Who has more followers? Type 'A' or 'B': ").upper()
            elif A[1] < B[1]:
                clear()
                print(f"Sorry that's wrong. Your score: {score}")
                game_over = True
        elif choice == 'B':
            if B[1] > A[1]:
                clear()
                score += 1
                print(logo)
                print(f"You are right! Current score: {score}")
                A = B
                while A == B:
                    for n in data:
                        B = (random.choice(data))
                        B = list(B.values())
                print(f"Compare A: {A[0]} a {A[2]} from {A[3]}.")
                print (vs)
                print(f"Against B: {B[0]} a {B[2]} from {B[3]}.")
                choice = input("Who has more followers? Type 'A' or 'B': ").upper()
            elif B[1] < A[1]:
                clear()
                print(f"Sorry that's wrong. Your score: {score}")
                game_over = True
        else:    
            print("Incorrect entry. Game over!")
            game_over = True
                
            
print (logo)
play()