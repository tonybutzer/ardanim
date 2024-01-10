cat:
	cat Makefile

stwohour:
	salloc -N 1 -n 1 -c 4 -A impd -t 2:00:00

shell:
	srun --pty bash -i


run:
	./run_local.sh


publish:
	(cd ~/opt/lcnext_plan_proto; make publish)
