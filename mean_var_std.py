import numpy as np 

def calculate(list):
	if len(list) < 9:
		raise ValueError("List must contain nine numbers.")

	else:
		nw_arr = np.array(list).reshape(3,3)

		#ALL CALCULATIONS WITH THE 'AXIS-1, AXIS-2 AND FLATTENED' FORMAT REQUESTED 
	mean_clc = [(nw_arr.mean(axis = 0).tolist()), (nw_arr.mean(axis = 1).tolist()), (nw_arr.flatten().mean())]
	vrnce_clc = [(nw_arr.var(axis = 0).tolist()), (nw_arr.var(axis = 1).tolist()), (nw_arr.flatten().var())]
	stndr_clc = [(nw_arr.std(axis = 0).tolist()), (nw_arr.std(axis = 1).tolist()), (nw_arr.flatten().std())]
	max_clc = [(nw_arr.max(axis = 0).tolist()), (nw_arr.max(axis = 1).tolist()), (nw_arr.flatten().max())]
	min_clc = [(nw_arr.min(axis = 0).tolist()), (nw_arr.min(axis = 1).tolist()), (nw_arr.flatten().min())]
	sum_clc = [(nw_arr.sum(axis = 0).tolist()), (nw_arr.sum(axis = 1).tolist()), (nw_arr.flatten().sum())]

	calculations = {
	'mean': mean_clc,
	'variance': vrnce_clc,
	'standard deviation': stndr_clc,
	'max': max_clc,
	'min': min_clc,
	'sum': sum_clc
	}
	return calculations
