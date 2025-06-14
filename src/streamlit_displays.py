import streamlit as st
import pandas as pd


##############################
# stats in dataframe
##############################

def  display_tab(tab, metric='deltaonset'):
    precision=4
    st.header(f"metric: {metric}")
    tab_results = pd.DataFrame.from_dict(tab)
    
    keys = list(tab.keys())
    #st.write(keys)
    res=""
    for k in keys:
        s = str(round(tab[k][1]*100,2)) + " ± " + str(round(tab[k][7]*100,2)) + " & "
        res+= s
    #st.write(res)    
        
    
    tab_results.iloc[0] = tab_results.iloc[0].round(0)  # integers for the first line (N _elements)
    tab_results.iloc[1:] = tab_results.iloc[1:].round(precision)
    tab_results.index=['N_elements', 'mean', 'q1', 'median', 'q3', 'mini', 'maxi', 'stddev']
    
    if metric == 'ioiratios': 
        labove, rabove = 1.02, 1.9
        lbelow, rbelow = 0.7, 0.9
    else:
        labove, rabove = 0.01, 0.1
        lbelow, rbelow = (-0.01, -0.1) # pb negative number for highlight
    
    st.dataframe(tab_results.style.format(lambda x: "{:.0f}".format(x) if x == round(x) else "{:.4f}".format(x))
                                    .highlight_between(subset=(slice("median","median"), tab_results.columns),
                                                       left=labove, right=rabove, color="lightgreen")
                                    .highlight_between(subset=(slice("median","median"), tab_results.columns),
                                                       left=lbelow, right=rbelow, color="lightpink"))