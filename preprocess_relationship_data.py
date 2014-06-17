## Create TAB seperated csv file(s)
## For multiple files for rels, comma separated, without spaces like "rels1.csv,rels2.csv"
## (Optional) Valid types: int, long, float, double, boolean, byte, short, char, string
## (Optional) Specify concrete node-id's with: i:id
## 
## Example file
##
## name:string:users       name:string:users       type    since   counter:int
## Michael Selina  FATHER_OF       1998-07-10      1
## Michael Rana    FATHER_OF       2007-09-15      2
## Michael Selma   FATHER_OF       2008-05-03      3
## Rana    Selma   SISTER_OF       2008-05-03      5
## Selina  Rana    SISTER_OF       2007-09-15      7

## TRANSACTION to USER rels file 
def parse_user_edges():
	## transaction_data_and_key.txt is created by jointxn.py
	inputfile = open("transaction_data_and_key.txt","r")
	outputfile = open("rels1.csv", "a")

	## Property names in first row
	outputfile.write("transaction:string:transactions\tuser:string:users\ttype\tdate\tvalue\n")
	for line in iter(inputfile):
		index = line.strip().split(",")
		outputfile.write("Txn-"+str(index[0])+"\tUser-"+str(index[2])+"\tOUTPUT_TO\t"+str(index[3])+"\t"+str(index[4])+"\n")
		outputfile.write("Txn-"+str(index[0])+"\tUser-"+str(index[1])+"\tINPUT_FROM\t"+str(index[3])+"\t"+str(index[4])+"\n")
	inputfile.close()
	outputfile.close()

## TRANSACTION to TRANSACTION rels file
def parse_user_edge_inputs():
	inputfile = open("user_edge_inputs.txt","r")
	outputfile = open("rels2.csv", "a")

	## Property names in first row
	outputfile.write("transaction:string:transactions\ttransaction:string:transactions\ttype\n")
	for line in iter(inputfile):
		index = line.strip().split(",")
		for i in range(len(index)-1):
			outputfile.write("Txn-"+str(index[0])+"\tTxn-"+str(index[i+1])+"\tINPUT_FROM\n")	 
	inputfile.close()
	outputfile.close()

## TRANSACTION to PUBLIC KEY rels file
def parse_user_edge_inputs_public_keys():
	inputfile = open("user_edge_input_public_keys.txt","r")
	outputfile = open("rels3.csv", "a")

	## Property names in first row
	outputfile.write("transaction:string:transactions\tpubkey:string:pubkeys\ttype\n")
	for line in iter(inputfile):
		index = line.strip().split(",")
		for i in range(len(index)-1):
			outputfile.write("Txn-"+str(index[0])+"\tPubkey-"+str(index[i+1])+"\tINPUT_FROM\n")
	inputfile.close()
	outputfile.close()

## PUBLIC KEY to USER rels file
def parse_userkey_list():
	inputfile = open("userkey_list.txt", "r")
	outputfile = open("rels4.csv", "a")

	##Property names in first row
	outputfile.write("pubkey:string:pubkeys\tuser:string:users\ttype\n")
	i = 1
	for line in iter(inputfile):
		index = line.strip().split(",")
		for k in range(len(index)-1):
			outputfile.write("Pubkey-"+str(index[k+1])+"\tUser-"+str(i)+"\tBELONGS_TO\n")
		i += 1 
	inputfile.close()
	outputfile.close()

parse_user_edges()
parse_user_edge_inputs()
parse_user_edge_inputs_public_keys()
parse_userkey_list()

