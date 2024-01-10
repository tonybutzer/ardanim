#!/bin/sh

# We assume running this from the script directory
job_directory=$PWD/.job
#data_dir="${SCRATCH}/project/LizardLips"

lizards=("14_05_2022" "14_06_2022" "15_05_2022" "15_06_2022")

yr=2022
for h in {14..20}; do 
	for vt in {8..13} ; do 
		v=$(echo $vt | awk '{printf("%02d", $1)}')
		lizard=${h}_${v}_$yr

#for lizard in ${lizards[@]}; do

    job_file="${job_directory}/${lizard}.job"

    echo "#!/bin/bash
#SBATCH --account=butzer
#SBATCH --time=00:20:00
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -c 1
#SBATCH --mail-type=ALL
#SBATCH --mail-user=butzer@contractor.usgs.gov
#SBATCH --job-name=${lizard}.job
#SBATCH --output=.out/${lizard}.out
#SBATCH --error=.out/${lizard}.err
source /home/ec2-user/mambaforge/bin/activate card
## source /home/ec2-user/tony/source_conda.src
## source /home/butzer/miniconda3/bin/activate nlcd2
python3 anim.py ${lizard}" > $job_file
    sbatch $job_file

	done
done
