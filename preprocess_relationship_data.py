def parse_user_edges():
	inputfile = open("transaction_data_and_key.txt","r")
	outputfile = open(output, "a")

	for line in iter(inputfile):
		index = line.strip().split(",")
		outputfile.write("R "+str(index[0]+"; OUTPUT_TO;"+str(index[2]))+";\n")
		outputfile.write("R "+str(index[0]+"; INPUT_FROM;"+str(index[1]))+";\n")

		#for testing
		print ("R "+str(index[0]+"; OUTPUT_TO;"+str(index[2]))+";\n")
		print ("R "+str(index[0]+"; INPUT_FROM;"+str(index[1]))+";\n")


	inputfile.close()
	outputfile.close()

def parse_user_edge_inputs():
	inputfile = open("user_edge_inputs.txt","r")
	outputfile = open(output, "a")

	for line in iter(inputfile):
		index = line.strip().split(",")
		for i in range(len(index)-1):
			outputfile.write("R "+str(index[0])+"; INPUT_FROM; "+str(index[i+1])+";\n")
#			print ("R "+str(index[0])+"; INPUT_FROM; "+str(index[i+1])+";\n")
	 
	inputfile.close()
	outputfile.close()

def parse_user_edge_inputs_public_keys():
	inputfile = open("user_edge_inputs_public_keys.txt","r")
	outputfile = open(output, "a")

	for line in iter(inputfile):
		index = line.strip().split(",")
		for i in range(len(index)-1):
			outputfile.write("R "+str(index[0])+"; INPUT_FROM; "+str(index[i+1])+";"\n)
#			print ("R "+str(index[0])+"; INPUT_FROM; "+str(index[i+1])+";\n")

	inputfile.close()
	outputfile.close()



			
#Name of the output node file
output = "relationships.txt"

parse_user_edge()
#parse_user_edge_inputs()
#parse_user_edge_inputs_public_keys()
