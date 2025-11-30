import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
import sys
import os

# Configuration for plot aesthetics
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

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
        
    return pd.DataFrame(data)

def plot_distributions(df, output_dir):
    """Generates histograms for each score type."""
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    
    score_types = ['Mutation_Score', 'Hallucination_Score', 'Correctness_Score']
    colors = ['#1f77b4', '#d62728', '#2ca02c'] # Blue, Red, Green
    
    for ax, col, color in zip(axes, score_types, colors):
        if col in df.columns:
            sns.histplot(df[col], bins=10, kde=True, ax=ax, color=color)
            ax.set_title(f'Distribution of {col.replace("_", " ")}')
            ax.set_xlabel('Score (0.0 - 1.0)')
            ax.set_ylabel('Count')
            
            # Add mean line
            mean_val = df[col].mean()
            ax.axvline(mean_val, color='k', linestyle='--', label=f'Mean: {mean_val:.2f}')
            ax.legend()
            
    plt.tight_layout()
    save_path = os.path.join(output_dir, 'distribution_plots.png')
    plt.savefig(save_path)
    print(f"Generated '{save_path}'")
    plt.close()

def plot_correlations(df, output_dir):
    """Generates a heatmap of correlations."""
    cols = ['Mutation_Score', 'Hallucination_Score', 'Correctness_Score']
    # Filter only existing columns
    cols = [c for c in cols if c in df.columns]
    
    if len(cols) < 2:
        return

    plt.figure(figsize=(8, 6))
    corr = df[cols].corr()
    
    sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1, center=0, fmt='.2f')
    plt.title('Correlation Matrix of Scores')
    plt.tight_layout()
    save_path = os.path.join(output_dir, 'correlation_heatmap.png')
    plt.savefig(save_path)
    print(f"Generated '{save_path}'")
    plt.close()

def plot_pairplot(df, output_dir):
    """Generates a scatter matrix."""
    cols = ['Mutation_Score', 'Hallucination_Score', 'Correctness_Score']
    cols = [c for c in cols if c in df.columns]
    
    # Add a 'Cluster' column based on Correctness for coloring if it helps visualization
    plot_df = df[cols].copy()
    plot_df['Outcome'] = plot_df['Correctness_Score'].apply(lambda x: 'High' if x > 0.8 else ('Low' if x < 0.2 else 'Med'))
    
    pair_plot = sns.pairplot(plot_df, hue='Outcome', palette='viridis', diag_kind='kde')
    pair_plot.fig.suptitle('Pairwise Relationships between Scores', y=1.02)
    
    save_path = os.path.join(output_dir, 'pair_plot.png')
    plt.savefig(save_path)
    print(f"Generated '{save_path}'")
    plt.close()

def plot_3d_scatter(df, output_dir):
    """Generates a 3D scatter plot."""
    cols = ['Mutation_Score', 'Hallucination_Score', 'Correctness_Score']
    if not all(c in df.columns for c in cols):
        return

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Color by Correctness
    sc = ax.scatter(
        df['Mutation_Score'], 
        df['Hallucination_Score'], 
        df['Correctness_Score'],
        c=df['Correctness_Score'], 
        cmap='viridis',
        s=60, 
        edgecolor='w'
    )

    ax.set_xlabel('Mutation Score')
    ax.set_ylabel('Hallucination Score')
    ax.set_zlabel('Correctness Score')
    ax.set_title('3D View of Scores')
    
    cbar = plt.colorbar(sc, ax=ax, shrink=0.5, aspect=5)
    cbar.set_label('Correctness Score')

    save_path = os.path.join(output_dir, '3d_scatter.png')
    plt.savefig(save_path)
    print(f"Generated '{save_path}'")
    plt.close()

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
    
    print("-" * 30)
    print("Data Summary:")
    print("-" * 30)
    print(df[['Mutation_Score', 'Hallucination_Score', 'Correctness_Score']].describe())
    print("-" * 30)

    print("Generating plots...")
    plot_distributions(df, output_dir)
    plot_correlations(df, output_dir)
    plot_pairplot(df, output_dir)
    plot_3d_scatter(df, output_dir)
    
    print(f"\nVisualization complete. Check the '{output_dir}' folder.")

if __name__ == "__main__":
    main()