import time
import os


pole_a = [3,2,1]
pole_b = []
pole_c = []


def solve_hanoi(pole_a, pole_b, pole_c):
    num_disks = len(pole_a)
    hanoi_recursive(num_disks, pole_a, pole_c, pole_b)


def hanoi_recursive(n, source, destination, auxiliary):
    if(n>0):
        hanoi_recursive(n-1, source, auxiliary, destination)
        move_disk(source, destination)
        hanoi_recursive(n-1, auxiliary, destination, source)
        test =0
    

def move_disk(source, target):
    disk = source.pop()
    target.append(disk)
    print(f"A: {pole_a}, B: {pole_b}, C: {pole_c}")

# clear terminal
clear_terminal = "\033[H\033[J"
print(clear_terminal)


solve_hanoi(pole_a, pole_b, pole_c)






