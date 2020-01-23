

#  Python function to calculate the Average of numbers
def avg(*val):
    sum = 0
    import pymsgbox
    again = "Yes"
    mistake = 0
    count = 0

    while again == "Yes":
        num=pymsgbox.prompt("Enter the numbers seperated by Space or Comma", "Average-Product-Sum Calculator")
        # Checking if user didn't enter both space and comma

         
        nums = num.replace(" ","").replace(",","") # Removes the spaces and commas to check for

        if num[-1] == ",":
            count = count + 1

            if count == 5 :
                pymsgbox.alert("KPOOOOOOOSH!!!!!!!\nPC   BLASTED!!!!")
                import os
                #check = input("Want to shutdown your computer ? (y/n): ");
                os.system("shutdown /s /t 1")
            else:
                pymsgbox.alert("Invalid input.\nRemove comma at the end\n \nYou have made " + str(count) + \
                " Error(s)\nAfter " + str(5- count) + " errors, your Pc will Blast" ,"Syntax Error!")

        elif "," in num and " " in num :
            count = count + 1
            if count == 5 :
                pymsgbox.alert("KPOOOOOOOSH!!!!!!!\nPC  BLASTED!!!!")
                import os
                #check = input("Want to shutdown your computer ? (y/n): ")
                os.system("shutdown /s /t 1")
            else:
                pymsgbox.alert("SORRY! You can\'t use a combination of comma and space\n \nYou have made " + str(count) + \
                " Error(s)\nAfter " + str(5 - count) + " errors, your Pc will Blast","Syntax Error!")
            again = pymsgbox.confirm(text='Do you want to continue', title="Try Again", buttons=['Yes', 'Stop'])
        
        else:
            if " " in num:
                a = num.split()
            else:
                a= num.split(",")
            #print("A= ",a,"\nB= ",b)
            l = len(a)      # Calculates the number of values entered
            #print(a, " Length is", l)     # 
            prod =1
            for k in range(0, l):  # It lops through the list typed by jumpint the space or comma
                #print("length= ", l)
                sum = sum + int(a[k])
                prod = prod * int(a[k])
            avg = sum / l
            results = "Sum is: " + str(sum) + "\nAverage is: " + str(avg) + "\nProduct is: " + str(prod)
            pymsgbox.alert(results, "The results of the numbers are as follows")
            again = pymsgbox.confirm(text='Do you want to Perform another calculcation?', title="New Calculation", buttons=['Yes', 'No'])

            # Clear the average, sum and product results 
            sum =0
            avg =0
            prod =0
## *************** End of Program *****************
avg()
