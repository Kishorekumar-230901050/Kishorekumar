#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
info =pd.DataFrame([[3,9]]*4,columns=['S','R'])
print(info)
print(info.apply(np.sum,axis=0))
print(info.apply(np.sum,axis=1))
print(info.apply(np.sqrt))


# In[8]:


import pandas as pd
import numpy as np
a=pd.DataFrame([[2,4,6],[1,3,5],[5,8,7]],columns=['X',"Y",'Z'])
print(a)
print(a.agg(['min','max']))


# In[4]:


d2=pd.DataFrame([["Sai",88],["Sanjai",70]],columns=['Name','Id'])
print(d2)
d2['Age']=[20,18]                 
print("\n",d2)
d2["Sex"]=['Male','Male']
print("\n",d2)


# In[5]:


d2=pd.DataFrame([["Sai",88],["Sanjai",70]],columns=['Name','Id'])
a=d2.assign(age=[20,18])
print(a)


# In[6]:


import numpy as np
import pandas as pd
info=pd.DataFrame(np.random.randn(5,2),index=[3,2,0,4,1],columns=["3rd","4th"])
print(info)
a=info.sort_index()
print(a)
b=a.sort_values(by='3rd')
print(b)



# In[7]:


import pandas as pd
import numpy as np
left =pd.DataFrame({'id':[1,2,3,4],'Name':['Sai','Poo','Saba','Yuvi'],'Sub':['Sub1','Sub2','Sub4','Sub3']})
right=pd.DataFrame({'id':[1,2,3,4],'Name':['Sanjay','Saran','Som','Ruba'],'Sub':['Sub2','Sub4','Sub3','Sub5']})
print(left)
print(right)
print(pd.merge(left,right,on="id"))


# In[ ]:




