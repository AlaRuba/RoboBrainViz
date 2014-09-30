#! /usr/bin/env python
# 
# ===============================================================
#    Description:  Get a node from the RoboBrain graph backed by
#                  neo4j. 
# 
#        Created:  2014-09-15 21:23:41
# 
#         Author:  Ayush Dubey, dubey@cs.cornell.edu
# 
# Copyright (C) 2013, Cornell University, see the LICENSE file
#                     for licensing agreement
# ===============================================================
# 

import sys
import re
from py2neo import cypher


def get_node(handle):
    session = cypher.Session("http://ec2-54-68-208-190.us-west-2.compute.amazonaws.com:7474")
    tx = session.create_transaction()

    tx.append("MATCH (n { handle: '" + handle + "' }) "
              "RETURN n.media")

    results = tx.execute()

    assert len(results) == 1
    if len(results[0]) == 1:
        # node exists
        print '{'
        print '"nodes":['
        print '{"name":"'+handle+'"},'
        tx.append("MATCH (n { handle: '" + handle + "' })-[r]->nbr "
                  "RETURN r.handle,nbr.handle")
        nbrs = tx.execute()
        assert len(nbrs) == 1
        #if len(nbrs[0]) != 0:
            #print 'Out edges:'
        for pair in nbrs[0]:
            r = pair.values[0]
            nbr = pair.values[1]
            print '{"name":"'+nbr+'"},'
        print '],'
        print '"links":['
        count = 0
        for pair in nbrs[0]:
            nbr = pair.values[1]
            count += 1
            print '{"source":0,"target":'+str(count)+'},'
        print ']'
        print '}'
    else:
        print 'Node ' + handle + ' does not exist.'

    tx.commit()

    print 


def main(args):
    if len(args) != 2:
        print 'This script requires exactly one argument, i.e. the handle of the node.'
        sys.exit(-1)

    get_node(args[1])


if __name__ == "__main__":
    main(sys.argv)
