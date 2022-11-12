from cbs import cbs_main
from make import make_input
import matplotlib.pyplot as plt
import time
import numpy as np

maps = ['arena','orz107d','lak105d']
agents = [2, 3, 4, 5, 6, 7]

for map in maps:
	cbs_score = []
	cbs_times = []
	for agent in agents:
		cbs = 0
		cbs_time = []
		for i in range(10):
			make_input(map,'input_'+map+'_'+str(agent)+'.yaml',agent)
			start_time = time.time()
			cbs += cbs_main('input_'+map+'_'+str(agent)+'.yaml','output.yaml')*10
			cbs_time.append(time.time() - start_time)
		cbs_score.append(cbs)
		cbs_times.append(np.mean(cbs_time))
	plt.title(map)
	plt.plot(agents,cbs_score)
	plt.xlabel('Agents')
	plt.ylabel('Accuracy')
	plt.show()
	plt.title(map)
	plt.plot(agents,cbs_times)
	plt.xlabel('Agents')
	plt.ylabel('Run Times')
	plt.show()