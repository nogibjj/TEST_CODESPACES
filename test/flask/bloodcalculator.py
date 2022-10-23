def interface():
    print("My Program")
    print("Options:")
    print("9 - Quit")
    keep_running = True
    while keep_running:
        choice = input("Enter your choice: ")
        if choice == "9":
            return


def input_HDL():
    HDL_input = input("Enter HDL value: ")
    return int(HDL_input)


def check_HDL(HDL_result):
    if HDL_result >= 60:
        return "Normal"
    elif 40 <= HDL_result < 60:
        return "Borderline Low"
    else:
        return "Low"


def HDL_driver():
    HDL_value = input_HDL()
    HDL_result = check_HDL(HDL_value)
    output_HDL(HDL_value, HDL_result)


def output_HDL(HDL_value, HDL_result):
    print("The HDL value of {} is considered {}".format(HDL_value, HDL_result))


# Modify interface to add the HDL analysis option and call your HDL driver function


def input_LDL():
    LDL_input = input("Enter LDL value: ")
    return int(LDL_input)


def check_LDL(LDL_result):
    if LDL_result < 130:
        return "Normal"
    elif 130 <= LDL_result < 159:
        return "Borderline High"
    elif 160 <= LDL_result < 189:
        return "High"
    else:
        return "Very High"


def LDL_driver():
    LDL_value = input_LDL()
    LDL_result = check_LDL(LDL_value)
    output_LDL(LDL_value, LDL_result)


def output_LDL(LDL_value, LDL_result):
    print("The LDL value of {} is considered {}".format(LDL_value, LDL_result))


# Using the feature branch approach
def check_total_cholesterol(TC_result):
    if TC_result < 200:
        return "Normal"
    elif 200 <= TC_result < 239:
        return "Borderline High"
    else:
        return "High"
