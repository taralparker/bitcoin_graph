bitcoin_graph
=============
Using the [Bitcoin Transaction Network Data](http://compbio.cs.uic.edu/data/bitcoin/), we can create node and relation csv files for [Neo4j](http://http://neo4j.com/download/) that are compatible with [Batch Import](https://github.com/jexp/batch-import/tree/20).

Getting Started
-------------
Download:

[Bitcoin Transaction Network Data](http://compbio.cs.uic.edu/data/bitcoin/)

Install:

[Neo4j](http://http://neo4j.com/download/)

[Batch Import](https://github.com/jexp/batch-import/tree/20)

Creating Nodes and Relationships
--------------
1. Run join_txn.py
2. Run preprocess_node_data.py
3. Run preprocess_relationship_data.py

Importing into Neo4j
--------------
Move your nodes[1,2,3].csv and rels[1,2,3,4].csv files to the [batch-import](https://github.com/jexp/batch-import/tree/20) file.

Here is a sample configuration for batch.properties on a 6gb machine. The import will run faster if you remove auto-indexing (batch_import.node_index.*) 

1. dump_configuration=false
2. cache_type=none
3. use_memory_mapped_buffers=true
4. neostore.propertystore.db.index.keys.mapped_memory=500M 
5. neostore.propertystore.db.index.mapped_memory=500M
6. neostore.nodestore.db.mapped_memory=200M
7. neostore.relationshipstore.db.mapped_memory=3G
8. neostore.propertystore.db.mapped_memory=200M
9. neostore.propertystore.db.strings.mapped_memory=500M
10.  
11. batch_import.nodes_files=nodes1.csv,nodes2.csv,nodes3.csv
12. batch_import.rels_files=rels1.csv,rels2.csv,rels3.csv,rels4.csv
13.  
14. batch_import.node_index.users=exact
15. batch_import.node_index.transactions=exact
16. batch_import.node_index.pubkeys=exact

Starting up Neo4j
---------------
Navigate to /neo4j-community-2.1.2/conf$ 

In neo4j-server.properties set the path of the db 

org.neo4j.server.database.location= to your graph. (e.g. = batch-import/test.db)


In neo4j.properties, set 

allow_store_upgrade=true


Navigate to /neo4j-community-2.1.2/bin$

$ ./neo4j start


Go to [localhost:7474](localhost:7474) to see the graph. 



