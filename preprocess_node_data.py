## Create TAB seperated csv file(s)
## For multiple files for nodes, comma separated, without spaces like "node1.csv,node2.csv"
## (Optional) Valid types: int, long, float, double, boolean, byte, short, char, string
## (Optional) Specify concrete node-id's with: i:id
##
## Example File:
##
## name:string:users       age     works_on
## Michael 37      neo4j
## Selina  14

## Parse and format the USER nodes into a new file
def parse_userkey():
	inputfile = open("userkey_list.txt", "r")
	outputfile = open("nodes1.csv","a")

	i = 0
	## Property names in first row
	outputfile.write("user:string:users\ttype\n")	
 	for line in iter(inputfile):
		i += 1
		outputfile.write("User-"+str(i)+"\tUserNode\n")
	inputfile.close()
	outputfile.close()


## Parse and format the PUBKEY nodes into a new file
def parse_pubkey():
	inputfile = open("pubkey_list.txt", "r")
	outputfile = open("nodes2.csv","a")

	i = 0
	## Property names in first row
 	outputfile.write("pubkey:string:pubkeys\ttype\tkey\n")
	for line in iter(inputfile):
		i += 1
		line = line.strip()	
		outputfile.write("Pubkey-"+str(i)+"\tPubkeyNode\t"+line+"\n")
	inputfile.close()
	outputfile.close()


## Parse and format the TRANSACTION nodes into a new file
def parse_transaction():
	## transaction_data_and_key is created by jointxn.py
	inputfile = open("transactionkey_list.txt", "r")
	outputfile = open("nodes3.csv","a")

	i = 0
	##Property names in first row
	outputfile.write("transaction:string:transactions\ttype\ttxn\n")
 	for line in iter(inputfile):
		i +=1 
		outputfile.write("Txn-"+str(i)+"\tTxnNode"+"\t"+line)	
	inputfile.close()
	outputfile.close()


parse_userkey()
parse_pubkey()
parse_transaction()

