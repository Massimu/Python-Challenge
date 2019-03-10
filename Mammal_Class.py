import os
#------------------------------------------------------------------------------
#Main CLASS
class Mammal:
    #initialization
    sex = ""
    age = 0
    
    #Generic attributes: SEX and AGE
    def __init__(self, sex, age):
        self.sex = sex
        self.age = age
    
    #Factory:
    @staticmethod 
    def factory():
        filepath = os.path.join(os.getcwd(),'D://projects/KIT/mammals.txt')   #change path !!!!!
        with open (filepath, 'r') as f:
            lines = f.readlines()
        mamals = []
        for l in lines:
            args = l.split(' ')
            if (len(args)==4):                
                if "dog" in args[0].lower():
                    mamals.append(Dog(args[1],args[2],args[3]))
                elif "cat" in args[0].lower():
                    mamals.append(Cat(args[1],args[2],args[3]))
                else:
                    mamals.append(Whale(args[1],args[2],args[3]))
        return mamals
            
    #assign and get generic features     
    def set_sex(self, sex):
        self.sex = sex

    def set_age(self, age):
        self.age = age
     
    def get_sex(self):
        return self.sex
    
    def get_age(self):
        return self.age 
#------------------------------------------------------------------------------  
#Dog
class Dog(Mammal):
    
    has_vaccinated = ""
    #assign and get specific feature
    def __init__(self, sex, age, has_vaccinated):
        super().__init__(sex,age)
        self.has_vaccinated = has_vaccinated
     
    def set_has_vaccinated(self, has_vacinate):
        self.has_vacinate = has_vacinate
     
    def get_has_vaccinated(self):
        return  self.has_vacinate    
    
    def __str__(self):
        return '{:<0}  {:>12}  {:<12} has vaccinated: {:<12}'.format(str(self.__class__.__name__),self.sex,self.age,self.has_vaccinated)
#------------------------------------------------------------------------------   
#Cat  
class Cat(Mammal):
    
    birthplace = ""
    #assign and get specific feature
    def __init__(self, sex, age, birthplace):
        super().__init__(sex,age)
        self.birthplace = birthplace
     
    def set_birthplace(self, birthplace):
        self.birthplace = birthplace
     
    def get_birthplace(self):
        return  self.birthplace
    
    def __str__(self):
        return '{:<0}  {:>12}  {:<12} birthplace: {:<12}'.format(str(self.__class__.__name__),self.sex,self.age,self.birthplace)
#------------------------------------------------------------------------------
#Whale      
class Whale(Mammal):
    
    livingplace = ""
    #assign and get specific feature    
    def __init__(self, sex, age, livingplace):
        super().__init__(sex,age)
        self.livingplace = livingplace
     
    def set_livingplace(self, livingplace):
        self.livingplace = livingplace
       
    def get_livingplace(self):
        return  self.livingplace  
        
    def __str__(self):
        return '{:<0}  {:>10}  {:<12} livingplace: {:<12}'.format(str(self.__class__.__name__),self.sex,self.age,self.livingplace)
#------------------------------------------------------------------------------
#output:
print(Mammal.factory())
print("\n\nNAME      ","SEX    ","AGE        ","Feature\n--------------------------------------------")
mammals = Mammal.factory()
for i in mammals:
    print(i)
print("---------------------------------------------\n")
#print(type(Mammal.factory()[0]))
    
    