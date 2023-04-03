#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# można dodać jeszcze pętlę while i iterować aż | 0 - fun(root estimation) | < threshold


# In[61]:


def function(x):
    
    return x - 500
# root = 500


# In[62]:


def bisection(fun, a, b, num_of_iterations):
    
    
    
    
    
    
    if fun(a)*fun(b) > 0:                          # if there is no root between a and b
        
        
        return "choose different interval"
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    else:                                         # if there is a root between a and b
        
        c = (a+b)/2    # let c be between a and b
        counter = 0    # count the number of iterations (just for fun)
        
        
        
        
        
        
        
        
        
        
        
        if fun(a)*fun(c) < 0: # if the root is between a and c
            
            
             
                
                
            for i in range(1, num_of_iterations + 1):
                
                d = (a+c)/2   # let d be between a and c
                holder = d
                
                
                if fun(a)*fun(d) < 0:   # if the root is between a and d
                    c = holder
                elif fun(c)*fun(d) < 0: # if the root is between c and d
                    a = holder
                    
                    
                counter = counter + 1
                
            
            return 'root estimation:',c, 'fun(root estimation): ', fun(c), 'number of iterations: ',  counter
        
        
        
        
        
            
        elif fun(b)*fun(c) < 0: # if the root is between b and c
                
            for i in range(i, iterat + 1):
                
                d = (b+c)/2   # let d be between b and c
                holder = d
                
                
                if fun(b)*fun(d) < 0:  # if the root is between b and d
                    c = holder
                elif fun(c)*fun(d) < 0: # if the root is between c and d
                    b = holder
                    
                    
                counter = counter + 1
                    
            
            return 'root estimation:',c, 'fun(root estimation): ', fun(c), 'number of iterations: ',  counter
            
            


# In[66]:


print(bisection(fun = function, a = 5, b = 2000, num_of_iterations = 20))      # miejsce zerowe, wartość w miejscu zerowym (zero), liczba iteracji


# In[ ]:




