#/usr/bin/env python

from mod_python import apache

# we want the handler to run after the request has been processed. 
# only define a cleanup handler.

def cleanuphandler(req):
	
	# filter on request type.  We don't need to go any further for 
	# certain http methods.	
	exit_methods = ["GET", "HEAD", "PROPFIND", "PROPPATCH"]
	if req.method in exit_methods:
		sys.stderr.write("update_git_repo: no action for " + req.method)
		exit
		
	# now, we want to call our git update script.  
	req.get_basic_auth_pw()
	cmd = "/var/www-backup/scripts/do_update.sh "+req.user
	(ret, out) = commands.getstatusoutput(cmd)
	if status:
		sys.stderr.write("update_git_repo: update failed: " + out)
		exit
	sys.stderr.write("update_git_repo: success");

