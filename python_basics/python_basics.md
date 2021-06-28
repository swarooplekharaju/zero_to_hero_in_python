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

                       
                              
                              



    
PART 2 :

1.Software architecture in python :
