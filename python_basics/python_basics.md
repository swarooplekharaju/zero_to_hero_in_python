SYALLABUS  :

THIS IS A FAST TRACK PYTHON COURSE DIVIDED INTO THREE PARTS :

PART 1 : EFFECTIVE PYTHON 
  
    CONTENTS :
     1. LAMBDA 
     2. MAP,FILTER AND REDUCE 
     3. FUNCTIONS WITH *ARGS AND **KWARGS 
     4.

PART 2 : BUILTIN DATA TYPES 


3. BASIC OPPS : CLASSES , OBJECTS ,STATICS ETC. EVERYTHING ON CLASS LEVEL 


PART 1 :  

    1.EFFECTIVE PYTHON :
  
    INTORDUCTION : 
     In this chapter we will learn the concepts which makes us the better, efficient and fast way of doing the python coding
     all the code is commited to under the following directory 
   
     1. LAMBDA :
   
     lambda is an anynonuus function 
   
     In simple words it is a short hand way of writing a function 
   
     lets see the example and the output 
      lambda x : x**3
     
     this is a lambda function which returns the cuberoot of the values 
  
     lambda fucntion can be stored in the variables and can be reused in the code 
      
     these are major uses of the lambda , I hope we had a great start about writing faster functions 
     instead of writing 
     def square(x):
     return x**x 
     I hope now you guys can write a faster lambda function 
     
      



![image](https://user-images.githubusercontent.com/45656883/123250411-a4b8e480-d507-11eb-88c9-fb8a04ce8652.png)
  
  
![image](https://user-images.githubusercontent.com/45656883/123250776-16912e00-d508-11eb-9804-fa8629b8b63d.png)
  

    2. UNDERSTANDING MAP AND ITS USES :
       
       DEFINITION : 
             
                   THE simple use of map is it takes the function and sequence as input 
                   
                   applies the function to list of elements in the sequential manner 
                   
                   it returns the map object , we should explictly convert the map to list or tuple 
                   
                   syntax :  map (func,*iterables/list)
                   
                   lets see an simple example : 
                   in the following example we have passed the 
                   lambda function and list
                   we can only pass  one list to the map 
                   
   ![image](https://user-images.githubusercontent.com/45656883/123251558-f746d080-d508-11eb-9fb3-e6bc714f57ec.png)
              
                   case 2 : handling multiple lambda functions in a single map 
                   
                   lets make a list of two lambda functions
                   we know that map takes a list and a function 
                   outer layer -- > loop of number or loop over a sequence 
                   inside the map -->
                           so we will pass each item in the list as an argument to the following template of map 
                           which is  -->
                   value = list(map(lambda x: x(i), funcs))
                   
                   
   ![image](https://user-images.githubusercontent.com/45656883/123588887-12b22400-d806-11eb-8fa3-92ae1a7392ef.png)
                
                   
                   
               CHAPTER 2 : UNDERSTANDING FILTER : 
                              filter takes an input conditional function and a iterator 
                              fiter checks the value and returns if the condition is truee 
                              filter is an another way or functional or lambda way of writing an list comprehension 
                              
                              example  :
                               list(filter(lambda x :x>3 ,[1,2,3,4]
                               output is : 3,4 
               CHAPTER 3 : UNDERSTANDING REDUCE :
                          the main advantage of taking reduce is it performs operations on adjacent items in the list 
                          and reduces to a single value 
                          like adding all the items in the list to one 
                          or square and add all the items to 1 
                          it means like finally use the arithematic operation to get into 1
               
   ![image](https://user-images.githubusercontent.com/45656883/123597516-0ed7cf00-d811-11eb-8de9-db7ae06c8c7d.png)

                       
                              
              CHAPTER 4 : UNDERSTANDIN GLOBALS 
                IN THIS CHAPTER WE WILL SEE THE USES AND APPLICATIONS OF GLOBLAS 
                understanding global keyword 
                when the variable of the larger scope is used inside a function or lesser scope 
                we use global 
                global keyword at the larger scope is not valubale /no use 
                
                we can create a config.py and store all the global variables inside the file and access them 
                
                NOTE : 
                 GLOBAL VARIABLES are the values where variable names and values are initially defined 
                 they are mutable and can be modified in terms of value .
                 
                 you can see the following example 
                 config.a is a global value in the config.py module 
                 but it is accesed and modified in the other module 
                 so lets be clear , global values can be modified [ keyword is global]
                
                    

![image](https://user-images.githubusercontent.com/45656883/123957616-a08a3c80-d9c9-11eb-872a-19f5745058bd.png)


                 globals part  2 : how the scope of global works 
                 
                 a normal variable x inside any function is a local variable 
                 a normal variable inside inner/nested function is non local variable 
                 a variable with bigscore/ out of any functions in module is a gloabal variable
                 if a variable is declared as gloabal , it does two things 
                   1. if  global variable is not there it creates the gloabal variable 
                   2. if a gloabal variable is there it connects with the global variable and we can perform actions 
                   
                 in the following code 
                   we dont have gloabal variable x 
                   we have only local variable x --> because x is declared only inside a main_function 
                   in the inner_function we declared a new global variable 
                     -- > which means that global x is differnt and local x is different 
                  
   ![image](https://user-images.githubusercontent.com/45656883/123959791-2e672700-d9cc-11eb-9f86-c7f8fbee3272.png)

                 
                  



    
PART 2 :

1.Software architecture in python :
