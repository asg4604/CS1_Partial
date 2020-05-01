from stack import *

red_can = make_empty_stack()
red_can.color = "R"

green_can = make_empty_stack()
green_can.color = "G"

blue_can = make_empty_stack()
blue_can.color = "B"

def get_bottom_color(can):
    pointer = can.top
    while True:
        if pointer.rest is None:
            return pointer.value
        else:
            pointer = pointer.rest

def push_multiple(stack, lst):
    [push(stack, elem) for elem in lst]

def move_ball(from_can, to_can):
    push(to_can, pop(from_can))


def can_is_good(can):
    pointer = can.top
    while pointer.rest:
        if pointer.rest.value != pointer.value:
            return False
        pointer = pointer.rest
    return True


def get_matching_can(ball, can_lst):
    for can_idx in range(len(can_lst)):
        if can_lst[can_lst].color == ball:
            return can_idx

def get_good_can(ball, can_lst, bottom_color, cur_idx):
    for can_idx in range(len(can_lst)):
        if can_lst[can_idx].color != bottom_color and can_idx != cur_idx:
            return can_idx


#Zeros will be replaced with indices later on
def strategy(can_lst):
    bottom_color = get_bottom_color(can_lst[0])
    pointer = can_lst[0].top
    while pointer.rest:
        ball = pointer.value
        idx = get_good_can(ball, can_lst, bottom_color, 0)
        move_ball(can_lst[0], g)

        pointer = pointer.rest







push_multiple(red_can, "G")
can_lst = [red_can, green_can, blue_can]
print(get_good_can("G", can_lst, "G", 0))

