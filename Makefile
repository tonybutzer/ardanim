cat:
	cat Makefile


publish:
	git add .
	git commit -m "auto commit from make - aug2023"
	git push

git: publish


big:
	find . -size +20M
