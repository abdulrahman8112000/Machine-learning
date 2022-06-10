is_teacher=False
is_expert=True


if is_teacher and is_expert:
    print("you are a mster teacher")

elif is_teacher and not is_expert:
    print("at least you are getting there")

elif not is_teacher:
    print("you need teaching powers")