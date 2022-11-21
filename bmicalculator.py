


def result(bmmi):

    if bmmi <=16:
        return "Severe Thinness"
    elif bmmi <=17:
        return "Moderate Thinness"    
    elif bmmi <= 18.5:
        return "Mild Thinness"   
    elif bmmi <=25:
        return "Normal" 
    elif bmmi <=30:
        return "Overweight"   
    elif bmmi <=35:
        return "Obese Class I"    
    elif bmmi <= 40:
        return "Obese Class II"  
    elif bmmi > 40:
        return "Obese Class III"  

    # elif gender == "c":
    #     if bmmi <=16:
    #         return "Severe Thinness"
    #     elif bmmi <=17:
    #         return "Moderate Thinness"    
    #     elif bmmi <= 18.5:
    #         return "Mild Thinness"   
    #     elif bmmi <=25:
    #         return "Normal" 
    #     elif bmmi <=30:
    #         return "Overweight"   
    #     elif bmmi <=35:
    #         return "Obese Class I"    
    #     elif bmmi <= 40:
    #         return "Obese Class II"  
    #     elif bmmi > 40:
    #         return "Obese Class III"   


def bmi(height,weight):

    weight_as_int = int(weight)
    height_as_float = float(height)
    bmi = weight_as_int / height_as_float ** 2
    bmi = weight_as_int / (height_as_float * height_as_float)

    bmi_as_int = int(bmi)
    print(f"Your BMI is {bmi_as_int}")

    return result(bmi_as_int)




height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")



bodymass = bmi(height, weight)

print(bodymass)



