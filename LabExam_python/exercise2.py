# def total_value(number_list):
#     total = 0
#     for i in number_list:
#         total += i
#     return total
#
#
# def high_card(number_list):
#     high_number = 0
#     for i in range(len(number_list)):
#         if high_number < number_list[i]:
#             high_number = number_list[i]
#     return high_number
#
#
# def sort_order(number_list):
#     sort_list = []
#     while len(number_list) != 0:
#         lowest_number = number_list[0]
#         for i in range(len(number_list)):
#             if lowest_number > number_list[i]:
#                 lowest_number = number_list[i]
#         number_list.remove(lowest_number)
#         sort_list.append(lowest_number)
#     return sort_list


# create lists
hearts_list = []
spade_list = []
club_list = []
diamond_list = []

number_of_cards_written = int(input("How many cards are you going to write: "))
counter = 0
while counter != number_of_cards_written:
    user = input("H (Heart), S (Spade), C (Club) or D (Diamond) and the number of card 1 to 10 example(H-5)\n")
    if len(user) >= 3:
        user_card = user[:1].upper()
        user_num = int(user[2:])

        if user_card in "HCDS" and 1 <= user_num <= 10:
            counter += 1
            if user_card == "H":
                hearts_list.append(user_num)
            elif user_card == "C":
                club_list.append(user_num)
            elif user_card == "D":
                diamond_list.append(user_num)
            elif user_card == "S":
                spade_list.append(user_num)
        
        elif user_card in "HCDS" and 1 > user_num > 10:
            print("The number needs to between 1 to 10")
            
        elif user_card not in "HCDS" and 1 <= user_num <= 10:
            print("H (Heart), S (Spade), C (Club) or D (Diamond)")
            
        else:
            print("H (Heart), S (Spade), C (Club) or D (Diamond)\nThe number needs to between 1 to 10")
            
    else:
        print("WRONG! example(C-5)")
        

print("Hearts: ", hearts_list)
print("Spade: ", spade_list)
print("Club: ", club_list)
print("Diamond: ", diamond_list)

print("----------------")

# using function for total value
# hearts_total = total_value(hearts_list)
# spade_total = total_value(spade_list)
# club_total = total_value(club_list)
# diamond_total = total_value(diamond_list)

print("Total Values: ")
print("Hearts: ", sum(hearts_list))
print("Spade: ", sum(spade_list))
print("Club: ", sum(club_list))
print("Diamond: ", sum(diamond_list))

print("----------------")

# using function for finding high card
# hearts_high = high_card(hearts_list)
# spade_high = high_card(spade_list)
# club_high = high_card(club_list)
# diamond_high = high_card(diamond_list)

print("High Card: ")
print("Hearts: ", max(hearts_list))
print("Spade: ", max(spade_list))
print("Club: ", max(club_list))
print("Diamond: ", max(diamond_list))

print("----------------")

# using function for sorting the cards
# hearts_sort = sort_order(hearts_list)
# spade_sort = sort_order(spade_list)
# club_sort = sort_order(club_list)
# diamond_sort = sort_order(diamond_list)

print("Sorted order: ")
print("Hearts: ", sorted(hearts_list))
print("Spade: ", sorted(spade_list))
print("Club: ", sorted(club_list))
print("Diamond: ", sorted(diamond_list))
