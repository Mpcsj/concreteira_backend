file_res = open('result.py','w')
with open('insert_initial_data.py','r') as f:
	for line in f:
		file_res.write(line.replace('Pedreia Um Valemix','Pedreira Um Valemix'))

file_res.close()