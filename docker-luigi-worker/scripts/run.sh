#!/bin/bash

#$LUIGI_HOME/scripts/init.sh
PYTHONPATH=$APP_HOME/workflows/examples/ luigi --module foo_complex2 examples.Foo >> /var/log/luigi/stdout.log
echo "done!!!"
exit 0

