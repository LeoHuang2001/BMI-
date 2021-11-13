h = float(input('請輸入身高(cm): '))
w = float(input('請輸入體重(kg): '))
h = h/100
bmi = w / (h**2)
bmi = round(bmi,2)
if bmi < 18.5 :
    print('體重過輕')
elif bmi >= 18.5 and bmi < 24 :
    print('你的BMI: ',bmi,'體重正常')
elif bmi >= 24 and bmi < 27 :
    print('你的BMI: ',bmi,'稍重')
elif bmi >= 27 and bmi < 30 :
    print('你的BMI: ',bmi,'輕度肥胖')
elif bmi >= 30 and bmi < 35 :
    print('你的BMI: ',bmi,'中度肥胖')
else :
    print('你的BMI: ',bmi,'重度肥胖')