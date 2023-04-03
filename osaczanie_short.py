#!/usr/bin/env python
# coding: utf-8

# In[19]:


# funkcja osaczanie_short() to przykład implementacji metody "krótszych przedziałów"
# funkcja osaczanie_short() przyjmuje 3 argumenty
# function ==> funkcja, której pierwiastek chcemy znaleźć
# init_value ==> punkt startowy
# step ==> długość kolejnych przedziałów

# iterujemy dopóki funkcja w punkcie startowym i krańcach lewego i prawego przedziału nie zmienia znaku
# jeśli funkcja w punkcie startowym i na krańcu któregoś z przedziałów zmieni znak, to wybierz ten przedział, na którego krańcu funkcja zmienia znak
# zwróć kraniec tego przedziału oraz kraniec tego przedziału pomniejszony lub powiększony o step

# dodatkowo funkcja zlicza nam liczbę iteracji oraz podaje jakość oszacowania wyrażoną długością przedziału


# In[20]:


def example_function(x):
    return x + 10


# In[21]:


def osaczanie_short(function, init_value, step):
    
    upstream = function(init_value + step)
    downstream = function(init_value - step)
    startpoint = function(init_value)
    
    step_length = step
    counter = 0

    while upstream*startpoint and downstream*startpoint >= 0:
        
        
        step = step + step_length
        upstream = function(init_value + step)
        downstream = function(init_value - step)
        
        counter = counter + 1
        
        print('f(',init_value+step,')','=',upstream,"-----",'f(',init_value-step,')','=', downstream)
        
    else:
        print('___________________________________________________________________')
        if upstream*startpoint <= 0:
            
            
            return 'the root is between:', init_value + step, 'and', (init_value + step) - step_length, 'number of iterations:', counter + 1, 'resolution:', step_length
        
        elif downstream*startpoint <= 0:
            
            
            return 'the root is between:', init_value - step, 'and', (init_value - step) + step_length , 'number of iterations:', counter + 1, 'resolution:', step_length
        


# In[22]:


print(osaczanie_short(function=example_function, init_value=1200, step = 1))


# In[ ]:




