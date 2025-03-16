import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_value_counts(df, column_name):
    """
    输入一个DataFrame和需要统计的列名，输出该列内容数量统计的条形图。

    参数:
    df (pd.DataFrame): 输入的数据框
    column_name (str): 需要统计的列名

    返回:
    None: 显示生成的条形图
    """
    # 检查列是否存在
    if column_name not in df.columns:
        raise ValueError(f"列 '{column_name}' 不存在于数据框中")

    # 统计每个类别的数量并升序排列（横轴）
    value_counts = df[column_name].value_counts().sort_index()
    # value_counts = df[column_name].value_counts().sort_index(ascending=False) # 用于倒序排列

    # 创建条形图
    plt.figure(figsize=(10, 6))
    sns.barplot(x=value_counts.index, y=value_counts.values, palette="viridis")

    plt.title(f'{column_name} ')
    plt.xlabel(column_name)
    plt.ylabel('数量')

    # 旋转x轴标签以避免重叠
    plt.xticks(rotation=45, ha='right')

    # 显示图表
    plt.tight_layout()
    plt.show()