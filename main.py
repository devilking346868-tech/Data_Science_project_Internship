import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

df = pd.read_csv('Diwali Sales Data.csv', encoding='unicode_escape')
df.drop(['Status', 'unnamed1'], axis=1, inplace=True)
df.dropna(inplace=True)
df['Amount'] = df['Amount'].astype('int')


def add_labels(ax, labels=None, fmt='%.0f', fontsize=10):
    for c in ax.containers:
        if c is None:
            continue
        if labels and len(labels) == len(c):
            ax.bar_label(c, labels=labels, fontsize=fontsize, fontweight='bold')
        else:
            ax.bar_label(c, fmt=fmt, fontsize=fontsize, fontweight='bold')


# GRAPH 1: Gender + Age Group
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

ax = sns.countplot(x='Gender', data=df, hue='Gender', palette='Set2', legend=False, ax=axes[0])
add_labels(ax, labels=['Female', 'Male'], fontsize=11)
axes[0].set_title('Buyers by Gender', fontsize=14, fontweight='bold')

ax = sns.countplot(data=df, x='Age Group', hue='Gender', palette='Set2', ax=axes[1])
add_labels(ax, fontsize=9)
axes[1].set_title('Buyers by Age Group & Gender', fontsize=14, fontweight='bold')
axes[1].legend(title='Gender')

plt.tight_layout()
plt.show()


# GRAPH 2: Top 10 States by Sales
sales_state = df.groupby('State', as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
plt.figure(figsize=(14, 6))
ax = sns.barplot(data=sales_state, x='State', y='Amount', hue='State', palette='viridis', legend=False)
add_labels(ax)
plt.title('Top 10 States by Sales Amount', fontsize=15, fontweight='bold')
plt.xticks(rotation=30, ha='right')
plt.tight_layout()
plt.show()


# GRAPH 3: Top 10 Product Categories by Sales
sales_cat = df.groupby('Product_Category', as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
plt.figure(figsize=(14, 6))
ax = sns.barplot(data=sales_cat, x='Product_Category', y='Amount', hue='Product_Category', palette='Set3', legend=False)
add_labels(ax, fontsize=9)
plt.title('Top 10 Product Categories by Sales', fontsize=15, fontweight='bold')
plt.xticks(rotation=35, ha='right')
plt.tight_layout()
plt.show()