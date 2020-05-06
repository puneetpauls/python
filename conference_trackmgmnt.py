# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 11:16:40 2017

@author: puneetpaul
"""
input_dict = {"Writing Fast Tests Against Enterprise Rails":"60",
"Overdoing it in Python":"45","Lua for the Masses":"30","Ruby Errors from Mismatched Gem Versions":"45",
"Ruby on Rails: Why We Should Move On":"60","Common Ruby Errors":"45","Pair Programg vs Noise":"45",
"Programg in the Boondocks of Seattle":"30","Ruby vs. Clojure for Back-End Development":"30",
"User Interface CSS in Rails Apps":"30","Networking Event":"15"}

#input_dict={"topic1":"60","topic2":"45","topic3":"30","topic4":"45","topic5":"45",
#"topic6":"60","topic7":"45","topic8":"30","topic9":"30","topic10":"45","topic11":"60","topic12":"45","topic13":"30","topic14":"45","topic15":"45",
#"topic16":"60","topic17":"45","topic18":"30","topic19":"30","topic20":"45"}

DAY = 1

def mrg_conferencedata(input_dict):
    selected=[]
    selected_morning=[]
    sum=0
    for key,value in input_dict.items():
        count = 0
        selected.append(key)
        sum=sum+int(value)
        for key1,value1 in input_dict.items():
            if key1 not in selected:
                sum=sum+int(input_dict[key1])
                if sum<180:
                    selected.append(key1)
                    count = count+1
                elif sum>180:
                    count = count+1
                    break
                elif sum==180:
                    selected.append(key1)
                    count = count+1
                    break
        if sum>180 or count == (len(input_dict) - 1):
            selected_morning=selected
            break
    print("The Morning Schedule is :- ")
    print(selected_morning)
    print("It's Lunch Time")
    return selected_morning

def aft_conferencedata(input_dict):
    selected=[]
    selected_afternoon=[]
    sum=0
    for key,value in input_dict.items():
        selected.append(key)
        count = 0
        sum=sum+int(value)
        for key1,value1 in input_dict.items():
            if key1 not in selected:
                sum=sum+int(input_dict[key1])
                if sum>180 or sum==240:
                    selected.append(key1)             
                    count = count+1
                    break
                elif sum>240:
                    selected=[]
                    count = count+1
                    break
                elif sum<240:
                    selected.append(key1)
                    count = count+1      

        if sum>180 or sum==240 or count == (len(input_dict) - 1):
            selected_afternoon=selected
            break
    print("The Afternoon Schedule is :- ")     
    print(selected_afternoon)
    return selected_afternoon

def arrange_data(input_dict, DAY):
    """This module loads data in jsn format and store it in data object """
    if len(input_dict) != 0:
        print( "The schedule for %s day" %(DAY))
        data = mrg_conferencedata(input_dict)
        for key in data:
            del input_dict[key]
        data1 = aft_conferencedata(input_dict)
        for key in data1:
            del input_dict[key]
        
        data = arrange_data(input_dict, DAY + 1)

        
if __name__ == "__main__":
    arrange_data(input_dict, DAY)
