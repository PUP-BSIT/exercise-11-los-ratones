import pandas as pd

def basic_calculations():
    df = pd.DataFrame({"Numbers": [10, 20, 30, 40, 50]})
    
    total = df["Numbers"].sum()      
    average = df["Numbers"].mean()   
    highest = df["Numbers"].max()    
    
    return f"""
    Sum: {total}
    Average: {average}
    Highest: {highest}
    """