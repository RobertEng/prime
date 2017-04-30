import pp
 
ppservers = ("*",)  # autodiscovery mode on!
 
# create the job server
job_server = pp.Server(ppservers=ppservers)
 
print "Starting pp! Local machine has {} workers (cores) available.".format(job_server.get_ncpus())


for computer, cpu_count in job_server.get_active_nodes().iteritems():
    print "Found {} with CPU count {}!".format(computer, cpu_count)