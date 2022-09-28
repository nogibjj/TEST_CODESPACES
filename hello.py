def bmi_calculator(weight, height):
    bmi = weight / height ** 2
    return bmi

def bmi_interface():
    print("This program calculates your BMI")
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in m: "))
    bmi = bmi_calculator(weight, height)
    print("Your BMI is: ", bmi)

if __name__ == "__main__":
    bmi_interface()

groupa=['ben','joe','sue']
groupb=[1,3,5,7,9]
