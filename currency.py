def int_to_inr(num):
    num_str = str(num)
    if len(num_str) > 3:
        last_three_digits = num_str[-3:]
        num_str = num_str[:-3]
        remaining_digits = len(num_str)
        if remaining_digits % 2 != 0:
            inr_str = num_str[0] + ","
            num_str = num_str[1:]
            remaining_digits = remaining_digits - 1
        else:
            inr_str = ""
        for i in range(0, remaining_digits, 2):
            inr_str = inr_str + num_str[i:i+2] + ","
        inr_str = inr_str[:-1] + "," + last_three_digits
    else:
        inr_str = num_str
    return inr_str

print(int_to_inr(504678)) # Output: 5,04,678
