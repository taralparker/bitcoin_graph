def parse_userkey():
	inputfile = open("userkey_list.txt", "r")
	outputfile = open(output,"a")

	i=0	
 	for line in iter(inputfile):
		i += 1
		outputfile.write("N "+"UserNode "+"User-"+str(i)+";\n")
		#for testing
#		print ("N "+"UserNode "+"User-"+str(i)+";\n")


	inputfile.close()
	outputfile.close()

def parse_pubkey():
	inputfile = open("pubkey_list.txt", "r")
	outputfile = open(output,"a")

	i=0
 	for line in iter(inputfile):
		i += 1
		line = line.strip()	
		outputfile.write("N "+"PubkeyNode "+"Pubkey-"+str(i)+";"+" pubkey:\""+line+"\";\n")
		#for testing
#		print ("N "+"PubkeyNode "+"Pubkey-"+str(i)+";"+" pubkey:"+line+";\n")

	inputfile.close()
	outputfile.close()

##NOT FINISHED..........
def parse_transaction():
	inputfile = open("transaction_data_and_key.txt", "r")
	outputfile = open(output,"a")

 	for line in iter(inputfile):
		index = line.strip().split(",")
		outputfile.write("N "+"TxnNode "+"Txn-"+str(index[0])+";"+" txn:\""+str(index[5])+"\", date:"+str(index[3])+", value:"+str(index[4])+";\n")	
		#for testing
#		print ("N "+"TxnNode "+"Txn-"+str(index[0])+";"+" txn:\""+str(index[5])+"\", date:"+str(index[3])+", value:"+str(index[4])+";\n")	
		
	inputfile.close()
	outputfile.close()

#Name of the output node file
output = "nodes.txt"

parse_userkey()
parse_pubkey()
parse_transaction()

