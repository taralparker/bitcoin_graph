transaction_merge = open("transaction_data_and_key.txt", "a")

from itertools import izip

for transaction_data_line, transaction_key_line in izip(open("user_edges.txt"), open("transactionkey_list.txt")):
	transaction_merge.write(str(transaction_data_line.strip()+","+transaction_key_line.strip()+"\n"))

