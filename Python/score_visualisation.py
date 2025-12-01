import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
import sys
import os

# Configuration for plot aesthetics
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)

def load_scores(filepath):
    """Loads NDJSON (Newline Delimited JSON) file."""
    data = []
    try:
        with open(filepath, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        data.append(json.loads(line))
                    except json.JSONDecodeError as e:
                        print(f"Skipping invalid JSON line: {e}")
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)
    
    if not data:
        print("No data found in file.")
        sys.exit(1)
        
    df = pd.DataFrame(data)
    
    # Ensure Prompt_Strategy column exists, default to 'Unknown' if missing
    if 'Prompt_Strategy' not in df.columns:
        df['Prompt_Strategy'] = 'Unknown'
        
    return df

def plot_strategy_comparison(df, output_dir):
    """Generates box plots comparing metrics across different strategies."""
    # Melt dataframe for seaborn boxplot format
    melted_df = df.melt(
        id_vars=['Prompt_Strategy'], 
        value_vars=['Mutation_Score', 'Hallucination_Score', 'Correctness_Score'],
        var_name='Metric', 
        value_name='Score'
    )
    
    plt.figure(figsize=(14, 8))
    sns.boxplot(x='Metric', y='Score', hue='Prompt_Strategy', data=melted_df, palette='Set2')
    
    plt.title('Performance Comparison: Naive vs CoT vs FewShot')
    plt.ylabel('Score (0.0 - 1.0)')
    plt.xlabel('Metric')
    plt.legend(title='Strategy', bbox_to_anchor=(1.05, 1), loc='upper left')
    
    plt.tight_layout()
    save_path = os.path.join(output_dir, 'strategy_comparison_boxplot.png')
    plt.savefig(save_path)
    print(f"Generated '{save_path}'")
    plt.close()

def plot_pairplot_by_strategy(df, output_dir):
    """Generates a scatter matrix colored by Prompt Strategy."""
    cols = ['Mutation_Score', 'Hallucination_Score', 'Correctness_Score', 'Prompt_Strategy']
    # Filter only existing columns
    cols = [c for c in cols if c in df.columns]
    
    pair_plot = sns.pairplot(df[cols], hue='Prompt_Strategy', palette='Set2', diag_kind='kde')
    pair_plot.fig.suptitle('Pairwise Relationships by Strategy', y=1.02)
    
    save_path = os.path.join(output_dir, 'pair_plot_strategy.png')
    plt.savefig(save_path)
    print(f"Generated '{save_path}'")
    plt.close()

def plot_3d_scatter_strategy(df, output_dir):
    """Generates a 3D scatter plot colored by Strategy."""
    cols = ['Mutation_Score', 'Hallucination_Score', 'Correctness_Score']
    if not all(c in df.columns for c in cols):
        return

    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')

    # Map strategies to colors manually for consistent legend
    strategies = df['Prompt_Strategy'].unique()
    colors = sns.color_palette('Set2', n_colors=len(strategies))
    strategy_color_map = dict(zip(strategies, colors))

    for strategy in strategies:
        subset = df[df['Prompt_Strategy'] == strategy]
        ax.scatter(
            subset['Mutation_Score'], 
            subset['Hallucination_Score'], 
            subset['Correctness_Score'],
            c=[strategy_color_map[strategy]],
            label=strategy,
            s=60, 
            edgecolor='w'
        )

    ax.set_xlabel('Mutation Score')
    ax.set_ylabel('Hallucination Score')
    ax.set_zlabel('Correctness Score')
    ax.set_title('3D View of Scores by Strategy')
    ax.legend(title="Prompt Strategy")

    save_path = os.path.join(output_dir, '3d_scatter_strategy.png')
    plt.savefig(save_path)
    print(f"Generated '{save_path}'")
    plt.close()

def print_summary_stats(df):
    """Prints a statistical summary table to console."""
    print("\n" + "="*50)
    print("AVERAGE SCORES BY STRATEGY")
    print("="*50)
    
    # Group by strategy and calculate mean
    summary = df.groupby('Prompt_Strategy')[
        ['Mutation_Score', 'Hallucination_Score', 'Correctness_Score']
    ].mean()
    
    print(summary)
    print("-" * 50)
    
    # Calculate counts to see sample sizes
    counts = df['Prompt_Strategy'].value_counts()
    print("\nSample Counts per Strategy:")
    print(counts)
    print("="*50 + "\n")

def main():
    filename = './Data/scores.json'
    output_dir = './Data'
    
    if not os.path.exists(filename):
        print(f"File '{filename}' not found in current directory.")
        return

    # Create output directory for pictures
    os.makedirs(output_dir, exist_ok=True)
    print(f"Images will be stored in directory: {os.path.abspath(output_dir)}")

    print("Loading data...")
    df = load_scores(filename)
    
    # Print numerical analysis
    print_summary_stats(df)

    print("Generating plots...")
    plot_strategy_comparison(df, output_dir)
    plot_pairplot_by_strategy(df, output_dir)
    plot_3d_scatter_strategy(df, output_dir)
    
    print(f"Visualization complete. Check the '{output_dir}' folder.")

if __name__ == "__main__":
    main()