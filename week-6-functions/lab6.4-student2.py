# Student 2
# a different way or dealing with the users choice, using Dict.
# Author: Fatima Oliveira
 
def displayMenu(): 
    print("What would you like to do?") 
    print("\t(a) Add new student") 
    print("\t(v) View students") 
    print("\t(q) Quit") 
    choice = input("Type one letter (a/v/q):").strip() 
    return choice 
 
# def doAdd(students): VERY VAGUE def
#    print("do add") 
# def doView(students):  Very Vagues def
#    print("do View") 
def doNothing(dumby): 
    pass 

def doAdd(students): 
    currentStudent = {} 
    currentStudent["name"]=input("Enter name :") 
    currentStudent["modules"]= readModules() 
    students.append(currentStudent) 

def readModules(): 
    modules = [] 
    moduleName = input("\tEnter the first Module name (blank to quit) :").strip() 

    while moduleName != "": 
        module = {} 
        module["name"]= moduleName 
        # I am not doing error handling 
        module["grade"]=int(input("\t\tEnter grade:")) 
        modules.append(module) 
        # now read the next module name 
        moduleName = input("\tEnter next module name (blank to quit) :").strip() 
 
    return modules 
 
def doView(students): 
    # we fill this in later 
    print(students) 
 
#the dict that maps a letter to function 
choiceMap = [{ 'a': doAdd}, 
    {'v': doView}, 
    {'q': doNothing}
    ] # q is a valid choice

#main program 
students = []
ChoiceMap = displayMenu() 
while(choiceMap != 'q'): 
    if choiceMap == "a": 
        # run the function 
        doAdd(students)
    elif choiceMap == "v":
        doView(students)
    else: # use did not enter something valid 
        print("\n\nplease select either a,v or q") 
     
    choiceMap=displayMenu() 
