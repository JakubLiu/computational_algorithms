#!/usr/bin/env python
# coding: utf-8

# In[5]:


# pierwotna postać funkcji, chcemy znaleźć jej pierwiastek

def original_function(x):
    return 0.3 * x ** 2 - 2


# In[6]:


# zmodyfikowana wersja poprzedniej funkcji, chcemy znaleźć jej punkt stacjonarny
# punkt stacjonarny tej funckji będzie miejscem zerowym pierwotnej funkcji

def modified_function(x):
    return -original_function(x) + x


# In[7]:


# argumenty: funkcja, której punkt stacjonarny chcemy znaleźć, wartość startowa (x0), maksymalny dopuszczalny błąd oszacowania
# z każdym obrotem pętli funkcja wypisuje nam: wartość funkcji w tej iteracji oraz różnice wartości |f(Xn+1) - f(Xn)|
# funkcja zwraca nam wartość funkcji, w momencie gdy osiągnięty zostanie (od góry) nasz maksymalny dopuszczalny błąd oszacowania
# dodatkowo funkcja zwraca także liczbę iteracji, co może mieć zastosowanie w diagnostyce działania funckji


# In[10]:


def fixed_point_iteration(function, init_value, acceptable_error):
    
    
    error = acceptable_error*10
    
    counter = 0
    
    while error > acceptable_error:
        
        output = function(init_value)
        
        new_input = function(output)
            
        init_value = new_input
            
        error = abs(function(output) - function(init_value))

        counter = counter + 1
        
        print('function value:',function(init_value),"     ", "margin of error:", error, "   ", "iteration:", counter)
    print("___________________________________________________________________________")
    print("___________________________________________________________________________")
    return "final function value: ", output, "number of iterations: ", counter + 1


# In[11]:


print(fixed_point_iteration(function = modified_function, init_value = 4000, acceptable_error = 10e-16))


# In[ ]:




