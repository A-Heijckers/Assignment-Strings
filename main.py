# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

Goal1 = "Ruud Gullit"
Goal2 = "Marco van Basten"
goal_0 = 32
goal_1 = 54
scorers = Goal1 + " " + str(goal_0) + ", " + Goal2 + " " + str(goal_1)
report = (f"{Goal1} scored in the {goal_0}nd minute"'\n'
          f"{Goal2} scored in the {goal_1}th minute")
print(report)


player = "Ruud Gullit"
first_name = player[(player.find("Ruud")):4]
print(first_name)

last_name_len = len(player[(player.find("Gullit")):11])
print(last_name_len)

e = player[0]+"."
print(e)
f = player[5:11]
name_short = (player[0])+(".") + " " + f
print(name_short)


chant = (first_name + "!" + " ") * 3 + (first_name + "!")
print(chant)
good_chant = (chant != " ")
print(good_chant != " ")
