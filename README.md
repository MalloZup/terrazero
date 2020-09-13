# terrazero

# Status: development/unstable

# Rationale

Terrazero is the fastest, minimalistic CLI taylored for terraform deployements.

Unlike many other utilities, you don't need any configuration for running terrazero.


During your terraform deployment copy the `node.py` to  your cloud instances.
You can do it with well-known terraform constructs.( provisioner etc)

After your deployment is done, you can use `terrazero`, which  will automatically detect ips from terraform output, so you can run `terrazero -c "uptime"`, this will run uptime to all your nodes you installed `node.py`.

This is just a possible feature.

# Features:

- Run remote command on all your host `terrazero "ls -l"

Warning: this project was made to learn purposes, so features can evolve or disapper until a shape.

# Technical details:

Under the hood it uses `zeromq` and the server/client pattern


# How to use this project right now:

This run command on all your nodes:

1) `./terrazero.py -c "ls"`

2) start nodes with `./node.py`


Warning: right now everything is pretty much hardcoded so you need to adapt/extend for your needs


