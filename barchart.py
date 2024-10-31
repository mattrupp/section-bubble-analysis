# Plot Colors bar chart
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from haas_section import color as c

def barchart(feature, df, df_owb, df_swb, part_dict={}, min_percentage=0):
    # Create a sample Series
    all_data = df.value_counts(feature)
    all_df = pd.DataFrame(all_data)
    all_df['Percentage'] = (all_df['count']/all_df['count'].sum()) * 100
    all_df['Data'] = 'All Orders'

    bubble_order_data = df_owb.value_counts(feature)
    bubble_order_df = pd.DataFrame(bubble_order_data)
    bubble_order_df['Percentage'] = (bubble_order_df['count']/bubble_order_df['count'].sum()) * 100
    bubble_order_df['Data'] = 'Bubble Orders'

    bubble_section_data = df_swb.value_counts(feature)
    bubble_section_df = pd.DataFrame(bubble_section_data)
    bubble_section_df['Percentage'] = (bubble_section_df['count']/bubble_section_df['count'].sum()) * 100
    bubble_section_df['Data'] = 'Bubble Sections'

    dss = pd.concat([all_df, bubble_order_df, bubble_section_df])
    dss.reset_index(drop=True)

    # Replace the part letter with description
    dss.rename(index=part_dict, inplace=True)

    # Filter the DataFrame
    dss_filtered = dss[dss['Percentage'] >= min_percentage]

    # Remove unused headings
    headings = dss_filtered.head().index.values.tolist()
    descriptive_name = list(part_dict.values())
    common_list = list(set(headings).intersection(set(descriptive_name)))
  

    # # Create the bar chart
    fig, ax = plt.subplots(figsize=(14, 5))
    sns.barplot(x=feature, y='Percentage',hue='Data', data=dss_filtered, ax=ax)

    # Customize the chart
    plt.title(f'{feature} by Percentage')
    plt.xticks(rotation=90)
    plt.xlabel(feature)
    plt.ylabel("Percentage")

    # Show the chart
    plt.show()