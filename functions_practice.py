running_kids = ["Pam", "Sam", "Andrea", "Will"]
swinging_kids = ["Marybeth", "Jenna", "Kevin", "Courtney"]
sliding_kids = ["Mike", "Jack", "Jennifer", "Earl"]
hiding_kids = ["Henry", "Heather", "Hayley", "Hugh"]


def run(names):
    for each in names:
        print(f"{each} ran")


def swing(names):
    for each in names:
        print(f"{each} swung")


def slide(names):
    for each in names:
        print(f"{each} slid")


def hide_and_seek(names):
    for each in names:
        print(f"{each} hid")

# run(running_kids)
# swing(swinging_kids)
# slide(sliding_kids)
# hide_and_seek(hiding_kids)


def chicken_monkey():
    for num in range(1, 101):
        if num % 5 == 0 and num % 7 == 0:
            print("ChickenMonkey")
        elif num % 5 == 0:
            print("Chicken")
        elif num % 7 == 0:
            print("Monkey")
        else:
            print(num)

# chicken_monkey()


def calc_dollars():
    piggyBank = {
        "pennies": 1,
        "nickels": 1,
        "dimes": 1,
        "quarters": 4
    }
    for key, value in piggyBank.items():
        if key == "pennies":
            pennies = value
        elif key == "nickels":
            nickels = value * 5
        elif key == "dimes":
            dimes = value * 10
        else:
            quarters = value * 25
    dollarAmount = (pennies + nickels + dimes + quarters) / 100
    print(f'${dollarAmount}')


# calc_dollars()

def calc_bank(amount):
    num = amount * 100
    not_q = num % 25
    quarters = round((num - not_q) / 25)
    not_q_or_d = not_q % 10
    dimes = round((not_q - not_q_or_d) / 10)
    not_q_d_or_n = not_q_or_d % 5
    nickels = round((not_q_or_d - not_q_d_or_n) / 5)
    pennies = round(num - ((quarters * 25) + (dimes * 10) + (nickels * 5)))
    piggy_bank = {
        "quarters": quarters,
        "dimes": dimes,
        "nickels": nickels,
        "pennies": pennies
    }
    print(piggy_bank)


# calc_bank(5.78)

nums = ["one", "two", "three", "four", "five"]

def lightning_func(li, string="I can count to"):
    for each in li:
        print(string + " " + each)
        
# lightning_func(nums, "I like")
