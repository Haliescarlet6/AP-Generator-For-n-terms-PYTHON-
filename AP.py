#!/usr/bin/env python
# coding: utf-8

# In[2]:


First_term = int(input("Enter the first term of your AP : "))
Common_difference = int(input("Enter the common difference of the AP : "))
Term_number = int(input("Enter the number of terms required : "))
AP_list = []
for i in range(0,Term_number+1):
    Next_term = First_term + (Common_difference * i)
    AP_list.append(Next_term)
    
    
AP = ', '.join(map(str,AP_list)) #Converts list to strings(IMP)
print()
print("The AP with",Term_number,"term is : ",AP)


# In[ ]:




