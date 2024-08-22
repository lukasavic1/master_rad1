import json
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import math

def read_json(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)

def create_comparison_chart(data_1, data_2, labels_1, labels_2, keys, title_suffix):
    sns.set(style="whitegrid")
    num_columns = len(keys)  # Number of columns is equal to the number of keys
    fig, axs = plt.subplots(1, num_columns, figsize=(15, 5))
    fig.suptitle(f'Uporedjivanje RAFT i Paxos algoritama - {title_suffix}', fontsize=16)

    for i, key in enumerate(keys):
        if key in data_1 and key in data_2:
            ax = axs[i] if num_columns > 1 else axs  # Handle single subplot case
            # Special handling for "dir_size" to rename axis label
            display_key = key if key != "dir_size" else "dir_size [MB]"
            sns.barplot(x=[labels_1, labels_2], y=[data_1[key], data_2[key]], ax=ax, palette="muted")
            ax.set_title(display_key.replace('_', ' ').capitalize(), fontsize=12)
            ax.set_xlabel("")
            ax.set_ylabel("")
        else:
            axs[i].remove()  # Remove empty axes

    # Remove any unused subplots
    for j in range(len(keys), num_columns):
        axs[j].remove()

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()

if __name__ == "__main__":

    tests = [
        ("perf/perf_stats_test1_Paxos.json", "perf/perf_stats_test1_RAFT.json"),
        ("perf/perf_stats_test2_Paxos.json", "perf/perf_stats_test2_RAFT.json"),
        ("perf/perf_stats_test3_Paxos.json", "perf/perf_stats_test3_RAFT.json")
    ]
    for test in tests:
        file_1, file_2 = test
        data_1 = read_json(file_1)
        data_2 = read_json(file_2)

        # Define keys for latency and other metrics
        latency_keys = ["min_op_latency", "max_op_latency", "avg_op_latency"]
        other_keys = ["startup_time", "total_time", "dir_size [MB]", "consistency_check_time"]

        # Create comparison charts
        create_comparison_chart(data_1, data_2, "Paxos", "RAFT", latency_keys, "Metrike latencije operacija")
        create_comparison_chart(data_1, data_2, "Paxos", "RAFT", other_keys, "Metrike sistema")
