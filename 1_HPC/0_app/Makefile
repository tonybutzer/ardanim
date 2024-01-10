cat:
	cat Makefile

salloc:
	salloc -N 1 -n 1 -c 4 -A impd -t 1:00:00

stwohour:
	salloc -N 1 -n 1 -c 4 -A impd -t 2:00:00

shell:
	srun --pty bash -i



run:
	python hpc_test_animate_true_color.py 20_10_2022
	python hpc_test_animate_true_color.py 16_07_2022


source:
	echo source /home/ec2-user/mambaforge/bin/activate card
