# Plot Colors bar chart
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from haas_section import color as c

def lineplot(feature, df, df_owb=pd.DataFrame(), df_swb=pd.DataFrame(), filter={}, part_dict={}, min_percentage=0, xticks=1):
    # Create a sample Series
    if filter:
         for k,v in filter.items():
              df = df[df[k] == v]
    all_data = df.value_counts(feature)
    all_df = pd.DataFrame(all_data)
    all_df['Percentage'] = (all_df['count']/all_df['count'].sum()) * 100
    all_df['Data'] = 'All Orders'
    avg_df = np.mean(all_df['Percentage'])

    valid_dfs = [all_df]

    if feature in df_owb.columns:
        if filter:
            for k,v in filter.items():
                 df_owb = df_owb[df_owb[k] == v]
        bubble_order_data = df_owb.value_counts(feature)
        bubble_order_df = pd.DataFrame(bubble_order_data)
        bubble_order_df['Percentage'] = (bubble_order_df['count']/bubble_order_df['count'].sum()) * 100
        bubble_order_df['Data'] = 'Bubble Orders'
        valid_dfs.append(bubble_order_df)

    if feature in df_swb.columns:
        if filter:
            for k,v in filter.items():
                 df_swb = df_swb[df_swb[k] == v]
        bubble_section_data = df_swb.value_counts(feature)
        bubble_section_df = pd.DataFrame(bubble_section_data)
        bubble_section_df['Percentage'] = (bubble_section_df['count']/bubble_section_df['count'].sum()) * 100
        bubble_section_df['Data'] = 'Bubble Sections'
        valid_dfs.append(bubble_section_df)

    dss = pd.concat(valid_dfs)

    sort_list = []
    if len(part_dict):
        # Replace the part letter with description
        dss.rename(index=part_dict, inplace=True)

        dss_index_values = dss.index.to_list()
        part_dict_values = list(part_dict.values())
        for item in part_dict_values:
                if item in dss_index_values:
                    sort_list.append(item)

    # Filter the DataFrame
    dss_filtered = dss[dss['Percentage'] >= min_percentage]

    # Create the bar chart
    fig, ax = plt.subplots(figsize=(20, 5))

    sns.lineplot(x=feature, y='Percentage',hue='Data', data=dss_filtered, ax=ax)

    filter_text = ''
    if filter:
        for k,v in filter.items():
            filter_text += ', ' + str(k) + " = " + str(v)
         
    # Customize the chart
    plt.title(f'{feature} by Percentage{filter_text}')
    plt.xticks(rotation=90)
    plt.xlabel(feature)
    plt.ylabel("Percentage")
    plt.axhline(y=avg_df, color='r', linestyle='--')

    # Eliminate some of the x-axis labels
    if xticks > 1:
        plt.xticks(range(0, len(dss_filtered.index.unique()), xticks))

    # Show the chart
    plt.show()