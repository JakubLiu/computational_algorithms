#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# funkcja osaczanie_long() to przykład implementacji metody "dłuższych przedziałów"
# funkcja osaczanie_long() przyjmuje 3 argumenty
# function ==> funkcja, której pierwiastka szukamy
# init_value ==> miejsce startowe
# step ==> początkowa długość przedziału

# iterujemy dopóki funkcja nie zmienia znaku w miejscu startowym oraz na krańcach lewego i prawego przedziału
# w każdej iteracji długość przedziału rośnie dwukrotnie
# jeśli na którymś z dwóch przedziałów funkcja zmieni znak, to wybierz ten przedział, w którym to się dzieje

# dodatkowo funkcja wypisuje liczbę iteracji oraz jakość oszacowania wyrażoną jako długość przedziału


# In[24]:


def example_function(x):
    return x + 10


# In[45]:


def osaczanie_long(function, init_value, step):
    
    upstream = function(init_value + step)
    downstream = function(init_value - step)
    startpoint = function(init_value)
    counter = 0
    
    while upstream*startpoint and downstream*startpoint > 0:
        
        step = 2*step
        counter = counter + 1
        upstream = function(init_value + step)
        downstream = function(init_value - step)
        
        print('f(',init_value+step,')','=',upstream,"-----",'f(',init_value-step,')','=', downstream)
    else:
        print('___________________________________________________________________')
        if upstream*startpoint < 0:
            
            resolution = abs((init_value + step) - init_value)
            return 'the root is between', init_value + step, 'and', init_value, 'number of iterations:', counter + 1, 'resolution:', resolution
        
        elif downstream*startpoint < 0:
            
            resolution = abs((init_value - step) - init_value)
            return 'the root is between', init_value - step, 'and', init_value, 'number of iterations:', counter + 1, 'resolution:', resolution


# In[46]:


print(osaczanie_long(function=example_function, init_value=1200, step = 1))


# In[ ]:




