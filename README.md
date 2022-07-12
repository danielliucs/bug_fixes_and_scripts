# bugFixes


For libgomp: Thread creation failed: Resource temporarily unavailable (export OMP_NUM_THREADS=1)

https://stackoverflow.com/questions/53351194/openmp-libgomp-thread-creation-failed-resource-temporarily-unavailable-when

For ERROR: GLEW Initialization error: Unknown error

Has yet to be resolved https://stackoverflow.com/questions/72207148/glew-initialization-error-focusing-a-window-requires-user-interaction

Temporary fix by commenting out env.render()


For GLIBCXX_3.4.29 not found

https://stackoverflow.com/questions/72205522/glibcxx-3-4-29-not-found



Tuple index out of range when sampling environment

https://github.com/openai/spinningup/issues/157

## Python ReadME
For the seeds_avg_and_plot_rewards.py file:\
*To make it support more experiments/tasks/seeds, all you would need to do is change the seeds, experiments, target_files, exp_tasks_names, and file_tasks_names list
