import pprint
import json
extra_dict_space = 0
def pretty_print(arr:list[list],start_indent:str="",count:int=0)->list:

    print_indent = start_indent+" "
    start_symbol = "{" if isinstance(arr,dict) else "["
    print(start_indent+start_symbol) # start of the iterable

    for i in arr:
        if isinstance(i,(list,dict)) :
            pretty_print(i,print_indent,count+1) # recursive call to the iterable in iterable
            

        elif isinstance(arr,list):
            print(f"{print_indent}{i},")

        elif isinstance(arr,dict):
            if isinstance(arr[i],(dict,list)):
                print(f"{print_indent}{i}:")
                pretty_print(arr[i],print_indent+" "*(len(i)+extra_dict_space),count+1)
            else:
                print(f"{print_indent}{i} : {arr[i]},")
        else:
            pass

    end_symbol = "}" if isinstance(arr,dict) else "]"


    if count > 0:
        print(start_indent+f"{end_symbol},")
    else:
        print(start_indent+end_symbol)






def main():

    nest_list = [1,2,'s','i','m',[3,4,[5,6],7,8],9]
    nest_dict = {"a":1,"b":2,"c":3,"d":4,"e":{"f":6,"h":7,"i":8},"p":10}
    test_list = [1,{2:3,4:5},[6,7],8]

    sample = json.loads("""{
  "rows": [
    {"value": 1, "valid": true},
    {"value": 2, "valid": true},
    {"value": 3, "valid": false}
  ]
}""")
    with open("temp.json","r") as f:
        sample_2 = json.load(f)

    data = sample_2


    # pretty_print(nest_list)
    print()
    # pretty_print(nest_dict)
    # print()

    # pretty_print(test_list)

    pretty_print(data)



if __name__ == "__main__":
    main()

