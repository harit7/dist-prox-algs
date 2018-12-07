from __future__ import division
import numpy as np

def soft_max(x): 
    if x>0:
        return x
    else:
        return 0

#def soft_threshold(k,a):
 #   return soft_max(a-k) - soft_max(-a-k)

# S_k(v)
def sign(x):
    if x>0:
        return 1
    elif(x<0):
        return -1
    else:
        return 0
def mod(x):
    if x>0:
        return x
    else:
        return -x
    
def soft_threshold_scalar(k,v):
    if mod(v)>k:
        return v-k*sign(v)
    else:
        return 0
    
def soft_threshold(k,v):
    out = np.copy(v)
    for i in range(0,len(v)):
        out[i] = soft_threshold_scalar(k,v[i])
    #print "soft :"+str(out)
    return out

def proc_point(x):
    return int(x*1000000)/10000.0
# last dimension is set to all 1s for the bias term in w
def genSynthDataSet(n=100,d=2,fun=None,outputFilePath=None):
    
    np.random.seed(2)
    A         = np.random.rand(n,d+1)*100 # scale
    n,m       = A.shape
    A[:,m-2]  = 1
    w         = np.random.rand(d)
    if(fun==None):
        print w
        A[:,m-1]  = map(lambda x: np.dot(w,x), A[:,range(0,m-1)])
    else:
        
        A[:,m-1]  = map(fun, A[:,range(0,m-1)])
    
    A = np.around(A, decimals=4)
    
    if(outputFilePath!=None):
        np.savetxt(outputFilePath,A,delimiter=",")
    else:
        return A

def generate_class_data(n=10,d=3):
    
    np.random.seed(2)
    
    DENSITY   = 0.2
    w         = np.random.randn(d)
    idxs      = np.random.choice(range(d), int((1-DENSITY)*d), replace=False)
    for i in idxs:
        w[i]  = 0
        
    offset    = 0
    sigma     = 0.5
    X         = np.random.normal(0, 5, size=(n,d+1))
    
    X[:,d-1]  = 1
    
    X[:,d]    = np.sign(np.dot(X[:,range(d)],w) + offset + np.random.normal(0,sigma,size =n))
    return w,X

    