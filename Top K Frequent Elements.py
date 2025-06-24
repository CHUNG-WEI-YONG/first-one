from collections import Counter
def Top_K_Frequent_Elements(n , p):
    counted = Counter(p)
    if len(p)==1:
        return(num[0])
    result = [num for num,freq in counted.most_common(n)]
    return result
   
        
        
    
