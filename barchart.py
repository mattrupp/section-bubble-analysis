# Plot Colors bar chart
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from haas_section import color as c

def barchart(feature, df, df_owb=pd.DataFrame(), df_swb=pd.DataFrame(), part_dict={}, min_percentage=0):
    # Create a sample Series
    all_data = df.value_counts(feature)
    all_df = pd.DataFrame(all_data)
    all_df['Percentage'] = (all_df['count']/all_df['count'].sum()) * 100
    all_df['Data'] = 'All Orders'

    valid_dfs = [all_df]

    if feature in df_owb.columns:
        bubble_order_data = df_owb.value_counts(feature)
        bubble_order_df = pd.DataFrame(bubble_order_data)
        bubble_order_df['Percentage'] = (bubble_order_df['count']/bubble_order_df['count'].sum()) * 100
        bubble_order_df['Data'] = 'Bubble Orders'
        valid_dfs.append(bubble_order_df)

    if feature in df_swb.columns:
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

    if sort_list:
        sns.barplot(x=feature, y='Percentage',hue='Data', data=dss_filtered, ax=ax, order=sort_list)
    else:
        sns.barplot(x=feature, y='Percentage',hue='Data', data=dss_filtered, ax=ax)
         
    # Customize the chart
    plt.title(f'{feature} by Percentage')
    plt.xticks(rotation=90)
    plt.xlabel(feature)
    plt.ylabel("Percentage")

    print(f'Index Count: {len(dss_filtered.index.unique())}')

    if len(dss_filtered.index.unique()) > 55:
         plt.xticks(range(0, len(dss_filtered.index.unique()), 15))

    # Show the chart
    plt.show()