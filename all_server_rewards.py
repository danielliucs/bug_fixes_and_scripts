import pandas as pd

def consolidate_n_files(folder, file, seeds, num_tasks):

    #initial read path
    csv_read_path = f'{folder}{seeds[0]}/{file}.csv'
    print(csv_read_path)
    csv_save_path = f'{file}_ALL.csv'
    col_names = []

    for i in range(len(seeds)):
        col_names.append(i)

    rewards_csv_all = pd.read_csv(csv_read_path, names=col_names)

    for i in range(1, len(seeds)):
        csv_read_path = f'{folder}{seeds[i]}/{file}.csv'
        print(csv_read_path)

        new_rewards = pd.read_csv(csv_read_path, names=col_names)

        tasks_counter = 0
        while tasks_counter < num_tasks:
            rewards_csv_all[i*num_tasks+tasks_counter] = new_rewards.iloc[:,tasks_counter]
            tasks_counter += 1

    rewards_csv_all.to_csv(csv_save_path, index=False, header=None)


if __name__ == '__main__':
    """Make sure the folder name at index i matches with the file name at index i"""
    results_folders = ["results_fed_avg_seed_", "results_fisher_aggregate_seed_"]
    file_names = ["A2C_RL_SERVER_FED_AVG",  "A2C_RL_SERVER_PERCENTILE_AGGREGATE"]
    seeds = [5, 10, 15]
    NUM_TASKS = 3
    
    for i in range(len(file_names)):
        consolidate_n_files(results_folders[i], file_names[i], seeds, NUM_TASKS)
