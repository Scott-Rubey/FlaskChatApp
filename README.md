The database:
For efficiency, perhaps entries could be stored in a local
data structure that periodically queries the DynamoDB entries
and stores any new message entries (i.e. with a timestamp greater
than the current final entry), subsequently adding those entries
as innderHTML to the DOM.

NOTES:  must create new EC2 instance and docker image from scratch
for changes to take effect!
